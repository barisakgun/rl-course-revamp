# Phase 7 handoff — Teaching Artifact Revision

Prepared 2026-09-30 for a fresh conversation. This is a navigation and planning summary, not a new source of accepted curriculum decisions.

## Current boundary

**Phases 1–6 are complete; the curriculum and final syllabus are frozen. Phase 7 has not started.** This handoff does not authorize artifact construction or reopen decisions. The next instructor request should select the first teaching artifact or batch to work on.

The instructor prefers a concise syllabus with flexibility on timing and requirements. Preserve the final `course/syllabus/syllabusFall26.docx` and instructor-produced `.pdf`. Their accepted fingerprints and freeze scope are in [syllabus decisions](../decisions/syllabus_decisions.yaml). Do not use `syllabusFall26_draft.docx` as the current syllabus, restore omitted detail, or update fingerprints automatically. Upload has not been verified.

## Read on resumption

1. Read `AGENTS.md` and the required context: `config/course.yaml`, `config/sources.yaml`, `config/taxonomy.yaml`, `config/provisional_plan.yaml`, `decisions/course_principles.md`, and `docs/repository_contract.md`.
2. Read the Phase 7 section of [workflow](../docs/workflow.md) and recent entries in the [decision log](../decisions/decision_log.md).
3. Use the authoritative decision file for the artifact being developed:

| Subject | Authoritative record | Useful generated view |
| --- | --- | --- |
| Topic inclusion, role, mastery, delivery and lecture sequence | `decisions/topic_decisions.yaml` | `output/lecture_plan.md`, `output/topic_details.md` |
| Grading and exam coverage | `decisions/grading_decisions.md` | `output/assessment_schedule.md` |
| Assignments, starter strategy, aggregation and LLM-report requirements | `decisions/assignment_decisions.md` | `output/assignments.md` |
| Project scope, milestones, team policy and LLM policy | `decisions/project_decisions.md` | `output/project.md` |
| Videos and checkpoints | `decisions/video_decisions.md` | `output/video_plan.md` |
| Reading policy | `decisions/reading_decisions.md` | `output/readings.md` — internal reference map only |
| Calendar constraints and week targets | `decisions/schedule_decisions.yaml` | `output/assessment_timeline.md`, `output/project_schedule.md` |
| Frozen syllabus identity and scope | `decisions/syllabus_decisions.yaml` | `output/syllabus.md` |

`config/provisional_plan.yaml` contains original hypotheses, some superseded by accepted decisions. Historical phase-completion reports also retain statements such as “Phase 2 has not begun” or earlier unresolved-work descriptions. Neither overrides current decisions. Analysis and generated views are not independent curriculum authority.

## What has been completed

- **Phases 1–2:** Seven course sources inventoried; evidence normalized into stable topic IDs, with source provenance, ambiguity records and book mappings. Start with `sources/current_course/manifest.yaml`, `analysis/source_summaries/current_course.md` and `analysis/normalized_topics.yaml` when reusing material. No broad collection or normalization rerun is needed.
- **Phases 3–4:** Curriculum reviewed and frozen, including scope/mastery/roles, prerequisite order, 26 logical lectures and two prerequisite-video units. Time and curriculum-consistency audits completed.
- **Phase 5:** High-level assignment, project, grading and reading decisions accepted. Implementation, pilots and concrete rubrics were deliberately deferred.
- **Phase 6:** Integrated workload, alignment and consistency audits completed with explicit operational limitations. Instructor simplified the syllabus, incorporated editorial suggestions, produced the PDF and froze it on September 29.
- **Generator alignment, September 30:** Exporter now reads the final DOCX, preserves its wording, hyperlinks, ordered/bulleted lists and merged table columns, and checks both frozen artifact fingerprints. Assignment/project records reflect the final wording. Generated views show the completed freeze and identify detailed schedules as internal planning. No DOCX/PDF changes were made.

