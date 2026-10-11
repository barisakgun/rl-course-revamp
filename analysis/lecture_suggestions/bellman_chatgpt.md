# Bellman equations and evaluation — ChatGPT initial suggestion

**Author/date:** ChatGPT, 2026-10-09. Independent initial suggestion under [pilot v2](../../docs/lecture_workflow.md), step 1. No counterpart suggestion was read. This is a recommendation, not accepted deck content or a rendering input.

**Accepted frame:** session 2.1 `bellman`, 58 teaching minutes; derive one expectation backup and perform policy-evaluation sweeps. Planning is Core, with derive/implement/analyze mastery across Week 2. No full convergence-proof sequence. The [session decisions](../../decisions/topic_decisions.yaml) place the old two-step transition prediction and formal state/action-value relationships here, integrated into the worked backup. Session 2.2 retains improvement, optimality/VI/PI and reward sensitivity. Detailed search-tree framing remains deferred to MCTS/model-based preparation. No 1.1/1.2 carryover enters this allocation.

## Main recommendation and introductory purpose

Propose a separate deck for session 2.1, provisionally named `bellman`. This local suggestion does not settle the general deck split beyond the pilot.

Start with the old DP deck's question: **given a policy and a model, how can we calculate how well the policy will do?** Values let us judge delayed consequences and eventually compare behavior. Averaging complete returns is one way to estimate them, but a known finite model offers another route. Bellman equations express consistency between a state's value and the values of possible successors. Repeated backups turn that relationship into a calculation.

Preserve the old material's explanation of dynamic programming: future subproblems recur; store one value per state and reuse it. A state may lead back to itself, so the equations can be cyclic. A backup carries value information from successors to the state being evaluated; it is a computation and does not require the agent to take a physical step.

**Recommended example:** adapt the old DP deck's 2×2 slippery grid for a fixed-policy calculation. Use it for the short two-step prediction, the expectation backup and all sweeps. This replaces repeated setup across the old 3×4 transition exercise, caveman illustrations and 2×2 value-iteration exercise. It preserves their teaching purposes without introducing three complete models. Reusing this same grid in 2.2 is a proposed cross-session choice for instructor approval, consistent with the plan's instruction to reuse one grid/table.

The accepted recycling robot remains a continuity reference, not the organizing structure of this lecture. Its probabilities and rewards are unchanged. Do not start by reciting all of 1.2's definitions or require recalling its final numerical value table to understand this lecture.

## Delta against the existing course

Slide numbers below are **PPTX positions, including hidden slides**. `MDP` means [2 - Markov Decision Processes.pptx](../../sources/current_course/2%20-%20Markov%20Decision%20Processes.pptx); `DP` means [3 - Dynamic Programming.pptx](../../sources/current_course/3%20-%20Dynamic%20Programming.pptx). Read the native slide text/equations and inspected relevant exported figures. These are proposed reuse choices.

