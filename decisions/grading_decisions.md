# Grading decisions

Category weights and the first two coverage windows are instructor decisions. The instructor clarified that midterm 3 remains in Week 13, through offline RL. The Week 14 version including LLM RL is retained only as a future template. Exam slots are separate from lectures, as confirmed by the instructor. Each midterm is 15%, explicitly confirmed; exact dates and durations remain to be finalized.

```yaml
schema_version: 1
state: weights-and-week-schedule-accepted-dates-pending
date: '2026-09-28'
categories_percent:
  midterms: 45
  project: 35
  assignments: 20
midterms:
- id: midterm_1
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
  scope: Weeks 1–5, before deep RL. Accepted taught/mastery scope governs questions; optional extensions are not
    silently examinable.
- id: midterm_2
  window_weeks:
  - 10
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
- Exact exam dates within accepted windows and exam durations
exam_slots: separate from scheduled lectures; explicitly accepted
exam_duration_minutes: null
final_exam_required: false
midterm_weights_percent:
- 15
- 15
- 15
```
