# Phase 6 handoff

For resuming teaching-material work in a fresh conversation, see the [Phase 7 handoff](phase7_handoff.md).

## Current boundary

**Syllabus frozen by the instructor; Phase 6 closed. Phase 7 has not started.** The authoritative freeze record and artifact fingerprints are in `decisions/syllabus_decisions.yaml`, with acceptance and reconciliation history in `decisions/decision_log.md`.

The current student-facing artifacts are `course/syllabus/syllabusFall26.docx` and the instructor-produced `course/syllabus/syllabusFall26.pdf`. The instructor completed the final edits and PDF conversion for upload. No upload or fresh agent verification of that final PDF is claimed.

No Phase 6 closeout task remains. Exact-date calendar finalization and operational follow-up remain after Phase 7, retaining the post-Week-2 checkpoint. Possible additional phases for work after lectures start remain a future workflow discussion.

## Generator alignment completed

The generators and Markdown views now use the frozen final syllabus. `output/syllabus.md` preserves its concise wording, assignment-count flexibility, links, lists and tables. It adds no internal deadlines, page limits, mandatory-video counts or detailed release rules. Accepted assignment records distinguish the current four-task plan from the syllabus's discretion to change the count; project records include the final disclosure and writing-quality policy.

- `decisions/syllabus_decisions.yaml`: accepted final DOCX/PDF identity, freeze scope and change rule.
- `output/syllabus.md`: generated final DOCX text view; `course/syllabus/template.md` is only its wrapper.
- `output/assessment_timeline.md`, `output/assessment_schedule.md`, `output/project_schedule.md`, `output/video_plan.md`: internal planning views, with actual dates pending.
- `output/audits/workload.md`, `output/audits/design_consistency.md`, `output/audits/syllabus_verification.md`: current checks and retained limitations. Related assignment/project views are refreshed.
- `analysis/syllabus_verification.json`: historical evidence for `syllabusFall26_draft.docx` only. Its five-page visual review does not certify the instructor-edited final files. Current checks verify frozen-file identity and text consistency; they do not claim a new visual review or upload.

The old detailed draft is superseded. Read AGENTS.md, required context and the current decision records on resumption. No tool now needs that old draft as its syllabus input.

## Audit findings and limits

Teaching remains 1,440 minutes plus 19 additional administration minutes, leaving 68 usable minutes. The configured 15% buffer and 20-minute syllabus briefing are accounted separately. No topics, mastery, grading weights or teaching minutes changed. Policy and offline units remain dense despite arithmetic fit.

Estimated total student effort is 158.7–235 hours for all four assignments or 148.7–222 for exactly three. These are unpiloted sensitivity ranges; upper bounds exceed the 150–180-hour target. Workload is accepted in principle, not empirically calibrated. Best-three grading retains the accepted limitation that an omitted task leaves its implementation evidence incomplete.

The accepted schedule removes the former same-week MT3/presentation conflict: MT3 is Week 13 and presentations Week 14. Actual-date prerequisite and preparation intervals, 21-day assignment windows, deadline spacing, staffing and grading turnaround are **pending**, not passed.

The supplied DOCX already states Tuesday/Thursday 14:30–15:40, CASEZ27. Retain this evidence rather than asking for it again; confirmation against the stabilized timetable and mapping all 26 lectures remain deferred.

## Deferred follow-up after Phase 7

| Item | Required check |
| --- | --- |
| Stabilized registration/timetable and October/November/December makeup dates | Reopen after Week 2; map all 26 logical lectures to dates without changing teaching scope. |
| Assignment dates | Preserve full 21-day windows after prerequisites; reconcile A1 early Week 7, stagger Week 11 and retain January spacing. |
| Exam dates/durations | Check taught coverage and preparation time, especially MT3 before the year-end/January constraints. |
| Official grade deadline and staffing | Verify Week 16 report is one week before grades and establish feasible January turnaround. |
| Final-report late days | Supplied policy permits remaining late days with a possible Incomplete; lateness can consume or exceed the grading buffer. Operational handling remains unresolved. |
| Presentation operation | Confirm TA availability, team count, three two-hour slots, online/recording arrangements and TA/group grading split/rubric. |

Concrete assignment scaffolds, pilots, run budgets, rubrics, excess-lateness penalty details and the example LLM-use report remain deferred until implementation before release. No policy numbers were invented. The assignment no-credit rule remains specific to assignments; the final syllabus also establishes project disclosure/report and writing-quality policy. Concrete instructions and rubrics remain deferred.

## Generator and verification workflow

- `scripts/design_data.py` reads accepted calendar-week targets; logical prerequisite labels do not generate fake deadlines.
- `scripts/schedule_report.py` provides the sole timeline renderer, also called by the integrated report. Its standalone command runs no audit and writes no syllabus.
- `scripts/phase6_report.py` audits and renders schedules/reports only. It does not modify the DOCX or Markdown syllabus. It always checks final DOCX/PDF identity against the accepted freeze record, checks published facts against decisions, and requires the Markdown export to match.
- `scripts/syllabus_report.py` exports Markdown from the frozen final DOCX without modifying either final artifact. Run it with Python 3 and PyYAML; changed frozen fingerprints cause a failure, not automatic acceptance.
- `scripts/phase5_report.py` and `scripts/assignment_report.py` consume the current schedule and distinguish known prerequisite IDs from unverified dates.

See `scripts/README.md` for regeneration and check commands. The instructor has now frozen the final syllabus; final dated validation remains deferred. No source collection or normalization rerun is needed.
