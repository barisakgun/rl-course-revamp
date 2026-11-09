# Project decisions

High-level project design is accepted. The revised week-level schedule is provisionally frozen until the post-Week-2 review. Presentation delivery is online and TA-led; exact slots and TA/peer grading weights remain open.

```yaml
schema_version: 1
state: high-level-design-accepted-with-in-semester-scheduling-caveat
accepted_structure:
- proposal
- formulation_design
- progress_evaluation
- presentation
- final_report
accepted_purpose: End-to-end RL formulation, implementation, baseline comparison, systematic evaluation and communication,
  following decisions/course_principles.md.
grading_source: decisions/grading_decisions.md#/categories_percent/project
scheduling_source: config/course.yaml#/design/project_presentations_outside_class_hours
tentative_detail_source: analysis/phase5_plan.yaml#/project (workload estimates, historical rationale and deferred
  operational suggestions only)
milestones:
- id: proposal
  name: Proposal
  week: 4
  weight_percent: 5
  length: 2 pages + references
  due_at: '2026-11-01T23:59:00+03:00'
  submission_platform: LearnHub
  submission_cutoff: The syllabus submission and late-day policies apply. Once grading begins, no further
    submissions or replacement files will be accepted.
  scope: Problem motivation and definition; tentative MDP/state-action-reward/horizon; one question and a tentative
    baseline. High-level, potentially incomplete related work should support motivation and problem definition.
    An initial evaluation plan should connect metrics and the intended comparison to the question, and address
    environment/data access, available compute and practical feasibility. An exhaustive survey, completed
    implementation and experimental results are not required at this stage.
  clarification_date: '2026-10-22'
  prerequisites:
  - formulate
  - mdp_values
  - bellman
  - improvement
  evidence: Problem and metric are well defined; no deep-RL implementation expected.
- id: formulation_design
  name: Formulation/design
  week: 7
  weight_percent: 5
  length: 2–3 pages
  scope: Refine formulation, establish a runnable environment/data pipeline and simple baseline, identify one planned
    comparison and evaluation protocol, record compute budget and fallback. Advanced policy method can remain a
    plan.
  prerequisites:
  - control_targets
  - linear
  - dqn_loop
  - dqn_diagnosis
  evidence: Defensible formulation and feasible design; no PPO/GAE completion required before their teaching.
  placement: later in the week
- id: progress_evaluation
  name: Progress and evaluation plan
  week: 11
  weight_percent: 7.5
  length: 3–4 pages
  scope: Show a working baseline and preliminary learning/evaluation result; specify held-out evaluation/seeds/budget,
    one ablation or controlled comparison, failure diagnosis and remaining work. Reuse unchanged formulation text.
  prerequisites:
  - dqn_diagnosis
  - baseline
  - actor_gae
  - ppo_contrast
  evidence: End-to-end execution and interpretable preliminary evidence, not a final benchmark win.
  placement: early in the week
- id: presentation
  name: Presentation
  week: 14
  weight_percent: 7.5
  length: 10 minutes + 3 minutes discussion per team
  scope: Problem, method/baseline, key evidence, limitations and contributions. Outside lecture hours; give each
    member a short explanation opportunity.
  prerequisites:
  - ppo_contrast
  evidence: Clear reasoning and ownership; project-specific advanced concepts prepared earlier if needed.
- id: final_report
  name: Final report and reproducibility package
  weight_percent: 10
  length: 6–8 pages + references
  deadline_rule: One week before letter grades are due
  expected_window: Week 16 (January 18–24, 2027); exact deadline must also satisfy the letter-grade rule
  scope: Consolidate prior reports into formulation, related work, baseline/method, implementation, evaluation,
    uncertainty/limitations and conclusions. Submit runnable code/configuration, seeds, environment versions, representative
    logs and contribution statement.
  prerequisites:
  - ppo_contrast
  evidence: Reproducible, justified conclusions and honest negative findings; no novelty or benchmark-superiority
    requirement.
  target_week: 16
team_size:
  encouraged:
  - 2
  - 3
  case_by_case:
  - 1
  - 4
presentation_plan:
  state: tentative-until-proposals-and-team-freeze
  expected_max_teams: 24
  slot_count: 3
  slot_minutes: 120
  teams_per_slot: 8
  talk_minutes: 10
  discussion_minutes: 3
  attendance: Each team attends only its own slot.
  peer_grading: TA and attending groups grade presentations; weight split, rubric, aggregation and moderation to
    be finalized.
  finalization_trigger: Review TA/student availability after Week 2; allocate final team slots after proposals/team
    freeze.
  schedule_conflict: Presentations in Week 14 are separated from Week 13 midterm 3. Exact slots and TA availability
    require confirmation.
  delivery: Online, TA-led and recorded; instructor unavailable for live attendance
accepted_types:
- Controlled reproduction plus one ablation
- Small RL application with justified formulation and baseline
- Focused modification of a familiar method
- Data-support/model-error/evaluation study with a working RL baseline
advanced_track: Offline or LLM RL projects need early self-study, a runnable simple baseline and a compute-feasible
  fallback by Week 7. Do not require all teams to use late topics; advanced extensions cannot postpone the Week
  11 progress evidence. Prefer small models, fixed datasets or supplied traces where appropriate, not costly model
  pretraining.
evaluation: One meaningful baseline and one controlled comparison; keep data/interaction/compute budgets explicit.
  Pilot on a laptop; use a planning target of three independent seeds when feasible and report limitations if fewer.
  Separate tuning from final evaluation and include a failure case.
grading_principle: Grade formulation, correctness, experimental reasoning and communication. Negative results can
  succeed if well supported; extra compute and polished prose do not substitute for understanding.
llm_use:
  source: course/syllabus/syllabusFall26.docx, Large Language Model (LLM) Use Policy; instructor-frozen 2026-09-29
  policy: LLMs may be used for coding and reports with disclosure; failure to disclose is treated as plagiarism.
    Students remain responsible for errors and must understand, check and explain submitted work. An LLM-use
    report is required for each report; requirement details will be provided before the first assignment/report.
    The one-shot/few-shot no-credit rule is specific to assignments, not extended to project coding.
  writing_quality: Project reports will lose marks for verbose, repetitive, unnecessarily detailed, unfocused or vague
    writing, including such writing frequently produced by AI tools.
  ownership_boundary: Students must choose and justify their project and develop its substantive content. Do not
    delegate project selection or the writing of an entire proposal or later project report to AI. Brainstorming
    and writing assistance remain permitted with disclosure; this is not a new project-coding restriction.
  ownership_boundary_authority: Instructor's proposal-guidelines request, 2026-10-22.
  operational_state: Instructor accepted the written-report LLM-use guidelines on October 22, 2026. The current wording is in
    course/projects/llm_use_written_reports_chatgpt/main.tex; the accepted PDF is in course/projects/handouts/.
    Publication is not recorded. Proposal-rubric calibration is now in progress; see proposal_grading_pilot.
proposal_guidelines_preparation:
  state: guidelines-accepted; rubric-in-calibration
  accepted_date: '2026-10-22'
  instruction_date: '2026-10-22'
  scope_source: milestones/proposal
  release: TBD
  due_source: milestones/proposal/due_at
  delivery: Give the standalone guidelines on proposal release day. The instructor now anticipates today or tomorrow;
    do not put a release date in the document. The November 1 deadline supersedes the earlier due-date TBD.
  deck_dates: The October 22 overview render retains its originally requested TBD placeholders. Update its proposal
    due date before release; other release/due dates remain unbooked. Do not regenerate the editable deck from text.
  guidelines_source: course/projects/proposal_guidelines_chatgpt/main.tex
  accepted_pdfs:
    proposal: course/projects/handouts/proposal_guidelines_chatgpt.pdf
    llm_use: course/projects/handouts/llm_use_written_reports_chatgpt.pdf
  pending_recommendations: analysis/project_proposal_preparation_chatgpt.md
  rubric_review: Revised for the instructor's November 9 grading pilot; see proposal_grading_pilot.
  remaining_release_details:
  - Publication of the instructor-edited guidelines and companion instructions (not yet recorded)
proposal_grading_pilot:
  state: ready-for-pilot; calibration-pending
  instruction_date: '2026-11-09'
  rubric_source: course/projects/proposal_rubric_chatgpt/main.tex
  ai_guidelines_source: course/projects/ai_proposal_grading_guidelines_chatgpt/main.tex
  scoring: Use the rubric's 18 scored rows totaling 100 points, with explicit full-credit and partial-credit anchors.
    Numeric weights are pilot allocations, not frozen cohort-wide grading policy. The proposal remains 5 percent
    of the overall course grade. Do not add requirements beyond the released proposal handout.
  advisory: Scope reasonableness accounts for group size. Assess RL centrality and expected RL versus infrastructure
    or other work separately. These assessments remain outside the numerical score and cannot add deductions or grade caps.
  calibration: Instructor will test a few proposals with two AIs and one human grader independently, then compare
    criterion judgments, evidence and advisory labels before deciding revisions. No pilot submissions have been graded
    as part of preparing these documents.
  scope: Update the rubric and draft AI grading guidelines only. Preserve accepted student-facing guidelines.
  review_source: analysis/proposal_grading_review.md
  instructor_decisions_2026_11_09:
    format_violations: Highlight page overflows and other format violations in the student feedback; grade content
      past the limit normally. No separate automatic format penalty or 10-points-per-page deduction. The instructor's
      later clarification retains current R16, including its format component, for the pilot; this supersedes the
      earlier blanket no-format-deduction and citation-only interpretation. Any equivalent-length estimate is diagnostic,
      not a penalty formula.
    r16: Keep the current four-point citations-and-format criterion and its current scoring guidance through the pilot.
      Reconsider a citation-only criterion and format handling after the pilot.
    technical_correctness: Technical errors enter the level scale and the required feedback.
    r01: Use R01a motivation/problem, R01b focused question and R01c RL rationale, four points each. This pilot split
      is instructor-approved. R01c asks why RL is appropriate; it does not require explicit superiority comparisons
      with other methods or exclude a justified one-step/bandit formulation.
    r12: Rephrase R12 as the intended evaluation experiments rather than a comparison.
    calibration_text: Calibration procedure lives only in the AI grading guidelines, not in the rubric.
    ai_runs: Run each AI multiple times per pilot proposal.
    student_feedback: Send all assessment output to students, including advisory labels, except the guidelines'
      section 7 review questions, whose release the instructor decides; may change after the pilot.
    scope_context: Feedback returns by the end of the week of 2026-11-09, leaving about 8 weeks for implementation,
      presentation and report. Most if not all teams will use AI help. The instructor will try to obtain HPC access
      for undergraduates who can justify it. Milestone timing is dynamic and may be adjusted during the semester;
      the scope context gives no fixed milestone dates.
    deferred: Row consolidation after the pilot; rounding. Layout cosmetics are low priority because the rubric is
      internal.
  revision_status: Recorded revisions and ChatGPT review corrections applied to both documents; PDFs regenerated
    for the pilot. R16 retained verbatim, confirmed by the instructor to Claude on 2026-11-09, so format may lower R16
    only. The guidelines now mark section 7 as "release will be decided by the instructor"; both documents are ready
    for the pilot. Calibration results and cohort-wide freeze remain pending.
regular_semester_template:
  presentation_window: Late Week 14 or early Week 15
  condition: Instructor available throughout; follows early-Week-14 midterm 3. This is a future-offering template,
    not the current semester schedule.
```
