# Midterm 1 — independent ChatGPT suggestion

Author: ChatGPT. Date: 2026-11-02. Confidential proposal, not an accepted exam. The exam's status and question choices live only in [the shared exam decisions](../../decisions/exams/midterm_1.md). This file contains a complete candidate, not render-ready content. Claude's suggestion was not read in preparing it.

## Basis and review of the new exam records

Authority: [grading decisions](../../decisions/grading_decisions.md), [exam workflow](../../docs/exam_workflow.md), [topic decisions](../../decisions/topic_decisions.yaml), and the shared deck decisions for [1.1](../../decisions/lectures/introduction.md), [1.2](../../decisions/lectures/mdp_values.md), [2.1–2.2](../../decisions/lectures/bellman.md), and [3.1–3.2](../../decisions/lectures/mc_td.md). The [session source index](../../output/lectures/session_sources.md) supplies the compiled topic/source mapping. Notation follows [the notation guide](../../course/notation_guide.md).

Instructor answers during this preparation: same exam for COMP 438 and 538; no delivery omissions beyond the recorded exclusions; adopt the exam workflow with corrections. The previously recorded 100-minute separate slot, supplied equation sheet, November 5 date, and short forward-λ question are sufficient for this proposal. No further instructor answer is required to complete step 1. On the final shared-record check, X1 also records acceptance of the finite λ formula on the sheet; this candidate already includes it. X3–X6 concern Claude’s candidate and are preserved for cross-review; they do not silently constrain this independent design.

Findings about the records, rather than Claude's candidate questions:

1. **Resolved documentation:** the workflow's draft/adoption language and midterm-1 438/538 assumption needed updating after today's answers. Keep other midterms' unresolved format choices separate.
2. **Resolved stale cross-reference:** `mc_td` O6 still described λ inclusion as unresolved. The November 2 grading decision resolves it at the introductory scope. Link to that decision; do not broaden it into a λ derivation or trace question. The scope group's later derive/implement masteries are not the standard for this exam.
3. **Schedule-view inconsistency found at step 1 (resolved during cross-review, 2026-11-02):** `output/assessment_schedule.md` still says Week 6 and all dates/durations unbooked; `output/assessment_timeline.md` is also a relative planning view. The authoritative record has November 5 and 100 minutes. With the October 5 semester anchor, November 5 is calendar Week 5. The legacy `window_weeks: [6]` must not override the decided date. Refresh affected generators/views before using these views for communication; do not manually edit generated reports or change assignment deadlines as a side effect. This does not block question drafting.
4. **Authority discoverability:** add grading and per-exam decisions/workflow to the repository contract's authority list, without moving question content into tracked governance files.
5. **Workflow clarity:** the question-only first-render check is blind to that render's solutions, not necessarily to the questions themselves after mutual review. Retain it as a fresh independent solve. Do not describe an AI's solve time as a measured student-time pilot.
6. **Source limitation:** this proposal uses shared accepted deck decisions, their explicit live/optional boundaries, and the instructor's no-additional-omissions confirmation. It does not inspect or adopt Claude-specific lecture files or frozen first-render prose as the current deck. Final cross-review should check candidate questions against the delivered slides; that remains a verification step, not a newly unresolved coverage choice.

No curriculum revision is proposed. No lecture minutes, required readings/videos, assignment requirements, or later-exam coverage are changed. No exam content has been added to tracked files.

## Coverage and weight

Every point is assigned once below, even where earlier knowledge is used in a later question. Percentages based on accepted planning minutes are context, not a mechanical rule for points.

