#!/usr/bin/env python3
"""Move named slides of a deck after another slide, optionally hiding them (Claude-built workflow).

    python3 scripts/move_slides_claude.py <deck.pptx> ID,ID,... --after ID [--hide] [--expect-sha SHA] [--dry-run]

Used to move existing (instructor-edited) slides, e.g. into an appendix, without rebuilding them: only the order
of the presentation's slide list changes, plus `show="0"` on the moved slides with --hide (hidden in the slide show,
the convention for appendix slides). The slides' own XML, notes and images are untouched. The moved slides keep
their relative order. A backup goes to output/deck_backups/ first; the deck must not be open in PowerPoint.
"""
import argparse, hashlib, io, shutil, time
from pathlib import Path

from pptx import Presentation

ROOT = Path(__file__).resolve().parent.parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('deck')
    ap.add_argument('names', help='comma-separated slide names (spec ids) to move')
    ap.add_argument('--after', required=True)
    ap.add_argument('--hide', action='store_true')
    ap.add_argument('--expect-sha')
    ap.add_argument('--dry-run', action='store_true', help='write <deck>.moved.pptx in the system temp folder only')
    a = ap.parse_args()
    deck_path = Path(a.deck)
    if deck_path.with_name('~$' + deck_path.name).exists():
        raise SystemExit('the deck appears to be open in PowerPoint (lock file exists). Close it first.')
    before = sha(deck_path)
    if a.expect_sha and before != a.expect_sha:
        raise SystemExit(f'deck SHA-256 {before} differs from the expected {a.expect_sha}; reconcile first.')
    prs = Presentation(deck_path)
    ids = prs.slides._sldIdLst
    by_name = {s._element.cSld.get('name'): (sid, s) for sid, s in zip(list(ids), prs.slides)}
    names = a.names.split(',')
    missing = [n for n in names + [a.after] if n not in by_name]
    if missing:
        raise SystemExit(f'deck has no slides named {missing}')
    if a.after in names:
        raise SystemExit('--after cannot be one of the moved slides')
    anchor = by_name[a.after][0]
    for n in names:
        sid, s = by_name[n]
        anchor.addnext(sid)
        anchor = sid
        if a.hide:
            s._element.set('show', '0')
    buf = io.BytesIO()
    prs.save(buf)
    if a.dry_run:
        import tempfile
        out = Path(tempfile.gettempdir()) / f'{deck_path.stem}.moved.pptx'
        out.write_bytes(buf.getvalue())
        print(f'dry run -> {out}')
        return
    backups = ROOT / 'output' / 'deck_backups'
    backups.mkdir(parents=True, exist_ok=True)
    bk = backups / f'{deck_path.stem}.{time.strftime("%Y%m%d-%H%M%S")}.{before[:8]}.pptx'
    shutil.copy2(deck_path, bk)
    deck_path.write_bytes(buf.getvalue())
    print(f'moved {len(names)} slides after {a.after}{" (hidden)" if a.hide else ""}; backup {bk.relative_to(ROOT)}; '
          f'new SHA-256 {sha(deck_path)}')


if __name__ == '__main__':
    main()