| Old block | Keep / cut / fix / move | Teaching purpose and proposed treatment |
| --- | --- | --- |
| DP 2–3, 38–39 | Keep/compress | Retain prediction versus control and the inputs/outputs. Put the known model and fixed policy up front. Evaluation answers how good this policy is; choosing a better one comes in 2.2. Remove repeated end-to-end recaps. |
| DP 23–24 | Keep and move earlier | Preserve the explanation of decomposition, repeated subproblems and stored solutions. Explain these ideas before presenting an iterative algorithm. Use the grid's recurring successor states, not a separate application catalog. Reserve the optimal-substructure argument about choosing actions for 2.2. |
| MDP 28, 30–33 | Keep the questions; compress the route | Preserve “why calculate values?” and “how can we calculate them?”, immediate reward plus discounted continuation, and simultaneous equations. Avoid a second MRP lecture and a matrix-inverse derivation. One verbal fixed-policy MRP connection suffices. |
| MDP 42–48 | Keep/adapt the probability reasoning | Multiply along successive outcomes and add probabilities of different routes to the same state. Use two right actions on the proposed 2×2 grid instead of replaying seven slides on a second grid. No expectimax/expectiminimax taxonomy. |
| MDP 59–60 | Keep/fix | Preserve the dialogue between state and action values, then combine the two averages. Use policy probabilities for actions and model probabilities for outcomes. The old q recursion is a deterministic-policy special case; show the stochastic continuation correctly. |
| MDP 61 | Promote a short derivation to live; fix | Students should see why return recursion implies the value equation. Replace the stray λ discount by γ, use R_{t+1}, and fix the final marginalization: after summing reward outcomes, use 𝒯 for the successor-value term. The old final line retains a free reward variable in a joint probability. |
| DP 4–7, 27 | Keep and combine | Retain fixed-policy equations, a finite linear system, synchronous evaluation and the backup diagram. Place the conceptual backup picture next to its explanation. Distinguish v_π from the estimate V and calculation sweeps from environment time. Do not repeat the same evaluation definition later. |
| DP 13–16 | Adapt for evaluation now; optimization in 2.2 | Preserve the small grid, boundary behavior and 80/10/10 dynamics. Replace maximization by a fixed policy. The old exercise fixes terminal value at 1 and charges a current-state living reward; the proposed version instead pays +1 on entry and has terminal continuation 0. This is an explicit model adaptation, not an equivalent transcription: recompute the numbers and relabel the diagram. Do not copy the old answers. |
| DP 20, 22 | Keep lightly after the example; fix | B_π names the update students have already performed. Explain convergence for finite discounted evaluation through probability averaging and discounting. The reward-bearing policy operator is affine, not generally linear as DP 20 claims. Avoid the full norm/contraction proof sequence. |
| DP 28–29 | Compress into the common example | Preserve the idea that different fixed behaviors have different values. The caveman pictures need no separate setup: the grid's deliberately limited always-right policy supplies this point. |
| MDP 62–67; DP 8–12, 17–19, 21, 25–26, 30–31, 34–40 | Move to 2.2 preparation | Preserve the purpose of control, optimality, improvement and VI/PI in their scheduled session. MDP 62's generic policy-specific q recursion must not gain a max as if it were already optimal. These are later reuse candidates, not approved verbatim slides or new assignments. |
| DP 41–42; hidden 43–46 | Defer/compress | Asynchronous methods remain optional later. Retain one closing sentence about the cost of full model expectations; sampled updates arrive in Week 3. No coding block, new homework or broad algorithm survey here. |

## Proposed teaching sequence

IDs are provisional and provide cross-review targets. Adjacent material may be split across slides at rendering. These are approximate allocations including questions and required spoken explanations, not measured durations.

| ID | Topic and student-facing purpose | Main treatment / check | Minutes |
| --- | --- | --- | ---: |
| B00 | Bellman equations and evaluation | Dedicated title following the accepted title-slide convention. | 0.5 |
| B01 | Evaluating a policy | What do we know (model, policy) and what do we want (expected return)? Why calculate it? Contrast judging a supplied behavior with finding a better one. DP 3/38. | 4 |
| B02 | Dynamic programming | Repeated future subproblems can share stored values. Explain why enumerating longer and longer possible futures repeats work; cyclic transitions require mutually consistent values. DP 23–24. | 3.5 |
| B03 | A small navigation problem | Establish the grid, slips, wall collisions, rewards, discount and always-right policy. Ask whether intending to move right guarantees moving right. DP 13 adapted. | 5 |
| B04 | Two-step transition prediction | Calculate probability of reaching the goal in two steps; distinguish routes from destination states. Keep the distribution as a compact check, not a second activity block. MDP 42–48 adapted. | 4 |
| B05 | State values and action values | A state value averages the first action under the policy. An action value fixes that action, then averages its outcomes and follows the policy afterward. Derive the two relationships verbally and symbolically. MDP 59. | 4 |
| B06 | Bellman expectation equation | Split return into the next reward and the remaining return. Condition on action/outcome and identify the successor value. Explain each probability and the meaning of the equality. MDP 60–61, book §3.5. | 7 |
| B07 | Action-value recursion | Substitute the policy-weighted successor action values. Ask which policy governs the next action and why no maximization appears. Include the deterministic special case verbally. | 3 |
| B08 | A system of value equations | Write the grid's three scalar equations. There are three unknown values even though paths can continue arbitrarily long. Explain solving simultaneous equations versus iterating; no matrix-inverse notation required. DP 5/27. | 4 |
| B09 | Iterative policy evaluation | Distinguish an equality satisfied by v_π from an assignment used to update V. Explain initialization, a full sweep and reading all successor estimates from the preceding table. DP 6–7. | 5 |
| B10 | First evaluation sweep | Work one state together, then fill the first table. With all initial values zero, the first update captures expected immediate reward. Goal-entry reward appears once. | 4 |
| B11 | Second evaluation sweep | Protected student work: calculate the next table from the previous one. Keep the policy fixed and the terminal estimate zero. | 5 |
| B12 | Interpreting the sweeps | Discuss why the lower-left value changes sign and why the lower-right state remains poor despite proximity to the goal. Reveal a third sweep as feedback, not extra arithmetic work. | 3 |
| B13 | Why repeated backups settle | Name B_π, describe its fixed point, explain the discount-based reduction of worst-case discrepancy, and distinguish a practical stopping threshold from exact equality. | 4 |
| B14 | What we can now calculate | Students distinguish the model, the fixed policy, an estimate and its target value. Evaluation has left the policy unchanged; 2.2 asks how to improve it. Mention known-model limitations briefly. | 2 |
| **Total** | | | **58** |

