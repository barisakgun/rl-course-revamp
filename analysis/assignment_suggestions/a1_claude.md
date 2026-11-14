# A1 first draft — Claude's suggestion

Author: Claude, 2026-11-14. Status: suggestion for instructor review and ChatGPT cross-review; not an accepted design. Revised the same day with the instructor's answers (section 8) and after ChatGPT's cross-review (`a1_review.md`, R1–R11 and the recheck).

Basis: A1 in `decisions/assignment_decisions.md` (tasks as amended 2026-11-14), `implementation_framework` and `fall_2026_exceptions` in the same file, sessions 2.1–4.2 in `decisions/topic_decisions.yaml`, and `course/notation_guide.md`.

No assignment code has been implemented or run. Every numeric setting marked *pilot* is a starting value to be fixed when the reference solution exists.

## 1. Summary

**Title:** Planning and learning from sampled transitions.

Students work on one small gridworld family through three parts:

1. **Planning with the model:** value iteration and policy iteration.
2. **Prediction from samples:** Monte Carlo and TD(0) on supplied episodes.
3. **Control from interaction:** one ε-greedy loop with SARSA and Q-learning targets, a decay schedule, and zero versus optimistic initialization.

- **Window:** two weeks from release (Fall 2026 special case).
- **Individual work**, with the LLM-use report required by the syllabus.
- **Dependencies:** Python 3.10 or later, `gymnasium` 1.x, `numpy`, `matplotlib`. No PyTorch in A1.
- **Estimated active effort:** 11 to 16 hours (my estimate; the planning range before the 2026-11-14 additions was 9 to 13). Parts 1 and 2 are meant to be finishable in the first week, Part 3 and the answers in the second.

## 2. Environment

One supplied Gymnasium environment, `GridWorld`, built from a text layout.

- **Spaces:** `Discrete` states (cell index) and four `Discrete` actions (up, right, down, left).
- **Conventions:** the handout fixes the state and action ordering, the `small` settings used for the public reference values, and the terminal-entry reward convention.
- **Model access:** `env.unwrapped.P[s][a]` is a list of `(probability, next_state, reward, terminated)` tuples, the same convention as Gymnasium's FrozenLake. Part 1 uses this table; Parts 2 and 3 use only `reset` and `step`.
- **Slip:** with probability `slip`, the agent moves perpendicular to the intended direction (half each side). Moving into a wall leaves the state unchanged.
- **Terminal cells:** goal cells and pit cells end the episode (`terminated=True`).
- **Time limit:** Gymnasium's time-limit wrapper ends long episodes with `truncated=True`. Students must treat the two flags differently.
- **Rewards and γ:** set per layout. The two lecture layouts keep the lecture settings so students can check numbers against the slides. `ledge` uses +1 on entering the goal, −1 on entering a pit, 0 otherwise, with γ = 0.95 (*pilot*). Its zero step reward is deliberate for the initialization comparison in Part 3: the zero table stays unchanged along an unrewarded trajectory, whereas +1 entries decrease on ordinary discounted backups. With a negative step reward, a tried zero-valued action would also fall below untouched ones, and the two tables would be harder to tell apart.

Three layouts:

| Layout | Use | Notes |
| --- | --- | --- |
| `tiny` | Debugging; ungraded public tests | The 2 × 2 lecture calculation grid with its lecture settings (terminal +1 on entry, −0.04 otherwise, γ = 0.5, motion 0.8/0.1/0.1). Small enough to check every number by hand |
| `small` | Graded tests for Parts 1 and 2 | The familiar 4 × 3 lecture grid with its lecture settings |
| `ledge` | Part 3 experiments | A wider grid with a row of pits between start and goal: a short path along the pit edge and a longer safe path. No slip. Differs from the 4 × 12 lecture cliff in size and rewards |

Scored correctness tests use `small` only; the marked short answers may interpret the supplied `ledge` runs (instructor, 2026-11-14). Hidden tests are the same checks on `small` with other settings (γ, slip) and other fixed inputs, not a separate layout.

The `tiny` tests run first and carry no points. The handout prints the `tiny` value table for the first two sweeps and at convergence, the improved policy, and one worked MC and TD(0) update, so a student can print their own tables and compare line by line. `tiny` has no wall or pit, so those cases are first exercised on `small`.

