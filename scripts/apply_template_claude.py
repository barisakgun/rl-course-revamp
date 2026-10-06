#!/usr/bin/env python3
"""Re-apply the (edited) course template to existing decks, keeping their content and animations.

    python3 scripts/apply_template_claude.py <deck.pptx> [<deck.pptx> ...] [--no-reflow] [--render]

For each deck:
  1. Work on a temporary copy; the deck is replaced only at the end, after a backup to
     output/deck_backups/<name>.<timestamp>.pptx (never overwritten). A failure leaves the deck unchanged.
  2. Let PowerPoint apply the template (its "apply template" command) to a temporary copy: the master,
     layouts and theme are replaced and each slide keeps the layout of the same name. Titles, placeholder
     text, the rule, footer and slide numbers follow the template automatically; animations, notes and
     manual edits stay. The deck itself is never opened in PowerPoint.
  3. Reflow (default): shapes the template cannot move by itself (free text boxes, pictures, tables,
     placeholders with a manual position) that sit in the old content area get their top-left corner
     mapped proportionally from the old master body frame to the new one, so shapes at the top follow the
     frame's top and shapes at the bottom stay inside its bottom. Nothing is resized.
  4. Report: slides whose layout is missing from the template, shapes that now extend past the content
     frame, template layouts whose own placeholder positions differ from the master body frame.
  5. Replace the deck with the result, then optionally render it (build_deck_claude.render).

Requires macOS + Microsoft PowerPoint for step 2. Template: course/templates/lecture_template_claude.pptx.
"""
import argparse, datetime, shutil, subprocess, sys, tempfile
from pathlib import Path

from pptx import Presentation
from pptx.oxml.ns import qn
from pptx.util import Emu

sys.path.insert(0, str(Path(__file__).parent))
import build_deck_claude as B  # noqa: E402

ROOT = B.ROOT
TEMPLATE = ROOT / 'course/templates/lecture_template_claude.pptx'
BACKUPS = ROOT / 'output/deck_backups'
TOL = Emu(int(0.3 * 36000))                     # 0.3 mm

APPLY = ('on run argv\n tell application "Microsoft PowerPoint"\n'
         '  open (POSIX file (item 1 of argv))\n'
         '  repeat 60 times\n   if exists presentation (item 2 of argv) then exit repeat\n   delay 1\n  end repeat\n'
         '  set p to presentation (item 2 of argv)\n'
         '  apply template p file name (item 3 of argv)\n  save p\n  close p saving no\n'
         ' end tell\nend run\n')


def body_frame(prs):
    body = next(ph for ph in prs.slide_master.placeholders if ph.placeholder_format.type == 2)
    return body.left, body.top, body.left + body.width, body.top + body.height


def title_bottom(prs):
    """Content is everything below the master title box (some shapes start above the body frame)."""
    title = next(ph for ph in prs.slide_master.placeholders if ph.placeholder_format.type == 1)
    return title.top + title.height


def rule_band(prs):
    rule = next((sh for sh in prs.slide_master.shapes if sh.name == 'Title rule'), None)
    return (rule.top, rule.top + rule.height) if rule is not None else None


def mm(e):
    return f'{Emu(e).mm:.1f}'


def layout_report(template):
    prs = Presentation(template)
    l, t, r, b = body_frame(prs)
    out = []
    for lay in prs.slide_layouts:
        if lay._element.get('showMasterSp') == '0':
            continue                                     # title/section/blank layouts are free-standing
        for ph in lay.placeholders:
            if ph.placeholder_format.type in (1, 3) or ph._element.spPr.find(qn('a:xfrm')) is None:
                continue
            if ph.top < t - TOL or ph.top + ph.height > b + TOL:
                out.append(f'template layout "{lay.name}": {ph.name} spans {mm(ph.top)}–{mm(ph.top + ph.height)} mm, '
                           f'master body is {mm(t)}–{mm(b)} mm')
    return out


