# Grading decisions

Each midterm is worth 15% and takes place outside lectures. The university bookings below apply to both COMP 438 and COMP 538. Booked times are local to Istanbul. Writing time is decided separately. The dates, times and rooms come from the spreadsheet attached to [Hilal Kakiz’s November 5 scheduling email](https://mail.google.com/mail/u/?authuser=baakgun%40ku.edu.tr#all/1a1ab529e4ac9ddd).

On 2026-11-02 the instructor decided that each midterm's coverage is set right before that midterm, from the material taught by then; the session lists below are planning windows until then. Midterm 1 covers sessions 1.1–3.2 (the class runs one week behind after a cancellation and a holiday). This coverage and format are for Fall 2026 only; the Weeks 1–5 window is kept as a non-binding template for future offerings.

```yaml
schema_version: 1
state: midterms-booked-midterm1-format-and-coverage-decided
date: '2026-11-05'
coverage_rule: Each midterm's coverage is decided by the instructor right before that midterm (2026-11-02). Session
  lists for undecided midterms are planning windows. Exam design and workflow guideline in docs/exam_workflow.md.
categories_percent:
  midterms: 45
  project: 35
  assignments: 20
midterms:
- id: midterm_1
  window_weeks:
  - 5
  window_status: University-set calendar Week 5 placement, confirmed by the instructor on 2026-11-02;
    the university schedules the exam. The decided date below governs Fall 2026.
  date: '2026-11-05'
  booked_start: '19:00'
  booked_end: '22:00'
  rooms: [SNAA21]
  duration_minutes: 100
  setting: Separate exam slot, not a lecture slot
  allowed_materials: Closed book, no aids. An equation sheet is supplied, as in previous exams (unlabelled equations,
    notation-guide symbols, within the covered material).
  return_mixtures: One short written or true/false question on the forward lambda-return at its 3.2 taught scope.
  courses: COMP 438 and 538 take the same exam (instructor, 2026-11-02).
  delivery_confirmation: No additional omissions or material shortening beyond the recorded lecture exclusions
    through session 3.2 (instructor, 2026-11-02).
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
    window_weeks:
    - 6
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
  - 9
  date: '2026-12-05'
  booked_start: '08:30'
  booked_end: '11:30'
  rooms: [SOSB10, SOSB11]
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
  state: current-semester-booked
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
    week: 12
    date: '2026-12-27'
    booked_start: '15:00'
    booked_end: '18:00'
    rooms: [SNAA21]
    coverage_sessions:
    - bandits
    - mcts
    - search_dyna
    - models
    - model_limits
    - offline_failure
    - offline_constraints
  clarification: The planning window covers taught material through logical 12.2 and excludes the LLM bridge.
  accepted_question_direction: Include a brief conceptual question on CQL conservatism at Exposure/explain level,
    replacing its A4 question; no extra exam category or assumed extra exam time.
unresolved:
- Writing durations of midterms 2 and 3
- Exam placement of control_targets, control_practice, linear and instability (decide before midterm 2)
exam_slots: separate from scheduled lectures; explicitly accepted
exam_duration_minutes: null
final_exam_required: false
midterm_weights_percent:
- 15
- 15
- 15
```
