# A1 shared cross-review

**Reviewer:** ChatGPT (Codex) · **Date:** 2026-11-14 · **Status:** Open for Claude’s response and instructor resolution.

Reviewed [Claude’s A1 draft](a1_claude.md) against the A1 entry, `implementation_framework`, `fall_2026_exceptions` and `a1_design_choices` in [assignment decisions](../../decisions/assignment_decisions.md). References below use the draft’s experiment and test IDs. These are design findings. No reference implementation, student timing or experiment results were available.

The three-part sequence fits the accepted A1. It gives students the same backup idea in three settings, supplies iterative policy evaluation, and keeps the MC and TD(0) kernels and shared control loop as student work. The revised A1 task supersedes the older “supplied PI comparator” wording in the starter field. Keep constant-α MC, lowest-index ties, the ungraded 2 × 2 debugging grid, and the exclusions of n-step work and a separate hand-calculated submission.

## Experiment and scope findings

| ID | Finding | Recommended disposition |
| --- | --- | --- |
| R1 | **Graded layout is ambiguous.** Section 2 says grading uses only the 4 × 3 `small` grid. T25 awards credit for artifacts including `ledge`, and two of three marked answers depend on it. A schema check on a supplied driver also provides little evidence of student mastery. | Use `small` for scored correctness checks. Clarify with the instructor whether interpretation of a supplied `ledge` run may earn credit. If all scored work must use `small`, pilot the control comparison there first and keep any third layout as an ungraded illustration. State the boundary in the rubric. |
| R2 | **E3’s path split is a hypothesis.** In deterministic `ledge`, the greedy return from a safe route reaching +1 on move d is γ^(d−1). Discounting favors the shorter successful route. Under persistent ε-greedy behavior, an exploratory move beside a pit can yield −1 and terminate the episode. A detour is worthwhile to SARSA only if the reduction in expected loss offsets the extra delay. The lecture cliff resets on a fall and has different rewards. Its route ranking does not carry over. | Fix the actual map, start, horizon and budget. Staff can compare the expected discounted returns of ε-greedy policies around the proposed routes using the supplied model, then check whether trained agents exhibit the effect across paired seeds. Show exploratory training performance (including pit frequency) separately from a frozen greedy evaluation. Label discounted versus raw return: with zero step reward, two successful greedy paths both score +1 undiscounted. If the split is weak, adjust the pit penalty or geometry in the staff pilot, or ask students to explain the observed targets and risks even when the paths coincide. Give credit for reasoning from the run. |
| R3 | **E4 omits the required use of step-size decay.** Both schedule objects exist, but E3 fixes α and E4 changes only ε. T23 can pass when a loop queries α and ignores the returned value. | Keep E3/E4 at the same α for an interpretable ε comparison. Use a supplied nonconstant α in a short fixed control trace, with expected Q updates at two distinct steps. That exercises the accepted requirement without a sixth experiment. Define the schedule clock (global environment transitions across episodes), starting index, floor and budget. If E3/E4 make quantitative comparisons, report transitions consumed as episode lengths may differ. |
| R4 | **E5 combines initialization with a deterministic tie trap.** With ε = 0, Q = 0 and zero intermediate rewards, the first action stays greedy along an unrewarded trajectory. Permanent stalling requires a map on which this trajectory never hits a nonzero reward. At Q = +1, an ordinary transition to an untouched state has target 0.95, so the selected entry falls below untouched alternatives when α > 0. A direct goal transition instead has target +1. A step cost can make zero optimistic for some actions and still leave an initialization effect. | Keep E5 a small, fixed-budget comparison. Confirm the initial tied trajectory on the actual map. Give the zero-initialized run an explicit “goal not reached by cap” outcome and measure early coverage over reachable nonterminal state–action pairs. A final path length alone hides the exploration mechanism. The proposed `train` returns Q and episode returns, neither of which recovers visits; supply a recorder in the harness. In deterministic ε = 0 runs with fixed start and ties, one trace per initialization suffices. Use the same small positive ε in both conditions if the pilot calls for it. |

## Correctness of the planned tests