| Session | Examinable scope at this stage | Candidate parts | Points |
| --- | --- | --- | ---: |
| 1.1 `formulate` | Explain/analyze state sufficiency, observation versus state, sequential formulation | Q1a–b | 10 |
| 1.2 `mdp_values` | Explain/analyze actions/rewards, return, policy-conditioned state/action values | Q1c–e | 14 |
| 2.1 `bellman` | Derive a finite expectation backup; execute and interpret evaluation sweeps | Q2a–b | 14 |
| 2.2 `improvement` | VI backups, greedy improvement, bounded improvement argument, VI/PI comparison | Q2c–e | 22 |
| 3.1 `mc_td` | First-visit MC, chronological TD(0), data-access taxonomy; average reward at recognize/explain only | Q3a–b, Q3d, Q5a | 18 |
| 3.2 `returns` | Target bias/variance reasoning, derive/calculate n-step targets, introductory λ interpretation, bounded evaluation diagnosis | Q3c, Q4, Q5b | 22 |
| **Total** | | | **100** |

Weekly split is 24/36/40. Accepted planning minutes are 104.5/118/117, approximately 30.8%/34.8%/34.5%. Week 1 has less standalone weight because its formulation/value knowledge is also used throughout Q2–Q4. Week 3 has slightly more because prediction methods and target reasoning need distinct evidence. This is a proposed split for instructor selection, not a change to accepted teaching priorities.

Not tested: control updates (including SARSA/Q-learning), exploration algorithms, importance sampling, approximation, backward traces, GAE, full convergence proofs, matrix inversion, hidden/zero-time slides, assignment-specific code, readings. Average reward receives two conceptual points, not an algorithm. λ receives one short three-point interpretation question. The shortened evaluation block gets four points; no confidence-interval computation, formal significance test, or appendix-only protocol is required. Batch MC/TD is covered teaching but not sampled in this candidate; an exam need not test every live example.

Learning-outcome evidence: Q1 addresses L02/L03; Q2 the derivation/reasoning component of L04; Q3–Q4 L04/L05/L06 within prediction; Q5 L05/L07 at the taught depth. This exam does not establish implementation mastery or claim complete course-outcome coverage.

## Delta against previous midterms

| Source inspected | Keep/adapt | Cut or correct for this exam |
| --- | --- | --- |
| Spring 2025 MT1, Q1, pp. 2–5 (`sources/current_course/exams/spring25/mt1/IntroToRLSpring25MT1.pdf`) | Keep a concrete MDP formulation and observation/state reasoning; replace the long Europa scenario with bounded delivery rules | Remove broad algorithm/control recommendations and representation/approximation choices. State the state-sufficiency assumptions explicitly instead of grading an underspecified world model |
| Same, Q2, pp. 6–9 | Keep short model tables, evaluation/VI sweeps, policy extraction and independent intermediate values | Use a new discounted MDP. Do not reuse the old undiscounted continuing positive-reward setup for an optimality question; its infinite-return behavior defeats a routine finite optimal-value interpretation. Do not infer optimality from an unverified qualitative heuristic |
| Same, Q3, pp. 10–11 | Keep trajectory reading, first-visit accounting, and chronological updates | Replace Q-value prediction/control/SARSA with state-value prediction; change episodes, discount and initialization. Explicitly reset the table between MC and TD |
| Same, Q4, pp. 12–13 | Reallocate its points to in-scope n-step/target reasoning and evaluation | All feature/weight and approximation computations are outside this exam |
| Same, equation sheet, p. 14 | Keep unlabelled equations on the last page | Convert notation and reward indexing. In particular, do not copy `V^π(s) = max_a Q^π(s,a)`: fixed-policy state value averages under π. Remove approximation/control equations |
| Spring 2023 MT1, Q1–Q5 (`sources/current_course/exams/spring23/mt1/IntroToRLSpring23MT1.tex`) | Keep short subparts and method-choice reasoning from Q1; compact model calculations from Q2 | Drop Q1's approximation subpart and Q3–Q5 control/approximation/policy-gradient material. Avoid importing the shop's underspecified inventory/customer memory requirements |
| Spring 2021 MT1, Q2–Q3 (`sources/current_course/exams/spring21/mt1/IntroToRLSpring21MT1.tex`) | Keep independent supplied tables and requests to justify extracted policies | Reduce repetitive arithmetic; do not import action-value TD or an unspecified MC step size |
| Fall 2019 MT1, Q1–Q3 (`sources/current_course/exams/fall19/mt1/document.tex`) | Keep finite DP tables and state-value MC | Cut eligibility traces, backward TD(λ), and control. Correct the old helper return's reward/discount indexing; it is not a source formula to reproduce |

