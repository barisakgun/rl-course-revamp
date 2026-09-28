#!/usr/bin/env python3
"""Validate Phase 2 evidence and render deterministic views; no network or source writes."""
import argparse
from collections import defaultdict
import hashlib
import json
import os
from pathlib import Path
import re
from urllib.parse import quote

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = 'analysis/normalized_topics.yaml'
NAMES = {
    'current_course': 'Baseline', 'silver_rl': 'Silver',
    'berkeley_cs285': 'CS285', 'stanford_cs234': 'CS234',
    'stanford_cs224r': 'CS224R', 'foundations-deep-rl-abbeel': 'Abbeel',
    'sutton': 'Sutton/White',
}
CODES = {'explicitly-covered': 'E', 'brief-exposure': 'B', 'reading-only': 'R',
         'assessment-only': 'A', 'unknown': '?', 'not-found': 'NF'}
DEPTH = {'developed': 'd', 'concise': 'c', 'mention': 'm', 'unknown': '?'}


class UniqueLoader(yaml.SafeLoader):
    pass


def mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f'Duplicate YAML key: {key!r}, line {key_node.start_mark.line + 1}')
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)


def read_yaml(path):
    return yaml.load((ROOT / path).read_text(), Loader=UniqueLoader)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def pointer(doc, value):
    for part in value.strip('/').split('/'):
        part = part.replace('~1', '/').replace('~0', '~')
        doc = doc[int(part)] if isinstance(doc, list) else doc[part]
    return doc


def plan_leaves(plan):
    for i, week in enumerate(plan['weekly_plan']):
        for group in ('topics', 'exposure', 'optional', 'transition'):
            for j, phrase in enumerate(week.get(group, [])):
                yield f'/weekly_plan/{i}/{group}/{j}', phrase
    for i, video in enumerate(plan['videos']):
        for j, phrase in enumerate(video['content']):
            yield f'/videos/{i}/content/{j}', phrase
    for i, assignment in enumerate(plan['assessment_hypotheses']['assignments']):
        yield f'/assessment_hypotheses/assignments/{i}/text', assignment['text']