## 3. Student tasks

Students edit three modules. Each function has a docstring with shapes, the notation-guide symbol it corresponds to, and the tie and terminal conventions.

### Part 1 — `dp.py` (planning)

Supplied: `policy_evaluation(P, policy, gamma, theta)`, iterative, returning V and its sweep count.

Conventions, stated in the handout: V starts at 0; sweeps are synchronous; a solver stops when the max-norm change is strictly below `theta`; the final sweep is counted; action ties go to the lowest index.

Students implement:

- `q_from_v(P, V, s, gamma)`: one-step lookahead for all actions in s.
- `value_iteration(P, gamma, theta)`: returns V and the number of sweeps.
- `policy_improvement(P, V, gamma)`: greedy policy for V.
- `policy_iteration(P, gamma, theta)`: alternates the supplied evaluation with improvement until the policy is stable; returns the policy, V, the number of improvement steps and the total evaluation sweeps.

### Part 2 — `prediction.py` (MC and TD(0))

Supplied:

- Files of complete episodes generated on `tiny` and `small` under a fixed policy that terminates, each a list of `(S_t, A_t, R_{t+1}, S_{t+1}, terminated, truncated)`. The cap is high enough that no episode is cut; this is verified when the data are generated, not achieved by dropping episodes.
- A separate small fixture with a truncated transition, used only for the TD(0) test.
- The true v^π from policy evaluation.
- `run_prediction(episodes, method, ...)`, which applies the student's kernel over the episodes in a fixed order from a common initial V and records the root-mean-square error against v^π over non-terminal, non-wall states.

Students implement:

- `returns(rewards, gamma)`: G_t for every step of an episode.
- `mc_update(V, episode, alpha, gamma)`: constant-α every-visit update, V(S_t) ← V(S_t) + α[G_t − V(S_t)], with no visit counts. All G_t are computed first; updates are then applied in chronological order.
- `td0_update(V, s, r, s_next, terminated, alpha, gamma)`: one TD(0) update.

### Part 3 — `control.py` (SARSA and Q-learning)

Supplied: `schedules.py` with `Constant` and `ExponentialDecay(start, rate, floor)`, each exposing `value(step)`; a visit-recording environment wrapper; the evaluation and plotting helpers. The schedule clock is the number of environment transitions so far across all episodes, starting at 0.

Students implement:

- `init_q(n_states, n_actions, value, terminal_states)`: a table filled with `value`, with terminal rows at 0.
- `epsilon_greedy_probs(q_row, epsilon)`: action probabilities, with the greedy action being the lowest-index maximizer.
- `select_action(q_row, epsilon, rng)`: samples from those probabilities with the supplied `numpy` generator.
- `sarsa_target(Q, r, s_next, a_next, terminated, gamma)` and `q_learning_target(Q, r, s_next, terminated, gamma)`.
- `train(env, method, gamma, epsilon_schedule, alpha_schedule, q_init, n_episodes, seed, select_fn=select_action)`: the shared loop. It reads ε and α from the schedules at every step, switches the target by `method`, and returns Q, per-episode raw returns and per-episode lengths. γ comes from the experiment configuration. The supplied driver derives the discounted return from the raw return and the episode length, and counts pit entries from the −1 outcome; both derivations rely on `ledge` having rewards only on terminal entry. Actions are chosen only through `select_fn`, so a test can pass a scripted selector. On a time-limit boundary both methods bootstrap from the final observation, and SARSA still selects a continuation action for its target.

### Experiments — `run_experiments.py` (supplied driver)

The driver calls the student functions with fixed configurations and writes `results.json` and the plots. Students do not write experiment code.

