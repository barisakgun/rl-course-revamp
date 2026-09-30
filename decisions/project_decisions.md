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
  length: 2 pages
  scope: Problem motivation; tentative MDP/state-action-reward/horizon; one question, candidate baseline, evaluation
    metric and access/compute feasibility. A small related-work pointer, not an exhaustive survey.
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
  operational_state: Concrete project LLM-report instructions and rubric details remain to be finalized before release.
regular_semester_template:
  presentation_window: Late Week 14 or early Week 15
  condition: Instructor available throughout; follows early-Week-14 midterm 3. This is a future-offering template,
    not the current semester schedule.
```
