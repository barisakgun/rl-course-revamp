#!/usr/bin/env python3
"""Validate the Phase 3 working proposal and regenerate its audit and review view.

Offline; reads config and normalized evidence without changing either or decisions.
Usage: python3 scripts/phase3_audit.py [--check]
Requires the repository's existing PyYAML dependency.
"""
import argparse
from collections import Counter
from pathlib import Path
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return yaml.safe_load((ROOT / path).read_text())


def number(value):
    return f'{value:,.1f}'.rstrip('0').rstrip('.')


def table(headers, rows):
    return '\n'.join(['| ' + ' | '.join(headers) + ' |',
                      '| ' + ' | '.join(['---'] * len(headers)) + ' |'] +
                     ['| ' + ' | '.join(str(c).replace('|', '/') for c in row) + ' |' for row in rows])


def policy_report(proposal, accepted, sessions, per_session, header, cfg):
    spec = proposal['policy_audit']
    selected = [s for s in sessions if s['id'] in spec['session_ids']]
    assert [s['id'] for s in selected] == spec['session_ids']
    assert len(selected) == accepted['constraints']['policy_live_lectures']
    capacity = sum(per_session[s['week'], s['slot']] for s in selected)
    admin = sum(s['administration_minutes'] for s in selected)
    teaching = sum(s['teaching_minutes'] for s in selected)
    low = sum(s['teaching_range'][0] for s in selected)
    high = sum(s['teaching_range'][1] for s in selected)
    stress = teaching * (1 + spec['pace_stress_fraction'])
    raw_teaching = len(selected) * cfg['course']['lecture_minutes'] - admin
    generic_buffer = raw_teaching - (capacity-admin)
    sac_minutes = accepted['constraints']['sac_live_minutes']
    rows = []
    for s in selected:
        pieces = '; '.join(f'{v["label"]}: {number(v["minutes"])}' for v in s['segments'])
        rows.append([f'{s["week"]}.{s["slot"]}', pieces, s['teaching_minutes'],
                     s['administration_minutes'],
                     number(per_session[s['week'], s['slot']] - s['teaching_minutes'] - s['administration_minutes']),
                     f'{s["teaching_range"][0]}–{s["teaching_range"][1]}'])
    text = ['# Focused audit: five policy-method lectures', '', header, '',
            '**Finding: feasible at the specified conceptual/mechanism depth, but tight.** '
            'The instructor’s proposal is plausible; the arithmetic does not support adding a full SAC proof or implementation workshop as well.', '',
            f'Five sessions provide **{number(capacity)} content minutes** before **{admin} minutes** of checkpoint administration: '
            f'**{number(capacity-admin)} teaching minutes**. The selected allocation is **{teaching}**, leaving **{number(capacity-admin-teaching)}** '
            'unallocated within the 85% teaching allowance for these sessions. '
            f'The instructor may also use the **{number(generic_buffer)}-minute generic buffer** at the expense of questions/consolidation; '
            f'the physical five-session teaching window after administration is **{number(raw_teaching)} minutes**.', '',
            '## Exclusive session segments', '',
            'Segments partition the session teaching total; they are not additional allocations. '
            'Accepted fixed durations (history, SAC and average reward elsewhere) resolve from the decisions file. '
            'All other segment durations are planning estimates, confidence '+spec['confidence']+'.', '',
            table(['Week.slot', 'Segment / minutes', 'Teaching', 'Admin', 'Unallocated', 'Demand range'], rows), '',
            '## Depth and prerequisites', '', spec['scope'], '',
            '- The ten-minute history covers motivation and historical placement, without mathematics or algorithm steps. It is paid for by moving the sampled-gradient example into the next session and reducing repeated overview time.',
            '- REINFORCE, baseline identity, critic bias, forward returns and a GAE example remain live. A backward-view existence mention takes one minute inside the return block; no backward-lambda math is assumed.',
            f'- SAC receives {sac_minutes} minutes after a ten-minute entropy introduction in the preceding session. Reuse DQN replay/targets, familiar critics and stochastic policies. Explain the entropy-augmented target, actor objective, brief reparameterized-sampling intuition, data flow and one comparison. The sampling intuition is inside this allowance, not an assumed untaught prerequisite. Do not add soft-policy-iteration proofs, temperature-tuning derivations, or a coding lab.',
            '- Reducing the earlier 40-minute SAC segment to the accepted 30 minutes releases ten minutes of local contingency. Replay/target/critic explanations are reused; the segment remains mechanism-level rather than a full proof or implementation workshop.',
            '- A chain-rule/probability recap is embedded in the gradient exposition; substantial remediation would exceed the selected allocation. The five-session sequence is contingent on the assumed basic ML/probability background.', '',
            '## Sensitivity', '',
            table(['Scenario', 'Teaching demand', 'Generic buffer needed beyond plan', 'Excess beyond physical window'], [
                ['Selected scope', teaching, number(max(0, teaching-(capacity-admin))), number(max(0,teaching-raw_teaching))],
                ['Planning range (not measured)', f'{low}–{high}', f'0–{number(max(0,high-(capacity-admin)))}', number(max(0,high-raw_teaching))],
                [f'{number(100*spec["pace_stress_fraction"])}% slower on selected teaching', number(stress), number(max(0,stress-(capacity-admin))), number(max(0,stress-raw_teaching))]
            ]), '',
            'The upper-demand case is a stress test, not a prediction. Borrowing generic buffer is authorized, but reduces questions/consolidation. '
            'A fit across five lectures may still require moving content between them when an individual session exceeds 70 minutes. '
            'The tightest conceptual transitions remain baseline→critic and n-step/forward mixture→GAE, followed by first-time SAC objectives.', '',
            '## Contingencies for review, not activated', '']
    for c in spec['contingencies']:
        text += [f'- **{c["name"]}** ({c["minutes_range"][0]}–{c["minutes_range"][1]} teaching minutes; {c["state"]}): '
                 +c['action']+' '+c['workload']]
    text += ['', 'Keep the current bounded five-session allocation as the working recommendation. '
             'The instructor has judged pacing doable and accepted the reviewed masteries. Video checkpoints govern any later supplement; no sixth lecture is scheduled.', '']
    return '\n'.join(text)