These are preparation references, not assigned reading. The 2025 PDF bearing the ordinary exam filename actually contains blue solutions; it was used as historical evidence, not as a blind solve. Its model table and equation sheet were also inspected visually.

## Candidate questions — without answers

Give these sections alone to the cross-reviewer first. Worked solutions and rubrics start after the equation-sheet section. All proposed times include reading each part and writing the answer; shared setup reading is charged to the first part.

General directions: show the essential calculations or a short justification. Terminal states have zero continuation value. Rewards shown on transitions are the total reward for that transition. Exact fractions or equivalent decimals are acceptable. Each question describes a separate problem. Tables supplied in later parts supersede earlier computed values where stated.

### Q1. Formulating a delivery task — 24 points, 15 minutes

A robot moves among three locations in a line: **left, middle, right**. A charger is at left, a package starts at middle, and its destination is right. Its battery level is an integer from 0 to 4. On each step it chooses one action. Moving toward a neighboring location succeeds with probability 1/2 and otherwise leaves its position unchanged; either outcome consumes one battery unit. Movement outcomes are independent given the present location and action. There is no other hidden environment variable.

At middle it can pick up the waiting package; at right it can deliver a carried package. These actions do not consume battery. At left it can recharge to 4. Waiting is allowed everywhere and does not consume battery. A move is legal only toward an existing neighbor and with positive battery. Reaching battery 0 on a move ends the episode in failure. Successful delivery also ends the episode. All other actions leave unspecified components unchanged. The total reward is +8 for successful delivery, −6 for failure, and −1 for every other transition. Use γ = 1/2.

**Q1a — 6 points; 4 minutes; 1.1; explain/analyze.** Describe a sufficient nonterminal Markov state and the terminal outcomes. Briefly explain why its components are needed. You need not enumerate all reachable states.

**Q1b — 4 points; 3 minutes; 1.1; analyze.** Suppose the robot observes its location and whether it is carrying the package, but not its battery. Is the current observation alone a Markov state? Give two situations with the same observation whose next-outcome distributions differ under the same action. Do not design a partial-observability solver.

**Q1c — 6 points; 3 minutes; 1.2; explain.** Describe the available actions, with their restrictions, and the reward rule. Is the failure reward −6 or −7? Explain briefly.

**Q1d — 4 points; 2 minutes; 1.2; explain/analyze.** For an independent completed trajectory whose rewards are −1, −1, +8, compute G₀ and G₁. The final +8 is paid on delivery; there are no subsequent rewards.

**Q1e — 4 points; 3 minutes; 1.2; explain.** Explain the difference between v^π(s) and q^π(s,a). Does fixing the first action in q^π(s,a) mean that all later actions must also equal a? Give a reason.

### Q2. Evaluation and improvement in a small MDP — 36 points, 24 minutes

There are two nonterminal states **A, B**, and a terminal state. Discount γ = 1/2. The table gives every possible transition; the probability column is ℳ(s,a,r,s′). All unlisted outcomes have probability zero.

| s | a | r | s′ | Probability |
| --- | --- | ---: | --- | ---: |
| A | wait | 1 | A | 1 |
| A | go | 0 | B | 1/2 |
| A | go | 4 | terminal | 1/2 |
| B | wait | 2 | B | 1 |
| B | exit | 3 | terminal | 1 |

The policy π chooses wait and go equally often at A and always chooses exit at B. Every sweep below is **synchronous**: all new entries use the previous sweep's table. Terminal continuation is always zero.

**Q2a — 6 points; 4 minutes; 2.1; derive.** Starting from the expected-return meaning of v^π, write the two scalar Bellman equations for this particular policy. Show where both the policy probability and transition probability enter at A. Explain why the remaining return after reaching B can be replaced by v^π(B). Do not solve the equations.