def validate(data):
    # All project YAML is parse-checked, but never rewritten.
    for path in sorted(ROOT.rglob('*.yaml')):
        if '.git' not in path.parts:
            read_yaml(path.relative_to(ROOT))
    for path in sorted(ROOT.rglob('*.yml')):
        if '.git' not in path.parts:
            read_yaml(path.relative_to(ROOT))
    configured = read_yaml('config/sources.yaml')
    source_ids = {s['id'] for s in configured['sources']}
    require(set(data['sources']) == source_ids, 'Configured source registry mismatch')
    require(set(data['books']) == {b['id'] for b in configured['books']}, 'Book registry mismatch')
    require(data['phase'] == 2 and data['status'] == 'complete', 'Phase 2 is not complete')
    require(not data['phase_boundary']['phase3_started'], 'Phase 3 boundary crossed')
    materials = {}
    for sid, info in data['sources'].items():
        manifest = read_yaml(info['manifest'])
        require(manifest['source_id'] == sid, f'Manifest identity: {sid}')
        require((ROOT / info['phase1_summary']).is_file(), f'Missing Phase 1 summary: {sid}')
        ids = [m['id'] for m in manifest['materials']]
        require(len(ids) == len(set(ids)), f'Duplicate material IDs: {sid}')
        materials[sid] = {m['id']: m for m in manifest['materials']}
        require(set(info['general_reading_material_ids']) <= set(ids), f'Invalid reading IDs: {sid}')
    corpus_list = json.loads((ROOT / data['inspection']['corpus']).read_text())
    corpus = {(r['source_id'], r['id']): r for r in corpus_list}
    require(len(corpus) == len(corpus_list), 'Duplicate corpus IDs')
    for record in corpus_list:
        require(record['status'] == 'text_extracted', f'Unextracted PDF: {record["id"]}')
        if record['source_id'] in source_ids:
            material = materials[record['source_id']][record['id']]
            for field in ('path', 'url'):
                if field in record:
                    require(record[field] == material.get(field), f'Corpus provenance changed: {record["id"]}')
        if 'path' in record:
            require(hashlib.sha256((ROOT / record['path']).read_bytes()).hexdigest() == record['sha256'],
                    f'Local PDF changed: {record["path"]}')
    for bid, book in data['books'].items():
        require(book['path'] == next(b['path'] for b in configured['books'] if b['id'] == bid), f'Book path: {bid}')
        require(hashlib.sha256((ROOT / book['path']).read_bytes()).hexdigest() == book['sha256'],
                f'Book changed: {bid}')
        require(not (ROOT / 'sources' / bid / 'manifest.yaml').exists(), 'Book must not have a manifest')
    plan = read_yaml('config/provisional_plan.yaml')
    taxonomy = read_yaml('config/taxonomy.yaml')
    topics = data['topics']
    topic_ids = {t['id'] for t in topics}
    require(len(topic_ids) == len(topics), 'Duplicate topic ID')
    mapped_pointers = set()
    evidence_count = 0
    for topic in topics:
        tid = topic['id']
        require(re.fullmatch('[a-z][a-z0-9_]*', tid), f'Invalid topic ID: {tid}')
        require(topic['name'] and topic['definition'], f'Missing definition: {tid}')
        require(not set(topic) & {'role', 'mastery', 'delivery', 'decision_state'}, f'Decision field: {tid}')
        require(set(topic['sources']) == source_ids, f'Incomplete source matrix: {tid}')
        for occurrence in topic['provisional_plan']:
            require(occurrence['path'] == 'config/provisional_plan.yaml', f'Unexpected plan path: {tid}')
            require(pointer(plan, occurrence['pointer']) == occurrence['source_phrase'], f'Stale plan mapping: {tid}')
            require(occurrence['state'] in ('provisional', 'non-binding'), f'Accepted plan mapping: {tid}')
            mapped_pointers.add(occurrence['pointer'])
        for bid, book_map in topic['book_mapping'].items():
            book = data['books'][bid]
            require(bool(book_map['references']) == (book_map['status'] == 'mapped'), f'Book status: {tid}')
            for ref in book_map['references']:
                a, b = ref['pdf_pages']
                require(1 <= a <= b <= book['pdf_pages'], f'Book pages: {tid}')
                require(ref['pdf_pages'] == [n + book['printed_to_pdf_offset'] for n in ref['printed_pages']],
                        f'Book offset: {tid}')
                require(str(ref['section']).split('.')[0] == str(ref['chapter']), f'Book chapter: {tid}')
                require(ref['section_title'] and ref['relationship'] in ('direct', 'related_background'), f'Book relation: {tid}')
        for sid, observation in topic['sources'].items():
            label = f'{tid}/{sid}'
            coverage = observation['coverage']
            require(coverage in CODES, f'Coverage: {label}')
            require(observation['confidence'] in ('high', 'medium', 'low'), f'Confidence: {label}')
            depth = observation['apparent_depth']
            require(depth['value'] in DEPTH and depth['basis'] == 'inference', f'Depth inference: {label}')
            require(depth['confidence'] in ('high', 'medium', 'low') and depth['rationale'], f'Depth confidence: {label}')
            evidence = observation['evidence']
            evidence_count += len(evidence)
            kinds = {e['evidence_kind'] for e in evidence}
            if coverage in ('explicitly-covered', 'brief-exposure'):
                require('teaching' in kinds, f'Missing teaching evidence: {label}')
                require(evidence[depth['evidence_index']]['evidence_kind'] == 'teaching', f'Depth evidence: {label}')
            elif coverage == 'reading-only':
                require('reading_pointer' in kinds and 'teaching' not in kinds, f'Reading-only evidence: {label}')
            elif coverage == 'assessment-only':
                require(bool(kinds & {'assessment', 'project'}) and 'teaching' not in kinds, f'Assessment-only evidence: {label}')
            elif coverage == 'unknown':
                require(observation.get('scope_note'), f'Unknown scope: {label}')
            elif coverage == 'not-found':
                require(observation.get('reviewed_scope'), f'Negative claim without scope: {label}')
            sequence = sorted({e['source_order'] for e in evidence if e['evidence_kind'] == 'teaching' and 'source_order' in e})
            require(observation['sequence'] == sequence, f'Sequence inconsistent: {label}')
            for ev in evidence:
                require(ev['material_id'] in materials[sid], f'Unknown material: {label}/{ev["material_id"]}')
                material = materials[sid][ev['material_id']]
                require(ev['manifest'] == data['sources'][sid]['manifest'], f'Manifest citation: {label}')
                require(ev['claim'] and ev['basis'] in ('direct_artifact_content', 'direct_catalog_listing'), f'Evidence basis: {label}')
                for field in ('url', 'path'):
                    if field in ev:
                        require(ev[field] == material.get(field), f'Citation {field} mismatch: {label}')
                if 'pdf_pages' in ev:
                    record = corpus[(sid, ev['material_id'])]
                    a, b = ev['pdf_pages']
                    require(1 <= a <= b <= record['pdf_pages'], f'Out-of-range pages: {label}')
                else:
                    require(ev.get('locator') or ev.get('provenance'), f'No citation locator: {label}')
                if 'supporting_index' in ev:
                    require((ROOT / ev['supporting_index']).is_file(), f'Missing support: {label}')
                for origin in ev.get('provenance', []):
                    if 'index_path' in origin:
                        require((ROOT / origin['index_path']).is_file(), f'Missing catalog: {label}')
            assessment = observation['assessment']
            require(set(assessment['types']) <= set(taxonomy['assessment']) - {'none'}, f'Assessment taxonomy: {label}')
            require((assessment['status'] == 'observed') == bool(assessment['evidence']), f'Assessment status: {label}')
            for idx in assessment['evidence']:
                require(evidence[idx]['evidence_kind'] in ('assessment', 'project'), f'Assessment index: {label}')
            for idx in assessment.get('explicit_exclusions', []):
                require(evidence[idx]['evidence_kind'] == 'assessment_exclusion', f'Exclusion index: {label}')
            for reading in observation['readings']:
                require(evidence[reading['evidence_index']]['evidence_kind'] == 'reading_pointer', f'Reading index: {label}')
            project = observation['project_relationship']
            require((project['status'] == 'observed') == bool(project['evidence']), f'Project status: {label}')
            for idx in project['evidence']:
                require(evidence[idx]['evidence_kind'] == 'project', f'Project index: {label}')
    expected_pointers = {p for p, _ in plan_leaves(plan)}
    require(mapped_pointers == expected_pointers, f'Incomplete plan mapping: {expected_pointers - mapped_pointers}')
    for ambiguity in data['ambiguities']:
        require(set(ambiguity['topic_ids']) <= topic_ids, f'Ambiguity topic ID: {ambiguity["id"]}')
    # Optional session guard, not needed on another machine or future checkout.
    guard = Path('/private/tmp/rl_phase2_protected.json')
    protected_count = 0
    if guard.is_file():
        for path, digest in json.loads(guard.read_text()).items():
            require(hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest, f'Protected file changed: {path}')
            protected_count += 1
    return materials, corpus, plan, {'topics': len(topics), 'source_topic_pairs': len(topics) * len(source_ids),
        'positive_pairs': sum(s['coverage'] not in ('unknown', 'not-found') for t in topics for s in t['sources'].values()),
        'evidence_references': evidence_count, 'provisional_items': len(expected_pointers),
        'provisional_mappings': sum(len(t['provisional_plan']) for t in topics),
        'pdf_artifacts': len(corpus), 'book_mapped_topics': sum(bool(t['book_mapping']['rl_book']['references']) for t in topics),
        'ambiguities': len(data['ambiguities']), 'protected_files_verified': protected_count}