## Worked example and mathematical checks

These details make the example reviewable. They are not instructions to display every equation and answer simultaneously.

### Proposed grid adaptation

Use coordinates from the old grid: lower-left (1,1), upper-left (1,2), lower-right (2,1), upper-right (2,2). The upper-right cell is terminal. At a nonterminal cell an action succeeds in its intended compass direction with probability 0.8 and slips into either perpendicular direction with probability 0.1 each. A move outside the grid leaves the state unchanged.

Pay **+1 total on entering the terminal cell**, **−0.04 on every other nonterminal transition**, and zero thereafter. Set γ = 0.5. These are this grid's parameters; they do not change the recycling robot. Label the goal “+1 on entry; continuation 0” rather than displaying a terminal value of +1. For bookkeeping, a terminal state stays terminal with zero reward.

Evaluate the policy that chooses **right at every nonterminal cell**. At the lower-right boundary it continues selecting right; an upward slip can end the episode. A fixed policy need not be sensible to be worth evaluating.

| State | Outcomes under right: next state, reward, probability | ℛ(s, right) |
| --- | --- | ---: |
| (1,1) | (2,1), −0.04, 0.8; (1,2), −0.04, 0.1; (1,1), −0.04, 0.1 | −0.04 |
| (1,2) | terminal, +1, 0.8; (1,2), −0.04, 0.1; (1,1), −0.04, 0.1 | 0.792 |
| (2,1) | (2,1), −0.04, 0.9; terminal, +1, 0.1 | 0.064 |

Starting at (1,1), two right actions reach the goal by either route through (2,1) or (1,2): 0.8×0.1 + 0.1×0.8 = **0.16**. The full two-step distribution on ((1,1), (1,2), (2,1), terminal) is **(0.02, 0.02, 0.80, 0.16)**. This preserves the old transition exercise's multiplication/addition reasoning. Forward probabilities predict destinations; the ensuing backup weights the reward and continuation value of each possible outcome.

### Relationships and derivation

Use the [approved notation](../../course/notation_guide.md): 𝒯, ℳ, ℛ, lower-case true values and upper-case tabular estimates. In an episodic model successor sums include the terminal state, whose continuation value is zero. Reward sums range over possible numerical reward outcomes; ℛ is not a reward-set symbol.

