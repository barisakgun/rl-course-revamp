#!/usr/bin/env python3
"""Download the lecture/discussion slides listed in external source manifests.

Reads `sources/<source_id>/manifest.yaml` for the linked-only reference courses and
saves every `lecture_slides` / `discussion_slides` PDF to `sources/<source_id>/lectures/`.
Writes `sources/<source_id>/lectures/index.json` with the URL, local file, size,
SHA-256, HTTP status and retrieval time of each item, so local copies keep their
provenance. Manifests are not modified (they remain the Phase 1 inventory).

The PDFs are git-ignored like the other local source PDFs; the index is tracked.
Existing files are kept unless --refresh is given.

Usage:
    python3 scripts/download_source_slides.py            # all configured linked sources
    python3 scripts/download_source_slides.py silver_rl  # one source
    python3 scripts/download_source_slides.py --refresh
"""
import argparse
import datetime as dt
import hashlib
import json
import pathlib
import sys
import urllib.error
import urllib.parse
import urllib.request

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_SOURCES = ['silver_rl', 'berkeley_cs285', 'stanford_cs234', 'stanford_cs224r']
SLIDE_TYPES = {'lecture_slides', 'discussion_slides'}
USER_AGENT = 'Mozilla/5.0 (course-reference download; rl-course-revamp)'


def slide_materials(source_id):
    manifest = yaml.safe_load((ROOT / 'sources' / source_id / 'manifest.yaml').read_text())
    for item in manifest.get('materials', []):
        url = item.get('url')
        if item.get('material_type') in SLIDE_TYPES and url and url.lower().split('?')[0].endswith('.pdf'):
            yield item


def fetch(url):
    request = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
    with urllib.request.urlopen(request, timeout=120) as response:
        return response.status, response.read()


def download_source(source_id, refresh):
    out_dir = ROOT / 'sources' / source_id / 'lectures'
    out_dir.mkdir(exist_ok=True)
    index_path = out_dir / 'index.json'
    previous = {e['url']: e for e in json.loads(index_path.read_text())['items']} if index_path.exists() else {}
    entries, seen = [], set()
    for item in slide_materials(source_id):
        url = item['url']
        if url in seen:
            continue
        seen.add(url)
        name = pathlib.PurePosixPath(urllib.parse.urlparse(url).path).name
        target = out_dir / name
        entry = {'url': url, 'material_id': item.get('id'), 'title': item.get('title'),
                 'material_type': item.get('material_type'), 'offering': item.get('offering'),
                 'file': name}
        if target.exists() and not refresh and url in previous and previous[url].get('status') == 'downloaded':
            entries.append(previous[url])
            continue
        try:
            status, data = fetch(url)
            if not data.startswith(b'%PDF'):
                raise ValueError('response is not a PDF')
            target.write_bytes(data)
            entry.update(status='downloaded', http_status=status, bytes=len(data),
                         sha256=hashlib.sha256(data).hexdigest())
        except (urllib.error.URLError, ValueError, TimeoutError) as exc:
            entry.update(status='failed', error=str(exc))
        entry['retrieved_at'] = dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds')
        entries.append(entry)
        print(f"{source_id}: {entry['status']:10} {name}", flush=True)
    index = {'source_id': source_id,
             'note': 'Local copies of slides listed in manifest.yaml; for instructor reference, not redistribution.',
             'items': entries}
    index_path.write_text(json.dumps(index, indent=2, ensure_ascii=False) + '\n')
    failed = [e for e in entries if e['status'] != 'downloaded']
    print(f'{source_id}: {len(entries) - len(failed)} downloaded, {len(failed)} failed')
    return failed


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('sources', nargs='*', default=DEFAULT_SOURCES)
    parser.add_argument('--refresh', action='store_true', help='re-download files that already exist')
    args = parser.parse_args()
    failed = [f for s in args.sources for f in download_source(s, args.refresh)]
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()
