#!/usr/bin/env python3
"""Regenerate the fallback images of native equations in a deck, from a PowerPoint render (Claude-built workflow).

    python3 scripts/refresh_math_fallbacks_claude.py <deck.pptx> [--dry-run]

A text box holding native equations is stored as mc:AlternateContent: PowerPoint shows the mc:Choice (the live
equation); other viewers (LibreOffice, possibly Keynote or Google Slides) show the mc:Fallback, which PowerPoint writes
as a picture of the box. PowerPoint refreshes that picture only when it re-saves the box itself, so equations edited
outside PowerPoint keep stale pictures, and builder-generated boxes have a text copy without the equations.

This script renders every equation box alone on its slide (temporary copies, exported by PowerPoint from the system temp
folder), crops each box (extended to any overflowing text), makes the white background transparent, and replaces each
fallback with a picture of exactly that frame. Slide content seen in PowerPoint does not change. A backup of the deck
goes to output/deck_backups/ first. Requires macOS, Microsoft PowerPoint and pdftoppm (as build_deck_claude.py --render).
"""
import argparse, copy, hashlib, io, shutil, subprocess, sys, time
from pathlib import Path

import numpy as np
from PIL import Image
from pptx import Presentation
from pptx.shapes.shapetree import SlideShapeFactory
from pptx.util import Emu

sys.path.insert(0, str(Path(__file__).parent))
import build_deck_claude as B  # noqa: E402

MC = '{http://schemas.openxmlformats.org/markup-compatibility/2006}'
P = '{http://schemas.openxmlformats.org/presentationml/2006/main}'
A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
DPI = 200
PAD = 0.04                                   # inches of margin around the crop


def targets(prs):
    """(slide index, AlternateContent element) for every equation box, per slide in document order."""
    out = []
    for i, s in enumerate(prs.slides):
        acs = [ac for ac in s.shapes._spTree.iterchildren(MC + 'AlternateContent')
               if ac.find(MC + 'Choice') is not None and ac.find(MC + 'Fallback') is not None
               and next(ac.find(MC + 'Choice').iter('{http://schemas.microsoft.com/office/drawing/2010/main}m'), None)
               is not None]
        out.append((i, acs))
    return out


def box_of(slide, ac):
    """Shape frame in inches (x, y, w, h), inherited from the layout for placeholders without their own xfrm."""
    sp = ac.find(MC + 'Choice')[0]
    shape = SlideShapeFactory(sp, slide.shapes)
    return tuple(Emu(v).inches for v in (shape.left, shape.top, shape.width, shape.height))


def isolated_copy(deck, keep):
    """Copy of the deck where slide i keeps only its keep[i]-th equation box (others emptied), all slides unhidden."""
    prs = Presentation(deck)
    for (i, acs), k in zip(targets(prs), keep):
        s = prs.slides[i]
        s._element.attrib.pop('show', None)
        for el in s._element.findall(P + 'timing'):      # animations would point at removed shapes
            s._element.remove(el)
        tree = s.shapes._spTree
        for child in list(tree):
            if child.tag in (P + 'nvGrpSpPr', P + 'grpSpPr'):
                continue
            if k is not None and k < len(acs) and child is acs[k]:
                continue
            tree.remove(child)
    return prs


def render_pages(prs, work, tag):
    path = work / f'iso_{tag}.pptx'
    prs.save(path)
    B.render(path, work / f'iso_{tag}_sheet.png', work)
    pdf = sorted(work.glob('render_*.pdf'))[-1]
    keep = work / f'iso_{tag}.pdf'
    shutil.copy(pdf, keep)
    for old in work.glob(f'iso_{tag}-*.png'):
        old.unlink()
    subprocess.run(['pdftoppm', '-r', str(DPI), '-png', str(keep), str(work / f'iso_{tag}')], check=True)
    return sorted(work.glob(f'iso_{tag}-*.png'))