| ID | Question | Configuration | Output |
| --- | --- | --- | --- |
| E1 | Do the two planners agree, and how much work does each do? | VI and PI on `small` | Values, policies; VI sweeps; PI improvement steps and total evaluation sweeps, reported separately |
| E2 | How do MC and TD(0) errors evolve on the same data? | Both kernels on the supplied `small` episodes; two α values each | Root-mean-square error against v^π after each episode |
| E3 | Which path does each control method learn? | SARSA and Q-learning on `ledge`, constant ε = 0.1, α = 0.5 (*pilot*), 10 seeds | Exploratory training: discounted and raw return, pit frequency, transitions used. Separately, a frozen greedy evaluation and the greedy path of each |
| E4 | What does decaying ε change? | E3 repeated with the supplied ε decay | Same outputs as E3 |
| E5 | What does initialization change when ε = 0? | Q-learning on `ledge`, ε = 0, Q initialized to 0 and to +1 | One trace per table: whether the goal was reached by the cap, greedy path length if so, and coverage of reachable non-terminal state-action pairs at the same transition count for both tables (from the supplied recorder) |

With the lowest-index tie rule, the zero-initialized agent at ε = 0 keeps choosing the first action and learns nothing until the time limit, while the optimistic table explores without any ε. That is a stark contrast. If the pilot shows it is too degenerate to be instructive, run E5 at a small ε (for example 0.05) for both tables instead. Either picture has to be confirmed in the pilot before the handout states it. If ε is positive, the two tables are compared on paired seeds.

A model-level check on the candidate `ledge` map (cross-review R2) shows the optimal greedy route and the optimal ε-soft route differ: 9 against 11 moves at 4 × 8, pit −1, γ = 0.95, ε = 0.1, and likewise in the other 35 settings tried. Whether trained agents show this within the budget is a pilot item. Answers are credited for reasoning from the student's own run, not for a particular path.

### Short answers — `answers.md`

Three answers, at most four sentences each, each tied to the student's own plots:

1. E2: one difference between the MC and TD(0) curves and its cause.
2. E3 and E4: compare the greedy paths and training pit frequencies you observed. How do the two targets help explain your results at constant ε, and what changed when ε decayed?
3. E5: what the optimistic table did differently, in the student's own words.

The handout gives optimistic initialization one short paragraph, since it is not taught in class, and says the idea returns later in the course.

## 4. Tests

Public tests ship with the starter with their expected numbers, on `tiny` (ungraded, for debugging) and on `small` (graded). Hidden tests repeat the graded checks on `small` with other settings and different fixed inputs. All scored tests call student functions on known inputs; none depends on a particular random number sequence.

**Part 1**

| ID | Check |
| --- | --- |
| T1 | `q_from_v` on a fixed V, including a state with slip outcomes |
| T2 | VI value table matches expected values within tolerance |
| T3 | VI greedy policy on the converged table: each chosen action is among the maximizers within tolerance |
| T4 | Terminal states keep value 0 |
| T5 | Two values of γ give the two expected tables |
| T6 | VI sweep count under the stated conventions |
| T7 | `policy_improvement` on a fixed V that contains an exact tie: the lowest index is chosen |
| T8 | PI stops on a stable policy when actions tie (no oscillation) |
| T9 | PI values and policy match independent reference values and admissible optimal actions. Agreement with the student's own VI is reported, not scored |

**Part 2**

| ID | Check |
| --- | --- |
| T10 | `returns` on a fixed reward sequence with γ < 1 |
| T11 | Constant-α MC on an episode that revisits a state: one update per visit in chronological order, each with its own G_t (the two orders give different values) |
| T12 | V after two fixed episodes |
| T13 | TD(0) on one fixed transition |
| T14 | TD(0) on a terminated transition with a non-zero successor value: target is r |
| T15 | TD(0) on the truncated fixture: bootstrap from the final observation is kept |
| T16 | Values after the full supplied episode file, both methods |

**Part 3**

| ID | Check |
| --- | --- |
| T17 | `init_q`: fill value applied; terminal rows are 0 |
| T18 | `epsilon_greedy_probs` at ε = 0, ε = 1 and ε = 0.2; ties go to the lowest index; sums to 1 |
| T19 | `select_action` frequencies over many seeded draws match those probabilities within a wide tolerance |
| T20 | SARSA target uses the supplied next action; Q-learning target uses the maximum |
| T21 | Both targets on a terminated transition, with a non-zero sentinel successor row |
| T22 | Scripted trace with a scripted selector and unequal successor values: SARSA backs up and then executes the same action; Q-learning uses the maximum; only the visited entry changes |
| T23 | Same trace under a non-constant α and ε: Q values at two distinct steps match, so α is used at the stated clock indices. The scripted selector records the ε it receives: checked for the initial action at step 0, the SARSA continuation action at the next index, and the first action after a reset at the cumulative transition index |
| T24 | Same trace across a time-limit boundary: both methods bootstrap, SARSA uses a sampled continuation action, and the environment is then reset |
| T25 | `results.json` has finite values, the expected shapes and the configuration fields. Required for submission; no points |

