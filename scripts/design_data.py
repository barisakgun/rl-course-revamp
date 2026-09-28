"""Shared joins and schedule derivation; no curriculum state is stored here."""
from datetime import date, timedelta
from phase3_audit import read
from phase5_report import decision


def assignments():
    analysis=read('analysis/assignment_proposal.yaml')
    accepted=decision('assignment')
    scope={a['id']:a for a in accepted['assignments']}
    items=[{**estimate,**scope[estimate['accepted_assignment_ref']]} for estimate in analysis['assignments']]
    return analysis,accepted,items


def assignment_schedule():
    _,accepted,items=assignments()
    sessions={s['id']:s for s in read('decisions/topic_decisions.yaml')['lecture_plan']}
    calendar=read('analysis/phase6_review.yaml')['calendar']['session_dates']
    rule=accepted['schedule_policy'];by_id={a['id']:a for a in items}
    result=[]
    dated=all(k in calendar for a in items for k in a['prerequisites'])
    for aid in rule['order']:
        a=by_id[aid]
        last=max(a['prerequisites'],key=lambda k:(sessions[k]['week'],sessions[k]['slot']))
        s=sessions[last];coordinate=(s['week']-1)+(s['slot']-1)/2
        ready=date.fromisoformat(calendar[last]) if dated else coordinate
        start=ready
        end=start+timedelta(days=rule['duration_days']) if dated else start+rule['duration_days']/7
        result.append({'id':aid,'last_session':last,'ready':ready,'start':start,'end':end,'delayed':False,'dated':dated})
    return result


def when(value):
    if isinstance(value,date):return value.isoformat()
    week=int(value)+1;slot=1+round((value-int(value))*2)
    return f'{week}.{slot}'