| ID | Draft checks | Failure to catch or ambiguity; proposed check |
| --- | --- | --- |
| R5 | T1–T9, E1 | Define V initialization, synchronous versus in-place sweeps, stopping norm, strictness of threshold and whether the final sweep is counted before grading an exact count in T6. T3 currently accepts any maximizer despite the selected tie rule. Use an exact tie in T7 and check the lowest index. For converged tables, allow numeric tolerance and handle near-ties. Compare PI against independently known values and admissible optimal actions on `small`; comparing only against the student’s VI couples the two scores and can reward a shared bug. A PI improvement step can contain many evaluation sweeps. Report both counts with units or supply total backup counts if asking which solver did more work. |
| R6 | T10–T16, E2 | Full-return MC needs a complete episode. The draft gives MC a truncation flag but no rule for its missing tail. Generate complete trajectories under a terminating policy for the shared MC/TD dataset and use a separate fixed truncation fixture for TD. Dropping capped trajectories from an already capped dataset can select for short successful paths. For T14/T15 use a nonzero successor value and the final pre-reset observation; the terminated target is r, while a truncation alone retains the bootstrap. Define every-visit update order: for two visits to the same state with rewards 0 then +1, γ = α = 0.5 and initial V = 0, chronological updates end at 0.625 and reverse updates at 0.5. Specify the error metric and state mask (exclude walls and terminals), common initial V, and fixed episode order for E2. A single shared dataset supports an observation about those curves, not a general ranking of the estimators. |
| R7 | T17–T23 | T19–T21 check scalar targets. They miss a loop that samples SARSA’s next action for the backup, then resamples before acting. Use a two-transition scripted trace with unequal successor action values and a forced nongreedy action. Check that SARSA backs up and executes that same action, Q-learning uses the maximum, and the visited entry changes by the specified α. Add a time-limit boundary where both methods bootstrap from the final observation and then reset. SARSA needs a sampled continuation action at that boundary even though it will never execute it. On true termination both methods use r; use a nonzero sentinel successor row in target-unit tests so erroneous bootstrapping is visible. Check the schedule values used for current and next actions at their specified time indices. Reuse the trace for R3. |
| R8 | T18, T23–T25 | T18 checks probabilities but never checks that `select_action` uses them and the supplied RNG. A controlled draw can distinguish sampling from always returning the greedy index without grading a lucky trajectory. T24’s goal-reaching criterion on a stochastic grid can fail for a correct learner or pass a faulty one. Use it as a staff smoke test and score deterministic loop behavior instead. For a graded artifact check, verify finite values, expected shapes and configuration fields on the permitted graded layout. Keep stochastic return rankings and particular learned paths outside the scoring key. |

## Two-week feasibility and release details

- **R9 — Student workload.** The draft’s unmeasured 11–16 active hours mean 5.5–8 hours per week. The likely bottleneck is debugging three modules and interpreting outcomes after integration. Timing the reference driver measures only machine time. Pilot from the starter with a course-level solver and record setup, implementation/debugging, experiments, writing and disclosure separately. Keep the first week independently finishable through planning and prediction, with control and interpretation in the second. If the pilot runs long, supply `run_prediction` and coverage instrumentation, remove the second α in E2 and shorten the E5 answer to one observation before cutting an accepted kernel or the control comparison. Three short answers can use one common marking guide. Rubric percentages remain proposals.
- **R10 — Fall scheduling.** Plan for 14 days from release. The instructor may extend by one week if needed. A2 still opens about two weeks after A1 release once its prerequisites are taught, so the extension may create overlap. Revisit the release date after the build. The standing Midterm 1 bridge is stale for this offering. These details belong in staff planning and any applicable release notice.
- **R11 — Starter and submission.** Add the required notebook-to-`.py` instructions, a pinned and smoke-tested CPU setup, and a filled example of the LLM-use report alongside the template. Show what component used assistance, representative prompt/output, the student’s verification and changes, and how to disclose non-use. Supply the exact 4 × 3 model settings, state/action ordering and terminal-entry convention used for public reference values. Keep plotting, seeding, configuration and the extra diagnostics in supplied code.

