#!/usr/bin/env python3
"""Export the frozen syllabus to Markdown without changing either source artifact.

Requires Python 3 and PyYAML. Identity is checked against accepted decisions,
not against the historical draft's visual-review record.
"""
import argparse
import hashlib
import re
from pathlib import Path
from xml.etree import ElementTree as ET
from zipfile import ZipFile

import yaml

ROOT = Path(__file__).resolve().parents[1]
NS = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
W = '{' + NS['w'] + '}'
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'


def freeze_record():
    return yaml.safe_load((ROOT/'decisions/syllabus_decisions.yaml').read_text())


def check_frozen():
    record = freeze_record()
    assert record['state'] == 'frozen', 'Syllabus is not recorded as frozen'
    for artifact in record['artifacts'].values():
        path = ROOT/artifact['path']
        assert path.is_file(), f'Missing frozen artifact: {path}'
        assert hashlib.sha256(path.read_bytes()).hexdigest() == artifact['sha256'], (
            f'Frozen artifact changed: {path}. Review with the instructor; do not auto-update fingerprints.')
    return record


def val(element, path, default=None):
    item = element.find(path, NS)
    return item.get(W+'val', default) if item is not None else default


def plain(element):
    return ''.join(e.text or '' if e.tag == W+'t' else '\n' if e.tag in (W+'br', W+'cr')
                   else '\t' if e.tag == W+'tab' else '' for e in element.iter())


def escape(text):
    return re.sub(r'([\\`*_\[\]<>|])', r'\\\1', text)


def inline(element, links):
    parts = []
    for child in element:
        if child.tag == W+'hyperlink':
            label = escape(plain(child))
            target = links.get(child.get(R+'id'))
            parts.append(f'[{label}](<{target}>)' if target else label)
        elif child.tag == W+'r':
            parts.append(escape(plain(child)))
        elif child.tag not in (W+'pPr', W+'rPr'):
            parts.append(inline(child, links))
    return ''.join(parts).strip().replace('\n', '<br>')


def heading_prefix(element):
    # The instructor uses direct font formatting, including inconsistent outline
    # levels on body paragraphs. Font size/bold distinguish actual headings.
    style = val(element, 'w:pPr/w:pStyle', '')
    if style == 'Title':
        return '# '
    if re.fullmatch(r'Heading[1-6]', style):
        return '#' * min(int(style[-1])+1, 6) + ' '
    sizes = [int(e.get(W+'val')) for e in element.findall('.//w:sz', NS)]
    if sizes and max(sizes) >= 28:
        return '# ' if max(sizes) >= 32 else '## '
    runs = [e for e in element.findall('.//w:r', NS) if plain(e).strip()]
    # An empty w:b means true.
    bold = runs and all(e.find('w:rPr/w:b', NS) is not None and
                        val(e, 'w:rPr/w:b', 'true') not in ('false', '0', 'off') for e in runs)
    return '## ' if bold and element.find('w:pPr/w:outlineLvl', NS) is not None else ''


def inspect():
    docx = ROOT/freeze_record()['artifacts']['docx']['path']
    with ZipFile(docx) as z:
        body = ET.fromstring(z.read('word/document.xml')).find('w:body', NS)
        rels = ET.fromstring(z.read('word/_rels/document.xml.rels'))
        links = {e.get('Id'): e.get('Target') for e in rels if e.get('Type', '').endswith('/hyperlink')}
        numbering = ET.fromstring(z.read('word/numbering.xml'))
    abstracts = {e.get(W+'abstractNumId'): e for e in numbering.findall('w:abstractNum', NS)}
    nums = {e.get(W+'numId'): e for e in numbering.findall('w:num', NS)}
    counters = {}
    paragraphs, tables, md = [], [], []
    section = None
    for element in body:
        if element.tag == W+'p':
            value = plain(element).strip()
            if not value:
                continue
            paragraphs.append(value)
            prefix = heading_prefix(element)
            large_heading = any(int(e.get(W+'val')) >= 28 for e in element.findall('.//w:sz', NS))
            if large_heading:
                section = value
            elif section == 'Prerequisites' and element.find('w:pPr/w:numPr', NS) is None:
                # These smaller bold labels sit under the 14-point section heading.
                prefix = '### '
            num_id = val(element, 'w:pPr/w:numPr/w:numId')
            if num_id is not None:
                level = val(element, 'w:pPr/w:numPr/w:ilvl', '0')
                num = nums[num_id]
                abstract = abstracts[val(num, 'w:abstractNumId')]
                definition = abstract.find(f'w:lvl[@w:ilvl="{level}"]', NS)
                fmt = val(definition, 'w:numFmt')
                assert level == '0' and fmt in ('bullet', 'decimal'), 'Review unsupported list format'
                if fmt == 'bullet':
                    prefix = '- '
                else:
                    start = val(num, f'w:lvlOverride[@w:ilvl="{level}"]/w:startOverride',
                                val(definition, 'w:start', '1'))
                    key = (num_id, level)
                    counters[key] = counters.get(key, int(start)-1)+1
                    prefix = f'{counters[key]}. '
            md.append(prefix+inline(element, links))
        elif element.tag == W+'tbl':
            rows, rendered_rows = [], []
            width = len(element.findall('w:tblGrid/w:gridCol', NS))
            for row in element.findall('w:tr', NS):
                cells, rendered_cells = [], []
                for cell in row.findall('w:tc', NS):
                    ps = cell.findall('w:p', NS)
                    cells.append('\n'.join(plain(p).strip() for p in ps))
                    rendered_cells.append('<br>'.join(inline(p, links) for p in ps))
                    span = int(val(cell, 'w:tcPr/w:gridSpan', '1'))
                    cells.extend(['']*(span-1))
                    rendered_cells.extend(['']*(span-1))
                assert len(cells) == width, 'Review unsupported table grid'
                rows.append(cells)
                rendered_rows.append('| '+' | '.join(rendered_cells)+' |')
            tables.append(rows)
            rendered_rows.insert(1, '| '+' | '.join(['---']*width)+' |')
            md.append('\n'.join(rendered_rows))
    return paragraphs, tables, '\n\n'.join(md)+'\n'


