# Session 3.1 (`mc_td`): initial content suggestion (Claude)

**Claude's step-1 suggestion** (`docs/lecture_workflow.md`, pilot v2), 2026-10-21. Analysis only: nothing here is accepted. It becomes historical after step 3. The deck's status lives in [`decisions/lectures/mc_td.md`](../../decisions/lectures/mc_td.md).

**Scope of this file:**
- the full 3.1 teaching sequence;
- the old-deck delta for the whole old deck (it spans 3.1 and 3.2);
- a placement proposal for the three book examples (O1).

The 3.2 sequence itself is a later step-1 suggestion. The 3.2 lines below only show that the O1 placement fits.

All numbers are checked by `scripts/check_mc_td_claude.py`.

## Accepted frame

From `decisions/topic_decisions.yaml` (`mc_td`) and `output/lectures/session_sources.md` §3.1:
- **Allocation:** 59 teaching minutes (range 54–70), in two segments: MC/TD, data access and shared example (54) and average-reward objective (5, `average_reward_live_minutes`). The delivery allowance goes up to 63, but the plan is made to 59 first.
- **Worked activity:** shared MC/TD trajectory; five-minute average-reward contrast.
- **Prediction group:** core; explain / derive / implement / analyze. MC and TD(0) on one shared trajectory; implement representative MC/TD prediction, not all variants. The data-access taxonomy is brief and revisited later.
- **Average reward:** exposure; recognize / explain. No differential-value derivation, no algorithm.
- **Deck decisions D1–D3:**
  - one deck for 3.1–3.2;
  - the 2×2 grid as running example, with the book examples as standalone illustrations;
  - no psychology connection; average reward stays.
- **A1 dependency:** A1 asks students to "complete small MC-prediction and TD(0)-prediction update kernels on a shared trajectory". The in-class trajectory is the direct preparation.

## What students already have

**From 1.2 (`mdp_values`):**
- G_t = R_{t+1} + γG_{t+1}, and backward return calculation (M12).
- The continuing tail (M13).
- "Average repeated complete returns to estimate a value", said in the notes of M14 with no estimator notation.
- The continuing rescue robot and its two policies' values at γ = 0.5 (M17):
  - always-search: 3.60 / 1.60;
  - search-high/recharge-low: 3.64 / 1.82.
- M09a named "average" as a return option and deferred it to Week 3.

**From 2.1–2.2 (`bellman`):**
- The 2×2 grid (B03): entry reward +1 at the goal, −0.04 otherwise, γ = 0.5, and the always-right policy.
- Exact values of always-right (B08a, B21):
  - (1,1): 14/275 ≈ 0.051;
  - (1,2): 46/55 ≈ 0.836;
  - (2,1): 32/275 ≈ 0.116.
- Synchronous sweeps V_k (B09–B12).
- The Bellman expectation equation.
- Q-value iteration as the bridge to sampling (B24a: "Q-learning uses sampled transitions for this kind of target").
- GPI (B27: "in a few weeks … using experience").
- B28's questions on which computations need the model.
- 2.1's opening brainstorm (B00b notes) already seeded "use sample averages to estimate the expectation; prepare them for MC".

## Is the old material substantial?

**Yes.** `4 - Model Free Prediction.pptx` slides 3–41 cover 3.1 and 3.2 directly. Slides 42–44 cover 3.2's n-step targets. Slides 45–59 (λ-return, traces) belong to Week 8 or are cut. Average reward comes from `6 - Value Function Approximation.pptx` slides 37–40 (PDF 32–35). The delta below starts from these decks. I did not need to ask about substantiality.

## Central idea and the motivation thread

Everything in Week 2 needed 𝒯 and ℛ. 3.1 keeps the **same grid and the same policy, but hides the model.** Students can only run the policy and watch. Because 2.1 gave the exact values, students can see how far one episode's estimates are from the truth.

The session answers two questions:
- **Monte Carlo:** v^π(s) is an expected return, so average sampled returns.
- **TD(0):** the Bellman equation says a value equals the expected one-step reward plus the discounted next value. So take one sample of that right-hand side, using the current estimate for the next value.

