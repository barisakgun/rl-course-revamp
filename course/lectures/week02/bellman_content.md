# Bellman equations and dynamic programming — first-render content

**Shared:** instructor, Claude and ChatGPT. Author: ChatGPT, 2026-10-09.
**Frozen (historical):** first-render input for `course/lectures/week02/bellman_claude.pptx`, rendered 2026-10-09. Not maintained: the PPTX is the source from that render on. Do not use this file to rebuild or overwrite the deck. Status: [deck decisions](../../../decisions/lectures/bellman.md).
**Current status and accepted choices:** [deck decisions](../../../decisions/lectures/bellman.md). Discussion and validation: [shared review](../../../analysis/lecture_suggestions/bellman_review.md).
**Scope of this input:** the session 2.1 portion of the single deck covering 2.1–2.2. Session 2.2 content is not yet prepared. Render these slides in the order below; do not invent the remainder. This is a first-render input, frozen at the first render under [pilot v2](../../../docs/lecture_workflow.md). After that, the saved PPTX is the teaching source.

## Rendering instructions

- Use the established course template. Keep equations, tables and diagrams editable. Reuse old native objects where specified, correcting their notation and labels. Visual refinement can follow instructor editing; correctness, context and the purpose of each calculation belong in this first draft.
- Old references use **PPTX positions including hidden slides**: `MDP` = [2 - Markov Decision Processes.pptx](../../../sources/current_course/2%20-%20Markov%20Decision%20Processes.pptx); `DP` = [3 - Dynamic Programming.pptx](../../../sources/current_course/3%20-%20Dynamic%20Programming.pptx). Reuse references identify objects/explanations to adapt, not whole slides to copy unchanged.
- Display order: **B00, B01, B03a, B03, B04, B02, B05, B06, B07, B08, B08a, B09, B10, B11, B12, B13, B14, B15, B16**. IDs retain the original suggestion's anchors while incorporating the reviewed order. The 19 live-slide targets sum to **60 minutes**. Do not infer timing from slide count. No hidden backup slides are required for this render.
- Follow the [notation guide](../../notation_guide.md): ℳ(s,a,r,s′), 𝒯(s,a,s′), ℛ(s,a); R_{t+1}; v_π/q_π for true values; V_k for estimates after k sweeps; 𝔼 for expectation. Use B_π for the policy operator. Convert old P/T/R and upper-case true values. The formula sources below specify the intended mathematics if old native objects need editing.
- All live examples here use γ = 0.5. Terminal-entry payoff is the **total** reward on that transition, replacing the living reward; terminal continuation is zero. Do not copy old terminal values of +1/−1, old value tables or policy arrows without recomputation. The unchanged recycling robot is a brief continuity reference only.
- Required live cues below count within the slide targets. Optional answer details are identified. B08 asks students to write an equation; B11 is the protected calculation activity. Keep answers in notes until the specified later reveal, with room for annotation. Do not require animations to make the sequence usable.
- B08a supplies writing space for the instructor's tablet derivation. Do not add typed matrix symbols or an inverse formula to slides or backups; that notation has not been approved for typed content.
- The introductory 3×4 grid and calculation 2×2 grid are different MDPs with shared movement rules. Label the switch explicitly. No detailed expectimax/search-tree framework is introduced.

## B00 — Bellman equations and dynamic programming

**Time:** 0.5 minute. **Reuse/build:** title layout from the accepted course convention (Introduction A21).

**Display:** “COMP438/538 Reinforcement Learning”; topic **“Bellman Equations and Dynamic Programming”**; “Barış Akgün”; “Fall 2026”. Follow the established centered course-title layout, without a tagline or illustration.

**Note:** This deck covers Week 2. Today's portion develops policy evaluation and the Bellman optimality equations.

## B01 — Evaluating a policy

**Time:** 3 minutes. **Reuse:** DP 3's prediction/control distinction and DP 38's known-model framing, condensed.

