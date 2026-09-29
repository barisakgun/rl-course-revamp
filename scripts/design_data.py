"""Shared joins and accepted week targets; never invent dated assessment windows."""
from phase3_audit import read
from phase5_report import decision


def assignments():
    analysis = read('analysis/assignment_proposal.yaml')
    accepted = decision('assignment')
    scope = {a['id']: a for a in accepted['assignments']}
    items = [{**estimate, **scope[estimate['accepted_assignment_ref']]}
             for estimate in analysis['assignments']]
    return analysis, accepted, items


def week_label(week, placement=None):
    return f'Week {week}' + (f' ({placement})' if placement and placement != 'unspecified' else '')


def milestone_when(m):
    target = week_label(m.get('week', m.get('target_week')), m.get('placement'))
    return target + ('; ' + m['deadline_rule'] if 'deadline_rule' in m else '')


def assignment_schedule():
    _, accepted, items = assignments()
    sessions = {s['id']: s for s in read('decisions/topic_decisions.yaml')['lecture_plan']}
    by_id = {a['id']: a for a in items}
    result = []
    for aid in accepted['schedule_policy']['order']:
        a = by_id[aid]
        assert a['prerequisites'] and set(a['prerequisites']) <= sessions.keys()
        last = max(a['prerequisites'], key=lambda k: (sessions[k]['week'], sessions[k]['slot']))
        target = a['schedule']
        assert target['due_week'] >= target['release_week']
        result.append({'id': aid, 'last_session': last,
                       'release': week_label(target['release_week']),
                       'deadline': week_label(target['due_week'], target.get('due_placement')),
                       'release_week': target['release_week'], 'due_week': target['due_week'],
                       'duration_days': accepted['schedule_policy']['duration_days'],
                       'dated': False})
    return result