**Q2b — 8 points; 5 minutes; 2.1; analyze/apply.** Starting with V₀(A)=V₀(B)=0, perform two synchronous policy-evaluation sweeps for π. Fill in V₁(A), V₁(B), V₂(A), V₂(B), showing each backup.

**Q2c — 8 points; 5 minutes; 2.2; analyze/apply.** Start again from V₀(A)=V₀(B)=0. Perform two synchronous **value-iteration** sweeps, showing both available action-backup values at each state and identifying the maximum. Do not continue the table from Q2b.

**Q2d — 8 points; 5 minutes; 2.2; analyze.** Independently of Q2b–c, the exact values of the original policy are supplied: v^π(A)=5/2 and v^π(B)=3. Compute q^π for each of the four state/action pairs. State the greedy improved policy and check that its selected q^π value is at least v^π at each state.

**Q2e — 6 points; 5 minutes; 2.2; derive/analyze.** Explain why the inequalities checked in Q2d imply that following the improved policy from then on cannot lower the value. Give the repeated-substitution argument in words or equations; a full convergence theorem is not required. Then state the main difference between a policy-iteration cycle and a value-iteration sweep.

### Q3. Learning a fixed policy's values from episodes — 20 points, 14 minutes

A fixed policy π produced these two complete episodes. Each arrow is labelled by the reward received on that transition. Discount γ = 1/2.

- Episode 1: A —0→ A —2→ B —4→ terminal.
- Episode 2: A —0→ B —2→ terminal.

The actions are omitted because this question only evaluates π. The data are consistent with a Markov environment with stochastic rewards/transitions.

**Q3a — 7 points; 5 minutes; 3.1; analyze/apply.** Use **first-visit Monte Carlo sample averages** over both episodes to estimate V(A) and V(B). List the included returns and the number of included visits for each state. Do not count the second visit to A in episode 1.

**Q3b — 7 points; 4 minutes; 3.1; analyze/apply.** Independently of Q3a, initialize V(A)=2 and V(B)=0. With α=1/2, process **episode 1 only**, chronologically, using TD(0). For each transition give the target and the updated value of the current state. Use the current table just before each update, including for the self-transition.

**Q3c — 4 points; 3 minutes; 3.2; analyze.** Assess each statement with a one-sentence reason, under a fixed policy, with finite expected returns and finite target variances:

1. “An unbiased MC return target guarantees that a constant-step-size MC estimate equals the true value after every episode.”
2. “A TD(0) target always has lower variance than an MC return, regardless of the current value table.”

**Q3d — 2 points; 2 minutes; 3.1; explain.** The learner receives this saved dataset, collects no new interactions, and estimates the values of the same π that generated it. Classify the data access as online or offline, and the policy relationship as on-policy or off-policy. Give a brief reason for each.

### Q4. Choosing the length of a prediction target — 14 points, 10 minutes

This is a new independent episode, with γ=1/2:

A —2→ B —0→ C —4→ terminal, with time indices 0,1,2,3.

Hold the value table fixed throughout: V(A)=0, V(B)=4, V(C)=6, and terminal value 0. Targets are for the visit to A at time 0; do not update the table between calculations.

**Q4a — 4 points; 3 minutes; 3.2; derive.** Expand the return recursion twice and replace the unobserved return after the second transition with its value estimate. Write the resulting two-step target G₀:₂ symbolically before inserting numbers.

**Q4b — 6 points; 4 minutes; 3.2; analyze/apply.** Calculate the one-step target G₀:₁, two-step target G₀:₂, and full return G₀. For the full return, indicate why there is no additional bootstrap term.

**Q4c — 1 point; 1 minute; 3.2; explain.** If this episode arrives one transition at a time, at which time index does the two-step target for A first become available? Must the learner wait until termination here?

**Q4d — 3 points; 2 minutes; 3.2 introductory λ scope; explain.** A student sets λ=1 in the finite episodic forward λ-return to remove bootstrapping, then concludes that the target must be more accurate than TD(0). Assess both claims briefly. No λ calculation, derivation or backward trace is requested.

