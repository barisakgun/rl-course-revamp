#!/usr/bin/env python3
"""Pull edits made to a built deck in PowerPoint back into its YAML content spec (Claude-built workflow).

    python3 scripts/pull_deck_claude.py <edited.pptx> <spec.yaml> [--write]

The edited deck is compared with a fresh in-memory build of the current spec (build_deck_claude.py),
using the slide names (spec ids) and `yaml:<field>` shape names the builder writes:

  * changed text, bullets (with levels), tables, images and speaker notes  -> spec fields
  * slides reordered, deleted or duplicated                                 -> spec slide list
  * new slides of a simple form (title + bullets, or title + picture + text) -> new spec entries
    (images are referenced by repository path when an identical file exists)
  * anything the spec cannot express (moved/resized shapes, extra shapes, unsupported new slides,
    formatting other than bold/italic/links) is REPORTED, because a rebuild would drop it.

Inline markup follows the builder: **bold**, *italic*, [text](url), <url>. Formatting that a field gets by
default (e.g. bold column headings) is not written back as markup.

Without --write this is a dry run. With --write the spec is updated in place; comments and layout are
preserved (ruamel.yaml). New slides get no `minutes` estimate, so `build_deck_claude.py --check` fails until
the instructor sets one: the time budget is a decision, not an extraction.
"""
import argparse, copy, hashlib, io, re, sys
from pathlib import Path

from pptx import Presentation
from pptx.oxml.ns import qn
from pptx.util import Emu
from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap, CommentedSeq

sys.path.insert(0, str(Path(__file__).parent))
import build_deck_claude as B  # noqa: E402

ROOT = B.ROOT
TOL_MM = 0.5
TEXT_FIELDS = re.compile(r'^(title|subtitle|byline|lead|footnote|caption|(left|right)\.heading|steps\.\d+|'
                         r'boxes\.\d+\.\d|callouts\.\d+\.\d)$')
OPTIONAL = {'footnote', 'caption', 'lead', 'byline'}
IMAGE_DIRS = ('course', 'sources')


# ---------------------------------------------------------------- reading a deck

def run_list(paragraph):
    out = []
    for r in paragraph.runs:
        link = r.hyperlink.address if r.hyperlink.address else None
        out.append([r.text, bool(r.font.bold), bool(r.font.italic), link])
    merged = []
    for r in out:                                  # PowerPoint splits runs for spelling/language marks
        if merged and merged[-1][1:] == r[1:]:
            merged[-1][0] += r[0]
        else:
            merged.append(r)
    return merged


def level_of(p):
    pPr = p._p.pPr
    if pPr is None:
        return 0
    if pPr.get('lvl'):
        return int(pPr.get('lvl'))
    if pPr.get('marL') and pPr.find(qn('a:buChar')) is not None:   # older builder output: indent only
        return max(0, round((Emu(int(pPr.get('marL'))).inches - 0.25) / 0.31))
    return 0


def paragraphs(shape):
    paras = [(level_of(p), run_list(p)) for p in shape.text_frame.paragraphs]
    return [(lvl, runs) for lvl, runs in paras if ''.join(r[0] for r in runs).strip()]


def defaults(runs_lists):
    """Formatting every run of the reference field has; such formatting is the field's default style."""
    runs = [r for rl in runs_lists for r in rl if r[0].strip()]
    return (bool(runs) and all(r[1] for r in runs), bool(runs) and all(r[2] for r in runs))


def to_markup(runs, dflt=(False, False)):
    out = []
    for text, bold, italic, link in runs:
        bold, italic = bold and not dflt[0], italic and not dflt[1]
        core = text.strip()
        if not core:
            out.append(text)
            continue
        lead, trail = text[:len(text) - len(text.lstrip())], text[len(text.rstrip()):]
        if link:
            core = f'<{link}>' if core == link else f'[{core}]({link})'
        elif bold:
            core = f'**{core}**'
        elif italic:
            core = f'*{core}*'
        out.append(lead + core + trail)
    return re.sub(r'\s+', ' ', ''.join(out)).strip()


