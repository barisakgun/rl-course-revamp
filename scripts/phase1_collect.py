#!/usr/bin/env python3
"""Bounded Phase 1 inventory helpers; no topic normalization or curriculum edits.

Requires requests, beautifulsoup4, PyYAML; local/PDF inspection uses Poppler.
Pages retain link/heading/table indexes, not full third-party documents.
Network commands honor robots.txt, do not authenticate, and do not execute code.
"""
import argparse
import hashlib
import json
import re
import subprocess
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlsplit, urldefrag
from urllib.robotparser import RobotFileParser

import requests
import yaml
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
CACHE = Path(tempfile.gettempdir()) / 'rl-phase1-cache'
CACHE.mkdir(exist_ok=True)
UA = 'RLCourseInventory/1.0'
ROBOTS = {}
SEEDS = {
    'silver_rl': [('teaching', 'https://davidstarsilver.wordpress.com/teaching/')],
    'berkeley_cs285': [('home', 'https://rail.eecs.berkeley.edu/deeprlcourse/'),
        ('syllabus', 'https://rail.eecs.berkeley.edu/deeprlcourse/syllabus/'),
        ('resources', 'https://rail.eecs.berkeley.edu/deeprlcourse/resources/'),
        ('calendar', 'https://rail.eecs.berkeley.edu/deeprlcourse/calendar/')],
    'stanford_cs234': [('home', 'https://web.stanford.edu/class/cs234/'),
        ('modules', 'https://web.stanford.edu/class/cs234/modules.html'),
        ('assignments', 'https://web.stanford.edu/class/cs234/assignments.html'),
        ('project', 'https://web.stanford.edu/class/cs234/project.html'),
        ('scpd', 'https://web.stanford.edu/class/cs234/scpd.html'),
        ('faq', 'https://web.stanford.edu/class/cs234/faq.html')],
    'stanford_cs224r': [('home', 'https://cs224r.stanford.edu/'),
        ('projects', 'https://cs224r.stanford.edu/projects/cs224r_final_projects.html')],
}


def now():
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')


def policy(url):
    parts = urlsplit(url)
    origin = f'{parts.scheme}://{parts.netloc}'
    if origin not in ROBOTS:
        robot_url = origin + '/robots.txt'
        try:
            response = requests.get(robot_url, headers={'User-Agent': UA}, timeout=15)
            rp = RobotFileParser()
            if response.status_code == 200:
                rp.parse(response.text.splitlines())
                mode = 'parsed'
            elif response.status_code == 404:
                rp.parse([])
                mode = 'not_present_404'
            else:
                rp = None
                mode = f'unknown_http_{response.status_code}'
            ROBOTS[origin] = (rp, {'url': robot_url, 'status': mode, 'checked_at': now()})
        except requests.RequestException as exc:
            ROBOTS[origin] = (None, {'url': robot_url, 'status': 'unknown_transport_error', 'detail': str(exc), 'checked_at': now()})
    rp, record = ROBOTS[origin]
    # Do not crawl automatically when policy retrieval is unresolved.
    return rp is not None and rp.can_fetch(UA, url), record


def fetch(url, method='GET'):
    allowed, robots = policy(url)
    if not allowed:
        return None, {'url': url, 'checked_at': now(), 'status': 'not_fetched_robots_policy', 'robots': robots}
    try:
        r = requests.request(method, url, headers={'User-Agent': UA}, timeout=25,
                             allow_redirects=False, stream=True)
        for _ in range(5):
            if not r.is_redirect:
                break
            redirected = urljoin(r.url, r.headers['Location'])
            r.close()
            allowed, redirect_policy = policy(redirected)
            if not allowed:
                return None, {'url': url, 'resolved_url': redirected, 'checked_at': now(),
                              'status': 'not_fetched_redirect_policy', 'robots': redirect_policy}
            r = requests.request(method, redirected, headers={'User-Agent': UA}, timeout=25,
                                 allow_redirects=False, stream=True)
        return r, {'url': url, 'resolved_url': r.url, 'checked_at': now(),
                   'http_status': r.status_code, 'content_type': r.headers.get('Content-Type'),
                   'status': 'reachable' if r.ok else 'http_error', 'robots': robots}
    except requests.RequestException as exc:
        return None, {'url': url, 'checked_at': now(), 'status': 'transport_error', 'detail': str(exc), 'robots': robots}


def page(source, slug, url):
    r, record = fetch(url)
    if r is not None and r.ok:
        content = r.content
        record['sha256_of_retrieved_html'] = hashlib.sha256(content).hexdigest()
        soup = BeautifulSoup(content, 'html.parser')
        for node in soup(['script', 'style']):
            node.decompose()
        record['title'] = soup.title.get_text(' ', strip=True) if soup.title else ''
        record['headings'] = [h.get_text(' ', strip=True) for h in soup.find_all(re.compile('^h[1-6]$'))]
        record['links'] = []
        for i, a in enumerate(soup.find_all('a', href=True)):
            href = urljoin(r.url, a['href'])
            if not href.startswith(('http://', 'https://')):
                continue
            parent = a.find_parent(['tr', 'li', 'p'])
            heading = a.find_previous(re.compile('^h[1-6]$'))
            record['links'].append({'index': i, 'label': a.get_text(' ', strip=True), 'url': href,
                'heading': heading.get_text(' ', strip=True) if heading else '',
                'context': parent.get_text(' ', strip=True)[:2500] if parent else ''})
        record['tables'] = [[tr.get_text(' ', strip=True) for tr in table.find_all('tr')] for table in soup.find_all('table')]
        # Full page text is temporary inspection material, not a repository mirror.
        (CACHE / f'{source}-{slug}.txt').write_text(soup.get_text('\n', strip=True))
        r.close()
    save(ROOT / 'sources' / source / 'snapshots' / f'{slug}_index.json', record)
    print(source, slug, record['status'], len(record.get('links', [])), 'links', flush=True)
    time.sleep(0.25)