def check_content(cfg, policy, grading, project):
    """Check published facts only; omitted internal detail is not a syllabus promise."""
    record = check_frozen()
    paragraphs, tables, _ = inspect()
    full = '\n'.join(paragraphs)
    normalize = lambda s: s.strip().rstrip('.').casefold()
    start = paragraphs.index('Learning Outcomes')+1
    end = paragraphs.index('Textbook')
    assert [normalize(s) for s in paragraphs[start:end]] == [normalize(o['text']) for o in cfg['learning_outcomes']]
    grade_table = next(t for t in tables if t[0] == ['Type', 'Description', 'Grade %'])
    weights = {r[0]: r[-1] for r in grade_table[1:]}
    for key, label in [('assignments', 'Assignments'), ('midterms', 'Midterms'), ('project', 'Final Project')]:
        assert float(weights[label]) == grading['categories_percent'][key], label
    assert float(weights['Total']) == sum(grading['categories_percent'].values()) == 100
    exam_description = next(r[1] for r in grade_table if r[0] == 'Midterms')
    count, weight = map(int, re.fullmatch(r'(\d+) Midterms, (\d+)% each', exam_description).groups())
    assert grading['midterm_weights_percent'] == [weight]*count
    assert not grading['final_exam_required'] and 'There will be no final exam.' in full
    offered = re.search(r'There are (\d+) planned programming assignments', full)
    dropped = re.search(r'If there are more than (\d+), the lowest one will be discarded', full)
    assert int(offered[1]) == policy['aggregation']['offered_count']
    assert int(dropped[1]) == policy['aggregation']['counted_count']
    assert 'The number may change depending on how the semester proceeds.' in full
    assert 'plan_scope' in policy['aggregation']
    milestones = [float(m[1]) for p in paragraphs if (m := re.fullmatch(r'.+ \((\d+(?:\.\d+)?)%\)', p))]
    assert milestones == [m['weight_percent'] for m in project['milestones']]
    assert project['team_size']['encouraged'] == [2, 3] and 'Teams of 2–3 are encouraged' in full
    assert project['team_size']['case_by_case'] == [1, 4] and 'individual work and four-person teams may be considered' in full
    for phrase in ['LLMs may be used for coding and reports with disclosure.',
                   'An LLM-use report is required for each assignment and report.',
                   'The requirement details will be given before the first assignment/report.',
                   'For assignments, one-shot or few-shot delegation of the assignment solution receives no credit.',
                   'failure to do so is treated as plagiarism',
                   'these exams assess their knowledge of the material']:
        assert phrase in full, phrase
    assert policy['llm_use']['allowed']
    assert 'one-shot or few-shot delegation of the assignment solution' in policy['llm_use']['no_credit_rule']
    assert normalize(project['llm_use']['writing_quality']) in normalize(full)
    return {'freeze': record, 'checks': [
        'Frozen DOCX and instructor-produced PDF fingerprints match accepted decisions.',
        'All eight learning outcomes match configuration; 20/45/35 grading, three 15% midterms and no final exam agree with decisions.',
        'Four planned assignments and the conditional lowest-score drop agree with the current plan; syllabus discretion to change the count is preserved.',
        'Five project milestone weights and the team-size policy agree with decisions.',
        'Disclosure/report obligations, the assignment-specific no-credit rule and project-report writing policy are retained.',
        'Markdown preserves the final DOCX wording, hyperlinks, ordered/bulleted lists and table columns; omitted internal timing and release detail is not injected.'
    ]}


def build():
    check_frozen()
    _, _, body = inspect()
    return (ROOT/'course/syllabus/template.md').read_text().replace('{{syllabus_content}}', body.rstrip())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    content = build()
    target = ROOT/'output/syllabus.md'
    if args.check:
        assert target.read_text() == content, 'Stale syllabus Markdown view'
    else:
        target.write_text(content)
    print('Syllabus Markdown matches frozen DOCX; DOCX/PDF identity verified. No new visual review claimed.')


if __name__ == '__main__':
    main()