def notes_of(slide):
    if not slide.has_notes_slide:
        return ''
    text = slide.notes_slide.notes_text_frame.text
    head, sep, _ = text.rpartition('\n\nTarget: ')            # trailer written by the builder
    return (head if sep else text).strip()


def deck_slides(prs):
    out = []
    for s in prs.slides:
        tagged, untagged = {}, []
        for sh in s.shapes:
            if sh.name.startswith('yaml:'):
                tagged[sh.name[5:]] = sh
            elif sh.name.startswith('deco:'):
                continue
            elif sh.is_placeholder and sh.has_text_frame and not sh.text_frame.text.strip():
                continue                                       # empty placeholder
            else:
                untagged.append(sh)
        out.append({'id': s._element.cSld.get('name') or None, 'slide': s, 'tagged': tagged,
                    'untagged': untagged})
    return out


def geom(sh):
    return tuple(Emu(v).mm for v in (sh.left or 0, sh.top or 0, sh.width or 0, sh.height or 0))


def describe(sh):
    text = sh.text_frame.text.strip().replace('\n', ' / ')[:50] if sh.has_text_frame else ''
    kind = 'picture' if sh.shape_type == 13 else 'table' if sh.has_table else 'shape'
    return f'{kind} "{sh.name}"' + (f' ({text!r})' if text else '')


# ---------------------------------------------------------------- spec access

def get_path(node, path):
    for part in path.split('.'):
        node = node[int(part)] if part.isdigit() else node[part]
    return node


def set_path(node, path, value):
    parts = path.split('.')
    for part in parts[:-1]:
        node = node[int(part)] if part.isdigit() else node[part]
    last = parts[-1]
    node[int(last) if last.isdigit() else last] = value


def nest(items):
    """[(level, text)] -> nested list in the spec's bullet format."""
    root = []
    stack = [root]
    for lvl, text in items:
        lvl = min(lvl, len(stack))
        while len(stack) > lvl + 1:
            stack.pop()
        while len(stack) < lvl + 1:
            cur = stack[-1]
            if not (cur and isinstance(cur[-1], list)):
                cur.append([])
            stack.append(cur[-1])
        stack[-1].append(text)
    return root


def seq(items):
    out = CommentedSeq()
    for it in items:
        out.append(seq(it) if isinstance(it, list) else it)
    return out


def flow(items):
    s = CommentedSeq(items)
    s.fa.set_flow_style()
    return s


# ---------------------------------------------------------------- images

_index = None


def find_image(blob):
    global _index
    if _index is None:
        _index = {}
        for top in IMAGE_DIRS:
            for f in (ROOT / top).rglob('*'):
                if f.suffix.lower() in ('.png', '.jpg', '.jpeg', '.gif') and f.is_file():
                    _index.setdefault(hashlib.sha1(f.read_bytes()).hexdigest(), f.relative_to(ROOT).as_posix())
    return _index.get(hashlib.sha1(blob).hexdigest())


# ---------------------------------------------------------------- comparison