The current `course/` file inventory contains syllabus artifacts only; new lecture decks, runnable assignments, project handouts and video materials have not been built there. Existing teaching sources remain evidence and reuse candidates, not verified revised deliverables. Local assignment briefs 1A/1B exist, but their starter code was not supplied; do not assume runnable packages are available.

## Design constraints to carry into artifact work

These are reminders of decisions, not a replacement for their authoritative records.

- Preserve foundations and conceptual progression rather than adding algorithm coverage. Keep Core/Exposure/Extension and mastery distinctions intact; CQL is a bounded conceptual Exposure contrast, while scaffolded IQL and bounded Double DQN implementation are accepted.
- There are 26 logical 70-minute lectures. Teaching uses 1,440 minutes plus 19 additional administration minutes, leaving 68 usable minutes after the configured 85% allowance and separate 20-minute syllabus briefing. Small margins in policy/GAE/PPO and offline units require careful examples and pacing; semester slack is not freely transferable between sessions.
- Grading is assignments 20%, three midterms at 15% each, and project 35%; no final exam. The current internal assignment plan is four individual tasks, counting the best three. The syllabus permits changing the count and dropping the lowest if more than three are offered. Any actual count change requires an aggregation/alignment/workload review.
- A1: planning, MC/TD and tabular control. A2: linear approximation, DQN and a Double DQN target switch. A3: REINFORCE/baselines, actor-critic/GAE calculations and analysis using supplied PPO code; no PPO/SAC implementation requirement. A4: scaffolded IQL and offline data-support diagnosis; no CQL implementation requirement. Full tasks and boundaries are in assignment decisions.
- Project work remains an end-to-end RL study with meaningful baselines and evaluation. Teams of 2–3 are encouraged; individual/four-person exceptions are considered case by case. Well-supported negative results can succeed. Milestone weights are 5/5/7.5/7.5/10 percent of the course grade.
- LLM disclosure and usage reports are required as specified in the final syllabus and decisions. The one-shot/few-shot no-credit rule remains specific to assignments; it is not extended to project coding. Project reports are subject to the final writing-quality policy. Detailed rubric/penalty interpretation and example reports still need implementation work.
- Two prerequisite-video units remain the internal plan: search background before MCTS, and transformer/autoregressive/pretraining/SFT background before live LLM RL. Scope checkpoints are Weeks 4, 8 and 11; the seven-day release lead is tentative. No third policy video is automatically required.
- **No student readings are assigned.** The generic Phase 7 workflow mentions reading lists, but the accepted decision excludes reading-selection/expansion work for this semester. No mandatory LLM assignment is required.
- Estimated total student effort remains **158.7–235 hours for all four assignments, or 148.7–222 for exactly three**, against a 150–180-hour target. These are unpiloted ranges, accepted in principle, not demonstrated workload fit. Best-three grading also leaves an accepted implementation-evidence gap when a task is omitted.

## Remaining Phase 7 work

Phase 7 is artifact-by-artifact, as defined in the workflow. The following is a proposed implementation order, not an accepted new schedule:

1. **Map reuse for the selected lecture block.** Inspect the relevant local slides and examples against accepted session scope/mastery. Identify what can be retained, revised or created; avoid a full-course rewrite before reviewing an initial unit.
2. **Produce the first lecture package.** A practical starting point is logical Week 1, then Week 2: slides, instructor notes, worked examples and short checks for understanding. Account for the Week 1 syllabus briefing and configured buffer. Review the resulting artifact before propagating its format across the course.
3. **Build assignments in release order, starting with A1.** Recover or recreate suitable starter code; implement reference solutions, deterministic checks and bounded experiments. Pin dependencies, pilot on expected student hardware, calibrate active effort and manual grading, and prepare clear submission instructions and the example LLM-use report. Numerical rubric/penalty choices are not already accepted.
4. **Prepare project handouts and rubrics as needed.** Translate accepted milestone purposes and scope into usable instructions without inventing dates or extra deliverables. Include disclosure guidance, contributions, evaluation and reproducibility expectations. Operational presentation arrangements remain deferred as below.
5. **Develop remaining lectures, exercises and video materials in teaching order.** Keep video content within accepted prerequisite scope; use checkpoints for adjustments. Validate derivations, examples and code; inspect rendered decks/documents. If detailed exam materials are requested, follow accepted coverage/mastery and keep solutions separate from student releases.