**Display**

> How can we compute expected return when the task can continue indefinitely?

- Given: a model of the environment and a policy.
- Prediction / policy evaluation: calculate the policy's state and action values.
- Control: find a policy with higher expected return.

> Values account for delayed consequences and help us compare decisions.

**Required live cue:** Recall the open question after the robot's value table in 1.2, without repeating that table or its calculations. Averaging repeated returns has sampling variation, and stopping a continuing trajectory leaves a tail. A known model lets us average outcomes directly. The Bellman equation represents the entire future through successor values. A finite number of iterative updates can still be approximate; distinguish that later from solving the finite system exactly. Today the policy first stays fixed. Improving it is the next question.

**Sources:** DP 3/38; book §§3.5/4.1; accepted 1.2 closing question.

## B03a — Gridworld as an MDP

**Time:** 3 minutes. **Reuse:** MDP 37–40: the native 3×4 map and movement-rule objects, plus its MDP-formulation questions. Omit the old learning/planning discussion block.

**Display/figure:** show columns 1–4 from left to right and rows 1–3 from bottom to top. Start at (1,1); (2,2) is a wall. Mark terminal cells (4,3) “+1 on entry” and (4,2) “−1 on entry”. Label the other accessible cells “living reward −0.04”.

- Actions: up, down, left, right.
- Intended direction: 0.8; each perpendicular direction: 0.1.
- A blocked movement leaves the agent in the same cell.
- Entering either terminal cell ends the episode; no rewards follow.
- γ = 0.5 for today's examples.

**Prompt:** “What are the states, actions, model, rewards and objective?”

**Required live cue / answers:** State is the accessible cell, with the grid and rules fixed. There are nine nonterminal cells (𝒮), and eleven accessible cells including the two terminals (𝒮⁺); the wall is not a state. The model describes the possible actual movements after an intended action. A policy chooses an action; it does not select which slip occurs. The objective is expected discounted return. On a terminal-entry transition the reward is +1 or −1 total, not that amount minus 0.04. Colliding with an outer boundary or the internal wall still incurs −0.04. These rules differ from the old nonzero terminal-value convention, so use no old computed values here.

**Sources:** MDP 37/38/40; decisions C7/C8.

## B03 — A smaller grid for calculations

**Time:** 2 minutes. **Reuse:** DP 13's native 2×2 cells and 80/10/10 movement diagram. Replace its value-iteration prompt, terminal-value labels and initial estimates.

**Display/figure**

| (1,2) | (2,2): goal |
| --- | --- |
| (1,1): start | (2,1) |

> Same movement rules, smaller map. This is a separate MDP.

- Goal entry: +1 total; every other transition before termination: −0.04.
- Goal continuation value: 0. Discount: γ = 0.5.
- Fixed policy π: choose **right** at every nonterminal cell.

**Required live cue:** Draw rightward policy arrows only in the three nonterminal cells. At the lower-right boundary the policy still intends to go right; an upward slip can reach the goal. Evaluation can assess an inefficient policy. Moves into a boundary stay in the same cell. The goal has no chosen action; for bookkeeping only, we may keep it absorbing with reward zero. No nonzero terminal value is initialized.

**Sources:** DP 13 adapted; decisions C7/C8. The smaller map is not a value-preserving reduction of B03a.

## B04 — Two-step transition prediction

**Time:** 3.5 minutes. **Reuse:** MDP 42–48's branching explanation and path-probability reasoning. Adapt the figure to two right actions on B03; remove the old 3×4 tree's probabilities and destinations.

**Display:** retain the small grid beside a two-step outcome tree. Start at (1,1). First-step branches: (2,1) with 0.8, (1,2) with 0.1, (1,1) with 0.1.

> Under the always-right policy, what is the probability of reaching the goal in two steps?