class Pull:
    def __init__(self, spec_rt, spec_path, report_layout=False):
        self.report_layout = report_layout
        self.spec = spec_rt
        self.spec_path = spec_path
        self.changes, self.lost, self.notes = [], [], []
        self.exports = []                                  # (path, blob) to write for unmatched images

    def field(self, sid, path, ref, ed, target):
        if TEXT_FIELDS.match(path):
            rp, ep = paragraphs(ref), paragraphs(ed)
            dflt = defaults([r for _, r in rp])
            old = ' '.join(to_markup(r, dflt) for _, r in rp)
            new = ' '.join(to_markup(r, dflt) for _, r in ep)
            if path.startswith('boxes.') and path.endswith('.0'):
                old, new = (re.sub(r'^\d+\.\s*', '', v) for v in (old, new))
            if old != new:
                set_path(target, path, new)
                self.changes.append(f'{sid}: {path}: {old!r} -> {new!r}')
        elif path.endswith('bullets'):
            rp, ep = paragraphs(ref), paragraphs(ed)
            dflt = defaults([r for _, r in rp])
            old = [(lvl, to_markup(r, dflt)) for lvl, r in rp]
            new = [(lvl, to_markup(r, dflt)) for lvl, r in ep]
            if old != new:
                set_path(target, path, seq(nest(new)))
                self.changes.append(f'{sid}: {path}: {len(old)} -> {len(new)} items; edited text: '
                                    + ' | '.join(t for _, t in new))
        elif path == 'table':
            self.table(sid, ref, ed, target)
        elif path == 'image':
            if ref.image.sha1 != ed.image.sha1:
                found = find_image(ed.image.blob)
                if found:
                    target['image'] = CommentedMap(path=found)
                    self.changes.append(f'{sid}: image -> {found}')
                else:
                    self.lost.append(f'{sid}: image replaced by a file not found under {IMAGE_DIRS}; '
                                     'save it in the repository and rerun')
        n = 3 if path == 'table' else 4                    # PowerPoint grows table rows to fit text
        if self.report_layout and max(abs(a - b) for a, b in list(zip(geom(ref), geom(ed)))[:n]) > TOL_MM:
            self.lost.append(f'{sid}: {path} position differs from a fresh build '
                             + '({:.1f},{:.1f} {:.1f}x{:.1f} mm); kept in the PPTX, not in the spec'.format(*geom(ed)))

    def table(self, sid, ref, ed, target):
        rt, et = ref.table, ed.table
        rrows = [[c for c in r.cells] for r in rt.rows]
        erows = [[c for c in r.cells] for r in et.rows]

        def cell(rows, i, j, dflt):
            return ' '.join(to_markup(r, dflt) for _, r in paragraphs(rows[i][j]))

        def dflt_for(i, j):
            if i < len(rrows) and j < len(rrows[0]):
                return defaults([r for _, r in paragraphs(rrows[i][j])])
            return (i == 0 or j == 0 or i == len(erows) - 1, False)

        old = [[cell(rrows, i, j, dflt_for(i, j)) for j in range(len(rrows[0]))] for i in range(len(rrows))]
        new = [[cell(erows, i, j, dflt_for(i, j)) for j in range(len(erows[0]))] for i in range(len(erows))]
        if old == new:
            return
        t = target['table']
        t['header'] = flow(new[0])
        has_total = 'total' in t
        body = new[1:-1] if has_total else new[1:]
        t['rows'] = CommentedSeq(flow(r) for r in body)
        if has_total:
            t['total'] = flow(new[-1])
        if len(new[0]) != len(t['widths']):
            t['widths'] = flow([1.0] * len(new[0]))
            self.lost.append(f'{sid}: table column count changed; column widths reset to equal')
        self.changes.append(f'{sid}: table changed ({len(old)}x{len(old[0])} -> {len(new)}x{len(new[0])})')

    def slide(self, sid, ref, ed, target):
        for path, rsh in ref['tagged'].items():
            esh = ed['tagged'].get(path)
            if esh is None:
                if path in OPTIONAL:
                    del target[path]
                    self.changes.append(f'{sid}: {path} deleted')
                else:
                    self.lost.append(f'{sid}: required {path} shape deleted; spec value kept')
                continue
            self.field(sid, path, rsh, esh, target)
        for path in ed['tagged'].keys() - ref['tagged'].keys():
            self.lost.append(f'{sid}: shape tagged yaml:{path} has no counterpart in this slide kind; not pulled')
        for sh in ed['untagged']:
            self.lost.append(f'{sid}: added {describe(sh)} is not in the spec; a rebuild drops it')
        old, new = (target.get('notes') or '').strip(), notes_of(ed['slide'])
        if old != new:
            target['notes'] = new + '\n' if new else ''
            self.changes.append(f'{sid}: notes edited')

    # ---- new slides
    def new_slide(self, ed, taken):
        s = ed['slide']
        title_sh = s.shapes.title
        title = title_sh.text_frame.text.strip() if title_sh is not None else ''
        tid = title_sh.shape_id if title_sh is not None else None
        content = [sh for sh in list(ed['tagged'].values()) + ed['untagged'] if sh.shape_id != tid]
        pics = [sh for sh in content if sh.shape_type == 13]
        texts = [sh for sh in content if sh.has_text_frame and sh.text_frame.text.strip()]
        used = {sh.shape_id for sh in pics + texts}
        rest = [sh for sh in content if sh.shape_id not in used]
        words = re.findall(r'[a-z0-9]+', title.lower()) or ['slide']
        sid, k = words[0], 1
        while len(sid) < 18 and k < len(words):
            sid += '_' + words[k]
            k += 1
        base, n = sid, 2
        while sid in taken:
            sid, n = f'{base}_{n}', n + 1
        entry = CommentedMap(id=sid)
        bullets = None
        if not rest and not pics and len(texts) == 1:
            entry['kind'] = 'bullets'
        elif not rest and len(pics) == 1 and len(texts) == 1:
            entry['kind'] = 'image_bullets'
        else:
            self.lost.append(f'new slide "{title}" has a layout the spec cannot express '
                             f'({len(pics)} pictures, {len(texts)} text shapes, {len(rest)} other); not pulled')
            return None
        entry['title'] = title
        paras = paragraphs(texts[0])
        bullets = seq(nest([(lvl, to_markup(r)) for lvl, r in paras]))
        if entry['kind'] == 'image_bullets':
            pic, tx = pics[0], texts[0]
            found = find_image(pic.image.blob)
            if not found:
                found = (Path(self.spec_path).parent / 'media' / f'{sid}.{pic.image.ext}').relative_to(ROOT).as_posix()
                self.exports.append((found, pic.image.blob))
            entry['image'] = CommentedMap(path=found)
            pcx = Emu(pic.left + pic.width / 2).inches
            entry['image_side'] = 'right' if pcx > B.W / 2 else 'left'
            entry['image_width'] = round(Emu(pic.width).inches, 2)
            if pic.line.fill.type is None:
                entry['image_border'] = False
            pcy, tcy = Emu(pic.top + pic.height / 2).inches, Emu(tx.top + tx.height / 2).inches
            if abs(pcy - tcy) < 0.15 * Emu(pic.height).inches:
                entry['valign'] = 'middle'
            bulleted = tx.is_placeholder or any(p._p.pPr is not None and p._p.pPr.find(qn('a:buChar')) is not None
                                                for p in tx.text_frame.paragraphs)
            if not bulleted:
                entry['bullet_style'] = 'none'
        entry['bullets'] = bullets
        entry['minutes'] = None
        entry['sources'] = flow(['instructor slide added in PowerPoint'])
        entry['instructor_voice'] = flow(['whole slide'])
        entry['verify'] = flow([])
        entry['notes'] = notes_of(s) + '\n' if notes_of(s) else ''
        geo = geom(texts[0])
        self.changes.append(f'new slide "{title}" -> id {sid}, kind {entry["kind"]}'
                            + (f', image {entry["image"]["path"]}' if 'image' in entry else ''))
        self.notes.append(f'{sid}: set `minutes`; text box was at ({geo[0]:.1f},{geo[1]:.1f}) mm and is now '
                          f'placed by the {entry["kind"]} kind')
        return entry


