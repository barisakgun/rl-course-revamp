# Phase 6 handoff

## Current boundary

**Syllabus frozen by the instructor; Phase 6 closed. Phase 7 has not started.** The authoritative freeze record and artifact fingerprints are in the latest entry of `decisions/decision_log.md`.

The current student-facing artifacts are `course/syllabus/syllabusFall26.docx` and the instructor-produced `course/syllabus/syllabusFall26.pdf`. The instructor completed the final edits and PDF conversion for upload. No upload or fresh agent verification of that final PDF is claimed.

No Phase 6 closeout task remains. Exact-date calendar finalization and operational follow-up remain after Phase 7, retaining the post-Week-2 checkpoint. Possible additional phases for work after lectures start remain a future workflow discussion.

### Before reusing the repository tools in Phase 7

The existing Markdown syllabus, syllabus verification record and generator checks refer to the earlier detailed draft. They do not represent the final concise syllabus. Reconcile final policy wording with structured records and update generator input/export assumptions before reuse; preserve the instructor's flexibility and do not restore removed detail to make old checks pass. This is repository housekeeping for the later work, not a condition on the accepted freeze.

Read AGENTS.md, required context and the latest decision-log entry on resumption. Treat the package description below as the history of the earlier integration pass, not as identification of the frozen artifact.

## Earlier integration package

- `course/syllabus/syllabusFall26_draft.docx`: revised five-page syllabus with compact topic outline, accepted assessment weeks, project milestones, prerequisite videos, no assigned readings and assignment LLM-use rules.
- `output/syllabus.md`: generated directly from the actual DOCX; the old independently populated Markdown syllabus is replaced. `course/syllabus/template.md` is now only its export wrapper.
- `output/assessment_timeline.md`, `output/assessment_schedule.md`, `output/project_schedule.md`, `output/video_plan.md`: current accepted week targets, with exact dates explicitly pending.
- `output/audits/workload.md`, `output/audits/design_consistency.md`, `output/audits/syllabus_verification.md`: updated audit results and limitations. Related assignment/project views were refreshed.
- `analysis/syllabus_verification.json`: original paragraph preservation hashes, editorial review and final DOCX hash tied to a complete five-page visual review. Any further DOCX edit requires rerendering and renewed review.

The earlier draft preserved the catalog description and official prerequisite text verbatim, including the then-supplied `Cop421/521` spelling; the instructor subsequently corrected that name. Class hours, contacts, submission/late-day policy, conduct and makeup policies are retained. The obsolete phrase “early final” was changed to “early exam” to match the accepted absence of a final exam.

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

Concrete assignment scaffolds, pilots, run budgets, rubrics, excess-lateness penalty details and the example LLM-use report remain deferred until implementation before release. No policy numbers were invented. The assignment no-credit rule was not extended to projects; the supplied general disclosure obligation remains in the syllabus.

## Generator and verification workflow

- `scripts/design_data.py` reads accepted calendar-week targets; logical prerequisite labels do not generate fake deadlines.
- `scripts/schedule_report.py` provides the sole timeline renderer, also called by the integrated report. Its standalone command runs no audit and writes no syllabus.
- `scripts/phase6_report.py` audits and renders schedules/reports only. It does not modify the DOCX or Markdown syllabus. With a syllabus review record, it checks the actual DOCX and exported Markdown, including the visual-review hash.
- `scripts/syllabus_report.py` exports Markdown from the editable DOCX without modifying it. Run it with the documents runtime Python; it requires only the standard library.
- `scripts/phase5_report.py` and `scripts/assignment_report.py` consume the current schedule and distinguish known prerequisite IDs from unverified dates.

See `scripts/README.md` for commands and the warning about the old draft path. The instructor has now frozen the final syllabus; final dated validation remains deferred. No source collection or normalization rerun is needed.