### Q5. Objectives and evidence — 6 points, 5 minutes

**Q5a — 2 points; 2 minutes; 3.1; recognize/explain.** Consider two policies for a continuing service task. One produces reward 0.75 every step. The other repeats the rewards 0,2,0,2,… forever. Which has higher long-run average reward per step, and why? No average-reward learning algorithm is required.

**Q5b — 4 points; 3 minutes; 3.2; analyze.** A report compares MC and TD prediction on a fixed policy. It tries many step sizes and selects each method's best setting using the same episodes/seeds on which it reports final value error. It then uses the single lowest-error run to claim that the selected method is generally better. Identify two weaknesses and one concrete repair for each. No statistical test or numerical uncertainty calculation is required.

## Proposed equation sheet

Renderer instruction: only the equations below, without names, explanatory headings, or references to question numbers, on the last page. Generic summation indices are local counters; all RL symbols follow the notation guide. The part directions, not the sheet, specify whether V is fixed, chronological, or a DP sweep table.

The general n-step formula is intentionally omitted because Q4a asks students to construct its two-step case from the supplied return recursion. The sheet supplies the λ mixture so its question remains interpretation, not recall. Including the finite λ formula is already accepted in the shared exam decisions (X1). The remaining sheet choices are proposed for cross-review/instructor selection.