def reflow(prs, old, new, report, old_title_bottom):
    sx = (new[2] - new[0]) / (old[2] - old[0])
    sy = (new[3] - new[1]) / (old[3] - old[1])
    moved = 0
    names = {l.name for l in prs.slide_layouts}
    for n, slide in enumerate(prs.slides, 1):
        lay = slide.slide_layout
        if lay.name not in names:
            report.append(f'slide {n}: layout "{lay.name}" is not in the template')
        if lay._element.get('showMasterSp') == '0':
            continue
        for sh in slide.shapes:
            inherits = sh.is_placeholder and sh._element.find('.//' + qn('a:xfrm')) is None
            if inherits or sh.top is None or sh.top < old_title_bottom - TOL:
                continue                                 # follows the layout, or lives in the title band
            if old != new:
                sh.left = Emu(int(new[0] + (sh.left - old[0]) * sx))
                sh.top = Emu(int(new[1] + (sh.top - old[1]) * sy))
                moved += 1
            band = rule_band(prs)
            if band and sh.top < band[1] and sh.top + sh.height > band[0]:
                report.append(f'slide {n}: "{sh.name}" overlaps the title rule ({mm(sh.top)} mm); '
                              'slide shapes hide master shapes')
            if sh.top + sh.height > new[3] + TOL:
                report.append(f'slide {n}: "{sh.name}" ends at {mm(sh.top + sh.height)} mm, '
                              f'below the content frame ({mm(new[3])} mm)')
    return moved


def apply(deck, template, do_reflow=True):
    deck = Path(deck).resolve()
    before = Presentation(deck)
    old, old_tb = body_frame(before), title_bottom(before)
    # A fixed folder (next to the render folders) rather than a new random one each run: sandboxed
    # PowerPoint may ask for file access the first time it sees a folder, which blocks scripting.
    work = Path(tempfile.gettempdir()) / 'deck_render' / '_apply'
    work.mkdir(parents=True, exist_ok=True)
    tmp = work / f'{deck.stem}.apply.pptx'
    tmp.unlink(missing_ok=True)
    shutil.copy2(deck, tmp)
    try:
        subprocess.run(['osascript', '-e', APPLY, str(tmp), tmp.name, str(template)], check=True, timeout=300)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        tmp.unlink(missing_ok=True)
        sys.exit(f'PowerPoint could not apply the template to {deck.name} (is a dialog open in PowerPoint?); '
                 'the deck is unchanged')
    prs = Presentation(tmp)
    new = body_frame(prs)
    report = []
    if len(prs.slide_masters) > 1:
        report.append(f'{len(prs.slide_masters)} slide masters after applying; unused old masters can be '
                      'deleted in Slide Master view')
    moved = reflow(prs, old, new, report, old_tb) if do_reflow else 0
    prs.save(tmp)
    stamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    backup = BACKUPS / f'{deck.stem}.{stamp}.pptx'
    BACKUPS.mkdir(parents=True, exist_ok=True)
    with deck.open('rb') as src, backup.open('xb') as dst:     # backup only when replacing
        shutil.copyfileobj(src, dst)
    shutil.copy2(tmp, deck)
    tmp.unlink()
    return backup, old, new, moved, report


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('decks', nargs='+')
    ap.add_argument('--template', default=str(TEMPLATE))
    ap.add_argument('--no-reflow', action='store_true', help='only apply the template; move nothing')
    ap.add_argument('--render', action='store_true', help='render each deck afterwards for review')
    a = ap.parse_args()
    template = Path(a.template).resolve()
    for line in layout_report(template):
        print('TEMPLATE', line)
    for d in a.decks:
        backup, old, new, moved, report = apply(d, template, not a.no_reflow)
        rel = Path(d).resolve().relative_to(ROOT)
        print(f'{rel}: template applied; backup {backup.relative_to(ROOT)}')
        print(f'  body frame {mm(old[1])}–{mm(old[3])} -> {mm(new[1])}–{mm(new[3])} mm (top–bottom); '
              f'{moved} content shapes repositioned' if not a.no_reflow else '  no reflow')
        for r in report:
            print('  !', r)
        if a.render:
            work = Path(tempfile.gettempdir()) / 'deck_render' / Path(d).stem
            work.mkdir(parents=True, exist_ok=True)
            preview = ROOT / 'output/lectures' / rel.parent.name / f'{Path(d).stem}_preview.png'
            pages = B.render(Path(d).resolve(), preview, work)
            print(f'  rendered {len(pages)} slides to {work}; preview {preview.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