No slide template, output format or full-course production batch has been selected for Phase 7. When work starts, inspect existing editable source formats and use the relevant presentation/document skill. Resolve artifact-specific preferences when they matter; do not re-ask for already accepted curriculum facts or class hours.

Editable artifacts belong under `course/`; generated/rendered views belong under `output/`; reproducible utilities belong under `scripts/`. Preserve `sources/` as evidence. If implementation exposes a substantive scope, prerequisite or workload problem, record it and explicitly revisit the appropriate decision process; do not silently change the frozen design. Run the time-budget audit after substantive curriculum revisions.

## Deliberately deferred until after Phase 7

Keep the instructor's post-Week-2 registration/attendance checkpoint. These tasks are not prerequisites for starting teaching-artifact work:

- Map all 26 logical lectures to actual dates, including one makeup each in October, November and December. Do not equate logical teaching weeks with calendar weeks. Class hours already appear in the syllabus: Tuesday/Thursday 14:30–15:40, CASEZ27.
- Verify full 21-day assignment windows after taught prerequisites, especially A1's early-Week-7 target; stagger Week 11 deadlines and retain January spacing. Current internal release/due targets are A1 4/early 7, A2 6/9, A3 8/late 11, A4 12/15.
- Confirm exam dates/durations and preparation intervals. Internal targets are MT1 Week 6 through logical Week 5; MT2 Week 10 from DQN through SAC, excluding bandits; MT3 Week 13 from bandits through offline RL, excluding the LLM bridge. The LLM-inclusive Week 14 version is a future-offering template.
- Confirm presentation staffing, team slots, online/recorded arrangements and TA/group grading split. Current internal target is Week 14, tentatively three two-hour slots of eight teams, with own-slot attendance.
- Check the Week 16 final-report target against the official letter-grade deadline and feasible January grading capacity. The retained final-report late-day/Incomplete policy can consume the intended one-week grading buffer.
- Revisit whether additional workflow phases would help manage work after lectures start. This is a note for later discussion; no extra phases have been defined or adopted.

Task pilots, rubric construction and run-budget calibration belong to artifact implementation before release; do not mistakenly defer those along with calendar mapping.

## Verification and practical restart

All checks below passed at the generator-alignment closeout. They are read-only freshness/consistency checks, not proof that future teaching artifacts or actual-date schedules are ready. Python 3 with PyYAML is required.

```sh
python3 -B scripts/syllabus_report.py --check
python3 -B scripts/phase3_audit.py --check
python3 -B scripts/phase4_audit.py --check
python3 -B scripts/phase5_report.py --check
python3 -B scripts/assignment_report.py --check
python3 -B scripts/phase6_report.py --check
python3 -B -m unittest discover -s scripts -p 'test_syllabus_report.py'
```

The three regression tests cover export fidelity, rejection of changed frozen artifacts, and published-fact drift. See [scripts README](../scripts/README.md) for regeneration order; generated files should be regenerated from their sources rather than hand-edited.

`analysis/syllabus_verification.json` is historical visual-review evidence for the old draft only. Current [syllabus verification](../output/audits/syllabus_verification.md) checks final-file identity and text consistency; it does not claim a new final-PDF layout review or upload. Current workload/design limitations are in [workload](../output/audits/workload.md) and [design consistency](../output/audits/design_consistency.md).

At handoff, the workspace contains uncommitted alignment changes; no commit was requested. Inspect `git status` before editing, preserve existing changes, and leave Word lock-file lifecycle changes alone. The immediate next step is to follow the instructor's chosen Phase 7 artifact request, using this handoff and the linked decisions rather than restarting course design.