def crop(page_png, blank_png, box):
    """Crop the box (extended to its content within 0.5 in), keeping only pixels that differ from the blank layout
    render (so title rules, footers and background stay out); the rest is transparent."""
    im = np.asarray(Image.open(page_png).convert('RGB')).astype(np.float32)
    bg = np.asarray(Image.open(blank_png).convert('RGB')).astype(np.float32)
    H, W = im.shape[:2]
    x, y, w, h = box
    sx, sy = W / B.W, H / B.H
    own = np.abs(im - bg).max(axis=2) > 12            # pixels drawn by this box
    rx0, ry0 = max(0, int((x - 0.5) * sx)), max(0, int((y - 0.5) * sy))
    rx1, ry1 = min(W, int((x + w + 0.5) * sx)), min(H, int((y + h + 0.5) * sy))
    ink = np.argwhere(own[ry0:ry1, rx0:rx1])
    bx0, by0, bx1, by1 = x, y, x + w, y + h
    if len(ink):
        (iy0, ix0), (iy1, ix1) = ink.min(axis=0), ink.max(axis=0)
        bx0, by0 = min(bx0, (rx0 + ix0) / sx), min(by0, (ry0 + iy0) / sy)
        bx1, by1 = max(bx1, (rx0 + ix1 + 1) / sx), max(by1, (ry0 + iy1 + 1) / sy)
    bx0, by0 = max(0, bx0 - PAD), max(0, by0 - PAD)
    bx1, by1 = min(B.W, bx1 + PAD), min(B.H, by1 + PAD)
    c = (slice(int(by0 * sy), int(by1 * sy)), slice(int(bx0 * sx), int(bx1 * sx)))
    tile, mask = im[c], own[c]
    alpha = 255 - tile.min(axis=2)                      # white -> transparent; ink keeps full opacity
    alpha[(alpha < 6) | ~mask] = 0
    a = np.maximum(alpha, 1)[..., None] / 255
    rgb = ((tile - (1 - a) * 255) / a).clip(0, 255)     # un-blend from the white background
    rgba = np.dstack([rgb, alpha]).astype(np.uint8)
    buf = io.BytesIO()
    Image.fromarray(rgba, 'RGBA').save(buf, 'PNG', optimize=True)
    return buf.getvalue(), (bx0, by0, bx1 - bx0, by1 - by0)


def replace_fallback(slide, ac, png, frame):
    fb = ac.find(MC + 'Fallback')
    old = fb[0] if len(fb) else None
    choice_sp = ac.find(MC + 'Choice')[0]
    cnv = choice_sp.find('.//' + P + 'cNvPr')
    _, rid = slide.part.get_or_add_image_part(io.BytesIO(png))
    x, y, w, h = (int(Emu(int(v * 914400))) for v in frame)
    xml = (f'<p:sp xmlns:p="{P[1:-1]}" xmlns:a="{A[1:-1]}" xmlns:r="{R[1:-1]}"><p:nvSpPr>'
           f'<p:cNvPr id="{cnv.get("id")}" name="{cnv.get("name")}"/><p:cNvSpPr><a:spLocks noRot="1" noChangeAspect="1" '
           'noMove="1" noResize="1" noTextEdit="1"/></p:cNvSpPr><p:nvPr/></p:nvSpPr><p:spPr>'
           f'<a:xfrm><a:off x="{x}" y="{y}"/><a:ext cx="{w}" cy="{h}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/>'
           f'</a:prstGeom><a:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></a:blipFill>'
           '</p:spPr><p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:endParaRPr lang="en-US"/></a:p></p:txBody></p:sp>')
    from lxml import etree
    new = etree.fromstring(xml)
    old_rids = [b.get(R + 'embed') for b in old.iter(A + 'blip')] if old is not None else []
    for c in list(fb):
        fb.remove(c)
    fb.append(new)
    for r in old_rids:
        if r != rid:
            slide.part.drop_rel(r)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('deck')
    ap.add_argument('--dry-run', action='store_true', help='render and report, do not change the deck')
    a = ap.parse_args()
    deck = Path(a.deck).resolve()
    prs = Presentation(deck)
    tg = targets(prs)
    passes = max((len(acs) for _, acs in tg), default=0)
    print(f'{sum(len(acs) for _, acs in tg)} equation boxes on {sum(1 for _, acs in tg if acs)} slides; {passes} render pass(es)')
    work = B.render_dir(deck.stem)            # reuse the deck's render folder: PowerPoint already has access
    results = {}
    blank = render_pages(isolated_copy(deck, [None] * len(tg)), work, 'blank')   # layout only, for subtraction
    for k in range(passes):
        keep = [k if len(acs) > k else None for _, acs in tg]
        pages = render_pages(isolated_copy(deck, keep), work, str(k))
        for (i, acs) in tg:
            if len(acs) > k:
                results[(i, k)] = crop(pages[i], blank[i], box_of(prs.slides[i], acs[k]))
    if a.dry_run:
        for (i, k), (png, fr) in sorted(results.items()):
            print(f'slide {i + 1} box {k}: {len(png)} bytes, frame {tuple(round(v, 2) for v in fr)}')
        return
    stamp = time.strftime('%Y%m%d-%H%M%S')
    sha = hashlib.sha256(deck.read_bytes()).hexdigest()[:8]
    backup = B.ROOT / 'output/deck_backups' / f'{deck.stem}.{stamp}.{sha}.pptx'
    shutil.copy2(deck, backup)
    for (i, acs) in tg:
        for k, ac in enumerate(acs):
            png, fr = results[(i, k)]
            replace_fallback(prs.slides[i], ac, png, fr)
    prs.save(deck)
    print(f'replaced {len(results)} fallbacks; backup {backup.relative_to(B.ROOT)}')


if __name__ == '__main__':
    main()