def pull(edited, spec_rt, spec_plain, spec_path, report_layout=False):
    ref = {s['id']: s for s in deck_slides(B.make_presentation(spec_plain))}
    by_id = {s['id']: s for s in spec_rt['slides']}
    p = Pull(spec_rt, spec_path, report_layout)
    out, seen = CommentedSeq(), set()
    for ed in deck_slides(edited):
        sid = ed['id']
        if sid in by_id and sid not in seen:
            seen.add(sid)
            p.slide(sid, ref[sid], ed, by_id[sid])
            out.append(by_id[sid])
        elif sid in by_id:                                   # duplicated in PowerPoint
            entry = copy.deepcopy(by_id[sid])
            n = 2
            while f'{sid}_{n}' in by_id or f'{sid}_{n}' in seen:
                n += 1
            entry['id'] = f'{sid}_{n}'
            seen.add(entry['id'])
            p.slide(entry['id'], ref[sid], ed, entry)
            p.changes.append(f'{sid} duplicated -> {entry["id"]}')
            p.notes.append(f'{entry["id"]}: check `minutes` and `verify` of the duplicate')
            out.append(entry)
        else:
            entry = p.new_slide(ed, set(by_id) | seen)
            if entry is None:
                continue
            same = next((e for e in spec_rt['slides'] if e['id'] not in seen and e.get('title') == entry['title']
                         and e.get('kind') == entry['kind'] and not ed['tagged']), None)
            if same is not None:                       # untagged slide already in the spec (matched by title)
                p.changes.pop()                        # not new after all
                p.notes.pop()
                for k in ('bullets', 'image', 'image_side', 'image_width', 'image_border', 'valign', 'bullet_style',
                          'notes'):
                    if k in entry and entry[k] != same.get(k) and not (k == 'notes' and not entry[k] and not same.get(k)):
                        same[k] = entry[k]
                        p.changes.append(f'{same["id"]}: {k} updated (slide matched by title)')
                p.exports = [x for x in p.exports if not x[0].endswith(f'/{entry["id"]}.' + x[0].rsplit('.', 1)[-1])]
                entry = same
            seen.add(entry['id'])
            out.append(entry)
    for sid in by_id:
        if sid not in seen:
            p.changes.append(f'{sid} deleted')
    old_order = [s['id'] for s in spec_rt['slides'] if s['id'] in seen]
    new_order = [s['id'] for s in out if s['id'] in old_order]
    if old_order != new_order:
        p.changes.append('slides reordered: ' + ', '.join(s['id'] for s in out))
    spec_rt['slides'] = out
    return p


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('deck')
    ap.add_argument('spec')
    ap.add_argument('--write', action='store_true', help='update the spec in place (default: dry run)')
    ap.add_argument('--report-layout', action='store_true',
                    help='also list shapes positioned differently from a fresh build (kept in the PPTX)')
    a = ap.parse_args()
    spec_path = Path(a.spec).resolve()
    rt = YAML()
    rt.preserve_quotes = True
    rt.width = 4096
    rt.indent(mapping=2, sequence=4, offset=2)
    spec_rt = rt.load(spec_path.read_text(encoding='utf-8'))
    import yaml
    spec_plain = yaml.safe_load(spec_path.read_text(encoding='utf-8'))
    spec_plain['_path'] = spec_path.relative_to(ROOT).as_posix()
    p = pull(Presentation(a.deck), spec_rt, spec_plain, spec_path, a.report_layout)
    print(f'{len(p.changes)} change(s) pulled into the spec:')
    for c in p.changes:
        print('  +', c)
    print(f'{len(p.lost)} edit(s) the spec cannot express (kept in the PPTX; a rebuild from the spec would drop them):')
    for c in p.lost:
        print('  !', c)
    for c in p.notes:
        print('  ?', c)
    if not a.write:
        print('dry run; rerun with --write to update', spec_path.relative_to(ROOT))
        return
    for rel, blob in p.exports:
        dest = ROOT / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists():
            sys.exit(f'{rel} exists; not overwriting')
        dest.write_bytes(blob)
        print('exported image', rel)
    with spec_path.open('w', encoding='utf-8') as f:
        rt.dump(spec_rt, f)
    print('updated', spec_path.relative_to(ROOT))


if __name__ == '__main__':
    main()