Both use one update form, V(S_t) ← V(S_t) + α[U_t − V(S_t)], and differ only in the target U_t. The same form returns for n-step targets (3.2), Sarsa and Q-learning (Week 4) and semi-gradient methods (Week 5).

**Explicit motivation time** (pilot v2 lesson, `bellman` retrospective). About 15 of the 58 minutes go to "why" before "how":
- T02: what is lost without the model;
- T03: why sample at all;
- T05/T06: why incremental updates and why a constant step size;
- T09: why not wait for the outcome (driving home);
- T10: where the TD target comes from (the Bellman equation);
- T17: why another objective for continuing tasks.

## Teaching sequence for 3.1 (slide level, unpolished)

Slide IDs are proposals. Minutes are planning targets.

| ID | Slide | Content and reason | Sources | Min |
| --- | --- | --- | --- | ---: |
| T00 | Title | Title Slide layout: course name; **Model-Free Prediction** / instructor / Fall 2026. | deck title format | 0.5 |
| T01 | So far | Recap of DP evaluation, PI/VI and GPI (B27). Every computation used 𝒯 and ℛ (B28's answer). Today: evaluation from experience; next week: improvement from experience. | old 3 (updated: Q-value iteration was taught), B27, B28 | 2 |
| T02 | Brainstorm: the model is hidden | The 2×2 grid with "?" on the transition arrows and the same always-right policy. "You can only run the policy and watch. How would you estimate v^π((1,1))? What did DP use that you no longer have? What if a run never ends?" Students should propose averaging returns. The last question sets up TD and continuing objectives. | old 9, 15; 1.2 M14 notes; 2.1 B00b | 3 |
| T03 | Why learn from samples? | Two reasons. (1) The model is unknown or unreliable: a robot on snow; an unknown reward such as ad revenue. (2) A model exists only as a simulator, or is too large to sweep: we can sample games but not enumerate them. Full-width backup (DP) vs sample backup (one S_t, A_t, R_{t+1}, S_{t+1}): the cost per update does not depend on the number of successors, but many samples are needed. Planning-vs-learning pictures, with labels changed (see delta). | old 4, 5, 11, 12; book §8.5 for expected vs sample updates (no detail) | 3 |
| T04 | Monte Carlo: average the returns | v^π(s) ≐ 𝔼_π[G_t ∣ S_t = s]: estimate it by the average of observed returns after visits to s (law of large numbers). Episode S_0, A_0, R_1, …, S_T; G_t = R_{t+1} + γR_{t+2} + ⋯ + γ^{T−t−1}R_T. Model-free, but episodes must terminate. Question: "(2,1) is visited twice in one episode; which returns count?" leads to first-visit and every-visit; both converge (book §5.1). | old 16–17 (indexing fixed), book §5.1, CS234 L3 PDF 10–13 | 3.5 |
| T05 | From averages to updates | The incremental mean V(s) ← V(s) + (1/N(s))[G − V(s)], derived from the average in two lines. Generic form V(S_t) ← V(S_t) + α[U_t − V(S_t)]: move a fraction α of the error toward a target. Motivation: no stored return lists; one form for every method in the course. Spoken link to Week 5: with the target held fixed, it is a gradient step on ½(U_t − V)² (qualification from review R15). | old 18–19 (V̄ and V_k indices removed), book §2.4 "NewEstimate ← OldEstimate + StepSize[Target − OldEstimate]", CS234 L3 PDF 15–16 | 4 |
| T06 | Averaging vs tracking | With 1/N(s), every return has equal weight: the exact sample average, which converges for a fixed policy. With a constant α, recent returns weigh more (a recency-weighted average). That tracks a changing target, which matters when the policy changes (Week 4, GPI). Robbins–Monro conditions in one line: Σα = ∞, Σα² < ∞. Constant α violates the second, so the estimates keep fluctuating. | old 19–20 (compressed; spelling fixed), book §2.5 | 2 |
| T07 | First-visit MC prediction | The book's algorithm box. Every-visit drops the "unless" line. Say once that the book writes v_π. | old 21, book §5.1 PDF 114 | 1.5 |
| T08 | **Shared trajectory: MC** (protected) | One episode under always-right: (1,1) → right → (2,1), R₁ = −0.04; (2,1) → right bumps and stays, R₂ = −0.04; (2,1) → slip up into the goal, R₃ = +1. Students compute the returns backward, then the constant-α MC updates (α = 0.5, V = 0). Answers: G₂ = 1, G₁ = 0.46, G₀ = 0.19. Then V((1,1)) = 0.095 and V((2,1)) = 0.23 (first-visit; every-visit would also use G₂ = 1). Exact values from 2.1: 0.051 and 0.116. The episode was lucky: probability 0.8·0.9·0.1 = 0.072, and from (2,1) the goal is reached only on a 0.1 slip. | D2, B03/B21 values, CS234 L3 PDF 14 (repeated-state worked trajectory) | 5 |
| T09 | Why wait for the end? Driving home | **Example 6.1** as the motivation for TD, before the formula. Show the prediction table first: "When would you revise your estimate for 'leaving office': at home, or when you hit the traffic?" Then the MC and TD arrow panels (γ = 1, α = 1; the values are times to go, i.e. costs). TD "learns a guess from a guess". | old 28 (moved before the formula), book Ex. 6.1 PDF 144, Sutton TD slides PDF 2–20 | 3.5 |
| T10 | The TD target | Recall v^π(s) = 𝔼_π[R_{t+1} + γv^π(S_{t+1}) ∣ S_t = s] (2.1). DP computes this expectation with the model (B09). TD takes one sample of it and puts the current V in place of v^π: U_t = R_{t+1} + γV(S_{t+1}). The update is V(S_t) ← V(S_t) + α[R_{t+1} + γV(S_{t+1}) − V(S_t)], with TD error δ_t. **Bootstrapping** means updating an estimate from another estimate. The target is an estimate for two reasons: it samples the expectation, and it uses V instead of v^π (book §6.1). Contrast with the MC target G_t. | old 24–26 (notation fixed; the Robbins–Monro remark qualified), book §6.1 PDF 143–146 | 4.5 |
| T11 | TD(0) prediction | The book's box: V(terminal) = 0; it updates after every step, learns from incomplete episodes and needs no termination. | old 27, book §6.1 | 1.5 |
| T12 | **Shared trajectory: TD(0)** (protected) | Same episode, α = 0.5, V = 0, updates in time order. δ₀ = −0.04 gives V((1,1)) = −0.02. δ₁ = −0.04 gives V((2,1)) = −0.02. δ₂ = 1 + 0 − (−0.02) = 1.02 gives V((2,1)) = 0.49. The third update reads the value the second one changed, so order matters within an episode. The terminal value is 0. | D2, book §6.1 | 5 |
| T13 | What did each method learn? | Table: state, MC, TD, exact v^π. (1,1): 0.095, −0.02, 0.051. (2,1): 0.23, 0.49, 0.116. Questions: (a) Why did TD's (1,1) estimate not see the goal? It was updated before the goal was reached; the information moves back over later visits (repeating the same episode gives 0.0925; notes only). (b) Which would you trust after one episode? After 1,000? Leads into 3.2: bias and variance. | numbers checked by script | 3 |
| T14 | Sampling and bootstrapping | Backup diagrams for DP, MC and TD (Silver), then the two-way table: DP bootstraps and does not sample (needs the model); MC samples and does not bootstrap (needs episode ends); TD does both. | old 37–40 (old 40's "real world" broadened: samples may come from a simulator), Silver L4 PDF 12–30 | 3 |
| T15 | When can each method learn? | MC: after the episode ends; terminating tasks only. TD: after every step; incomplete episodes; continuing tasks. Efficiency, bias and variance claims wait for 3.2. | old 29 (first half), old 22 (episodic only) | 2 |
| T16 | What data does the agent learn from? | Brief taxonomy anchored on today's methods, each with a pointer to where it returns: prediction vs control (Week 4); model-free vs model-based (Weeks 10–11; certainty equivalence in 3.2 gives a first look); on-policy vs off-policy (data from π vs from a behaviour policy b, Week 4); online vs offline (the agent keeps collecting data vs a fixed dataset, Week 12). Today's MC/TD are model-free, on-policy prediction; TD can run online. | old 8, 13, 14 (definitions fixed) | 4 |
| T17 | **Continuing tasks: which objective?** | TD can learn in tasks that never end; what should it predict? 1.2's answer was the discounted return. The alternative is the **average reward** per step: r(π) ≐ lim_{h→∞} (1/h) Σ_{t=1}^{h} 𝔼[R_t ∣ S_0, A_{0:t−1} ∼ π] (book eq. 10.6). Robot, continuing rescue model: always-search spends 60% of steps at high and 40% at low, so r = 0.6·2 + 0.4·0.5 = **1.4** (students check). Search-high/recharge-low spends 5/6 and 1/6, so r = 5/3 ≈ **1.67**. Contrast: at γ = 0.5 the two objectives rank the policies the same way (1.2 M17; wording corrected after review R11), but at γ = 0.1–0.3 (checked) always-search has the higher discounted value in both states. The discounted ranking depends on γ (and in general on the start state); the average-reward ranking does not, because all future rewards count equally. The start state does not matter in the long run (ergodicity, said in words). One spoken line: values in this setting are measured relative to r(π) (book §10.3), and the setting returns with approximation in continuing tasks (book §10.4). No derivation or algorithm. | old VFA PPTX 37 (definition only; 38–40 not used), book §10.3 PDF 271–275, Sutton on-policy control slides PDF 11–18, 1.2 M02/M07/M17 | 5 |
| T18 | Summary and next | MC averages complete returns; TD moves toward one reward plus the next estimate. Exit question: "Which update can you apply before the episode ends? Which needs the next state's estimate?" Next: 3.2 asks how accurate these estimates are (random walk, "you are the predictor", bias/variance) and what lies between MC and TD (n-step). Week 4 learns q, because greedy improvement from v needs the model (B28). | old 6 (roadmap, one line) | 2 |

**Targets sum to 58 minutes** against the 59-minute allocation:
- the MC/TD segment (T00–T16, T18) sums to 53, against its accepted 54;
- average reward (T17) is 5, as accepted.

The protected calculations are T08 and T12 (10 minutes), plus the student check in T17.

**Alternatives considered:**
- **Taxonomy first (old order, old 9–14).** I suggest placing it after both methods (T16), so that each category has a concrete anchor. Up front it is abstract, and the old wording conflated the categories.
- **A shorter, two-step trajectory** ((1,1) → (2,1) → goal). It saves about 1.5 minutes but loses the repeated state (first-visit vs every-visit) and the order effect inside TD.
- **Sample-average MC (1/N)** in T08. After one episode the estimates equal the returns (0.19, 0.46). This is simpler, but the step size then differs from TD's α = 0.5, which confuses the comparison of targets.
- **Evaluating π′ = (up, right, up)** instead of always-right. Its exact values are also known (B21r), but always-right's values were derived step by step in 2.1, so the comparison with the truth lands better.

## O1: where Examples 6.1, 6.2 and 6.4 go

**Recommendation (A): use the deck split.**
- **6.1 (driving home) in 3.1** as the motivation for TD (T09).
- **6.2 (random walk) and 6.4 (you are the predictor) in 3.2.**

**No change to average reward (5 minutes), and no use of the allowance in 3.1** (targets 58 of 59).

Reasons:
- **The book's argument chain stays together in 3.2.** TD usually learns faster in practice (6.2). Why? Batch updating (Example 6.3, old 33). Batch TD finds the certainty-equivalence estimate and exploits the Markov property (6.4, old 34–36). This is 3.2's "bias and variance" content. 6.4's 0-vs-0.75 answer needs batch updating and the Markov argument, which 3.1 does not have.
- **6.2 serves 3.2's accepted worked activity** ("inspect noisy learning curves and a baseline comparison"). The curves are RMS errors averaged over 100 runs, for several step sizes. Is the MC–TD comparison fair if each method uses its best α? That is the evaluation reasoning 3.2 needs. The 19-state n-step α-sweep (old 44) then extends the same random walk to n-step targets.
- **6.1 is about when an update can be made**, which is 3.1's question (T09, T15).

Rough 3.2 feasibility. This is not a 3.2 suggestion; its step 1 will set the real sequence.

| Block | Min |
| --- | ---: |
| recap | 2 |
| bias/variance of the targets | 5 |
| 6.2 | 3 |
| batch + 6.4 + certainty equivalence | 5 |
| MC vs TD summary | 2 |
| unified view → n-step | 2 |
| n-step target | 4 |
| n-step trace (protected) | 6 |
| choosing n | 2 |
| evaluation reasoning | 10 |
| wrap-up | 2 |
| **Total** | **≈ 43** |

That leaves about 15 minutes of the 58 for 3.2's own motivation and discussion. Both examples fit without the allowance.

**Alternatives:**
- **(B) 6.1 and 6.4 in 3.1, 6.2 in 3.2.** 3.1 rises to about 61 minutes and uses the allowance (recorded as "fine for delivery; planning estimate unchanged"). 6.4 would then be a puzzle without batch updating, and 3.2 would have to come back to it.
- **(C) All three in 3.1.** About 64 minutes, over the allowance unless average reward is cut to 4 minutes (needs your explicit decision on `average_reward_live_minutes`). Not recommended: it crowds the protected calculations, and 6.2 loses its link to 3.2's learning curves.

## Delta against the old deck `4 - Model Free Prediction.pptx` (PPTX slide numbers)

| Old slides | Action | Where / what |
| --- | --- | --- |
| 1 | fix | T00 title format |
| 2 (announcement), 7 (hidden recap), 23 (recap) | cut | Administrative or redundant |
| 3 | fix | T01, updated to the redesigned Week 2 (Q-value iteration was taught; asynchronous DP got one line) |
| 4–5 | keep | T03, merged. Diagram label v_k becomes V_k (C6) |
| 6 | cut | One roadmap line in T18 |
| 8 (hidden) | fix | Prediction vs control, one line in T16. "Q-learning: TD for q" stays in Week 4 |
| 9 | fix | T02/T03, one line. P(s′, r ∣ s, a), T and R become ℳ, 𝒯 and ℛ; typo "or bot" |
| 10 | cut | The loop was taught in 1.1/1.2. The robot-soccer video in its notes is optional motivation for T03 (untimed; your choice) |
| 11 | fix | T03 pictures. Labels "Offline (MDPs)" / "Online (RL)" become "Planning with a known model" / "Learning from experience": "offline" now means fixed-data RL (Week 12). These images differ from 1.2's hidden appendix MA1 |
| 12 | keep | T03, compressed |
| 13–14 | fix | T16. Errors: off-policy is "learn about a target policy from data generated by a different behaviour policy", not "learn optimal values"; on/off-policy is not "similar to online/offline" or "batch/offline vs online" |
| 15 | keep | T02, merged |
| 16–17 | fix | T04. Episode indexing (s₁, a₁, r₁ → S_0, A_0, R_1); the return's last term γ^{T−1−t}R_{T−1} becomes γ^{T−t−1}R_T; V^π becomes v^π |
| 18–19 | fix | T05. V̄ becomes V. Drop the V_k/N_k visit indices: V_k means DP sweeps (C6). N(s) needs a guide entry (Q3). The "non-stationary?" question moves to T06 |
| 20 | fix | T06, compressed. Spelling Robbins–Monro; the 1/(k ln k) example is cut |
| 21 | keep | T07 |
| 22 | split | "Only episodic" goes to T15. Unbiased/high variance, non-Markov and "inefficient for Markov" go to 3.2 |
| 24 | keep | T10/T11 |
| 25–26 | fix | T10. r_t becomes R_{t+1}; V̄^π becomes V. "Sample return" becomes "TD target". "TD update is also a case of RM" becomes: TD(0) converges with suitably decreasing step sizes (book §6.2), but its target is not an unbiased sample of a fixed quantity, so the averaging argument does not carry over unchanged |
| 27 | keep | T11 |
| 28 | keep, move | T09, before the TD formula (O1) |
| 29 | split | "Learn before/without the outcome; continuing tasks" goes to T15. Convergence speed and "Is MC useless?" go to 3.2. "TD is better suited for exploration (why?)" is cut: unclear, and a control question |
| 30–36 | move | 3.2: bias/variance (notation fixed), MC vs TD, 6.2, batch, 6.4, certainty equivalence, Markov property |
| 37–40 | keep | T14 |
| 41 | move | 3.2, as the bridge to n-step. The λ axis is only mentioned there |
| 42–44 | move | 3.2, n-step. Old 43 has indexing errors: G_t^{(n)} = R_t + … becomes G_{t:t+n} = R_{t+1} + γR_{t+2} + ⋯ + γ^{n−1}R_{t+n} + γ^n V(S_{t+n}). Its MC line γ^T R_T is wrong |
| 45–51 | move | Week 8 (8.1 `actor_gae`, forward λ mixture) |
| 52–59 | cut | Not needed in Week 3. Week 8 gets an existence mention only (`backward_trace_mention`; `backward_trace_math: false`). The bell/light credit-assignment example on 53 is psychology (7.2) |
| VFA 37 (PDF 32) | fix | T17, definition only. The book's p(s′, r ∣ s, a) form is not needed. μ_π is avoided; T17 says "fraction of time" in words |
| VFA 38–40 (PDF 33–35) | not used | Differential Bellman equations and the algorithm are out of scope. 40's discounting-with-approximation point gets one spoken line in T17 |

## Notation needed (`course/notation_guide.md`)

- **Available in the guide:** G_t; V(s); α; δ_t; U_t; b(a ∣ s); r(π) (described as "the 5-minute continuing-task contrast only"); 𝒟; v^π.
- **Missing: the visit count N(s)** for MC sample averages. The guide has only the bandit N_t(a). See Q3.
- **Avoid V_k in MC/TD:** V_k is reserved for DP sweeps (C6). The update uses V(S_t) with ←. A time index V_t would be possible if needed; the guide allows "with subscript t when time matters".
- **Avoid μ in T17:** the guide's μ(s) is the on-policy distribution of Weeks 5–6. The fractions are stated in words.

## Questions for the instructor

**Q1 (O1, cross-session placement).** Do you accept recommendation A?
- 6.1 in 3.1;
- 6.2 and 6.4 in 3.2;
- average reward stays 5 minutes;
- 3.1 slide targets 58, with no allowance.

Alternatives B (6.4 also in 3.1, about 61 minutes, uses the allowance) and C (all in 3.1, needs average reward cut to 4) are above.

**Q2 (example choice for average reward).** The 2×2 grid is episodic, so T17 needs a continuing example. I suggest the 1.2 **continuing rescue robot**:
- its γ = 0.5 values are already known;
- the two policies give clean average rewards (1.4 vs 5/3);
- the discounted ranking flips at small γ.

The alternative is the grid with a restart after the goal, which needs new numbers and a new model statement.

**Q3 (notation).** Should N(s) be added to the guide as "number of (first) visits to s so far; MC sample averages"? It matches the book's §2.4 counts, CS234 L3 and the old deck. Alternatively, T05 could say it in words and show only the constant-α form.

**Not reasons to pause (listed for cross-review):**
- the shared trajectory, α = 0.5 and always-right (within D2);
- the taxonomy after the methods (T16);
- moving 6.1 before the TD formula;
- the old-deck fixes above.

## Correctness notes for whoever writes the first-render content

- **The DP sample-backup claim.** For a fixed V, 𝔼[R_{t+1} + γV(S_{t+1}) ∣ S_t = s] under π equals the DP evaluation backup of V at s. The TD target is therefore an unbiased sample of the DP backup of the current table; it need not be unbiased for v^π(s). True successor values are sufficient for that, not necessary (corrected after review R14). Both statements belong in the notes of T10, so that 3.2's bias discussion does not contradict it.
- **T13 is one episode.** Do not claim that either method is "better" from it. In particular, TD's 0.49 for (2,1) is not evidence that TD overestimates.
- **T17's claim is scoped.** "The ranking depends on γ" is shown here in both states (γ = 0.1–0.3 vs 0.5). The general statement is about discounted objectives, not this robot alone.
- **Notes-only backup for T17.** Weighting (1 − γ)v^π by the long-run fractions gives r(π) for every γ (book §10.4): 1.4 and 5/3, checked for γ ∈ {0.1, 0.3, 0.4, 0.5, 0.9}. Not on a slide.
- **Driving home is a prediction of time to go.** Lower is better there, unlike our rewards. Say it once.
