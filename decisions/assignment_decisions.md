# Assignment decisions

High-level assignment design is accepted. Concrete rubrics and the example LLM-use report are deferred to the semester; current schedules are derived from the accepted three-week rule.

```yaml
schema_version: 1
state: high-level-design-accepted
grading_source: decisions/grading_decisions.md#/categories_percent/assignments
llm_use:
  allowed: true
  disclosure: Include examples of how LLMs were used.
  no_credit_rule: Instructor specifies no credit for one-shot or few-shot delegation of the assignment solution.
  operational_definition_state: pending
  boundary: Prompt count alone is not yet an operational rubric; clarify evidence of student reasoning, verification
    and modification during assignment design.
  report_requirements:
  - Identify which task components used an LLM; include representative prompts and output excerpts.
  - Explain what was accepted, rejected or changed, and why; supply at least one relevant check/debugging example
    if an LLM contributed a solution.
  - Explain the submitted update/experiment in the student’s own terms. Disclose non-use without manufacturing logs.
  report_state: accepted; provide an example report when preparing concrete assignments
unresolved: []
design_scope: High-level tasks, individual/best-three policy and starter strategy accepted. Timing follows the Phase
  6 rule. Rubric/example work is outside the Phase 5 gate and deferred to the semester.
aggregation:
  offered_count: 4
  counted_count: 3
  method: best-three-of-four
  formula: assignment category score = 20 × mean(highest three normalized scores); omitted submissions count as
    zero
  normalized_score_range:
  - 0
  - 1
  completion_rule: No separate requirement to complete all four is adopted.
authorship: individual
staffing_constraint: At most one TA, possibly none; minimize routine hand grading and repeated bespoke experiment
  setup.
refinements:
  A1: Remove the separately hand-graded predict-one-target task.
  A3: Use an existing PPO implementation for clipping/behavior analysis; no PPO or SAC implementation requirement.
  A4: Scaffolded IQL implementation accepted; CQL conceptual assessment stays in midterm 3.
  rubric: Finalize rubrics when concrete assignments exist; prior numerical splits are not adopted.
assignments:
- id: A1
  title: Planning and learning from sampled transitions
  prerequisites:
  - improvement
  - mc_td
  - returns
  - control_practice
  group_ids:
  - formulation
  - planning
  - prediction
  - control
  - evaluation
  outcomes:
  - L02
  - L03
  - L04
  - L06
  - L07
  purpose: Make the common backup structure and the difference between a model, sampled returns and control targets
    concrete.
  tasks:
  - Implement one value-iteration solver on a small supplied MDP; compare supplied policy-iteration results rather
    than implementing a second planning solver.
  - Complete small MC-prediction and TD(0)-prediction update kernels on a shared trajectory. Use supplied checks
    for n-step/terminal handling and a compact interpretation of the comparison; no separate hand-worked target
    submission.
  - Implement one shared epsilon-greedy tabular control loop with SARSA and Q-learning target choices; compare one
    deliberately chosen exploratory-control case.
  starter: One small gridworld/MDP API, trajectory data, plotting and evaluation harness, supplied PI comparator,
    tests for terminal handling. Local HW1A is the conceptual reuse base; its starter code was not supplied in this
    repository and must be recovered or recreated before release.
  exam_bridge: 'Midterm 1: work through an unfamiliar backup or diagnose a changed target. Do not ask students to
    memorize their code.'
  schedule:
    release_week: 4
    due_week: 7
    due_placement: early
- id: A2
  title: Representation, instability and a small DQN
  prerequisites:
  - linear
  - instability
  - dqn_diagnosis
  group_ids:
  - approximation
  - deep_value
  - double_estimators
  - evaluation
  - maximization_bias_core
  - double_dqn_core
  outcomes:
  - L04
  - L06
  - L07
  purpose: Separate representation insufficiency from unstable learning, then explain the replay/target machinery
    through a controlled implementation.
  tasks:
  - Implement a linear semi-gradient update. Use supplied contrasting feature sets/data to distinguish a sufficient
    representation, an insufficient representation, and an off-policy instability example.
  - Complete the DQN TD loss, terminal mask, target-network update and replay sampling hooks in a supplied small
    training loop.
  - Run one short end-to-end learner and one controlled replay/target comparison; use supplied longer traces to
    extend diagnosis without requiring long training.
  - Add Double DQN as a target-selection switch in the existing DQN update. Use the online network to select the
    next action and the existing target network to evaluate it. Grade with fixed tensor/terminal tests; no separate
    environment, double-estimator essay or required performance advantage.
  starter: Small CPU-feasible environment, neural network/optimizer scaffolding, bounded replay store, fixed run
    configurations, divergence demonstration, reference traces and plotting. Adapt local HW1B ideas without requiring
    the entire Pacman framework or its unrelated questions; linked code has not been executed.
  exam_bridge: Midterm 1 may assess only already-taught linear/instability reasoning. Midterm 2 may assess DQN/replay/target
    reasoning; do not require completed A2 in midterm 1.
  grading_design: Mostly automated update/target tests and standard output files; at most one short diagnostic response
    using the existing experiment. Do not award points for Double DQN outperforming DQN in a small stochastic run.
  schedule:
    release_week: 6
    due_week: 9
    due_placement: unspecified
- id: A3
  title: Policy-gradient estimators and update diagnosis
  prerequisites:
  - baseline
  - actor_gae
  - ratios
  group_ids:
  - policy_estimators
  - policy_updates
  - evaluation
  outcomes:
  - L04
  - L06
  - L07
  - L08
  purpose: Implement a representative policy estimator and connect variance reduction, critic targets and constrained
    updates without another full algorithm stack.
  tasks:
  - Implement REINFORCE with reward-to-go and an action-independent learned baseline in a supplied harness. Keep
    score-function/baseline derivation in the midterm assessment path; use fixed estimator checks here instead of
    another long derivation to grade.
  - Compare a baseline/no-baseline condition at a fixed interaction budget; analyze supplied multi-seed results
    if full repeats are too slow.
  - Construct a simple actor-critic target and a short GAE sequence in provided code cells with automatic checks;
    connect them to forward returns through a compact answer.
  - Use supplied, pinned PPO code on one small environment. Run a reference configuration and one changed clip-range
    setting with other settings held fixed; inspect standardized reward, likelihood-ratio, clip-fraction, approximate-KL
    and entropy diagnostics. Answer two short structured questions about update behavior and its limits. No PPO/SAC
    implementation, broad tuning sweep or extra algorithm comparison.
  starter: Supplied small policy/value networks, rollout API, optimizer and diagnostic plots. Students own the estimator,
    baseline loss and their integration; reference tests catch sign, discount, terminal and accidental-baseline-gradient
    errors. Supply the PPO implementation, dependency environment, instrumented diagnostics and fixed configurations;
    students do not install an arbitrary library or instrument it themselves. Provide reference traces if short
    runs are inconclusive.
  exam_bridge: 'Midterm 2: modify a return/baseline/ratio in a small example and predict the consequence. Students
    may attempt A3 for preparation, but the exam must not assume submission, solution access or graded feedback
    before its deadline.'
  grading_design: Automate run configuration/metrics checks and calculation tests. Manually grade two short interpretations
    using one common answer guide. Do not grade stochastic return rankings. Clip fraction outside the ratio interval
    is not identical to the fraction whose surrogate is clipped for a given advantage sign; clipping is not a hard
    bound on actual policy change.
  schedule:
    release_week: 8
    due_week: 11
    due_placement: later
- id: A4
  title: Scaffolded IQL and offline data support
  prerequisites:
  - offline_failure
  - offline_constraints
  group_ids:
  - offline_concepts
  - offline_iql
  - bc_motivation
  - evaluation
  outcomes:
  - L04
  - L05
  - L06
  - L07
  - L08
  purpose: Implement the three central IQL losses in a supplied small training system, then diagnose data-support
    effects at the accepted bounded Core implementation scope.
  tasks:
  - Inspect two provided fixed datasets for the same small environment with different action support; identify the
    evaluation protocol and a coverage limitation.
  - 'Implement three bounded functions: expectile value loss, Q regression against a supplied reward/next-V target
    convention, and advantage-weighted policy fitting. For a discrete-action teaching task, use supplied categorical
    policy machinery and weighted log likelihood; optimizer, network, target updates and stability settings are
    provided.'
  - Train the scaffolded IQL learner on the two datasets and compare with supplied BC and naive offline-Q baselines
    using fixed budgets. No BC/CQL/SAC implementation or environment-data collection.
  - Submit standardized curves/table and two short answers explaining one support-dependent result and a limitation.
    Correctness tests cover losses, terminal handling, gradient stops and weights; do not require a benchmark win
    or exhaustive parameter search.
  starter: Provide datasets, small networks, optimizers, target-network handling, bounded advantage weights, training/evaluation
    loop, BC/naive-Q reference outputs and loss-level tests. Reuse familiar DQN regression and policy log-likelihood
    interfaces. Include explicit equations, tensor shapes and gradient-flow notes; no new required paper reading
    or GPU dependency.
  exam_bridge: Midterm 3 uses shared lecture-level offline examples. It must not assume A4 has been submitted or
    its feedback released.
  grading_design: Automated numeric and gradient tests for the three losses; a smoke-run artifact and one standardized
    table; manually grade two short support/failure interpretations. Staff must pilot data and the complete solution
    before release.
  schedule:
    release_week: 12
    due_week: 15
    due_placement: unspecified
schedule_policy:
  release: Immediately after the last relevant teaching session in prerequisites
  duration_days: 21
  overlap_rule: Keep original releases after prerequisites; allow one-week overlaps between A1/A2 and A2/A3. Do
    not delay releases to serialize assignments.
  order:
  - A1
  - A2
  - A3
  - A4
  calendar_rule: Calendar-week targets are provisionally frozen in each assignment schedule. Final dates must retain
    at least 21 elapsed days after prerequisite-ready release. Reconcile early Week 7 A1 with the actual Week 4
    teaching/makeup dates at the post-Week-2 review; do not silently shorten the window.
  prior_january_target: A4 due Week 15; preserve spacing before the Week 16 project final report when assigning
    dates.
deferred_to_semester:
- Concrete rubric/penalty details
- Example LLM-use report
- Implementation, pilot calibration and final run budgets before task release
accepted_design:
  delivery: Release instructions and starter code asynchronously; no new lecture administration or mandatory reading/video
    is assumed. Any required walkthrough must be budgeted before assignment release. Solutions/feedback are part
    of the assignment support plan, not extra examinable reading.
  starter_strategy: Use one small interface across A1/A2 where useful and a compatible trajectory/evaluation interface
    for A3. Recover local starter code only if available and suitable; current inventory does not supply a runnable
    local package. Pin dependencies, supply smoke tests and deterministic small target checks. Do not claim reference
    code has been tested or redistribution cleared; check permissions if adapting external code. Phase 5 specifies
    this strategy, not implementation of teaching artifacts.
  submission_proposal: Code/notebook, compact answers in provided response cells, essential plots/tables and a short
    process/disclosure appendix. No separate long report. Include a no-LLM-use declaration when applicable; do not
    require invented interactions.
```