\[
G_t=\sum_{k=0}^{T-t-1}\gamma^kR_{t+k+1},\qquad G_t=R_{t+1}+\gamma G_{t+1},\qquad G_T=0.
\]
\[
v^\pi(s)=\mathbb E_\pi[G_t\mid S_t=s],\qquad
q^\pi(s,a)=\mathbb E_\pi[G_t\mid S_t=s,A_t=a].
\]
\[
v^\pi(s)=\sum_a\pi(a\mid s)q^\pi(s,a).
\]
\[
q^\pi(s,a)=\sum_{s',r}\mathcal M(s,a,r,s')[r+\gamma v^\pi(s')].
\]
\[
v^*(s)=\max_a\sum_{s',r}\mathcal M(s,a,r,s')[r+\gamma v^*(s')],\qquad
\pi^*(s)\in\operatorname*{argmax}_a q^*(s,a).
\]
\[
V_{k+1}(s)=\sum_a\pi(a\mid s)\sum_{s',r}\mathcal M(s,a,r,s')[r+\gamma V_k(s')].
\]
\[
V_{k+1}(s)=\max_a\sum_{s',r}\mathcal M(s,a,r,s')[r+\gamma V_k(s')].
\]
\[
V(S_t)\leftarrow V(S_t)+\alpha[U_t-V(S_t)].
\]
\[
U_t=G_t,\qquad U_t=R_{t+1}+\gamma V(S_{t+1}).
\]
\[
V(s)\leftarrow V(s)+\frac{1}{N(s)}[G_t-V(s)],\qquad S_t=s.
\]
\[
G_t^\lambda=(1-\lambda)\sum_{n=1}^{T-t-1}\lambda^{n-1}G_{t:t+n}
 +\lambda^{T-t-1}G_t,\qquad 0\leq\lambda<1,\quad t<T.
\]
\[
G_t^1=G_t,\qquad G_t^0=G_{t:t+1}.
\]

For rendering/solution checking only: the finite-mixture formula includes the terminal remainder; at a last-step state it reduces to G_t. Endpoint λ=0 uses the usual polynomial convention for zeroth powers. N(s) means the count after including the current first visit. Those conventions must agree with question wording; do not introduce an every-visit variant on the sheet.

---

## Worked answers and partial-credit rubric

**Cross-review boundary: solve the questions above before reading below.**

General grading proposal: award method credit for a correct setup with arithmetic errors; do not repeatedly penalize a propagated arithmetic slip. Later parts with supplied/reset values are graded from those values. Credit equivalent sufficient state representations and valid concise arguments. No negative marking is proposed. All point allocations below sum to their question totals.

### Q1 answers — 24

- **a (6):** A sufficient state records location, battery level, and package status (waiting at middle or carried). Terminal outcomes are successful delivery and battery failure. Reachable nonterminal combinations suffice; a delivered-package flag can instead encode the success terminal. Location determines legal/possible moves, pickup, delivery and recharge (1); battery determines failure and subsequent capability (1); package status determines pickup/delivery possibilities (1). Explain that the next-state/reward law is determined by these components and the chosen action, with no further history needed under the stated independence assumptions (2). Identify both terminal outcomes (1). An equivalent explicit package-location representation earns full credit. A time counter or full history is unnecessary, but harmless redundancy alone does not lose credit.
- **b (4):** No (1). For example, same location middle and carrying the package, battery 1 versus 2 (1); take the move toward right (1). Battery 1 fails with probability 1, while battery 2 survives the move, whether it reaches right or stays at middle (1). Both are reachable in suitable histories. The observation hides information needed for the next reward/termination distribution. Do not require a belief-state construction.
- **c (6):** Legal neighboring moves with positive battery (1); pickup/delivery conditional on location and package status (1); recharge only at left and wait anywhere (1). Total +8 delivery and −6 failure (1); −1 otherwise (1); failure pays −6, not −7, because these are mutually exclusive total-reward cases, not a penalty added to a living reward (1). Prose is sufficient; no unapproved new symbols are needed.
- **d (4):** G₀=−1+(1/2)(−1)+(1/4)8=1/2; G₁=−1+(1/2)8=3. Each return: correct discounted expression (1), correct result (1). No continuation after the last reward.
- **e (4):** v^π conditions on the starting state and averages the first action under π (1); q^π additionally conditions on taking a particular first action (1). Later actions follow π (1); they need not repeat a, and future transitions/actions/rewards are averaged as appropriate (1).

### Q2 answers — 36

**a (6).**

\[
v^\pi(A)=\tfrac12[1+\tfrac12v^\pi(A)]
+\tfrac12\{\tfrac12[0+\tfrac12v^\pi(B)]+\tfrac12[4+\tfrac12\cdot0]\},
\qquad v^\pi(B)=3.
\]

Equivalently, v^π(A)=3/2+v^π(A)/4+v^π(B)/8. From the return recursion, condition on the first action and transition; by the Markov property and continued use of π, the remaining expected return at B is v^π(B). Rubric: policy averaging (1), wait reward/continuation (1), go outcome averaging (1), reward/discount/terminal convention in the go branch (1), B equation (1), conditional-return explanation (1). The exact solution, not required, is (5/2,3).

**b (8).**

| k | Vₖ(A) | Vₖ(B) |
| --- | ---: | ---: |
| 0 | 0 | 0 |
| 1 | 3/2 | 3 |
| 2 | 9/4 | 3 |

V₁(A)=3/2. V₂(A)=3/2+(3/2)/4+3/8=9/4. B always exits and gives 3. Each of four requested cells: correct old-table backup (1), result (1). If a student uses in-place updates, retain correct Bellman/method credit but deduct the timing-dependent result credit; do not charge the same convention mistake repeatedly beyond affected cells.

**c (8).**

| Sweep | A: wait | A: go | New V(A) | B: wait | B: exit | New V(B) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1, from (0,0) | 1 | 2 | 2 | 2 | 3 | 3 |
| 2, from (2,3) | 2 | 11/4 | 11/4 | 7/2 | 3 | 7/2 |

For each state/sweep row: both action backups (1 total, 0.5 each), selecting/reporting the maximum (1). Total four rows × 2. The action at B changes from exit to wait between sweeps; this tests why maximizing immediate reward is insufficient.

**d (8).** q^π(A,wait)=1+(1/2)(5/2)=9/4; q^π(A,go)=2+(1/4)3=11/4; q^π(B,wait)=2+(1/2)3=7/2; q^π(B,exit)=3. Each value earns 1 (4). The greedy policy chooses go at A and wait at B (1 each). Check 11/4≥5/2 and 7/2≥3 (1 each). These are action values under the original π after the first action, not the exact values of following the new policy forever. Do not label them v*.

**e (6).** The old value at each state is no larger than the expected immediate reward plus discounted old value after one step under the improved policy. Apply that same inequality to each successor's old value, again taking the improved policy's action. Repeating produces its multi-step expected reward sum plus a discounted old-value tail. Since γ=1/2 and values are bounded in this finite discounted MDP, the tail vanishes; the limiting return is the improved policy's value, at least v^π. Rubric: one-step inequality interpreted (1); substitution at successor states (1); continuation under the new policy (1); bounded discounted-tail conclusion/nondecrease (1). Policy iteration alternates evaluation of a fixed policy and greedy improvement (1); value iteration uses the maximizing backup each sweep without first completing a separate fixed-policy evaluation (1). No proof that the extracted policy is already optimal is requested.

### Q3 answers — 20

**a (7).** Episode 1 first visit to A: 0+(1/2)2+(1/4)4=2. First B return: 4. Episode 2 first A return: 0+(1/2)2=1; first B return: 2. Thus V(A)=(2+1)/2=3/2 and V(B)=(4+2)/2=3. N(A)=N(B)=2. Rubric: correct included returns for A (2, 1 each), for B (1, 0.5 each); correct averaging/counts (2, 1 per state); final estimates (2, 1 per state). The later A in episode 1 has return 4 but is excluded from first-visit averaging.

**b (7).** Start afresh at (2,0), not the MC table.

| Transition | Target Uₜ | Updated entry | Table after update, (A,B) |
| --- | ---: | --- | --- |
| A —0→ A | 0+(1/2)2=1 | V(A)=2+(1/2)(1−2)=3/2 | (3/2,0) |
| A —2→ B | 2+(1/2)0=2 | V(A)=3/2+(1/2)(2−3/2)=7/4 | (7/4,0) |
| B —4→ terminal | 4 | V(B)=0+(1/2)(4−0)=2 | (7/4,2) |

Each target (1) and each correct update from the student's current table (1), plus explicit use of the reset initialization/chronological convention (1). Target and subtraction in the first row both use the pre-update value 2. A later update to B does not retroactively alter the prior update to A.

**c (4).** Both statements are false. An unbiased random target concerns an expectation across samples, not equality of each estimate to the true value; sampling noise and initialization can remain with constant α (false + explanation = 2). Bootstrapping often reduces sampled-future variability, but arbitrary inaccurate successor estimates can introduce variability, so there is no universal ordering for the given claim (false + explanation = 2). A numerical counterexample or variance proof is not required and is not an extra grading criterion.

**d (2).** Offline: fixed saved data with no new interactions (1). On-policy: the evaluated policy is the generating policy (1). These axes are distinct; “offline therefore off-policy” is incorrect. Each mark includes its reason.

### Q4 answers — 14

**a (4).** G₀=R₁+γG₁=R₁+γR₂+γ²G₂. Replacing G₂ with V(S₂) gives G₀:₂=R₁+γR₂+γ²V(S₂). Credit first expansion (1), second expansion/correct discount powers (1), replacement at the second successor (1), correct target expression (1). No n-step update implementation or changing-table derivation is required.

**b (6).** G₀:₁=2+(1/2)4=4. G₀:₂=2+(1/2)0+(1/4)6=7/2. G₀=2+(1/2)0+(1/4)4=3. Each target: expression (1), answer (1). For the full return, the expression credit requires no nonzero terminal bootstrap: the episode ended and terminal continuation is zero. The C value 6 is used in the two-step target; it is replaced by the realized reward 4 in the full return.

**c (1).** At time 2, after observing R₂=0 and S₂=C, before termination at time 3 (1, including the distinction). The table is supplied and fixed, so its entry at C is already available.

**d (3).** At λ=1 the finite episodic mixture is the full return and does not bootstrap (1). The accuracy guarantee is false (1). Eliminating table-induced target bias does not eliminate sampling variability; squared error/learning performance need not improve, and a good bootstrapped estimate may help (1). No numerical mixture or formal bias–variance decomposition is required.

### Q5 answers — 6

**a (2).** The alternating policy has higher average reward: (0+2)/2=1 per step versus 0.75 (1 for each correct rate/comparison, 2 total). Do not compare first-step rewards or use discounted return for an average-reward objective. An explanation as equal-length totals earns full credit. No pointwise limit of the alternating sequence is assumed.

**b (4).** First, selecting step size using the final evaluation episodes/seeds risks an optimistic selection result; tune on a separate validation set and evaluate the fixed selection on fresh held-out episodes/seeds (weakness 1 + repair 1). Second, one selected best run does not establish typical or reliable performance; use multiple independent runs and report the aggregate with variability/uncertainty instead of the best seed (weakness 1 + repair 1). Equivalent valid wording is accepted. Do not require a particular interval formula, new experiments by students, or appendix-only terminology. Fair budgets are relevant but cannot substitute for addressing the two stated flaws unless the answer explains their connection.

## Time and feasibility audit

| Question | Points | Part times (minutes) | Total minutes |
| --- | ---: | --- | ---: |
| Q1 | 24 | 4 + 3 + 3 + 2 + 3 | 15 |
| Q2 | 36 | 4 + 5 + 5 + 5 + 5 | 24 |
| Q3 | 20 | 5 + 4 + 3 + 2 | 14 |
| Q4 | 14 | 3 + 4 + 1 + 2 | 10 |
| Q5 | 6 | 2 + 3 | 5 |
| **Total** | **100** | | **68** |

Estimates are unpiloted student-work estimates. The candidate leaves 32 minutes of the 100-minute slot for orientation, equation-sheet lookup, checking and individual variation; it is 7 minutes below the workflow's approximate 75-minute task ceiling. The estimate is not evidence that every student will finish. Q1's scenario and Q2e's argument are the main uncertainty; cross-review should check them first. Keep Q1 on one question page where possible, and keep the Q2 model visible beside its first calculation parts.

The exam's 75% task guideline is distinct from `config/course.yaml`'s 0.85 **teaching** fraction. There is no curriculum revision, so existing lecture-time allocations are unchanged. For reference, six covered sessions have nominal capacity 6×70×0.85−20=337 minutes; accepted planning allocations total 339.5 minutes, with existing instructor-authorized delivery allowances. This proposal adds zero live minutes and does not claim to resolve the semester's calendar loss.

Displacement: compared with the old exam patterns, control/approximation calculations are replaced by in-scope n-step reasoning, target diagnosis and evaluation. Within this candidate, the improvement argument uses time otherwise available for a longer numerical MDP exercise; the short λ item replaces, rather than adds to, another n-step subpart. No full batch-learning question, matrix solution, or second formulation scenario is added.

Verification performed: numerical solutions independently recomputed with exact rational arithmetic (policy evaluation, VI, supplied exact policy values, all four action values, first-visit MC, chronological TD and n-step targets). Point and part-time sums checked. Conceptual claims checked against shared accepted scopes and the notation guide. This is self-checking; mutual cross-review and a fresh question-only check after rendering remain necessary.

## Choices for the cross-review/instructor stage

- Select/merge questions only after the mutual review; no candidate part is accepted by this file.
- Consider whether Q2e's short improvement argument is the desired difficulty anchor; it exercises the accepted repeated-expansion reasoning. If removed, replace its four points/time with another in-scope reasoning part rather than increasing calculation volume automatically.
- Retain the intentionally small λ and average-reward weights. Do not import their later-course depth.
- Check the equation sheet against the chosen questions, especially any derivation that a merged sheet would directly supply.
- Resolve the stale generated calendar views before relying on them for announcements. Current date/format authority remains the grading decision.

Stop after this independent suggestion. Cross-review, question selection, render-ready content and rendering are subsequent steps.

Post-step-1 maintenance note (ChatGPT, 2026-11-02): the instructor confirmed the university-set Week 5 placement. The grading record and generated assessment schedule/timeline now agree on the date and duration; the earlier schedule-view follow-up is closed. Candidate questions and independent reasoning above are unchanged.
