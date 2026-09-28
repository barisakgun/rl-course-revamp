#!/usr/bin/env python3
"""Extract already inventoried PDFs for Phase 2 inspection; never edit sources.

Local/previously cached PDFs need no network. --network permits fetching the
inventoried teaching/assessment PDFs missing from the temporary cache. Full PDF
text stays temporary; analysis/phase2/corpus.json stores provenance and hashes.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import yaml
from phase1_collect import fetch

ROOT=Path(__file__).resolve().parents[1]
CACHE=Path(tempfile.gettempdir())/'rl-phase1-cache'
OUT=ROOT/'analysis/phase2/corpus.json'
KINDS={'lecture_slides','discussion_slides','assignment','exam','exam_solutions','project_guidelines','syllabus','course_administration'}


def inspect(task,network):
    sid,m=task
    rec={k:m[k] for k in ['id','title','material_type','instructional_use','offering','path','url','sequence','sequence_label'] if k in m}
    rec['source_id']=sid
    rec['manifest_path']=f'sources/{sid}/manifest.yaml' if sid!='rl_book' else 'config/sources.yaml'
    rec['checked_at']=datetime.now(timezone.utc).isoformat(timespec='seconds')
    path=ROOT/m['path'] if 'path'in m else CACHE/(m.get('remote_sha256','missing')+'.pdf')
    # Persisted corpus metadata allows reuse of newly inspected PDFs.
    old=PREVIOUS.get((sid,m['id']),{})
    if not path.exists() and old.get('sha256'):path=CACHE/(old['sha256']+'.pdf')
    if not path.exists():
        if not network:return dict(rec,status='not_cached')
        response,access=fetch(m['url'])
        rec['access']=access
        if response is None:return dict(rec,status=access['status'])
        if not response.ok:
            response.close();return dict(rec,status=access['status'])
        data=response.content;response.close()
        if not data.startswith(b'%PDF'):return dict(rec,status='non_pdf_response')
        path=CACHE/(hashlib.sha256(data).hexdigest()+'.pdf');path.write_bytes(data)
    digest=hashlib.sha256(path.read_bytes()).hexdigest()
    result=subprocess.run(['pdftotext','-layout',str(path),'-'],capture_output=True,text=True)
    if result.returncode:return dict(rec,status='extraction_failed',detail=result.stderr)
    (CACHE/(digest+'.txt')).write_text(result.stdout)
    pages=result.stdout.split('\f')
    if not pages[-1].strip():pages.pop()
    rec.update(status='text_extracted',sha256=digest,pdf_pages=len(pages),text_characters=len(result.stdout))
    print(sid,m['id'],len(pages),'pages',m['title'],flush=True)
    return rec


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--network',action='store_true');args=p.parse_args()
    PREVIOUS={(r['source_id'],r['id']):r for r in json.loads(OUT.read_text())} if OUT.exists() else {}
    tasks=[]
    for src in yaml.safe_load((ROOT/'config/sources.yaml').read_text())['sources']:
        manifest=yaml.safe_load((ROOT/'sources'/src['id']/'manifest.yaml').read_text())
        for m in manifest['materials']:
            if m['material_type'] in KINDS and (m.get('path') or m.get('url','')).lower().endswith('.pdf'):tasks.append((src['id'],m))
    tasks.append(('rl_book',dict(id='rl_book',title='Reinforcement Learning: An Introduction',material_type='book',instructional_use='reference_not_course_evidence',path='sources/RLbook2020.pdf')))
    CACHE.mkdir(exist_ok=True)
    with ThreadPoolExecutor(max_workers=3) as pool:records=list(pool.map(lambda task:inspect(task,args.network),tasks))
    OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(records,indent=2,ensure_ascii=False)+'\n')
    print('Inspected',sum(r['status']=='text_extracted' for r in records),'of',len(records),'PDFs')