Ungraded smoke test, public: after seeded training on `small`, the greedy policy reaches the goal.

Not tested: exact learned Q-tables, which method scores higher, and anything about forward λ-returns (excluded 2026-11-08).

## 5. Grading proposal

Rubric numbers are open; this is a starting point.

| Component | Share | How graded |
| --- | --- | --- |
| Part 1 tests | 25 | Script |
| Part 2 tests | 25 | Script |
| Part 3 tests | 35 | Script |
| Experiment artifact (T25, plots present) | required | Script; no points |
| Three short answers | 15 | By hand, one common answer guide |
| LLM-use report | required | Checked for presence and the syllabus rule; no points |

Hand grading is three short answers per student.

## 6. Files

Proposed shared location: `course/assignments/a1/`.

| Path | Content | Released to students |
| --- | --- | --- |
| `handout.md` | The assignment text, rendered to PDF | Yes |
| `starter/rlhw/` | `envs/gridworld.py`, `schedules.py`, `evaluate.py`, `plotting.py`, supplied `policy_evaluation` | Yes |
| `starter/dp.py`, `prediction.py`, `control.py` | Student modules with function stubs | Yes |
| `starter/run_experiments.py`, `answers.md`, `llm_report.md` | Driver and response templates | Yes |
| `starter/data/` | Supplied episodes and true values | Yes |
| `starter/tests/` | Public tests with expected numbers | Yes |
| `solution/` | Reference implementation | No |
| `grading/` | Hidden tests, grading script, answer guide | No |

The `rlhw` package is meant to carry over to A2 and A3 (environment, seeding, evaluation, results format).

Submission: one archive with the three modules, `results.json`, the plots, `answers.md` and `llm_report.md`.

## 7. Build order

1. Environment and its own tests.
2. Reference solution for all three parts.
3. Public and hidden tests, checked against the reference solution and against deliberately wrong variants (bootstrap on termination, optimistic terminal rows, max instead of sampled action).
4. Pilot E1–E5; fix the *pilot* settings; time the full run on a laptop.
5. Strip the solution into the starter; write the handout.
6. Starter documents: notebook-to-`.py` instructions, a filled LLM-use report example beside the template, and the pinned dependency file.
7. Clean-machine CPU install and smoke test.
8. Timed pilot from the starter, recording setup, implementation, experiments and writing separately; then release.

## 8. Instructor answers and open questions

Answered 2026-11-14:

- **n-step:** left out.
- **MC variant:** constant-α, no visit counts. If convergence suffers in the pilot, visit-count (sample-mean) step sizes can be added, for TD(0) as well.
- **Tie rule:** lowest index, for now, as the easier one to implement.
- **Layouts:** the 4 × 3 grid is graded; the 2 × 2 grid is added for debugging only.
- **Release date:** revisited once the assignment is built.
- **Grading boundary:** scored tests on the 4 × 3 only; marked answers may use the `ledge` runs.

Still open:

1. **Pilot:** who does the timed pilot from the starter (review R9).
2. **Grading shares** in section 5.
3. **E5 form:** ε = 0 with the stark contrast, or a small ε, decided from the pilot.

## 9. Limits of this draft

- No assignment code exists. The Gymnasium details used here were confirmed locally on Gymnasium 1.4.0 (Python 3.11, NumPy 1.26): the `P[s][a]` tuple format, the five-value `step` return and the time-limit wrapper.
- The `ledge` settings (size, γ, ε, α, episode count) are unpiloted. The SARSA and Q-learning paths must actually differ under them before E3 is fixed.
- Constant-α MC and TD(0) fluctuate around the true values instead of converging; whether the E2 curves are clear enough at the chosen α is a pilot question.
- The effort estimate is not from a pilot. If the pilot runs long, the trim order is: drop the second α in E2, shorten the E5 answer to one observation; no accepted kernel or the control comparison is cut.