def build():
    cfg = read('config/course.yaml')
    proposal = read('analysis/phase3_proposal.yaml')
    evidence = read('analysis/normalized_topics.yaml')
    taxonomy = read('config/taxonomy.yaml')
    course, design = cfg['course'], cfg['design']
    weeks, slots, duration = course['planned_weeks'], course['lectures_per_week'], course['lecture_minutes']
    fraction = design['planned_content_fraction']
    topics = {t['id']: t for t in evidence['topics']}
    accepted = read(proposal['accepted_topics_source'])
    accepted_groups = {g['id']: g for g in accepted['scope_decisions']}
    assert len(accepted_groups) == len(accepted['scope_decisions'])
    groups = {}
    for g in proposal['groups']:
        assert not {'topic_ids', 'scope', 'delivery', 'mastery', 'role', 'status', 'status_scope'} & g.keys(), 'Accepted scope duplicated in analysis'
        scope = accepted_groups[g['accepted_scope_ref']]
        groups[g['id']] = {**scope, **g}
    video_text = (ROOT / proposal['accepted_videos_source']).read_text()
    video_blocks = re.findall(r'```yaml\n(.*?)\n```', video_text, re.S)
    assert len(video_blocks) == 1, 'Expected one authoritative video YAML block'
    video_data = yaml.safe_load(video_blocks[0])
    video_decisions = {v['id']: v for v in video_data['videos']}
    for v in proposal['videos']:
        assert not {'required', 'scope'} & v.keys(), 'Accepted video state duplicated in analysis'
        v.update(video_decisions[v['accepted_video_ref']])
        first=next(s for s in accepted['lecture_plan'] if s['id']==v['before'])
        v['release_week']=first['week']-video_data['release_policy']['lead_days']//7
    sessions = accepted['lecture_plan']
    for s in sessions:
        for segment in s.get('segments', []):
            if 'accepted_minutes_ref' in segment:
                assert 'minutes' not in segment, 'Accepted duration duplicated in analysis'
                segment['minutes'] = accepted['constraints'][segment['accepted_minutes_ref']]
        if s.get('segments'):
            assert sum(x['minutes'] for x in s['segments']) == s['teaching_minutes'], s['id']
    by_id = {s['id']: s for s in sessions}
    assert proposal['state'] == 'frozen_curriculum_with_assessment_proposals'
    assert len(groups) == len(proposal['groups']) and len(by_id) == len(sessions)
    assert [(s['week'], s['slot']) for s in sessions] == [(w, slot) for w in range(1, weeks+1) for slot in range(1, slots+1)]
    owners = Counter(t for g in groups.values() for t in g['topic_ids'])
    assert all(n == 1 for n in owners.values()), 'Topic classification duplicated across groups'
    assert set(owners) <= topics.keys(), 'Unknown normalized topic ID'
    provisional = {t['id'] for t in topics.values() if t['provisional_plan']}
    assert provisional <= owners.keys(), f'Provisional items without disposition: {provisional - owners.keys()}'
    for g in groups.values():
        assert g['role'] in taxonomy['role']
        for field, vocab in [('mastery', 'mastery'), ('status', 'status'), ('delivery', 'delivery'), ('assessment_expectation', 'assessment')]:
            assert set(g[field]) <= taxonomy[vocab].keys(), (g['id'], field)
        assert g['status'] or g['role'] == 'extension', 'Included group needs proposed status'
        if set(g['mastery']) & {'derive', 'implement', 'analyze'}:
            assert set(g['assessment_expectation']) & {'exam', 'assignment', 'project'}
    order = {s['id']: i for i, s in enumerate(sessions)}
    for s in sessions:
        assert set(s['group_ids']) <= groups.keys()
        assert all(order[r] < order[s['id']] for r in s['requires']), f'Prerequisite order: {s["id"]}'
        lo, hi = s['teaching_range']
        assert 0 <= lo <= s['teaching_minutes'] <= hi
        assert s['administration_minutes'] >= 0
    for v in proposal['videos']:
        assert v['before'] in by_id
        assert len(v['playback_minutes']) == len(v['student_effort_minutes']) == 2
        assert v['release_week'] < by_id[v['before']]['week']
    assert len(proposal['videos']) == course['target_videos']
    assert sum(s['id'] == 'bandits' for s in sessions) == accepted['constraints']['bandit_live_lectures']
    scheduled_groups = {g for s in sessions for g in s['group_ids']}
    assert all(g['role'] == 'extension' or 'video' in g['delivery'] or g['id'] in scheduled_groups for g in groups.values())
    nominal = course['nominal_semester_lectures']
    available = nominal - course['holiday_conflicts'] - course['instructor_absences'] + course['makeup_lectures']
    planned = weeks * slots
    assert planned <= available
    contact = planned * duration
    overheads = design['in_class_overheads']
    overhead = sum(h['minutes'] for h in overheads)
    capacity = contact * fraction - overhead
    weekly_capacity = {w: slots * duration * fraction - sum(h['minutes'] for h in overheads if h['week'] == w) for w in range(1, weeks+1)}
    # The config specifies overhead weeks. For session-level auditing only, place
    # each configured overhead in that week's first session; do not alter config.
    per_session = {(s['week'], s['slot']): duration * fraction - (sum(h['minutes'] for h in overheads if h['week'] == s['week']) if s['slot'] == 1 else 0) for s in sessions}
    teaching = sum(s['teaching_minutes'] for s in sessions)
    admin = sum(s['administration_minutes'] for s in sessions)
    allocated = teaching + admin
    assert allocated <= capacity, 'Semester overload'
    for s in sessions:
        assert s['teaching_minutes'] + s['administration_minutes'] <= per_session[s['week'], s['slot']], f'Session overload: {s["id"]}'
    assert design['project_presentations_outside_class_hours'], 'Reallocate presentations before auditing an in-class scenario'
    demand = {x['week']: x for x in proposal['provisional_demand']}
    assert set(demand) == set(weekly_capacity)
    for d in demand.values():
        assert 0 <= d['minutes'][0] <= d['minutes'][1]
    header = ('Generated by `python3 scripts/phase3_audit.py` from [the working proposal](phase3_proposal.yaml), '
              '[accepted topic scopes](../decisions/topic_decisions.yaml), [accepted video delivery](../decisions/video_decisions.md), '
              '[course constraints](../config/course.yaml), and normalized topic IDs/taxonomy. '
              'Edit the appropriate source, then regenerate. **Curriculum frozen; accepted classifications and baseline lecture plan come from decisions. Assessment paths remain proposals; timings remain estimates. Phase 5 complete; Phase 6 in progress.**\n')
    lines = ['# Phase 3 teaching-time audit', '', header, '', '## Result', '', proposal['audit_notes']['verdict'], '',
             '## Capacity and administration', '',
             f'- Calendar check: {nominal} − {course["holiday_conflicts"]} − {course["instructor_absences"]} + {course["makeup_lectures"]} = {available} available lectures; {weeks} × {slots} = {planned} planned. Losses are not subtracted again.',
             f'- Planned contact: {planned} × {duration} = **{number(contact)} minutes**. Configured reserve: **{number(contact * (1-fraction))} minutes** ({number(100*(1-fraction))}%).',
             f'- Content capacity: {number(contact)} × {fraction} − {number(overhead)} configured overhead = **{number(capacity)} minutes**.',
             f'- Proposed teaching: **{number(teaching)} minutes**; additional project/checkpoint administration: **{number(admin)} minutes**; combined **{number(allocated)} minutes**.',
             f'- Unallocated capacity beyond the configured reserve: **{number(capacity-allocated)} minutes**. It is distributed across weeks, not a movable free lecture.',
             '- The configured syllabus overhead is placed in Week 1, session 1. Additional project administration is charged separately. The 85% baseline is for advance planning; the generic buffer is available during delivery under the accepted policy.',
             '- Presentations: **0 live lecture minutes**, as configured. Attendance and preparation outside class remain workload; their length and cohort size are unknown.', '',
             '## Estimation conventions', '',
             'All demand ranges are pedagogical planning estimates, not source-course measurements or statistical confidence intervals. '
             'Observed lecture/deck order is not elapsed teaching time. Content minutes proxy initial teaching depth/effort; '
             'no slide-count conversion or student-workload multiplier is used. '
             'Ranges include the planned worked activity. The generic buffer normally supports questions, extra examples and consolidation, but the instructor may reallocate it to longer explanations. '
             'A selected allocation inside a range is a teaching target, not proof that its upper end will fit.', '',
             'Each session is one integrated teaching block. DQN/replay/targets, MC/TD/bias–variance and PPO/ratios are not charged independently by topic ID. '
             'Repeated groups are deliberate stages or revisits with different activities, not duplicated whole-topic estimates.', '',
             '## Provisional plan: estimated demand before narrowing', '',
             'The provisional plan has no authoritative minute allocations or accepted mastery. These low-confidence ranges assume '
             'a central explanation/example for each main method, brief exposure items, and no full optional sections. '
             'They do not treat every main-list item as Core. Narrower intended mastery would lower the estimates; that choice needs to be explicit. '
             'Additional project administration is not included in these provisional demand ranges.', '']
    rows=[]
    for w in range(1,weeks+1):
        d=demand[w];lo,hi=d['minutes'];cap=weekly_capacity[w]
        rows.append([w,number(cap),f'{lo}–{hi}', 'likely overload' if lo > cap else ('tight/uncertain' if hi > cap else 'fits range'), d['scope_assumption']])
    lines += [table(['Week','Capacity','Estimated demand','Assessment','Scope assumption'],rows), '',
              f'Total provisional estimate: **{sum(d["minutes"][0] for d in demand.values()):,}–{sum(d["minutes"][1] for d in demand.values()):,} minutes**. '
              'This sum uses whole-week blocks; it does not sum overlapping topic IDs. It diagnoses scope pressure, not a measured historical deficit.', '',
              '## Proposed weekly allocations', '']
    rows=[]
    for w in range(1,weeks+1):
        ss=[s for s in sessions if s['week']==w];t=sum(s['teaching_minutes'] for s in ss);a=sum(s['administration_minutes'] for s in ss)
        lo=sum(s['teaching_range'][0] for s in ss);hi=sum(s['teaching_range'][1] for s in ss)
        raw_week = slots * duration - sum(h['minutes'] for h in overheads if h['week'] == w)
        rows.append([w,number(weekly_capacity[w]),t,a,number(weekly_capacity[w]-t-a),f'{lo}–{hi}',number(max(0,hi+a-weekly_capacity[w])),number(max(0,hi+a-raw_week))])
    lines += [table(['Week','Capacity','Teaching','Added admin','Unallocated','Teaching range','Upper demand beyond planning budget','Upper demand beyond physical week'],rows),'',
              'Excess beyond the planning budget may use the instructor-authorized generic buffer; excess beyond the physical week requires moving or reducing content. The same minutes cannot support both extra teaching and questions/consolidation.', '',
              '## Session audit', '',table(['Week.slot / block','Available','Teaching + admin','Teaching range / confidence','Worked activity and scope limit'],
              [[f'{s["week"]}.{s["slot"]} `{s["id"]}`',number(per_session[s['week'],s['slot']]),f'{s["teaching_minutes"]} + {s["administration_minutes"]}',f'{s["teaching_range"][0]}–{s["teaching_range"][1]} / {s["confidence"]}',s['worked_activity']+' '+s['feasibility_note']] for s in sessions]),'',
              '## Depth, dependency and sensitivity findings','',
              '- **Weeks 2, 7 and 8 are the main foundational risks.** Bellman improvement, score-function gradients, and actor–critic/GAE need observed student understanding. The Week 8 first block is especially tight within the expanded five-lecture policy sequence.',
              '- Prerequisite order is checked for declared session dependencies. Policy improvement precedes control; n-step targets and baselines precede GAE; ratios precede PPO; UCB precedes UCT; PPO/ratios and contextual decisions precede LLM transfer. This is a dependency check, not a Phase 4 consistency audit.',
              '- Week 4 proposal and Week 7 design checkpoint may use formulation, baselines and evaluation, but cannot require algorithms first taught in Weeks 11–13. Advanced projects need later refinement or bounded independent preparation, to be reviewed in Phase 5.',
              '- IQL is the primary offline method, with CQL a brief contrast. SAC receives a mechanism treatment, and the LLM comparison uses one shared sample group. Full derivations/implementations of all these methods are not implied. See the [focused policy audit](policy_time_budget.md).',
              '- Required readings do not fund the live reductions. Two substantive prerequisite videos are used; their study load is separate. Any additional policy video remains an unaccepted contingency.', '',
              proposal['audit_notes']['pressure_response'], '',
              f'Sensitivity: simultaneous upper estimates require **{sum(s["teaching_range"][1] for s in sessions)+admin:,} minutes**, '
              f'**{number(sum(s["teaching_range"][1] for s in sessions)+admin-capacity)} over the advance-planning capacity**. '
              'These correlated upper estimates are a stress scenario, not a predicted outcome. Losing one planned session would remove '
              f'{number(duration*fraction)} content minutes before any session-specific overhead; the earlier/later placement determines which prerequisites must be replanned.', '',
              '## Separate out-of-class workload', '',table(['Item','Playback estimate','Student effort estimate','Treatment'],
              [[v['id'],f'{v["playback_minutes"][0]}–{v["playback_minutes"][1]} min',f'{v["student_effort_minutes"][0]}–{v["student_effort_minutes"][1]} min',('Required' if v['required'] else 'Optional refresher')+f'; before `{v["before"]}`. '+v['fallback']] for v in proposal['videos']]),'',
              'Video student effort includes pauses/self-checks; confidence is low. Both videos carry prerequisite preparation. '
              'BFS/DFS are assumed; the search video develops the bridge beyond those basics, with any elementary recap skippable. '
              'The LLM video includes transformer, autoregressive-model, pretraining and SFT background. '
              'Proposed initial release weeks are 8 and 10, before the Week 10 and Week 13 live units; the Week 11 checkpoint can verify/update the LLM preparation. '
              f'Total playback is {sum(v["playback_minutes"][0] for v in proposal["videos"])}–{sum(v["playback_minutes"][1] for v in proposal["videos"])} minutes; '
              f'total student study effort is {sum(v["student_effort_minutes"][0] for v in proposal["videos"])}–{sum(v["student_effort_minutes"][1] for v in proposal["videos"])} minutes. These estimates are separate from live capacity. '
              'The calendar already counts the configured losses and makeups: videos do not create replacement live lectures or justify adding losses a second time. '
              'The larger LLM recording mainly improves preparation; only the shorter live retrieval recap and local headroom fund the additional live estimator example.', '',proposal['audit_notes']['workload'],'',
              'No new mandatory reading, assignment count, deadline, grading scheme or project design is accepted here. '
              'Week 13 presentation attendance plus LLM preparation is an unresolved workload concentration. '
              'A later workload audit needs cohort/group count, presentation format/duration, assignment scope, and reading/video accessibility.', '',
              '## Review gate', '',
              'See [the instructor review](curriculum_review.md#remaining-review-points) and [focused policy audit](policy_time_budget.md). '
              'Curriculum freeze is recorded separately by instructor decision after the Phase 4 audit; arithmetic alone did not establish readiness.', '']
    lines += ['## Accepted delivery policy and video checkpoints', '', accepted['delivery_policy']['buffer_use'], '',
              accepted['delivery_policy']['questions'], '',
              table(['Week', 'Video checkpoint'], [[x['week'], x['action']] for x in video_data['checkpoints']]), '',
              video_data['change_rule'], '',
              'Other pacing options and deferred connections are recorded in [the future-topic register](future_topics.md). '
              'Neither tentative IRL nor LSTD is included in the base total.', '']
    lines += ['## Optional substitutions, excluded from the base total', '']
    for scenario in proposal['optional_scenarios']:
        assert scenario['session'] in by_id
        item = next(x for x in accepted['unresolved'] if x['id'] == scenario['accepted_suggestion_ref'])
        assert scenario['teaching_minutes'] == item['minutes_if_used']
        lines += [f'- **{scenario["id"]}**: {scenario["teaching_minutes"]} minutes in `{scenario["session"]}`. '
                  + scenario['replacement'] + ' ' + scenario['recommendation'], '']
    view=['# Proposed Phase 3 teaching plan and topic scope','',header,'',
          'This is an analytical candidate, not the accepted lecture plan. Session allocations are audited in [time_budget.md](time_budget.md). '
          'Accepted scope, mastery, role and status are loaded from decisions; assessment paths below remain proposed. A list of topic IDs is not a list of full algorithms to master.', '',
          '## Candidate sequence','',table(['Week.slot','Teaching block','Prerequisite blocks','Minutes (teaching / extra admin)'],
          [[f'{s["week"]}.{s["slot"]}',s['title'],', '.join(s['requires']) or 'Assumed audience background',f'{s["teaching_minutes"]} / {s["administration_minutes"]}'] for s in sessions]),'',
          '## Accepted scope and classifications','']
    for g in groups.values():
        display = g.get('display_name') or ' / '.join(topics[t]['name'] for t in g['topic_ids'][:3]) + (' and related concepts' if len(g['topic_ids']) > 3 else '')
        view += [f'### {display}', '', f'Group: `{g["id"]}`.', '',
                 f'**{g["role"]}** ({"accepted" if "role" in accepted_groups[g["accepted_scope_ref"]] else "proposed"}); accepted mastery: {", ".join(g["mastery"])}; status: {", ".join(g["status"]) or "unresolved individually; no required inclusion"}; delivery: {", ".join(g["delivery"])}.', '',
                 'Accepted scope: '+g['scope'], '', 'Topic IDs: '+', '.join(f'`{t}`' for t in g['topic_ids'])+'.', '',
                 'Assessment path to review later: '+', '.join(g['assessment_expectation'])+'.','']
        if g.get('status_scope'):view += ['Status scope: '+g['status_scope'],'']
    view += ['## Deliberately unresolved','',
             'Optional extensions have no accepted individual status, reading, mastery requirement or assessment. '
             'Topic IDs outside the provisional plan and these explicit groups are not automatically added. '
             'Proposed assessment paths express alignment needs only; they do not select assignment designs. '
             'Accepted content and mastery are recorded; remaining classification review and formal consistency audit belong to later work. Conservative Q-Learning (CQL) is confirmed as Exposure/explain in Week 12.2; no new time is added. LSTD is only an optional substitution.','']
    return {'analysis/time_budget.md':'\n'.join(lines), 'analysis/phase3_plan.md':'\n'.join(view), 'analysis/policy_time_budget.md':policy_report(proposal, accepted, sessions, per_session, header, cfg)}, (teaching,admin,capacity-allocated,len(owners))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true',help='Validate inputs and require generated files to match; write nothing')
    args=parser.parse_args()
    files, totals=build()
    for name,text in files.items():
        path=ROOT/name
        if args.check:
            assert path.exists() and path.read_text()==text, f'Stale generated file: {name}'
        else:
            path.write_text(text)
    print(f'Phase 3 proposal valid: teaching={totals[0]}, additional admin={totals[1]}, unallocated={totals[2]:.1f}; {totals[3]} topic dispositions. Frozen curriculum preserved; baseline allocations remain estimates.')


if __name__=='__main__':
    main()
