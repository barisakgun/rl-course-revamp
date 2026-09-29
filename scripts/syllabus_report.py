#!/usr/bin/env python3
"""Export the editable syllabus DOCX to Markdown and check its recorded review.

Uses only the Python standard library; run with the documents runtime Python.
Does not edit the DOCX or declare a visual review automatically.
"""
import argparse
import hashlib
import json
from pathlib import Path
from xml.etree import ElementTree as ET
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
DOCX = ROOT/'course/syllabus/syllabusFall26_draft.docx'
NS = {'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
W = '{'+NS['w']+'}'


def inspect():
    with ZipFile(DOCX) as z:
        body=ET.fromstring(z.read('word/document.xml')).find('w:body',NS)
    text=lambda e: ''.join(t.text or '' for t in e.iter(W+'t'))
    paragraphs=[];tables=[];md=[]
    for e in body:
        if e.tag==W+'p':
            value=text(e)
            if not value: continue
            paragraphs.append(value)
            style=e.find('w:pPr/w:pStyle',NS)
            sid=style.get(W+'val','') if style is not None else ''
            prefix={'Title':'# ','Heading1':'## ','Heading2':'### '}.get(sid,'')
            if e.find('w:pPr/w:numPr',NS) is not None: prefix='- '
            # Preserve exact DOCX text for hash checks; normalize Markdown line endings.
            md.append(prefix+value.rstrip())
        elif e.tag==W+'tbl':
            rows=[[text(c) for c in r.findall('w:tc',NS)] for r in e.findall('w:tr',NS)]
            tables.append(rows)
            escape=lambda v:v.replace('|','\\|').replace('\n','<br>')
            rendered=['| '+' | '.join(escape(v) for v in row)+' |' for row in rows]
            rendered.insert(1,'| '+' | '.join('---' for _ in rows[0])+' |')
            md.append('\n'.join(rendered))
    return paragraphs,tables,'\n\n'.join(md)+'\n'


def check_review(paragraphs):
    review=json.loads((ROOT/'analysis/syllabus_verification.json').read_text())
    hashes={hashlib.sha256(p.encode()).hexdigest() for p in paragraphs}
    assert all(p['sha256'] in hashes for p in review['preserved_paragraphs']), 'Preserved official/admin paragraph changed'
    assert hashlib.sha256(DOCX.read_bytes()).hexdigest()==review['visual_review']['docx_sha256'], 'DOCX changed after visual review; render and inspect again'
    assert review['visual_review']['all_pages_inspected'] is True
    assert len(review['visual_review']['pages'])==review['visual_review']['page_count']
    return review


def check_content(cfg,policy,grading,project,scheduled):
    """Check actual DOCX content against current accepted facts supplied by the audit."""
    paragraphs,tables,_=inspect();full='\n'.join(paragraphs)
    lookup={t[0][0]:t for t in tables}
    for o in cfg['learning_outcomes']:
        assert o['id']+'. '+o['text'][0].upper()+o['text'][1:] in paragraphs,o['id']
    rows=lookup['Task'][1:]
    plans={s['id']:s for s in scheduled}
    assert rows==[[a['id'],a['title'],plans[a['id']]['release'],plans[a['id']]['deadline']] for a in policy['assignments']]
    project_rows=lookup['Milestone'][1:]
    number=lambda n:str(int(n)) if int(n)==n else str(n)
    assert project_rows==[[m['name'],'Week '+str(m.get('week',m.get('target_week')))+(' ('+m['placement']+')' if 'placement' in m else ''),m['length'],number(m['weight_percent'])+'%'] for m in project['milestones']]
    weights={r[0]:r[2] for r in lookup['Component'][1:]}
    for k,v in grading['categories_percent'].items():assert weights[k.title()]==f'{v}%'
    exams=lookup['Exam'][1:]
    weeks=[e['window_weeks'][0] for e in grading['midterms']]+[grading['third_midterm']['current_semester_alternative']['week']]
    assert [r[1] for r in exams]==['Week '+str(w) for w in weeks]
    assert grading['midterm_weights_percent']==[15,15,15] and '15% each' in str(lookup['Component'])
    assert policy['aggregation']['counted_count']==3 and policy['aggregation']['offered_count']==4
    for phrase in ['highest three normalized scores','Missing submissions count as zero','completing all four is not required',
                   'at least 21 days','released after its relevant concepts','one week before letter grades',
                   'online, TA-led and recorded in Week 14','only its own slot','TA and attending groups grade',
                   'No student readings are assigned','Two required background videos','seven days before use',
                   'Weeks 4, 8 and 11','There is no final exam','one-shot or few-shot delegation',
                   'not automatically extended to projects','Exact dates, durations and arrangements are TBA']:
        assert phrase in full,phrase
    for req in policy['llm_use']['report_requirements']:assert req in paragraphs
    assert 'excludes bandits' in exams[1][2] and 'excludes LLM RL' in exams[2][2]
    assert 'Required book:' not in full and 'early final' not in full
    return check_review(paragraphs)


def build():
    paragraphs,_,body=inspect();check_review(paragraphs)
    return (ROOT/'course/syllabus/template.md').read_text().replace('{{syllabus_content}}',body.rstrip())


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args()
    content=build();target=ROOT/'output/syllabus.md'
    if args.check:assert target.read_text()==content,'Stale syllabus Markdown view'
    else:target.write_text(content)
    print('Syllabus Markdown matches DOCX; preserved text and recorded visual-review hash verified.')


if __name__=='__main__':main()