def local():
    config = yaml.safe_load((ROOT / 'config/sources.yaml').read_text())
    for source in config['sources']:
        if 'path' not in source:
            continue
        base = ROOT / source['path']
        records = []
        for p in sorted(base.rglob('*')):
            if not p.is_file() or 'snapshots' in p.relative_to(base).parts or p.name in ['manifest.yaml', 'README.md', '.DS_Store']:
                continue
            content = p.read_bytes()
            rec = {'path': str(p.relative_to(ROOT)), 'size_bytes': len(content), 'sha256': hashlib.sha256(content).hexdigest(), 'inspected_at': now()}
            if p.suffix.lower() == '.pdf':
                info = subprocess.run(['pdfinfo', str(p)], capture_output=True, text=True)
                rec['pdfinfo_exit_code'] = info.returncode
                rec['pdf_metadata'] = dict(line.split(':', 1) for line in info.stdout.splitlines() if ':' in line)
                rec['pdf_metadata'] = {k:v.strip() for k,v in rec['pdf_metadata'].items()}
                text = subprocess.run(['pdftotext', '-layout', str(p), '-'], capture_output=True, text=True)
                rec['text_extraction_exit_code'] = text.returncode
                rec['text_characters'] = len(text.stdout)
                rec['first_page_excerpt'] = text.stdout.split('\f')[0][:900]
                (CACHE / (rec['sha256'] + '.txt')).write_text(text.stdout)
                rec['embedded_urls'] = sorted(set(re.findall(r'https?://[^\s<>]+', text.stdout)))
            records.append(rec)
        save(base / 'snapshots/local_inventory.json', {'inspected_at': now(), 'source_id': source['id'], 'files': records})
        print(source['id'], len(records), 'local files', flush=True)


def probe(source):
    manifest = yaml.safe_load((ROOT / 'sources' / source / 'manifest.yaml').read_text())
    urls = sorted({urldefrag(x['url'])[0] for x in manifest['materials'] if x.get('url') and x.get('check_url', True)})
    results = []
    for url in urls:
        r, rec = fetch(url, 'HEAD')
        if r is not None:
            r.close()
        if rec.get('http_status') in [403, 405, 501]:
            r, rec = fetch(url)
            if r is not None:
                rec['signature'] = next(r.iter_content(32), b'').decode('latin1', errors='replace')
                r.close()
        rec['verification_level'] = 'http_metadata_only_not_content_review'
        results.append(rec)
        print(source, rec['status'], rec.get('http_status'), url, flush=True)
        time.sleep(0.15)
    save(ROOT / 'sources' / source / 'snapshots/link_checks.json', results)


def pdf(source, url):
    r, rec = fetch(url)
    if r is not None and r.ok:
        data = r.content
        r.close()
        if data.startswith(b'%PDF'):
            digest = hashlib.sha256(data).hexdigest()
            path = CACHE / (digest + '.pdf')
            path.write_bytes(data)
            text = subprocess.run(['pdftotext', '-layout', str(path), '-'], capture_output=True, text=True)
            (CACHE / (digest + '.txt')).write_text(text.stdout)
            info = subprocess.run(['pdfinfo', str(path)], capture_output=True, text=True)
            links = subprocess.run(['pdfinfo', '-url', str(path)], capture_output=True, text=True)
            rec.update(sha256=digest, pdfinfo=info.stdout, first_page_excerpt=text.stdout.split('\f')[0][:800],
                       embedded_urls=sorted(set(re.findall(r'https?://[^\s<>]+', text.stdout))),
                       annotation_urls=sorted(set(re.findall(r'https?://\S+', links.stdout))),
                       verification_level='pdf_text_inspected', text_extraction_exit_code=text.returncode)
        else:
            rec['status'] = 'unexpected_non_pdf_response'
    name = hashlib.sha256(url.encode()).hexdigest()[:16]
    save(ROOT / 'sources' / source / 'snapshots' / f'pdf_{name}.json', rec)
    print(source, rec['status'], url, flush=True)


def pdf_set():
    for sid in SEEDS:
        urls = set()
        for index in (ROOT / 'sources' / sid / 'snapshots').glob('*_index.json'):
            for link in json.loads(index.read_text()).get('links', []):
                url = link['url']
                if urlsplit(url).path.endswith('.pdf') and any(part in url.lower() for part in
                        ['easy21', '/homeworks/', '/assignments/', '/material/hw', 'project_outline',
                         'default_final_project', '_project_guidelines']):
                    urls.add(url)
        for url in sorted(urls):
            pdf(sid, url)
            time.sleep(0.25)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['pages', 'page', 'local', 'probe', 'pdf', 'pdf-set'])
    parser.add_argument('args', nargs='*')
    args = parser.parse_args()
    if args.mode == 'pages':
        for sid, pages in SEEDS.items():
            for slug, url in pages:
                page(sid, slug, url)
    elif args.mode == 'page':
        page(*args.args)
    elif args.mode == 'local':
        local()
    elif args.mode == 'probe':
        probe(*args.args)
    elif args.mode == 'pdf-set':
        pdf_set()
    else:
        pdf(*args.args)
