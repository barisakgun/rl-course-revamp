"""Read-only semantic PPTX comparison, independent of Markdown extraction.

Usage: python3 scripts/compare_pptx_content_chatgpt.py original.pptx rebuilt.pptx
Print JSON to stdout. Compares normalized visible paragraphs (ignoring object
ordering), notes, table cells, text-link targets and embedded picture bytes.
This is not a visual, animation, accessibility or formatting equivalence test.
"""
import argparse
from collections import Counter
import hashlib
import json
import posixpath
from pathlib import Path
from urllib.parse import unquote
from xml.etree import ElementTree as E
from zipfile import ZipFile

NS = {'p':'http://schemas.openxmlformats.org/presentationml/2006/main',
      'a':'http://schemas.openxmlformats.org/drawingml/2006/main',
      'r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
R = '{'+NS['r']+'}'

def inventory(file):
    with ZipFile(file) as z:
        def rels(owner):
            folder, name = posixpath.split(owner)
            part = folder+'/_rels/'+name+'.rels'
            if part not in z.namelist(): return {}
            return {r.get('Id'): (r.get('Target') if r.get('TargetMode')=='External' else
                    posixpath.normpath(posixpath.join(folder,unquote(r.get('Target')))).lstrip('/'),
                    r.get('Type'),r.get('TargetMode')=='External') for r in E.fromstring(z.read(part))}
        def paragraphs(node):
            # Normalize whitespace but retain paragraph text and duplicates.
            return [' '.join(''.join(t.text or '' for t in p.findall('.//a:t',NS)).split())
                    for p in node.findall('.//a:p',NS) if ''.join(p.itertext()).strip()]
        presentation=E.fromstring(z.read('ppt/presentation.xml'))
        links=rels('ppt/presentation.xml'); slides=[]
        for s in presentation.findall('p:sldIdLst/p:sldId',NS):
            part=links[s.get(R+'id')][0]; xml=E.fromstring(z.read(part)); relationships=rels(part)
            texts=[v for v in paragraphs(xml) if v]
            notes=[]
            for target,kind,external in relationships.values():
                if kind.endswith('/notesSlide') and not external:
                    note=E.fromstring(z.read(target))
                    for shape in note.findall('.//p:sp',NS):
                        ph=shape.find('p:nvSpPr/p:nvPr/p:ph',NS)
                        if ph is not None and ph.get('type') in {'sldImg','sldNum','dt','hdr','ftr'}:continue
                        notes.extend(v for v in paragraphs(shape) if v)
            images=[]
            for blip in xml.findall('.//p:pic/p:blipFill/a:blip',NS):
                target=relationships[blip.get(R+'embed')][0]
                images.append(hashlib.sha256(z.read(target)).hexdigest())
            tables=[[[paragraphs(cell) for cell in row.findall('a:tc',NS)] for row in table.findall('a:tr',NS)] for table in xml.findall('.//a:tbl',NS)]
            hyperlinks=[relationships[h.get(R+'id')][0] for h in xml.findall('.//a:rPr/a:hlinkClick',NS) if h.get(R+'id') in relationships]
            slides.append({'title':texts[0], 'paragraphs':dict(Counter(texts)), 'notes':notes,'tables':tables,
                           'links':dict(Counter(hyperlinks)), 'images':dict(Counter(images)), 'hidden':xml.get('show')=='0'})
    return slides

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('original',type=Path);parser.add_argument('rebuilt',type=Path)
    args=parser.parse_args(); a,b=inventory(args.original),inventory(args.rebuilt)
    result={'original_sha256':hashlib.sha256(args.original.read_bytes()).hexdigest(),
            'rebuilt_sha256':hashlib.sha256(args.rebuilt.read_bytes()).hexdigest(),
            'slide_counts':[len(a),len(b)],'slides':[]}
    for n,(x,y) in enumerate(zip(a,b),1):
        checks={key:x[key]==y[key] for key in x}
        differences={key:{'original':x[key],'rebuilt':y[key]} for key in x if not checks[key]}
        result['slides'].append({'slide':n,'title':x['title'],'checks':checks,'differences':differences})
    result['all_content_checks_pass']=len(a)==len(b) and all(all(s['checks'].values()) for s in result['slides'])
    result['totals']={key:sum(sum(s[key].values()) if isinstance(s[key],dict) else len(s[key]) for s in a) for key in ['paragraphs','notes','tables','links','images']}
    print(json.dumps(result,indent=2,ensure_ascii=False))
    return 0 if result['all_content_checks_pass'] else 1

if __name__=='__main__':raise SystemExit(main())