def esc(value):
    return str(value).replace('|', '\\|').replace('\n', ' ')


def local_link(path, output, fragment=''):
    return quote(os.path.relpath(ROOT / path, (ROOT / output).parent), safe='/') + fragment


def source_link(ev, output):
    catalog = next((p['index_path'] for p in ev.get('provenance', []) if 'index_path' in p), ev['manifest'])
    link = ev.get('url') or local_link(ev.get('path', catalog), output)
    if 'pdf_pages' in ev:
        link += '#page=' + str(ev['pdf_pages'][0])
    return link


def span(numbers):
    return str(numbers[0]) if numbers[0] == numbers[1] else f'{numbers[0]}–{numbers[1]}'


def topic_link(topic, output):
    return f'[{esc(topic["name"])}]({local_link("analysis/phase2/evidence_by_topic.md", output, "#" + topic["id"])})'


def header(title, output):
    return [f'# {title}', '', f'Generated by `scripts/phase2_report.py` from [normalized evidence]({local_link(DATA, output)}). Edit structured evidence, then regenerate.', '',
            'This is Phase 2 evidence organization. It assigns no redesigned-course role, mastery, delivery or inclusion decision.', '']


def book_refs(topic, data, output):
    result = []
    for ref in topic['book_mapping']['rl_book']['references']:
        link = local_link(data['books']['rl_book']['path'], output, '#page=' + str(ref['pdf_pages'][0]))
        result.append(f'[§{ref["section"]}, pp.{span(ref["printed_pages"])}]({link}) ({ref["relationship"].replace("_", " ")})')
    return '; '.join(result) or 'No direct mapping established'


