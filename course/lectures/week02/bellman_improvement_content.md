# Bellman/DP session 2.2 — initial render-ready content

**Shared:** instructor, Claude and ChatGPT. Prepared by ChatGPT, 2026-10-11, under [lecture workflow](../../../docs/lecture_workflow.md) step 4 and Bellman C21.
**Frozen (historical):** first-render input for the 2.2 slides B17–B28 appended to `course/lectures/week02/bellman_claude.pptx`, rendered 2026-10-11. Not maintained: the PPTX is the source from that render on. Do not use this file to rebuild or overwrite the deck. Status: [deck decisions](../../../decisions/lectures/bellman.md).
**Status and accepted choices:** [deck decisions](../../../decisions/lectures/bellman.md). Review, responses and verification: [shared review](../../../analysis/lecture_suggestions/bellman_review.md).
**Scope:** new 2.2 slides for the existing combined `bellman` deck. This is an addition specification, not a replacement source for its 2.1 portion. Freeze this file at the first render of this addition; thereafter the saved PPTX is the teaching source.

## Renderer handoff

- Append after B16 in `course/lectures/week02/bellman_claude.pptx`. Baseline SHA-256: `add3062bae827a723e7d5ad7bfe1682e80cd072cf053cf96fa33d534c056dbb3`, 22 slides. Preserve all existing instructor edits. If the saved deck has changed, reconcile with the latest deck rather than replacing it from an older file. Back up before any authorized PPTX edit.
- Do not modify or rebuild from the frozen 2.1 `bellman_content.md` or renderer YAML. This document specifies only the new slides. R24–R28 remain pending for the next PPTX-edit checkpoint; the shared review records both those obligations and fixes already present. Do not silently close them while appending content.
- Use the existing template, fonts, title/footer style and editable grid objects. Keep native PowerPoint equations, tables and diagrams editable. Equations use theme Accent 5 (#4472C4). Use the approved [notation](../../notation_guide.md): v^π, q^π, v^*, q^*, π^*, V_k, Q_k, ℛ, 𝒯, 𝔼. Superscripts identify policy/optimality; k counts computational sweeps.
- Display order: **B17, B18, B19, B20, B21, B21r, B22, B23, B24, B24r, B24a, B25, B26, B27, B28**. Fifteen new slides; targets sum to **57.5 minutes** against the unchanged 58-minute estimate. Required spoken cues are included. No earlier-session carryover or hidden required work.
- B21/B21r and B24/B24r are static question/answer pairs. Do not display answer slides before the calculation. No animation is necessary for these reveals. Do not accidentally show teacher answers in the student-facing question tables.
- Calculation grid: the existing separate 2×2 MDP, γ = 0.5, terminal +1 on entry, −0.04 on every other pretermination transition, zero terminal continuation. Reward-comparison grid: the familiar 3×4 MDP, **γ = 0.9**, explicitly announced on B26; ±1 total terminal-entry rewards, and the three specified living rewards. In either grid a terminal payoff replaces the living reward for that transition.
- Old source references below are **PPTX positions including hidden slides**. `DP` = [3 - Dynamic Programming.pptx](../../../sources/current_course/3%20-%20Dynamic%20Programming.pptx); `MDP` = [2 - Markov Decision Processes.pptx](../../../sources/current_course/2%20-%20Markov%20Decision%20Processes.pptx). Adapt native objects where specified; do not copy old numerical answers or nonzero terminal-value labels. PDF page numbers differ in places: MDP PPTX 52 is PDF 47.
- The suggested diagrams and equations below are source-accurate specifications, not a request to reconstruct existing 2.1 slides. Source citations and essential answers belong in notes. No new homework or reading instruction is added.

## B17 — Improving the policy

**Time:** 2 minutes. **Reuse:** DP 3 control framing and B14's grid/question for continuity; build a section opening within the existing deck, without a second course title slide.

**Display**

At (2,1), choosing up once and then following always-right gives higher expected return:

\[
q^\pi((2,1),\mathrm{up})\approx0.80036
\quad>\quad v^\pi((2,1))\approx0.11636.
\]

> Does choosing better actions at every visit give a better policy?

Today: policy improvement, policy iteration and value iteration.

**Notes:** π is the old always-right policy. These are solved policy values, not the last displayed evaluation-sweep estimates. The optional matrix home exercise is not a prerequisite: we supply the values again in B21. B15/B16 already defined optimality and the optimality equations; do not reteach them. The question is how to turn the earlier one-action comparison into a control method. Known model and finite discounted setting throughout.

## B18 — Greedy policy improvement

**Time:** 4 minutes. **Reuse:** DP 30's native greedy-extraction equation and DP 36's one-step comparison, converting notation. Keep the old model expectation; replace V^π/Q^π by v^π/q^π and P/R by 𝒯/ℛ.

**Display**

Use the current policy's values to compare candidate first actions:

\[
q^\pi(s,a)=\mathcal R(s,a)+\gamma
\sum_{s'\in\mathcal S^+}\mathcal T(s,a,s')v^\pi(s').
\]

Choose a maximizing action at each nonterminal state:

\[
\pi'(s)=\arg\max_{a\in\mathcal A(s)}q^\pi(s,a).
\]

For a deterministic current policy,

\[
q^\pi(s,\pi'(s))=\max_a q^\pi(s,a)
\ge q^\pi(s,\pi(s))=v^\pi(s).
\]

“Greedy” includes expected future return through v^π.

**Notes:** π′ means the changed policy. First interpret q^π as a chosen first action followed by π. Improvement chooses an action; it does not select a favorable random outcome. Keep the current action when it is tied for maximum; otherwise choose the first maximizing action in the order up, right, down, left. For a stochastic old policy the maximum dominates its policy-weighted average as well; one spoken sentence suffices. Terminal continuation is zero, with no terminal action. Given q^π, action selection needs only an argmax. Calculating these q values from v^π needs the model. Neither greedy selection nor a one-step score is yet an evaluation of π′.

**Check:** Is this greedy in immediate reward alone? No: the continuation term accounts for future consequences under the old policy.

**Sources:** book §4.2, printed 78–79 / PDF 100–101; Silver L3 PDF 16.

## B19 — Why policy improvement works

**Time:** 8 minutes, protected. **Reuse:** DP 36's statement and motivating question. Its “see the book for proof” instruction is replaced by the live argument below; no additional operator proof.

**Display**

If, at every nonterminal state,

\[
q^\pi(s,\pi'(s))\ge v^\pi(s),
\]

then following π′ throughout is at least as good:

\[
v^{\pi'}(s)\ge v^\pi(s).
\]

Why? Replace the old continuation with another improved action:

\[
\begin{aligned}
v^\pi(s)
&\le\mathbb E_{\pi'}[R_{t+1}+\gamma v^\pi(S_{t+1})\mid S_t=s]\\
&\le\mathbb E_{\pi'}[R_{t+1}+\gamma R_{t+2}
     +\gamma^2v^\pi(S_{t+2})\mid S_t=s]\\
&\le\cdots\longrightarrow v^{\pi'}(s).
\end{aligned}
\]

Finite MDP, bounded rewards, 0 ≤ γ < 1.

**Notes / required derivation:** First inequality: choose π′ once, then π. At every possible successor, v^π is no larger than the return from choosing π′ once there and then π. Substitute that inequality into the first expectation. Nonnegative probabilities and discount preserve the inequality. Expanding the substituted q term produces the second displayed line. Now the first two actions follow π′; only the remaining tail uses the old values. Repeat. Bounded old values multiplied by successive powers of γ have a vanishing tail, leaving the return of π′. For an episode, treat later rewards and continuation as zero after termination; no terminal action distribution is needed.

Ask students to explain the second inequality. The hypothesis must hold for every possible successor where the policy changes. Maximizing immediate reward alone does not establish it. The theorem is non-worsening from every state; it does not say every state must strictly improve. A strict one-step gain at a state gives strict value improvement there. Greedy improvement is a sufficient way to meet the condition. For stochastic π, use the policy-weighted average at the start rather than the deterministic-policy equality on B18.

**Sources:** book §4.2, printed 78–79 / PDF 100–101, especially eqs. 4.7–4.9; Silver L3 PDF 16–17; CS234 L2 PDF 24–27. This fulfills C18 without a full convergence-proof sequence.

## B20 — Policy iteration

**Time:** 4 minutes. **Reuse:** DP 26's loop and DP 31's structure; correct the policy/value indexing. Use separate evaluation and improvement blocks.

**Display**

1. Choose an initial policy.
2. **Evaluate:** calculate its values while keeping the policy fixed.
3. **Improve:** choose greedy actions while keeping those values fixed.
4. Repeat evaluation and improvement until the policy is stable.

Retain the current action when it is among the maximizing actions.

At stability, with exact evaluation,

\[
v^\pi(s)=\max_{a\in\mathcal A(s)}
\left[\mathcal R(s,a)+\gamma\sum_{s'\in\mathcal S^+}
\mathcal T(s,a,s')v^\pi(s')\right].
\]

This is the Bellman optimality equation: v^π = v^*.

**Notes:** Evaluation can use a linear solve or repeated fixed-policy sweeps, as in 2.1. The theorem uses exact evaluation; implementations using a stopping tolerance are approximate. Initialize an estimate if needed, but do not call that arbitrary estimate the true value of the policy. Under exact evaluation and current-action tie retention, a genuine policy change has a strict gain somewhere and loses nowhere. There are finitely many deterministic policies, so PI terminates after finitely many improving rounds. Do not claim finite exact convergence of the inner iterative evaluation: its limit may require infinitely many sweeps. The grid uses solved values to make the comparison exact. A stable policy under a rough estimate is not an exact optimality certificate. Tie retention avoids endlessly switching between equally good policies (book Exercise 4.4).

**Sources:** book §4.3, printed 80–82 / PDF 102–104; Silver L3 PDF 13/17; Abbeel L1 PDF 56–57 with these qualifications.

## B21 — Improving always-right on the grid

**Time:** 3 minutes; protected pair with B21r. **Reuse:** B14's editable 2×2 geometry and DP 30's improvement role. Preserve the terminal-entry caption; do not edit B14 itself.

**Display**

2×2 grid: terminal (2,2), +1 on entry and zero continuation; other transitions −0.04; γ = 0.5; motion 0.8/0.1/0.1.

**Solved values for π = always-right**

| State | v^π(s) |
| --- | ---: |
| (1,1) | 0.050909… |
| (1,2) | 0.836364… |
| (2,1) | 0.116364… |

> Calculate q^π((1,1), up). Is up better than right here?

\[
q^\pi((1,1),\mathrm{up})=
-0.04+0.5\left[0.8\left(\frac{46}{55}\right)
+0.1\left(\frac{32}{275}\right)
+0.1\left(\frac{14}{275}\right)\right].
\]

Then choose the improved action at each of the three nonterminal states.

**Notes:** Exact old values are 14/275, 46/55, 32/275 in the table order. Point to the upper-left successor (intended up), lower-right successor (right slip), and current cell (left slip blocked). Give students time before advancing. Answer: up gives 0.302909…, versus right 0.050909…. B14 already established the good up action at (2,1). The next slide supplies all action scores to confirm the choices; students need not calculate all 12 entries. These values were provided, so no optional homework assumption.

## B21r — The improved policy and its values

**Time:** 3 minutes; completes the protected six-minute PI activity. **Reuse:** same editable grid, now with arrows up at (1,1), right at (1,2), up at (2,1). Build the following table with native cells.

**Display**

Action scores under the **old** continuation policy:

| State | up | right | down | left |
| --- | ---: | ---: | ---: | ---: |
| (1,1) | **0.30291** | 0.05091 | −0.01127 | 0.02473 |
| (1,2) | 0.44036 | **0.83636** | 0.12618 | 0.33891 |
| (2,1) | **0.80036** | 0.11636 | 0.01491 | 0.09018 |

Reevaluate the changed policy π′ = (up, right, up):

\[
\begin{aligned}
v^{\pi'}((1,1))&=199/550\approx0.36182,\\
v^{\pi'}((1,2))=v^{\pi'}((2,1))&=469/550\approx0.85273.
\end{aligned}
\]

A further improvement leaves the policy unchanged; up and right tie at (1,1).

**Notes:** The values are higher than the old policy's at each of the three states. The one-action score 0.80036 is not the new policy's value 0.85273: the latter follows π′ after the first action too. At the next greedy check, up/right at (1,1) each score 0.361818…; retain up. This example needs the initial evaluation, one improving round, reevaluation and a stability check. One improvement reaches optimality here; this is not a general bound on PI rounds. Do not add another linear-system calculation. Exact checks compare the solution against all 64 deterministic policies.

**Sources for B21/B21r:** existing B14 model/values; old DP 28–31's evaluate/compare teaching purpose transferred from caveman to grid; book §4.2. Numbers recomputed under C8.

## B22 — Why shorten policy evaluation?

**Time:** 2.5 minutes. **Reuse:** DP 25's computational motivation and DP 26's transition to policy methods, reordered to follow PI; remove its erroneous V(s) successor expression.

**Display**

- A full policy evaluation may require many sweeps.
- Useful action choices may emerge before the values have settled.

> Must we finish evaluating each policy before making another improvement?

Value iteration combines a greedy choice with one backup using the current table.

**Notes:** Explain the order precisely: choose a policy greedily from the current V table; then do one evaluation backup for that chosen action using the same V table. Substitution folds the two operations into the max update on the next slide. This is the sense in which VI uses one evaluation sweep between improvements. It does not exactly evaluate the newly chosen policy, nor mean that one arbitrary old-policy evaluation sweep is itself the optimality update. Do not claim PI or VI is universally faster. This preserves the motivation before presenting another algorithm.

**Sources:** book §4.4 opening, printed 82–83 / PDF 104–105; Silver L3 PDF 18, CS285 L7 PDF 9.

## B23 — Value iteration

**Time:** 4 minutes. **Reuse:** DP 10–12's equation/algorithm objects, converted to the approved notation. Use the B16 state-optimality equation as an update, not a repeat derivation.

**Display**

For every nonterminal state s ∈ 𝒮,

\[
V_{k+1}(s)\leftarrow\max_{a\in\mathcal A(s)}
\left[\mathcal R(s,a)+\gamma\sum_{s'\in\mathcal S^+}
\mathcal T(s,a,s')V_k(s')\right].
\]

1. Initialize V₀ to zero, including terminal entries.
2. Compute each new nonterminal entry using the **old** table.
3. Replace the table after the full sweep; keep terminal entries zero.
4. Repeat until the largest sweep change is sufficiently small.

Extract a greedy policy using the final stored table V:

\[
\pi(s)=\arg\max_{a\in\mathcal A(s)}
\left[\mathcal R(s,a)+\gamma\sum_{s'\in\mathcal S^+}
\mathcal T(s,a,s')V(s')\right].
\]

**Notes:** k counts sweeps, not environment time; this is a synchronous two-table implementation. Arbitrary nonterminal initialization is possible, but our example starts at zero. The max selects the action; outcome probabilities remain averaged. Terminal payoff is in ℛ, not added again through terminal V. A finite table is generally approximate; use π rather than asserting π^* for an arbitrary stopped table. Choose ties consistently (up, right, down, left when no current action is retained).

One-line convergence explanation: in a finite discounted MDP, each action's average and then the maximum cannot enlarge the largest input discrepancy; discounting bounds the new largest discrepancy by γ times the old one. Repeated updates therefore approach v^*. A small sweep change is a practical stopping condition, not exact equality or an unexplained universal error certificate. Do not repeat the formal proof or iteration-count bounds.

**Sources:** book §4.4, printed 83 / PDF 105; Silver L3 PDF 23–24; old DP 21–22's convergence purpose compressed.

## B24 — A value-iteration sweep

**Time:** 5 minutes; protected pair with B24r. **Reuse:** DP 13's editable 2×2 grid/motion diagram and DP 14–16's exercise structure; replace all old values. Terminal caption: “+1 on entry; continuation 0”.

**Display**

γ = 0.5; living reward −0.04; synchronous VI from V₀ = 0.

| Sweep | (1,1) | (1,2) | (2,1) | Terminal |
| --- | ---: | ---: | ---: | ---: |
| V₁ | −0.04 | 0.792 | 0.792 | 0 |
| V₂ | ? | ? | ? | 0 |

> Compute V₂((1,1)) and identify the maximizing actions.

Every candidate action uses the same V₁ successor values.

**Notes:** First check the supplied V₁: the first backup at (2,1) chooses up, giving 0.8(+1) + 0.2(−0.04) = 0.792. Fixed always-right evaluation in 2.1 gave 0.064 there. Do not ask students to redo all of V₁. Work the four action scores for (1,1), ideally in pairs; students may use symmetry. Up/right each give 0.3144, down/left each −0.0184. All actions have −0.04 immediate reward from this state. Do not use just the single most valuable neighbor, slip probabilities cannot be chosen. Do not read an already updated V₂ entry. Allow working/explanation time before B24r. Other second-sweep cells are supplied as feedback, not another required calculation.

## B24r — Value-iteration results

**Time:** 3 minutes; completes the protected eight-minute VI activity. **Reuse:** B24 table layout with answers; use native cells and a small grid with both up/right arrows at (1,1).

**Display**

At (1,1): up/right each score **0.3144**; down/left each score **−0.0184**.

\[
V_2((1,1))=-0.04+0.5[0.8(0.792)+0.1(0.792)+0.1(-0.04)]
=0.3144.
\]

| Table | (1,1) | (1,2) | (2,1) | Terminal |
| --- | ---: | ---: | ---: | ---: |
| V₁ | −0.04 | 0.792 | 0.792 | 0 |
| V₂ | 0.3144 | 0.8296 | 0.8296 | 0 |
| V₃ | 0.34904 | 0.8492 | 0.8492 | 0 |
| v^* | 0.36182… | 0.85273… | 0.85273… | 0 |

Values keep changing even when the greedy actions agree.

**Notes:** The optimal row is the evaluated improved policy from B21r; it is supplied as a reference, not obtained by rounding V₃. With zero initialization and synchronous updates, Vₖ is the optimal expected discounted sum of the next k rewards with zero tail. An intermediate table need not be an infinite-horizon value function of any stationary policy. Greedy extraction using V₁ already gives an optimal policy for this small grid, even though V₁ differs from v^*. This is an example, not a universal stopping rule or a monotonic-policy-improvement guarantee for every VI intermediate policy. Show the second-sweep tied actions explicitly; a consistent tie choice is sufficient. Old DP 13–16's terminal value 1 and answers 0.37/0.01 are not applicable.

**Sources for B24/B24r:** old DP 13–16, book §4.4; Silver L3 PDF 23's intermediate-table qualification; exact recomputation in the checker.

## B24a — Q-value iteration

**Time:** 1.5 minutes. **Reuse:** B16's existing q-optimality equation as the mathematical base; DP 34's question becomes this short answered bridge. Do not add an exercise.

**Display**

Use action-value estimates directly:

\[
Q_{k+1}(s,a)\leftarrow\mathcal R(s,a)+\gamma
\sum_{s'\in\mathcal S}\mathcal T(s,a,s')
\max_{a'\in\mathcal A(s')}Q_k(s',a').
\]

- Q_k(s,a): action-value estimate after k sweeps.
- Greedy action selection from Q needs no model.
- Computing this expected update still needs the model.

Week 4: Q-learning uses sampled transitions for this kind of target.

**Notes:** Update every nonterminal state/action pair from the old Q table. The successor sum uses nonterminal 𝒮; terminal rewards remain in ℛ and terminal continuation contributes zero, so there is no max over an empty terminal action set. At convergence this estimates q^*. Action selection and learning the table have different information requirements. The later sample target is the observed reward plus discounted maximum next-action estimate (zero continuation when terminal); no Q-learning update, step size, convergence claim or new assignment here. Q_k is approved in C19 and the notation guide. This is a bridge within known-model DP, not a second live algorithm exercise.

**Sources:** B16; old DP 34; book §4.4 Exercise 4.10, printed 84 / PDF 106. C19.

## B25 — Policy iteration and value iteration

**Time:** 4 minutes. **Reuse:** DP 37's comparison and DP 39's common-backup purpose; correct unconditional claims about speed or early policy convergence.

**Display**

| | Policy iteration | Value iteration |
| --- | --- | --- |
| Main computation | Evaluate a fixed policy, then improve | Max backup at each state, each sweep |
| Intermediate table | Evaluates the current policy, exactly or approximately | May not be a policy's infinite-horizon values |
| Work per outer iteration | Evaluation work plus greedy improvement | One sweep over states and candidate actions |
| On our grid | One improving round, then reevaluation and stability | V₁, V₂, V₃ approach the same v^* |

A PI round and a VI sweep measure different amounts of work.

**Notes:** Dense VI sweep: O(|𝒮|²|𝒜|). A deterministic-policy evaluation sweep uses one selected action per state, O(|𝒮|²); improvement considers all actions and has the dense VI-sweep order of work. PI may require many such evaluation sweeps or a direct solve. Costs can be lower with sparse transitions; this grid has at most three distinct successors per action. Avoid repeating the full cost derivation from 2.1. Neither algorithm has a universal speed advantage. Our common limit is (0.361818…, 0.852727…, 0.852727…); the activity already showed both routes. Action ties can yield different equally optimal policy arrows. The accepted A1 implements VI and compares against supplied PI; this does not add a requirement to implement both.

**Check:** Does a small number of PI rounds establish lower total computation? No; count the evaluation work and action/successor backups too.

**Sources:** DP 25/37/39; book §4.4 opening/end; accepted assignment decisions A1.

## B26 — What is optimal depends on the reward

**Time:** 8 minutes, protected. **Reuse:** old MDP PPTX 52 (PDF 47), the question and side-by-side policy-map idea. Use B03a's 3×4 geometry as continuity; replace every old policy arrow and caption with the verified data below. Do not import the old value labels or terminal-boundary convention.

**Display**

Same 3×4 grid and motion model. **For this comparison, γ = 0.9.**

> With γ = 0.9, later rewards count more; this makes the risk/delay trade-off more visible than with γ = 0.5.

Three editable panels, labelled **living reward −2**, **living reward −0.04**, **living reward +0.2**. Each panel: coordinates increasing right/up; wall (2,2); goal (4,3) labelled “+1 on entry”; negative terminal (4,2) labelled “−1 on entry”. Both have continuation zero. Other transitions receive the panel's living reward, including blocked movements. Show the panels' maps/questions first if using a reveal; otherwise ask before advancing to the completed slide.

> At (3,2), should the policy choose right toward the −1 terminal, up, or left?
>
> Can a reward make avoiding the +1 terminal optimal?

**Exact arrow data for rendering**

Rows below are **top to bottom** (y = 3, 2, 1); columns x = 1, 2, 3, 4. `any` means all four actions maximize; show “any action” or four distinct arrows with a legend, not a uniquely preferred direction. Terminal cells get entry-reward labels, no policy arrows.

| Living reward | Top row (y=3) | Middle row (y=2) | Bottom row (y=1) |
| --- | --- | --- | --- |
| −2 | right; right; right; +1 terminal | up; wall; right; −1 terminal | right; right; right; up |
| −0.04 | right; right; right; +1 terminal | up; wall; up; −1 terminal | up; right; up; left |
| +0.2 | any; any; left; +1 terminal | any; wall; left; −1 terminal | any; any; any; down |

**Notes / reveal answers:** First announce the discount change from the earlier examples (C17). Hold γ = 0.9 across all three panels, along with geometry, transitions and terminal rewards; it is then the living reward that drives the comparison. Do not quietly compare different discounts across panels.

- With −2, prolonged living is sufficiently costly that the policy intends to enter the negative terminal from (3,2) or (4,1). Motion still slips; it does not deterministically “jump into the pit.” The policy optimizes expected discounted return, not our informal preference for the positive goal.
- With −0.04, the policy proceeds toward the positive goal, accounting for delay and risk: up at (3,2), and left away from the pit at (4,1). It accepts some slip risk along the route. No claim that this is a guaranteed safe path.
- With +0.2, following the displayed optimal policy keeps the process in nonterminal states. The return is `0.2 + 0.9(0.2) + … = 0.2/(1−0.9) = 2`, exceeding the immediate +1 exit. At (3,3), left turns away from the goal; at (3,2), left points into the wall, with safe perpendicular slips under the subsequent policy; at (4,1), down likewise avoids the pit. In the six `any` cells, every action's outcomes remain within states with optimal continuation 2. All nonterminal optimal values are 2. Terminal values remain zero.

Ask students which part of the specification made this behavior desirable. The algorithm cannot infer an unstated desire to finish. A terminal state does not imply every policy reaches it; discounting still makes this return finite. These scenarios do not change the robot's accepted rewards. No extra reward-shaping or reward-hacking taxonomy is needed.

**Sources:** MDP 51–52's motivation; accepted C8/C17; recomputed exact models. Old −0.4 and −0.04 produce the same arrows here; the unused zero-reward panel differs at (2,1). Use the three specified panels only.

## B27 — Generalized policy iteration

**Time:** 3.5 minutes. **Reuse:** DP 35's interaction and book §4.6's evaluation/improvement picture. Use two editable labeled blocks joined in a cycle, with the processes described in words; no extra geometric formalism.

**Display**

**Evaluation:** move the value estimates toward the current policy's values.

**Improvement:** move the policy toward greedy actions for the current estimates.

Generalized policy iteration describes how these processes interact, at different granularities.

- PI completes evaluation before improvement; VI combines improvement with a single backup.
- In a finite discounted MDP, exact-model asynchronous updates can also converge when every state continues to be updated.

Week 4 reuses evaluation and improvement with experience.

**Notes:** GPI names the common structure, rather than a third solver to implement. Evaluation and improvement can be interleaved more finely; mention partial evaluation in one sentence, without introducing another sweep-count symbol or pseudocode. The one asynchronous sentence fulfills C20. It concerns tabular exact backups with 0 ≤ γ < 1 and repeated coverage, not a guarantee for arbitrary sample-based learning. In-place updates can use the newest available entries; our numerical activities deliberately used synchronous old-table sweeps. No asynchronous exercise or homework. Do not claim every possible interaction of approximate processes converges.

**Sources:** DP 35/41–42; book §§4.5–4.6, printed 85–87 / PDF 107–109; Sutton DP slides PDF 24–25; Silver L3 PDF 18–19. C20.

## B28 — Planning with a known model

**Time:** 2 minutes. **Reuse:** DP 38–39's problem/algorithm summary, plus DP 43–45's model-availability question, condensed.

**Display**

| Task | Computation |
| --- | --- |
| Evaluate a supplied policy | Bellman expectation backups |
| Find a better policy | Greedy improvement using that policy's values |
| Solve control with a known model | Policy iteration or value iteration |

**Exit check:** Which computations need the transition and reward model? Which action-selection step can use a learned table directly?

Next: estimating values from sampled experience when the model is unavailable.

**Notes / answers:** Full expected evaluation and VI/PI/Q-value-iteration backups need the transition/reward model (or its equivalent full outcome distribution). Greedy selection from available action values uses the Q table directly; extracting from state values needs one-step model lookahead. Model-free prediction begins in Week 3; Q-learning follows in Week 4. Full expectations can also be costly in large spaces. Do not start an additional sampled-update derivation. The reward discussion established that values and optimal policies depend on the specified objective.

## Preparation verification and time audit

- Sources, mathematics, notation, motivation and scope received reciprocal review. The source base is the old DP/MDP slides, book Chapter 4 and the reference pages cited above; the latest saved 2.1 deck provides continuity. This file does not promote either initial proposal wholesale.
- Reproducible check: `python3 scripts/check_bellman_session22_chatgpt.py`. Exact rational calculations verify the model probabilities, inherited policy values, new action scores, PI results, VI sweeps and the γ = 0.9 reward-panel arrows/ties. Each reward-panel solution satisfies the Bellman optimality equation exactly. The 2×2 solution was checked against all 64 deterministic policies.
- Targets: 2 + 4 + 8 + 4 + 3 + 3 + 2.5 + 4 + 5 + 3 + 1.5 + 4 + 8 + 3.5 + 2 = **57.5 minutes**. The 58-minute estimate remains unchanged. Usable allowance is 70 × 0.85 = 59.5; 2 usable minutes and 12.5 physical minutes remain. Week 2's accepted estimates remain 60 + 58 = 118 against 119 usable, without transferring buffer between sessions.
- Protected: proof 8, PI activity 6, VI activity 8, reward discussion 8 = **30 minutes**. The Q bridge is funded by shortening repeated comparison/GPI language and the evaluation-motivation segment. No repeated optimality introduction, full convergence proof, new required reading/video or homework.
- These are planning targets, not proof of pedagogical fit. Watch the proof's second inequality, the distinction between one-action and new-policy values, and the explicitly announced discount switch. Numerical validation does not verify layout, slideshow delivery or audience pacing. Claude's initial append/render and the normal instructor/PPTX review come next; no extra text-polishing loop is required.