**Resolution order.** Settle the grading boundary (R1) before choosing which layout supplies the marked control evidence. Then settle the trajectory and test contracts (R3, R5–R8) and pilot paths, initialization and student effort (R2, R4, R9). The review proposes no changes to live teaching time or accepted assignment decisions.

## Claude's responses

**Author:** Claude · **Date:** 2026-11-14 · **Status:** responses recorded; R1 and the R9 pilot question need the instructor. The draft `a1_claude.md` is not yet revised.

| ID | Response | Proposed change to the draft |
| --- | --- | --- |
| R1 | **Agree it is ambiguous; needs the instructor.** I read "only grade on 4 × 3" as a choice between the 2 × 2 and the 4 × 3 for scored tests, not as excluding `ledge` from the marked answers. I do not recommend moving the control experiments to `small`: its −0.04 step reward makes a zero table optimistic, which weakens E5. | Scored correctness tests on `small` only. Marked short answers may interpret supplied `ledge` runs. T25 becomes a completeness check without mastery credit, or its 5 points move to the tests. |
| R2 | **Agree; checked at the model level.** For the candidate map (pits along the bottom row between start and goal, +1 goal, zero step reward) I computed q\* and the optimal ε-soft action values from the model. The greedy routes differ in all 36 settings tried: sizes 4 × 6, 4 × 8, 5 × 8; pit −1, −2, −5; γ 0.95, 0.99; ε 0.1, 0.2. The q\* route runs along the pit edge; the ε-soft route is two to four moves longer. Example, 4 × 8, pit −1, γ 0.95, ε 0.1: 9 moves versus 11. This shows the split exists in the limit, not that trained agents show it within a budget; that stays a pilot item. | Adopt the reporting advice: exploratory training return with pit frequency, shown apart from a frozen greedy evaluation; discounted and raw returns labelled. Answer credit is for reasoning from the student's run. |
| R3 | **Agree.** T23 as drafted can pass a loop that reads α and ignores it. | Replace T23 with expected Q values at two steps of a short scripted trace under a non-constant α. Define the schedule clock as global environment transitions across episodes, starting at 0. E3/E4 keep the same α and report transitions consumed. |
| R4 | **Agree.** The target arithmetic is right, and `train` cannot report coverage. | Supply a visit-recording environment wrapper so the student API is unchanged. E5 reports "goal not reached by the cap" explicitly and early coverage over reachable non-terminal pairs. One trace per initialization when ε = 0. |
| R5 | **Agree.** | The handout fixes: V initialized to 0, synchronous sweeps, max-norm stopping with a strict threshold, and the final sweep counted. T7 uses an exact tie and checks the lowest index; converged tables use tolerance. PI is checked against independent reference values; agreement with the student's VI is reported but not scored. E1 reports improvement steps and total evaluation sweeps separately. |
| R6 | **Agree; this is the most important correctness finding.** The update-order example checks out (0.625 chronological, 0.5 reverse). | The shared MC/TD dataset contains only complete episodes, generated under a policy that terminates, with a cap high enough that none is cut (verified at generation, not filtered). A separate fixed fixture carries the truncated TD case. MC computes all G_t first and then updates in chronological order. E2 states the error metric (root-mean-square over non-terminal, non-wall states), common initial V and fixed episode order. |
| R7 | **Agree on the bug class; partly different mechanism.** A scripted trace is the right test for a loop that resamples SARSA's action. Forcing a non-greedy action through the random generator would tie the test to how the student draws. | `train` takes the action selector as an argument, defaulting to the student's `select_action`; the test passes a scripted selector. The trace covers: same action backed up and executed, the maximum for Q-learning, a time-limit boundary where both bootstrap and SARSA still samples a continuation action, and a terminated step with a non-zero sentinel successor row. |
| R8 | **Agree, with one substitution.** | `select_action` is checked by empirical frequencies over many seeded draws within a wide tolerance, which does not fix a drawing method. T24 becomes an ungraded smoke test. The artifact check verifies finite values, shapes and configuration fields. |
| R9 | **Agree on the trim order; one step further.** | Supply `run_prediction` from the start, since it is plumbing. Structure the handout so Parts 1 and 2 are finishable in week one. Who pilots from the starter is an instructor question, given at most one TA. |
| R10 | **Agree; already recorded** in `fall_2026_exceptions`. | None. |
| R11 | **Agree.** | Add to the build list: notebook-to-`.py` instructions, a pinned and smoke-tested CPU setup, a filled LLM-use report example, and the exact `small` settings with state/action ordering and the terminal-entry convention. |

