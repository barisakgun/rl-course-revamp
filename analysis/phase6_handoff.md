# Phase 6 reset handoff

## Current stop boundary

The instructor has accepted a **provisional week-level schedule freeze**, to be reopened after the first two weeks of classes when registration and attendance stabilize. This is not final syllabus/design freeze. The latest instruction explicitly prohibits starting the syllabus or running the full audit now. Neither was done in the freeze-recording turn.

Read AGENTS.md and required context on resumption, then the latest decision-log entry, schedule/assignment/project/grading/video/reading decisions, this handoff and the generated `output/assessment_timeline.md`. Do not reconstruct decisions from old generated reports.

## Authoritative updates

- `decisions/schedule_decisions.yaml`: freeze scope/reopening trigger, three makeup months, 26 retained lectures and unresolved calendar inputs.
- `decisions/assignment_decisions.md`: each assignment's `schedule` gives accepted calendar-week targets. Prerequisites and the 21-day rule remain binding; early Week 7 A1 is a known mapping issue, not permission to shorten the assignment window.
- `decisions/grading_decisions.md`: MT1 Week 6, MT2 Week 10, MT3 Week 13; three 15% weights and coverage unchanged. Regular-semester MT3 early Week 14 remains separate.
- `decisions/project_decisions.md`: design late Week 7; progress early Week 11; TA-led online recorded presentations Week 14; final report target Week 16, still one week before letter grades. TA/group grading is accepted; split and operational rubric remain open. Regular-semester presentations late Week 14/early Week 15 are separate.
- `config/course.yaml`: two assumed lost holiday/unavailable slots and three makeup lectures retain the 26-session capacity. December 31 unavailability is a planning assumption, not verified official holiday status. Teaching topics/minutes were not changed.
- `decisions/decision_log.md`: acceptance and explicit audit/syllabus hold.

## Information completeness

Enough information exists for the provisional schedule and for a later syllabus draft with date placeholders. No new curriculum or high-level assessment choice is needed now. Remaining information is chiefly operational:

| Needed | When / purpose |
| --- | --- |
| Stabilized registration, student timetable, lecture weekdays and October/November/December makeup dates | Post-Week-2 reopening; check the supplied DOCX for already stated class hours before asking again. Map all 26 logical lectures to actual dates. |
| Exact exam dates, times, durations and arrangements | Confirm assessed topics were taught with preparation time before each exam. MT3 needs a feasible date before the year-end/January constraints. |
| Assignment release/deadline days and times | Preserve full 21-day windows after prerequisites; reconcile A1 early Week 7, stagger Week 11 submissions and January deliverables. |
| Official letter-grade deadline and grading turnaround | Verify Week 16 final report remains one week before grades; establish who can grade in January. |
| TA availability for January presentations and assessment support | Instructor previously expected at most one TA, possibly none; the accepted TA-led plan still depends on staffing confirmation. |
| Team count, presentation slots, online/recording arrangements, TA/peer grade split and rubric | Final slots after proposals/team freeze; no additional attendance requirement or grading weight is inferred. |
| Concrete assignment rubrics, LLM penalty operation/example report, tested scaffolds and runtime calibration | Intentionally deferred to implementation during the semester, before release. Not a reason to reopen accepted task selection now. |
| Syllabus administrative/policy text | Retrieve from the supplied DOCX first; no claim that all publication details have already been inspected. |

## Syllabus handoff — do not edit until requested

`course/syllabus/syllabusFall26_draft.docx` exists and remains untouched. Use the documents skill when editing/rendering it. Preserve its catalog description and official COMP341 and COMP421/521 prerequisites verbatim. The instructor authorizes streamlining objectives/other editable descriptions and using a compact topic table instead of a lecture-by-lecture list. Do not revise the teaching plan to compensate for the official prerequisite wording. Existing `output/syllabus.md` and the editable Markdown template predate the latest schedule freeze.

## Audit handoff — required later, not run now

A full **Phase 6 course-design consistency and workload audit** is required before final syllabus/design freeze under AGENTS.md and docs/workflow.md. It should use the updated schedule and revised syllabus. It does not require repeating source collection, normalization or the entire curriculum analysis.

Check prerequisite/date mapping, 21-day windows and overlaps, exact exam coverage/timing, project ordering and grading turnaround, online presentation attendance/staff effort, video lead times, workload against the 150–180-hour target, unchanged teaching budget, and agreement among decisions and the final syllabus. Carry unknown operational dates as explicit limitations if still unavailable; rerun affected calendar checks after the Week-2 reopening.

## Generated-file and script status

`scripts/schedule_report.py` renders **only** the current compact schedule from accepted decisions without invoking audits or syllabus generation. `output/assessment_timeline.md` is current.

Other existing generated schedules, assignment/project views, syllabus and audit reports **predate this freeze**. They retain older exam windows, progress/presentation weeks or logical-slot deadlines. They are not the authority and must be refreshed in the next authorized syllabus/audit pass. Do not interpret previous passing reports as validation of the new dated plan.

Before using `scripts/phase6_report.py` again, update it to consume accepted calendar-week targets rather than re-creating deadlines solely from logical lecture coordinates. It currently contains old narrative assumptions and also writes the syllabus/audits. Update `scripts/design_data.py`, `scripts/assignment_report.py` and `scripts/phase5_report.py` where they assume the prior schedule. Ensure the timeline has a single rendering path, retaining the new schedule-only renderer or calling it from the integrated report. Do not run these generators merely to refresh views while the user's audit/syllabus hold is active.

The new freeze was recorded through decision edits, a schedule-only rendering and basic YAML parsing. No full audit, topic revision, DOCX edit, or final Phase 6 completion claim occurred.