def render(data, materials, corpus, plan, stats):
    outputs = {}
    output = 'analysis/topic_matrix.md'
    lines = header('Topic evidence matrix', output)
    lines += ['E = explicitly covered in inspected teaching artifacts; B = brief exposure; R = reading-only; A = assessment-only; ? = unknown; NF = not found in a specified scope.', '',
              'Cell format: **coverage/depth @ source order; assessment**. Inferred depth: d = developed, c = concise, m = mention, ? = unknown. Assessment: hw = assignment, ex = exam, pr = project. These codes do not imply workload or mastery.', '',
              'Every ? is an explicit evidence gap, not “not taught.” A positive cell describes inspected artifacts, not verified live delivery. Source order uses local deck/lecture labels; durations and numbering are not comparable across courses. Topic links open the detailed citations, reading associations and qualifiers.', '',
              'Related book background is distinguished from a direct topic match. Book references are independent of course reading assignments. Plan weeks/video/assignment mentions remain provisional and non-binding.', '',
              f'| Topic | {" | ".join(NAMES[s] for s in data["sources"])} | Provisional references | Book |',
              '|---|' + '---|' * (len(data['sources']) + 2)]
    for topic in data['topics']:
        cells = [topic_link(topic, output)]
        for sid in data['sources']:
            obs = topic['sources'][sid]
            cell = CODES[obs['coverage']]
            if obs['coverage'] != 'unknown':
                cell += '/' + DEPTH[obs['apparent_depth']['value']]
                if obs['sequence']:
                    cell += ' @' + ','.join(map(str, obs['sequence']))
                if obs['assessment']['types']:
                    cell += '; ' + ','.join({'assignment': 'hw', 'exam': 'ex', 'project': 'pr'}[x] for x in obs['assessment']['types'])
                if obs['readings']:
                    cell += '; rd'
            cells.append(cell)
        occurrences = topic['provisional_plan']
        parts = ['W' + str(w) for w in sorted({p['week'] for p in occurrences if 'week' in p})]
        if any('/videos/' in p['pointer'] for p in occurrences):
            parts.append('video')
        if any('/assessment_hypotheses/' in p['pointer'] for p in occurrences):
            parts.append('assignment hypothesis')
        cells += [', '.join(parts) or '—', book_refs(topic, data, output)]
        lines.append('| ' + ' | '.join(cells) + ' |')
    lines += ['', '## Treatment qualifiers', '']
    for a in data['ambiguities']:
        lines.append(f'- **{a["id"]}** ({a["status"]}): {a["description"]}')
    lines += ['', '[Evidence gaps and completion criteria](phase2_completion.md). No frequency-based curriculum ranking is produced.', '']
    outputs[output] = '\n'.join(lines)

    output = 'analysis/phase2/evidence_by_topic.md'
    lines = header('Topic definitions and source evidence', output)
    lines += ['Physical PDF page numbers are 1-based. Book references additionally show printed pages. Claims are paraphrased; page spans may contain several distinct concepts. Read the topic definition and any qualification before inferring equivalence.', '',
              'Per-topic citations link to source artifacts. Hashes, retrieval times and extraction status are in [corpus.json](corpus.json); offering and original provenance remain in the linked manifests. `direct_catalog_listing` supports a pointer or stated task, not full review of the linked paper.', '']
    for topic in data['topics']:
        lines += [f'<a id="{topic["id"]}"></a>', '', f'## {topic["name"]}', '', f'ID: `{topic["id"]}`. {topic["definition"]}', '',
                  'Aliases: ' + (', '.join(topic['aliases']) or 'none recorded') + '.', '',
                  '**Book:** ' + book_refs(topic, data, output) + '. ' + topic['book_mapping']['rl_book']['note'], '']
        for occurrence in topic['provisional_plan']:
            lines += [f'- Provisional `{occurrence["pointer"]}` ({occurrence["state"]}): {occurrence["source_phrase"]}']
        if topic['provisional_plan']:
            lines.append('')
        for sid, obs in topic['sources'].items():
            lines += [f'### {NAMES[sid]}', '', f'Coverage: **{obs["coverage"]}**; evidence confidence: {obs["confidence"]}. Source order: {", ".join(map(str, obs["sequence"])) or "unknown / not applicable"}.', '',
                      f'Apparent depth: {obs["apparent_depth"]["value"]} (**inference**, {obs["apparent_depth"]["confidence"]} confidence). {obs["apparent_depth"]["rationale"]}', '',
                      f'Assessment: {obs["assessment"]["status"]}' + (f' ({", ".join(obs["assessment"]["types"])})' if obs['assessment']['types'] else '') + f'; project relationship: {obs["project_relationship"]["status"]}.', '']
            if not obs['evidence']:
                lines += [obs['scope_note'], '']
                continue
            for idx, ev in enumerate(obs['evidence']):
                title = materials[sid][ev['material_id']]['title']
                locator = 'PDF pp.' + span(ev['pdf_pages']) if 'pdf_pages' in ev else ev.get('locator', 'catalog provenance')
                lines += [f'- [{idx}] [{title}]({source_link(ev, output)}), {locator}; `{ev["material_id"]}`; {ev["evidence_kind"]}, {ev["basis"]}, {ev["confidence"]} confidence. {ev["claim"]}' + (f' **Qualifier:** {ev["qualification"]}' if ev.get('qualification') else '')]
                if ev.get('supporting_index'):
                    lines[-1] += f' [Supporting catalog]({local_link(ev["supporting_index"], output)}).'
                if ev.get('inspection_method'):
                    lines[-1] += f' Inspection: {ev["inspection_method"]}.'
            lines.append('')
            if obs['readings']:
                lines += ['Reading associations: ' + '; '.join(f'evidence [{r["evidence_index"]}], {r["use"]}, requirement: {r["requirement"]}' for r in obs['readings']) + '.', '']
            if obs['assessment'].get('explicit_exclusions'):
                lines += ['Explicit assessment exclusions: evidence ' + ', '.join(f'[{i}]' for i in obs['assessment']['explicit_exclusions']) + '. Exclusion from an exam is distinct from absence of teaching.', '']
    outputs[output] = '\n'.join(lines)

    output = 'analysis/phase2/book_mapping.md'
    lines = header('Course-topic mapping to the configured RL book', output)
    lines += ['Book ID: `rl_book`; direct file `sources/RLbook2020.pdf`; no book manifest. Printed page n corresponds to physical PDF page n+22 in this file.', '',
              'This maps normalized course/plan topics to book references. It is not a complete book-to-curriculum gap analysis. “No direct mapping established” is an unresolved mapping, not proof of absence. Related background does not establish coverage of a named modern algorithm. Course reading assignments are recorded separately.', '',
              '| Topic | Book references | Section titles | Qualification |', '|---|---|---|---|']
    for topic in data['topics']:
        bm = topic['book_mapping']['rl_book']
        lines += ['| ' + ' | '.join([topic_link(topic, output), book_refs(topic, data, output), esc('; '.join(r['section_title'] for r in bm['references'])) or '—', esc(bm['note'])]) + ' |']
    outputs[output] = '\n'.join(lines) + '\n'

    output = 'analysis/sequencing.md'
    lines = header('Observed source order and provisional-plan mapping', output)
    lines += ['Order comes from source-local lecture numbers or filenames. It is neither a time estimate nor a recommendation. Repeated topic mentions and pre/post-class variants do not count as extra teaching time. Unordered supplementary material remains separate.', '']
    for sid, info in data['sources'].items():
        lines += [f'## {NAMES[sid]}', '', info['offering'] + '. ' + data['inspection']['sequence_notes'][sid], '',
                  f'[Manifest]({local_link(info["manifest"], output)}) · [Phase 1 context]({local_link(info["phase1_summary"], output)})', '']
        groups = {}
        for topic in data['topics']:
            for ev in topic['sources'][sid]['evidence']:
                if ev['evidence_kind'] != 'teaching':
                    continue
                key = (ev.get('source_order'), ev['material_id'])
                group = groups.setdefault(key, {'ev': ev, 'topics': {}})
                group['topics'][topic['id']] = topic
        lines += ['| Source order | Teaching artifact | Normalized topics with teaching evidence |', '|---|---|---|']
        for (order, mid), group in sorted(groups.items(), key=lambda kv: (kv[0][0] is None, kv[0][0] or 0, kv[0][1])):
            title = materials[sid][mid]['title']
            lines += [f'| {order if order is not None else "Unordered"} | [{esc(title)}]({source_link(group["ev"], output)}) | ' + '; '.join(topic_link(t, output) for t in group['topics'].values()) + ' |']
        lines.append('')
        if info['general_reading_material_ids']:
            lines += ['General reading pointers are not expanded into topic coverage:', '']
            for mid in info['general_reading_material_ids']:
                material = materials[sid][mid]
                catalog = next((p['index_path'] for p in material.get('provenance', []) if 'index_path' in p), info['manifest'])
                link = material.get('url') or local_link(material.get('path', catalog), output)
                lines += [f'- [{material["title"]}]({link}) — `{mid}`, {material["instructional_use"]}.']
            lines.append('')
    occurrences = defaultdict(list)
    for topic in data['topics']:
        for occurrence in topic['provisional_plan']:
            occurrences[occurrence['pointer']].append(topic)
    lines += ['## Provisional curriculum', '', 'Source: `config/provisional_plan.yaml`. The group names below are retained as plan labels, not assigned taxonomy roles or accepted decisions. Every topic/exposure/optional/transition item, both video content lists and all four assignment hypotheses are mapped.', '']
    for i, week in enumerate(plan['weekly_plan']):
        lines += [f'### Week {week["week"]}: {week["title"]}', '', week['intent'], '']
        if week.get('supporting_video'):
            lines += [f'Supporting video reference: `{week["supporting_video"]}`.', '']
        lines += ['| Plan group | Original phrase | Normalized references |', '|---|---|---|']
        for group in ('topics', 'exposure', 'optional', 'transition'):
            for j, phrase in enumerate(week.get(group, [])):
                lines += [f'| {group} | {esc(phrase)} | ' + '; '.join(topic_link(t, output) for t in occurrences[f'/weekly_plan/{i}/{group}/{j}']) + ' |']
        lines.append('')
    for i, video in enumerate(plan['videos']):
        lines += [f'### Provisional video: {video["id"]}', '', video['purpose'], '', '| Original content | Normalized references |', '|---|---|']
        for j, phrase in enumerate(video['content']):
            lines += [f'| {esc(phrase)} | ' + '; '.join(topic_link(t, output) for t in occurrences[f'/videos/{i}/content/{j}']) + ' |']
        lines.append('')
    lines += ['### Assignment hypotheses (non-binding)', '']
    for i, assignment in enumerate(plan['assessment_hypotheses']['assignments']):
        lines += [f'- **{assignment["content"]}:** {assignment["text"]} Mapping: ' + '; '.join(topic_link(t, output) for t in occurrences[f'/assessment_hypotheses/assignments/{i}/text']) + '.']
    lines += ['', '### Project constraints', '', 'Copied at generation time from the provisional configuration; these are scheduling constraints rather than topic-coverage evidence.', '', '```yaml', yaml.safe_dump(plan['project_constraints'], sort_keys=False).rstrip(), '```', '']
    outputs[output] = '\n'.join(lines)

    output = 'analysis/phase2/ambiguities.md'
    lines = header('Mapping ambiguities and evidence gaps', output)
    for a in data['ambiguities']:
        lines += [f'## {a["id"]}', '', f'Status: **{a["status"]}**. {a["description"]}', '', 'Topics: ' + ', '.join(f'`{t}`' for t in a['topic_ids']) + '.', '']
        if a.get('evidence'):
            lines += ['Recorded locators: ' + '; '.join(a['evidence']) + '.', '']
    lines += ['## Evidence gaps', '']
    for gap in data['evidence_gaps']:
        lines += [f'### {gap["id"]}', '', 'Sources: ' + ', '.join(gap['sources']) + '.', '', gap['limitation'], '', '**Effect:** ' + gap['effect'], '', '**Possible follow-up:** ' + gap['next_action'], '']
    outputs[output] = '\n'.join(lines)

    output = 'analysis/phase2_completion.md'
    lines = header('Phase 2 completion report', output)
    lines += ['**PHASE 2 COMPLETE. Phase 3 has not started.**', '',
              f'The evidence model contains {stats["topics"]} stable topics, {stats["source_topic_pairs"]} explicit source-topic records across seven courses, {stats["positive_pairs"]} positive coverage records and {stats["source_topic_pairs"] - stats["positive_pairs"]} unknown records. It has {stats["evidence_references"]} topic-specific evidence references. These are model sizes, not curriculum scores.', '',
              f'{stats["pdf_artifacts"]} PDFs were text-extracted, including the configured book. Relevant content was reviewed with selected visual checks; extraction does not mean exhaustive review. {stats["book_mapped_topics"]} topics have direct or explicitly related book references. {stats["provisional_items"]} distinct plan items have {stats["provisional_mappings"]} normalized mappings, covering all 13 weeks, both videos and four non-binding assignment hypotheses.', '',
              '## Exit criteria', '', '| Criterion | Result | Evidence |', '|---|---|---|',
              '| Stable IDs for major topics | Met | Definitions and aliases in normalized_topics.yaml; all seven configured courses represented |',
              '| Ambiguities documented | Met | [Mapping ambiguities](phase2/ambiguities.md); uncertain equivalences kept separate |',
              '| Consistent source evidence | Met | Explicit coverage, sequence, inferred depth/confidence, assessment, reading, project and citation fields for every pair |',
              '| Provisional plan normalized | Met | Exact configuration pointers checked; [sequencing view](sequencing.md) retains provisional labels |',
              '| Matrix generated from structured evidence | Met | [Topic matrix](topic_matrix.md), deterministically rendered by phase2_report.py |',
              '| Important evidence gaps known | Met | Gaps below and in the ambiguity report; unknowns are not absence claims |', '',
              '## Artifacts and validation', '',
              '- [Structured evidence](normalized_topics.yaml): maintained source of truth for normalization.',
              '- [Topic matrix](topic_matrix.md) and [sequencing](sequencing.md): generated workflow outputs.',
              '- [Detailed citations](phase2/evidence_by_topic.md), [book mapping](phase2/book_mapping.md), and [ambiguities](phase2/ambiguities.md): generated inspection views.',
              '- [PDF inspection ledger](phase2/corpus.json): hashes, URLs/paths, extraction timestamps and page counts.',
              '- `python3 scripts/phase2_report.py --check-only --check-generated` validates YAML keys, topic/source/material IDs, coverage requirements, evidence indices, page bounds, book offsets, local-file hashes, taxonomy assessment values, all plan pointers and generated-file consistency.', '',
              'No configuration, source files, accepted decisions or teaching artifacts were changed by Phase 2. The session integrity check compares pre-phase hashes when its temporary guard file is present. Regeneration itself is offline and writes only the listed Phase 2 analysis views.', '',
              '## Blockers and evidence gaps', '', 'No blocker prevents completion of the Phase 2 evidence model. The following limitations constrain later claims:', '']
    for gap in data['evidence_gaps']:
        lines += [f'- **{gap["id"]}:** {gap["limitation"]} {gap["effect"]}']
    lines += ['', '## Next actions and stopping point', ''] + [f'- {a}' for a in data['phase_boundary']['next_actions']]
    lines += ['', 'No curriculum changes, pedagogical recommendations, accepted decisions, time-budget revision or Phase 3 comparison was performed.', '']
    outputs[output] = '\n'.join(lines)
    return outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-only', action='store_true', help='Validate without writing views')
    parser.add_argument('--check-generated', action='store_true', help='Fail if generated views are missing or stale')
    args = parser.parse_args()
    data = read_yaml(DATA)
    materials, corpus, plan, stats = validate(data)
    outputs = render(data, materials, corpus, plan, stats)
    if args.check_generated:
        for path, content in outputs.items():
            require((ROOT / path).is_file() and (ROOT / path).read_text() == content, f'Stale generated view: {path}')
    if not args.check_only:
        for path, content in outputs.items():
            (ROOT / path).write_text(content)
    print(json.dumps({'validation': 'passed', **stats, 'generated_views': len(outputs), 'wrote_views': not args.check_only}, indent=2))


if __name__ == '__main__':
    main()
