# Grading decisions

Category weights and the first two coverage windows are instructor decisions. The instructor clarified that midterm 3 remains in Week 13, through offline RL. The Week 14 version including LLM RL is retained only as a future template. Exam slots are separate from lectures, as confirmed by the instructor. Each midterm is 15%, explicitly confirmed; exact dates and durations remain to be finalized. On 2026-11-02 the instructor decided that each midterm's coverage is set right before that midterm, from the material taught by then; the session lists below are planning windows until then. Midterm 1 is fixed on November 5, 2026, covering sessions 1.1–3.2 (the class runs one week behind after a cancellation and a holiday). This coverage and format are for Fall 2026 only; the Weeks 1–5 window is kept as a non-binding template for future offerings.

```yaml
schema_version: 1
state: weights-and-week-schedule-accepted-dates-pending
date: '2026-09-28'
coverage_rule: Each midterm's coverage is decided by the instructor right before that midterm (2026-11-02). Session
  lists for undecided midterms are planning windows. Exam design and workflow guideline in docs/exam_workflow.md.
categories_percent:
  midterms: 45
  project: 35
  assignments: 20
midterms:
- id: midterm_1
  window_weeks:
  - 6
  date: '2026-11-05'
  duration_minutes: 100
  setting: Separate exam slot, not a lecture slot
  allowed_materials: Closed book, no aids. An equation sheet is supplied, as in previous exams (unlabelled equations,
    notation-guide symbols, within the covered material).
  return_mixtures: One short written or true/false question on the forward lambda-return at its 3.2 taught scope.
  courses: COMP 438 and 538 take the same exam (instructor, 2026-11-02).
  coverage_state: decided-2026-11-02
  coverage_sessions:
  - formulate
  - mdp_values
  - bellman
  - improvement
  - mc_td
  - returns
  scope: Sessions 1.1–3.2, Fall 2026 only (instructor, 2026-11-02; the exam date stayed fixed while the class runs
    one week behind). Accepted taught/mastery scope governs questions; optional extensions are not silently
    examinable. This semester, control_targets, control_practice, linear and instability are not in midterm 1; their
    exam placement is decided before midterm 2.
  future_template:
    coverage_sessions:
    - formulate
    - mdp_values
    - bellman
    - improvement
    - mc_td
    - returns
    - control_targets
    - control_practice
    - linear
    - instability
    scope: Planning window for a regular offering (Weeks 1–5, before deep RL), retained from the 2026-09-28 plan.
      Not binding; coverage is still decided right before the midterm, and these topics may change.
- id: midterm_2
  window_weeks:
  - 10
  coverage_state: planning-window
  coverage_sessions:
  - dqn_loop
  - dqn_diagnosis
  - reinforce
  - baseline
  - actor_gae
  - ratios
  - ppo_contrast
  scope: Weeks 6–8 plus 9.1, including SAC; bandits in 9.2 are excluded. Interpret up to bandits as before bandits,
    following explicit session list.
third_midterm:
  state: current-semester-week13-accepted
  future_template:
    week: 14
    coverage_sessions:
    - bandits
    - mcts
    - search_dyna
    - models
    - model_limits
    - offline_failure
    - offline_constraints
    - llm_mapping
    - llm_failure
    placement: Early in Week 14 in a regular semester with instructor availability throughout
  current_semester_alternative:
    week: 13
    coverage_sessions:
    - bandits
    - mcts
    - search_dyna
    - models
    - model_limits
    - offline_failure
    - offline_constraints
  clarification: Midterm 3 is frozen in calendar Week 13, covering taught material through logical 12.2 and excluding
    the LLM bridge. Exact date remains pending; avoid the assumed December 31 loss and January instructor absence.
  accepted_question_direction: Include a brief conceptual question on CQL conservatism at Exposure/explain level,
    replacing its A4 question; no extra exam category or assumed extra exam time.
unresolved:
- Exact dates and durations of midterms 2 and 3
- Exam placement of control_targets, control_practice, linear and instability (decide before midterm 2)
exam_slots: separate from scheduled lectures; explicitly accepted
exam_duration_minutes: null
final_exam_required: false
midterm_weights_percent:
- 15
- 15
- 15
```