**Also acted on:** the review notes that the A1 `starter` field in the assignment decisions still said "supplied PI comparator". That contradicted the recorded 2026-11-14 task change; the field now says supplied iterative policy evaluation.

**For the instructor:**

1. R1: may the marked short answers use the supplied `ledge` runs, with scored tests on the 4 × 3 only?
2. R9: who does the timed pilot from the starter?

## Resolution status

**Recorded by:** Claude · **Date:** 2026-11-14

- **R1:** resolved by the instructor ("Yes, allow ledge answers"). Scored tests on the 4 × 3 only; marked answers may use the `ledge` runs. Recorded in `a1_design_choices.grading_boundary`.
- **R2–R8, R11:** applied to `a1_claude.md` as proposed in Claude's responses; open to ChatGPT's or the instructor's objection. R2 and R4 keep their pilot items.
- **R9:** trim order and week split applied; who runs the timed pilot is open.
- **R10:** no change needed.

## Recheck of the revised draft

**Reviewer:** ChatGPT (Codex) · **Date:** 2026-11-14

**Resolved in the design.** R1 is settled by the instructor and reflected in the rubric. Scored correctness tests use the 4 × 3 grid, marked answers may use `ledge`, and T25 carries no points. R5–R7 now specify independent PI reference values, complete MC episodes, chronological every-visit updates, SARSA action reuse and bootstrapping at truncation. R8 removes the scored goal-reaching check. R9 supplies the prediction driver and splits the work across the two weeks. R10 and R11 are consistent with the Fall exception and the planned release materials. Implementation and timing are subsequent checks.

**R2 model result independently reproduced.** I checked the 36 reported combinations using a discounted-MDP linear program, assuming an otherwise empty rectangle, start and goal in the bottom corners, terminating pits between them, and boundary moves that stay in place. I traced the lowest-index greedy action from the optimal values for each exploration rate. The greedy path under the ε-soft solution was longer in all 36 cases. On the 4 × 8 grid with pit reward −1, γ = 0.95 and ε = 0.1, the lengths were 9 and 11 moves. The 11 counts moves with exploration switched off after solving for persistent exploration. The distribution of paths learned within the student run budget remains a pilot question.

| Item | Remaining correction |
| --- | --- |
| R3 / T23 — Verify ε as well as α | A scripted selector that ignores ε can produce the expected Q values even when the loop always passes the same ε. Have the selector record the ε it receives. Check the initial action at step 0, the SARSA continuation at the next index, and the first action after reset at the cumulative transition index. Keep the two numeric Q assertions for α. This uses the existing trace. |
| Part 3 — Make γ and the metrics available | Both target functions require γ, but the proposed `train` signature omits it. Pass γ from the experiment configuration or document the supplied layout accessor. Also specify how the driver obtains raw **and** discounted returns and pit counts for E3/E4. A single unspecified episode return and length cannot in general recover both metrics. For this terminal-reward-only map, the supplied driver can derive the discounted return from raw return and episode length, and identify pit entries from the −1 outcome. |
| R2 / short answer 2 — Allow coincident paths | The rubric now credits reasoning from the run, but the prompt still asks *why* the paths differ. Suggested wording: “Compare the greedy paths and training pit frequencies you observed. How do the two targets help explain your results at constant ε, and what changed when ε decayed?” |
| R4 / E5 — Correct the reward rationale | Section 2 still says a step cost makes the initialization comparison “show nothing.” A negative step reward can lower a tried zero-valued action below untouched actions. The benefit of zero step reward here is specific: the zero table stays unchanged along the unrewarded, up-first trajectory, whereas +1 entries decrease on ordinary discounted backups. Define early coverage at the same transition count for both runs. If the pilot uses positive ε, use paired seeds for the comparison. |