**Required live cue / answer:** Multiply probabilities along a route, then add disjoint routes ending at the same state. Through (2,1): 0.8×0.1; through (1,2): 0.1×0.8. Total **0.16**. The first step cannot terminate here, so “in two steps” also means “by step 2”. This is prediction using the model, with no sampled trial required.

**Renderer answer key:** second-step branches from (2,1): itself 0.9, terminal 0.1; from (1,2): terminal 0.8, itself 0.1, (1,1) 0.1; from (1,1): the same first-step distribution. Final probabilities on ((1,1), (1,2), (2,1), terminal) are (0.02, 0.02, 0.80, 0.16). Show the goal calculation at the reveal; the full distribution may stay in notes. This tree explains weighted outcomes, not a new search algorithm.

**Sources:** MDP 42–48, transferred to the accepted small grid.

## B02 — Reusing future subproblems

**Time:** 2 minutes. **Reuse:** DP 23–24's explanation, now after the concrete prediction.

**Display**

- Different routes can arrive at the same state.
- From that state, the same policy faces the same future problem.
- Store one value per state and reuse it when evaluating predecessors.

> Dynamic programming uses this repeated structure to compute values.

**Required live cue:** Point to repeated states in B04. Enumerating progressively longer futures repeats work. The Markov state and fixed stationary policy let a state summarize the expected continuation. Transitions can return to the same state, so its value may depend on itself. The values must satisfy their equations together; the graph need not be a one-way chain. This motivates the recursion and later sweeps before presenting their formulas.

**Sources:** DP 23–24; Silver lecture 3 PDF 3–5.

## B05 — State values and action values

**Time:** 4 minutes. **Reuse:** MDP 59's native relationships. Convert symbols and retain policy conditioning.

**Display**

> A state value averages the first action according to the policy.

\[
v_\pi(s)=\sum_{a\in\mathcal A(s)}\pi(a\mid s)q_\pi(s,a).
\]

> An action value fixes the first action, then follows the policy.