\[
v_\pi(s)=\sum_{a\in\mathcal A(s)}\pi(a\mid s)q_\pi(s,a),
\qquad
q_\pi(s,a)=\mathcal R(s,a)+\gamma\sum_{s'\in\mathcal S^+}\mathcal T(s,a,s')v_\pi(s').
\]

The immediate reward term is an expectation. This decomposition does not require reward to be independent of the next state. The joint form makes the outcome averaging explicit:

\[
\begin{aligned}
v_\pi(s)
&=\mathbb E_\pi[G_t\mid S_t=s]\\
&=\mathbb E_\pi[R_{t+1}+\gamma G_{t+1}\mid S_t=s]\\
&=\sum_a\pi(a\mid s)\sum_{s',r}\mathcal M(s,a,r,s')
   [r+\gamma v_\pi(s')]\\
&=\sum_a\pi(a\mid s)\left[\mathcal R(s,a)
   +\gamma\sum_{s'}\mathcal T(s,a,s')v_\pi(s')\right].
\end{aligned}
\]

Explain the key step: after arriving at s′, the Markov description and continued use of the same stationary policy make the expected remaining return v_π(s′). This replaces an average over entire futures by successor values; it does not replace each trajectory's actual remaining return by a deterministic value.

For action values, the first action is fixed and subsequent actions follow π:

\[
q_\pi(s,a)=\mathcal R(s,a)+\gamma\sum_{s'}\mathcal T(s,a,s')
\sum_{a'\in\mathcal A(s')}\pi(a'\mid s')q_\pi(s',a').
\]

For a terminal successor, read the entire continuation term as zero; no terminal action distribution is needed. A deterministic policy collapses the action average. Replacing it by a max changes the problem to optimal control and belongs in 2.2.

### Equations, updates and answer key

For the proposed always-right policy:

\[
\begin{aligned}
v_\pi(1,1)&=-0.04+0.5[0.1v_\pi(1,1)+0.1v_\pi(1,2)+0.8v_\pi(2,1)],\\
v_\pi(1,2)&=0.792+0.5[0.1v_\pi(1,1)+0.1v_\pi(1,2)],\\
v_\pi(2,1)&=0.064+0.5[0.9v_\pi(2,1)].
\end{aligned}
\]

The three equations share unknowns and can be solved simultaneously. In iterative evaluation, instead read the right-hand side using a stored estimate and write a new estimate. Set V initially to zero. For each sweep, preserve the old table, compute each new entry from that table using the fixed policy, and replace the table only when the sweep is complete. Use “sweep 0/1/2” as table headings rather than introducing another time-index convention. The book's in-place implementation uses updated entries immediately; mention this distinction so students do not mix the two conventions during the activity, without adding an asynchronous-method block.

| Sweep | V(1,1) | V(1,2) | V(2,1) | V(terminal) |
| --- | ---: | ---: | ---: | ---: |
| 0 | 0 | 0 | 0 | 0 |
| 1 | −0.04 | 0.792 | 0.064 | 0 |
| 2 | 0.0232 | 0.8296 | 0.0928 | 0 |
| 3 | 0.03976 | 0.83464 | 0.10576 | 0 |

For example, the second update of (1,1) is −0.04 + 0.5[0.1(−0.04) + 0.1(0.792) + 0.8(0.064)] = **0.0232**. Keep the second-sweep answers for the instructor's reveal. The third row of updates supports interpretation; do not ask students to perform many repetitive sweeps.

The exact fixed-policy values are **14/275, 46/55, 32/275** for (1,1), (1,2), (2,1), respectively. They are verification/answer-note material, not an additional live linear-system exercise. No claim of optimality follows from evaluating this policy.

After the concrete updates, name the full-table operation B_π: **V ← B_π V**, with **B_π v_π = v_π**. For a finite model with bounded rewards and 0 ≤ γ < 1, averaging cannot increase the largest discrepancy between two tables, and discounting shrinks it by at most a factor γ per synchronous sweep. This explains convergence to a unique fixed point without a norm-notation or theorem-proof detour. The operator includes the reward offset and is generally affine.

Stop a practical implementation when the largest change over a sweep is small enough for the intended accuracy. A small change is not exact equality or an unqualified numerical error certificate. Do not extend the discounted argument to γ = 1 without the appropriate episodic assumptions. This example stays at γ = 0.5.

## Reference-source contributions and limits

Page numbers in this table are physical PDF pages. Sources below were inspected locally, not inferred solely from the generated index. Their teaching choices are evidence, not authority for this course.

| Source inspected | Contribution to this proposal / limit |
| --- | --- |
| [Sutton & Barto](../../sources/RLbook2020.pdf), §3.5, printed 58–61 / PDF 80–83; Ch. 4 opening and §4.1, printed 73–76 / PDF 95–98 | Motivation for values, recursive consistency, backup diagrams, finite linear equations, iterative updates, synchronous versus in-place implementation and terminal continuation. Main correctness reference. Book Example 4.1 uses a different undiscounted 4×4 grid; do not import its numbers or convergence assumptions into our grid. |
| [Silver lecture 2](../../sources/silver_rl/lectures/lecture-2-mdp.pdf), PDF 29–36; [lecture 3](../../sources/silver_rl/lectures/lecture-3-planning-by-dynamic-programming-.pdf), PDF 3–11 and 35–38 | Particularly useful separation of the policy and environment averages, explanation of DP, visual sweeps and convergence intuition. Preserve explanations; omit the second student-MDP setup and the full contraction formalism. |
| [CS234 lecture 2](../../sources/stanford_cs234/lectures/lecture2post.pdf), PDF 3–15, especially 5–7 and 11–13 | Known-model framing, fixed-policy reduction and a one-iteration student exercise. Adapt the question format to our common grid rather than adding the rover. Policy-space counting/control material is for 2.2 if useful. |
| [CS224R tutorial](../../sources/stanford_cs224r/lectures/CS224R_Tutotial_Max.pdf), PDF 10–18 | Useful checks: whose future actions are being averaged, and does the Bellman equality hold for any arbitrary estimate? Preserve the equality-versus-update distinction. Do not copy its policy/index inconsistencies or call fixed-policy DP Q-learning. |
| [CS285 lecture 7](../../sources/berkeley_cs285/lectures/lec-7.pdf), PDF 4–9, especially the visual on 7 | Shows why a finite table can store the estimates and how current estimates supply continuation values. Use that explanation; leave its greedy improvement and fitted-value context to their scheduled sessions. |
| [Abbeel lecture 1](../../sources/foundations-deep-rl-abbeel/l1-mdps-exact-methods.pdf), PDF 22–25 and 54–57 | Useful contrast between policy averaging and maximization, especially the stochastic-policy question on 55. Its finite-horizon/terminal conventions and some successor-state indices need conversion; do not copy equations unchecked. |
| [Sutton DP slides](../../sources/sutton/7-8-DP.pdf), PDF 1–6 | Clear meaning of a sweep and a concise evaluation algorithm. Distinguish PDF positions from printed slide numbers. The displayed one-array algorithm is in-place; our student answer table uses synchronous sweeps. |

Course formulas use the already approved 𝒯/ℳ/ℛ notation. This proposal does not resolve O12's remaining general policy on quoting the book's p forms or learned-model notation; neither is needed for the displayed sequence. Matrix symbols and a new stopping-threshold symbol are avoided. No notation-guide edit is proposed.

## Alternatives and cross-review focus

The main choice for the instructor after cross-review is **the adapted 2×2 grid and its reuse in 2.2**. It is compact, retains the old exercise's native layout/dynamics, and leaves a visibly improvable policy for the next session. The explicit goal-entry reward convention is part of that proposal.

An alternative is the book/Silver 4×4 random-policy grid. It provides ready-made evaluation figures and a useful “expected steps to termination” interpretation, but needs a larger table and introduces an undiscounted episodic convergence case. It would replace the 2×2 example, not accompany it. A robot-only calculation offers stronger immediate continuity but less use of the old grid material and less preparation for the accepted 2.2 grid/table activity. I recommend the 2×2 adaptation.

For mutual review, focus on whether the early slides sufficiently motivate the computation, whether the transition exercise genuinely supports the backup rather than distracting from it, and whether students can distinguish fixed-policy expectation, a true-value identity and an estimate update. Check the terminal adaptation and every arithmetic answer. Also check that the mathematical block has not crowded out the 12-minute worked-sweep block. No counterpart review or instructor acceptance is claimed here.

## Timing and validation

Proposed targets sum to **58 minutes**, against **59.5 configured usable minutes** in a 70-minute session. This leaves 1.5 minutes inside the usable allowance and 12 physical minutes overall. The accepted 55–70 planning range is not treated as a reason to fill 70; 1.2's special 65-minute allowance is not imported. No scope, assessment, reading, video or student-workload change is proposed, so authoritative curriculum records and generated planning views remain unchanged.

Feasibility remains an estimate. The seven-minute derivation and first use of successor estimates are the main risks. If the flow is slow, shorten repeated symbolic exposition, linear-system discussion or operator terminology; protect the motivation and student sweeps. Do not create an additional derivation or exercise block merely because its arithmetic is available in the notes.

Validation used exact rational arithmetic for the proposed model: outgoing probabilities normalize, the two-step distribution sums to one, the first three synchronous sweeps match the table, and the exact values satisfy all three Bellman equations. Relevant source figures were visually inspected, including the old small grid, backup diagram and two-step transition tree. This is a content suggestion, not a rendered-deck or classroom timing check.

**Next workflow step:** the counterpart's independent suggestion and one mutual cross-review, followed by instructor choices. No shared rendering content, PPTX or renderer YAML has been created or modified.