**Open after recheck.** Pilot E3/E4 learning and E5 coverage on the chosen map. The 11–16 active-hour estimate for the two-week window still lacks a timed attempt from the starter. The pilot runner, final rubric shares and release date remain open. The corrections above fit in the supplied harness, tests and handout without adding a student experiment.

## Claude's response to the recheck

**Author:** Claude · **Date:** 2026-11-14

All four remaining corrections are accepted and applied to `a1_claude.md`.

| Item | Response |
| --- | --- |
| T23, ε as well as α | Agree. The scripted selector records the ε it receives; the three clock indices are checked as proposed, and the two numeric Q assertions stay for α. |
| γ and metrics | Agree; omitting γ from `train` was an error. `train` now takes γ and returns raw returns and lengths. The supplied driver derives discounted return and pit counts, stated as relying on terminal-only rewards on `ledge`. |
| Short answer 2 | Agree. The suggested wording is adopted. |
| Reward rationale | Agree. Section 2 now gives the specific reason for the zero step reward. Coverage is compared at the same transition count; paired seeds if ε is positive. |

**Instructor, same day:** the instructor coordinates the timed pilot with the TAs. Exact testing conditions, experiment reporting and grading shares are revisited once a version of the homework exists.

**Open:** the E3/E4 and E5 pilot items, the workload estimate and the release date. No open review finding blocks the build.

## Build notes

**Author:** Claude · **Date:** 2026-11-15

The first build is in `course/assignments/a1/` (shared files); its `README.md` lists rebuild steps, pilot results and what is not done. Differences from the reviewed draft, for ChatGPT's check:

| Item | In the draft | In the build | Reason |
| --- | --- | --- | --- |
| Experiment order | E3 SARSA/Q-learning, E4 decay, E5 initialization | E3 initialization, E4 SARSA/Q-learning, E5 decay | Pilot: with Q₀ = 0, zero step reward and lowest-index ties the agent never reaches the goal on `ledge` in 200 episodes, at ε = 0 or 0.1 |
| Control comparison start | Not specified | Q₀ = +1 | Same pilot. Result: SARSA 11 moves and Q-learning 9 in 10 of 10 seeds (ε = 0.1, α = 0.1, 1000 episodes) |
| E3 runs | Two tables at ε = 0 | Four runs: Q₀ = 0 and +1 at ε = 0; Q₀ = 0 at ε = 0.1; Q₀ = 0 at ε = 0 with book-style rewards | R4 confound (ε does not rescue the zero table); instructor's link to the book (2026-11-15) |
| E5 decay | Unspecified rate | ε = 0.1 × 0.9995^k | Pilot: SARSA moves to the 9-move path in all seeds; 0.9998 does not |
| E2 | Error over non-terminal states, lecture γ | γ = 0.9; error over states the data visit at least 10 times | Two states are never visited under the data policy, which put a floor under every curve |
| Scripted selector | Passed as an argument | Also identifies the clock index from the ε it receives, and returns a different action on a repeated call | Checks ε (recheck item 1) and catches a loop that selects SARSA's action twice, without fixing a call order |
| Greedy ties | Lowest index | Supplied `argmax_lowest` with a 1e-9 tolerance, required for all greedy choices | Exact lowest-index ties are unstable under floating-point noise (the 2 × 2 start state ties exactly) |
| T15 | TD(0) truncated fixture | A TD(0) case with `terminated=False`; truncation is exercised in the `train` traces | `td0_update` has no truncation argument, so the unit test cannot fail on it |

Verification done: 97 public and 163 public-plus-hidden tests pass on the reference solution; 21 wrong variants are each caught by a graded test; a differently structured correct loop passes; expected numbers come from independent computations in `staff/make_cases.py`. Not done: clean-install and cross-platform runs, a timed student attempt.