\[
q_\pi(s,a)=\mathcal R(s,a)+\gamma
\sum_{s'\in\mathcal S^+}\mathcal T(s,a,s')v_\pi(s').
\]

**Required live cue:** The two averages answer different questions: which action the policy chooses, and what the environment does after that action. ℛ is expected immediate reward. Separating its expectation from expected continuation does not require reward and next state to be independent. In a terminal state v_π is zero. For our always-right policy, v_π(s) = q_π(s,right), but other first actions still have action values under the same continuation policy.

**Check:** “If I change what the agent does after the first action, can that action's value change?” Yes. This formalizes the distinction introduced in 1.2.

**Sources:** MDP 59; book §3.5 Exercises 3.12–3.13; Silver lecture 2 PDF 31–32.

## B06 — Bellman expectation equation

**Time:** 6 minutes. **Reuse:** MDP 26's return split and MDP 60–61's native equations, with the corrections below. Keep the derivation visually sequential rather than one dense paragraph.

**Display**

\[
\begin{aligned}
v_\pi(s)
&=\mathbb E_\pi[G_t\mid S_t=s]\\
&=\mathbb E_\pi[R_{t+1}+\gamma G_{t+1}\mid S_t=s]\\
&=\sum_{a\in\mathcal A(s)}\pi(a\mid s)
  \sum_{s'\in\mathcal S^+,r}\mathcal M(s,a,r,s')
  [r+\gamma v_\pi(s')].
\end{aligned}
\]

Equivalent form using expected reward and next-state probabilities:

\[
v_\pi(s)=\sum_{a\in\mathcal A(s)}\pi(a\mid s)
\left[\mathcal R(s,a)+\gamma\sum_{s'\in\mathcal S^+}
\mathcal T(s,a,s')v_\pi(s')\right].
\]

> Expected immediate reward + discounted expected continuation.

**Required live cue:** Given the next Markov state and the same stationary policy, the expected remaining return is that next state's value. This is the step replacing the conditional expectation of G_{t+1}; a sampled G_{t+1} is not itself equal to v_π(S_{t+1}). The joint sum weights each numerical reward/next-state outcome. Its reward part gives ℛ and its continuation part marginalizes over reward to give 𝒯. Do not leave a free r in the marginal model or use ℛ as a reward set. With a deterministic policy the outer action average selects its single action.

**Check:** “Does this equality hold for any arbitrary table of numbers?” No: it characterizes the true value function. We will later use its right-hand side to update a provisional table.

**Sources:** MDP 26/60/61; book §3.5 equation 3.14, printed 59 / PDF 81; CS224R tutorial PDF 13–14. Correct the old λ to γ and old reward indices to R_{t+1}.

## B07 — Action-value recursion and backups

**Time:** 3 minutes. **Reuse:** DP 7's backup diagram and MDP 60's q equation. Match stochastic policy branches to the stochastic equation rather than retaining the old deterministic mismatch.

**Display**

\[
q_\pi(s,a)=\mathcal R(s,a)+\gamma
\sum_{s'\in\mathcal S}\mathcal T(s,a,s')
\sum_{a'\in\mathcal A(s')}\pi(a'\mid s')q_\pi(s',a').
\]

> A backup carries value information from possible successors to the state or action being evaluated.

**Visual:** open circles denote states, solid dots denote state/action pairs. Show the state-value pattern s → a → s′ and the action-value pattern (s,a) → s′ → a′ as compact companion diagrams. Label action branching π and outcome branching ℳ (reward and next state), or 𝒯 if the diagram shows only next states. Adapt native objects; do not copy a diagram whose model/policy labels contradict the equation.

**Required live cue:** Here the successor sum is over nonterminal 𝒮; terminal continuation is zero and requires no next-action policy. The next action follows π, so there is no max. Ask which branching belongs to the agent and which to the environment. A backup is a calculation, not the agent physically moving backward or taking a new step.

**Sources:** DP 7; MDP 60; book §3.5 backup diagrams, printed 59/61; Silver lecture 2 PDF 34.

## B08 — Three states, three value equations

**Time:** 3.5 minutes. **Reuse:** DP 5/27's finite-system explanation; keep the accepted small grid visible.

**Display:** policy π is always right; goal continuation is zero. Reveal the first equation, then ask students to write the other two from the grid.

\[
\begin{aligned}
v_\pi((1,1))&=-0.04+0.5[0.1v_\pi((1,1))+0.1v_\pi((1,2))+0.8v_\pi((2,1))],\\
v_\pi((1,2))&=0.792+0.5[0.1v_\pi((1,1))+0.1v_\pi((1,2))],\\
v_\pi((2,1))&=0.064+0.5[0.9v_\pi((2,1))].
\end{aligned}
\]

> The paths may be arbitrarily long; this policy has only three unknown nonterminal values.

**Required live cue / answer:** Each coordinate pair denotes one state. At (1,2), expected immediate reward is 0.8(1) + 0.2(−0.04) = 0.792. At (2,1), it is 0.1(1) + 0.9(−0.04) = 0.064. In both equations the successor term for terminal is zero. Do not add the terminal payoff again in the continuation term. Fixing the policy gives a Markov reward process; mention the connection once.

**Build:** keep the second and third equations as note answers until the instructor's reveal; a duplicate answer slide is unnecessary. If reveals are not implemented, show the first equation and leave writing space, with the other equations in notes.

**Sources:** DP 5/27; book §4.1; accepted grid adaptation.

## B08a — Solving the value equations

**Time:** 3 minutes. **Reuse/build:** a clean tablet-work slide carrying the three scalar equations from B08 compactly, with generous writing space. No typed matrix symbols.

**Display**

> Fixed policy: a linear system for the unknown state values.
>
> Write the system in matrix form and solve it.

**Required live cue:** The instructor derives the matrix form on the tablet. Use state order (1,1), (1,2), (2,1). Collect current-state coefficients and successor terms from B08; explain why there are no products of unknown values. A direct solve is practical for a small model, while large dense systems are expensive. An iterative method reuses local computations and can stop at an approximation. Avoid an unqualified claim that any problem containing a max has no analytic solution.

**Instructor answer notes:** exact values in this order are 14/275, 46/55, 32/275, approximately 0.05091, 0.83636, 0.11636. A generic dense direct solve has cubic arithmetic cost in the number of states; structure/sparsity can change the practical cost. No full complexity derivation is needed. Do not require students to do three-state elimination by hand here.

**Sources:** DP 5/27; MDP 31–33; book §4.1; decision C4.

## B09 — Iterative policy evaluation

**Time:** 3.5 minutes. **Reuse:** DP 6's synchronous update, with stochastic policy averaging and approved estimate notation. Replace its mislabeled “closed form” caption.

**Display**

\[
V_{k+1}(s)\leftarrow\sum_{a\in\mathcal A(s)}\pi(a\mid s)
\left[\mathcal R(s,a)+\gamma\sum_{s'\in\mathcal S^+}
\mathcal T(s,a,s')V_k(s')\right].
\]

- Initialize V₀(s) = 0, including the terminal state.
- Compute every new entry using the **old table**.
- After all states are updated, replace the table and repeat.
- Stop when the largest change over a sweep is sufficiently small.

> k counts computational sweeps. The policy stays fixed.

**Required live cue:** The equality for v_π becomes an assignment for an estimate V. One sweep updates every nonterminal state once. Keep the terminal estimate zero. The book also describes in-place updates using one array, where later updates may read newly changed entries. Those can produce different intermediate tables; this activity uses two tables and synchronous sweeps throughout. A small stopping change means approximate convergence, not exact equality or a universal error certificate.

**Sources:** DP 6/27; book §4.1 equation 4.5 and implementation discussion, printed 74–75 / PDF 96–97; CS234 lecture 2 PDF 12–13; notation decision C6.

## B10 — First evaluation sweep

**Time:** 4 minutes. **Reuse/build:** B03 grid beside an editable table; adapt DP 13–16's worked-table role, not its old numbers or maximization.

**Display:** always-right policy, γ = 0.5, V₀ = 0.

| Sweep | (1,1) | (1,2) | (2,1) | Terminal |
| --- | ---: | ---: | ---: | ---: |
| V₀ | 0 | 0 | 0 | 0 |
| V₁ | −0.04 | 0.792 | 0.064 | 0 |

> With zero initial continuation values, the first sweep gives expected immediate rewards.

**Required live cue:** Calculate (1,2) together, explicitly weighting the +1 goal-entry outcome and the two −0.04 outcomes. Ask students to supply (2,1) before revealing it. The value update uses an expectation over possible transitions; the robot does not physically collect 0.792 on a single step. A transition's reward and its next-state value have separate roles.

**Sources:** book §4.1; DP 13–16 format adapted; accepted grid model.

## B11 — Second evaluation sweep

**Time:** 5 minutes, protected student calculation. **Reuse/build:** same grid/table, with room to work. Answers remain in notes and appear on B12.

**Display**

| Sweep | (1,1) | (1,2) | (2,1) | Terminal |
| --- | ---: | ---: | ---: | ---: |
| V₁ | −0.04 | 0.792 | 0.064 | 0 |
| V₂ | ? | ? | ? | 0 |

> Compute V₂ using V₁ for every successor value. Keep the policy fixed.

**Instructor answers:** V₂((1,1)) = −0.04 + 0.5[0.1(−0.04) + 0.1(0.792) + 0.8(0.064)] = **0.0232**. V₂((1,2)) = 0.792 + 0.5[0.1(−0.04) + 0.1(0.792)] = **0.8296**. V₂((2,1)) = 0.064 + 0.5[0.9(0.064)] = **0.0928**. Terminal remains 0.

**Cue:** Check whether a student has inserted an action max, reused a freshly computed V₂ entry, or counted the goal payoff twice. Address these meanings before arithmetic slips. Do not shorten this activity to fit an unplanned extra explanation.

**Sources:** book §4.1; CS234 lecture 2 PDF 13 exercise structure; accepted grid model.

## B12 — What the sweeps mean

**Time:** 3 minutes. **Reuse/build:** reveal the editable answer table and retain the small grid.

**Display**

| Sweep | (1,1) | (1,2) | (2,1) | Terminal |
| --- | ---: | ---: | ---: | ---: |
| V₁ | −0.04 | 0.792 | 0.064 | 0 |
| V₂ | 0.0232 | 0.8296 | 0.0928 | 0 |
| V₃ | 0.03976 | 0.83464 | 0.10576 | 0 |

> Starting from V₀ = 0, k synchronous sweeps give the exact expected discounted sum of the first k rewards under this policy.

**Required live cue:** The model averages outcomes without sampling variation, but a finite sweep count still omits later rewards. Link to B04: from (1,1), expected second reward is 0.8(0.064) + 0.1(0.792) + 0.1(−0.04) = 0.1264. Therefore the expected two-step discounted sum is −0.04 + 0.5(0.1264) = 0.0232, exactly V₂((1,1)). After termination all later rewards are zero.

**Checks:** The lower-left value becomes positive when later rewards enter the estimate. The lower-right value remains low because the policy keeps choosing right into a boundary and relies on a slip. Nearness to the goal alone does not determine value. We have evaluated the same policy at every sweep. V₃ is supplied for interpretation, not another calculation assignment. Do not claim every state's error decreases at every sweep.

**Sources:** book §4.1; Claude's forward-prediction connection adopted in review R04, with R11/R12 qualifications.

## B13 — Why repeated backups settle

**Time:** 4 minutes. **Reuse:** DP 20/22's policy operator and convergence explanation, corrected and made concrete.

**Display**

\[
V_{k+1}=B_\pi V_k,\qquad B_\pi v_\pi=v_\pi.
\]

> B_π applies one full policy-evaluation sweep.
>
> Probability averaging cannot increase the largest discrepancy; discounting multiplies it by γ.

\[
\max_{s\in\mathcal S^+}|V_{k+1}(s)-v_\pi(s)|
\leq\gamma\max_{s\in\mathcal S^+}|V_k(s)-v_\pi(s)|.
\]

> Finite MDP, bounded rewards, fixed policy, 0 ≤ γ < 1: the sweeps converge to its unique value function.

**Required live cue:** Subtract the true-value equation from the update. The expected immediate rewards cancel; the remaining discrepancies are probability-weighted, then discounted. This is the one-line contraction argument, not a theorem-proof sequence. B_π includes a reward offset and is generally **affine**, correcting old DP 20's “linear operator” label. Its fixed point is the table unchanged by a sweep.

**Instructor check, optional numerical detail:** grid maximum errors for sweeps 0–3 are approximately 0.83636, 0.09091, 0.02771, 0.01115, each at most half the preceding maximum. Individual-state error need not fall: at (1,1) it increases from about 0.05091 to 0.09091 on the first sweep. Do not describe the table as “each error halves.” The k-step interpretation and the contraction guarantee are different claims. Do not extend this discounted argument to γ = 1 without additional episodic assumptions.

**Sources:** DP 20/22; Silver lecture 3 PDF 35–38; book §4.1; decisions C5/C6.

## B14 — A better first action?

**Time:** 2 minutes. **Reuse:** MDP 59's action-value relation; keep the small grid and its always-right policy visible.

**Display**

> At (2,1), compare continuing right with choosing up once, then following the same policy.

\[
v_\pi((2,1))=q_\pi((2,1),\text{right})=\frac{32}{275}\approx0.11636.
\]
\[
q_\pi((2,1),\text{up})
=0.792+0.5\left[0.1\left(\frac{14}{275}\right)+0.1\left(\frac{32}{275}\right)\right]
\approx0.80036.
\]

**Required live cue:** Up reaches terminal with probability 0.8; a left slip reaches (1,1), and a right slip hits the boundary and stays at (2,1). Its immediate expected reward is 0.792. The continuation values still belong to always-right. This suggests changing an action, but the computed q_π is not q_* and is not the value of repeatedly following an improved policy. The next question is what values are possible when future actions are also chosen optimally. The policy-improvement proof remains for 2.2.

**Sources:** book §4.2 opening, printed 76 / PDF 98; old DP 30/36 motivation only, without the theorem.

## B15 — Optimal values

**Time:** 2 minutes. **Reuse:** MDP 63's definitions, converted to the notation guide and stripped of the search/q-state framing.

**Display**

\[
v_*(s)=\max_\pi v_\pi(s),\qquad
q_*(s,a)=\max_\pi q_\pi(s,a).
\]

- v_*(s): best expected return from s.
- q_*(s,a): expected return after first taking a, then acting optimally.

\[
v_*(s)=\max_{a\in\mathcal A(s)}q_*(s,a).
\]

**Required live cue:** We now change the question from evaluating a supplied policy to finding the best achievable expected return. These maxima range over policies, not sampled lucky trajectories. In a finite discounted MDP, an optimal stationary deterministic policy can attain these statewise optimal values. This statement uses today's model assumptions; do not generalize it to every formulation of RL. Terminal value remains zero.

**Sources:** MDP 63; book §3.6, printed 62–64 / PDF 84–86. Decision C9 retains this in 2.1.

## B16 — Bellman optimality equations

**Time:** 3 minutes. **Reuse:** MDP 64's native equations, with ℛ/𝒯 and lower-case true values. Keep both optimality equations in this first draft; do not silently move them to 2.2 to fit an earlier target.

**Display**

\[
v_*(s)=\max_{a\in\mathcal A(s)}
\left[\mathcal R(s,a)+\gamma\sum_{s'\in\mathcal S^+}\mathcal T(s,a,s')v_*(s')\right].
\]

\[
q_*(s,a)=\mathcal R(s,a)+\gamma\sum_{s'\in\mathcal S}
\mathcal T(s,a,s')\max_{a'\in\mathcal A(s')}q_*(s',a').
\]

> The agent chooses an action; the environment's outcomes are still averaged.
>
> Next: policy improvement, value iteration and policy iteration.

**Required live cue:** At each nonterminal state, replacing the policy average with an action maximum expresses optimal choice with optimal continuation. For q_* the specified first action stays fixed; maximization applies to the following action. The second equation sums over nonterminal successors only, since terminal continuation is zero. We cannot select a favorable random outcome by moving the max over next states. In general the action maximum makes the system nonlinear; the straightforward fixed-policy linear-system solve no longer applies directly. Explain the parallel between the equations without a second full derivation or a policy-improvement proof.

**Closing cue:** Exact expected backups require the model. Later methods address sampled experience and larger representations. This is the end of the prepared 2.1 section; 2.2 will develop the algorithms within this same deck, without repeating this entire introduction.

**Sources:** MDP 64; book §3.6 equations 3.19–3.20, printed 63–64 / PDF 85–86; decision C9.

## Handoff boundary

Claude can use this file as the first-render input for the prepared 2.1 section. Session 2.2 still needs its independent suggestions and consolidation. Do not mark the combined deck complete or create filler slides for that section. Once the first PPTX exists, freeze this input and continue edits in the PPTX under pilot v2; later 2.2 additions must preserve any instructor edits already made to the 2.1 slides.

The instructor has explicitly retained the optimality equations and allowed the longer draft. Targets are **60 minutes**, including the live tablet work and student calculations. They leave 10 physical minutes and use 0.5 minute of the configured general buffer. Actual delivery and visual fit are not yet verified. Carry any substantive rendering issue to the shared review; there is no additional text-proposal review gate.
