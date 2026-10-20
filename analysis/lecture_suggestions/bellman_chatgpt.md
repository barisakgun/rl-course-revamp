# Bellman equations and evaluation — ChatGPT initial suggestion

**Navigation:** the original 2.1 suggestion below is historical. See [Session 2.2 independent suggestions](#session-22-independent-suggestions--chatgpt-2026-10-11) for the new step-1 proposal. Current deck status and accepted choices remain in [deck decisions](../../decisions/lectures/bellman.md).

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

## Session 2.2 independent suggestions — ChatGPT, 2026-10-11

**Workflow step 1; proposal only.** Continue the existing combined `bellman` deck after B16. This section leaves the historical 2.1 suggestion intact. No counterpart's 2.2 suggestion was read. The shared decisions/review and instructor-edited PPTX were read as requested; the PPTX and frozen first-render inputs were not edited. Current status lives only in [deck decisions](../../decisions/lectures/bellman.md).

**Accepted frame:** `improvement`, 58 teaching minutes; planning is Core with derive/implement/analyze mastery. Reuse a grid/table to compare improvement, VI and PI; protect the improvement argument and reward sensitivity. No full convergence-proof sequence; asynchronous DP optional. This proposal adds no reading, video or assessment requirement.

**Continuity checked:** latest saved PPTX SHA-256 `add3062bae827a723e7d5ad7bfe1682e80cd072cf053cf96fa33d534c056dbb3`, 22 slides. Read native text/equations and notes, and inspected existing preview pages 20/22 for the handoff; this was not a fresh PowerPoint render. B14 already compares up once with always-right; B15 defines optimal values; B16 supplies both optimality equations and the instructor's greedy extraction from q^*. B10's question-mark row and other instructor edits stay intact. R24–R28 remain recorded for the next PPTX edit under the instructor's latest instruction; see the dated shared-review addendum, including evidence of fixes already present. This proposal does not resolve them.

### Recommendation and motivation

Teach **improvement, then PI, then VI**, although the session title names VI first. Begin with B14's unanswered distinction: choosing up once and then following the old policy is better, but why should repeatedly following a changed policy be better? The local action comparison motivates the improvement theorem. PI then supplies a complete control procedure using the evaluation machinery students already know. Finally ask whether evaluating each policy fully is worth the work; this motivates VI as a shorter computation using the optimality equation already introduced in 2.1.

Use the **same 2×2 grid** for the calculations, with the solved always-right values supplied explicitly. No dependence on completing the optional matrix home exercise. Use the already introduced **3×4 grid** for the reward comparison: its two terminal outcomes expose a meaningful change in desired behavior. Neither map needs a second MDP-formulation lecture. Keep the 80/10/10 motion, walls, γ = 0.5, terminal-entry payoffs and zero continuation. Only the named living-reward comparison changes reward numbers.

### Delta against the old course

References are **PPTX positions**, including hidden slides. `DP` is [3 - Dynamic Programming.pptx](../../sources/current_course/3%20-%20Dynamic%20Programming.pptx); `MDP` is [2 - Markov Decision Processes.pptx](../../sources/current_course/2%20-%20Markov%20Decision%20Processes.pptx). Native text/equations were inspected; PDF page numbers can differ (MDP PPTX 52 is PDF 47).

| Old material | Keep / cut / fix / move | Teaching purpose retained and displacement |
| --- | --- | --- |
| DP 3, 8–9; MDP 63–64 | Compress recall | Keep the control problem and the question of how to compute a solution. B15–B16 already introduce optimality; no repeat definitions or second optimality derivation. The brief opening makes room for the improvement argument. |
| DP 30, 36 | Keep, move earlier, expand the central argument | Replace “just do policy extraction” and “see the book for proof” by meaning, a greedy action comparison, and two steps of the improvement argument. Use v^π/q^π and ℛ/𝒯. State that improvement is non-worsening everywhere, possibly strict somewhere; it need not strictly improve every state. |
| DP 26–31 | Keep PI structure; combine examples | Preserve evaluate/change/evaluate, the fixed-policy versus fixed-value distinction, and the stop condition. Replace the separate caveman examples (28–29) with the existing 2×2 grid. Repair 31's policy/value indexing; initializing a table to zero does not make it the policy's true value. |
| DP 9–12, 21, 25 | Keep VI motivation and algorithm; move after PI; fix | Explain why full evaluation may be excessive, then turn B16's equality into an update. Fix DP 25's successor V(s) to V(s′). Use “may stabilize earlier” for greedy actions, rather than asserting that policies always converge first or PI is always faster. Keep one qualified convergence explanation, not DP 22's full operator proof. |
| DP 13–16 | Keep grid and calculation/reveal structure; recompute | Preserve the student action comparison and sweeps. Replace the old 0.1 initial values and terminal value 1 with V₀ = 0 everywhere and reward +1 on entry. Old answers 0.37 and 0.01 are inapplicable. |
| DP 17–19 | Keep extraction purpose; merge into 2×2 comparison | Students choose an action using immediate reward plus expected continuation, rather than the largest neighboring cell. Do not import the old 3×4 values, γ = 0.99 or living reward −0.01 into this calculation. Its home exercise is not a new requirement. |
| MDP 52 (PDF 47) | Keep reward-sensitivity question; adapt pictures | Preserve the consequence of changing the objective while dynamics stay fixed. Recompute arrows under entry rewards and γ = 0.5. Do not reuse the old four policy pictures as numerical evidence for this model. Suggested three cases below replace repeated grid narration. |
| DP 23–24, 35, 37–39 | Keep comparison and GPI; compress duplicate summaries | B02 already explains stored subproblems. Retain what evaluation/improvement each changes, the relative work of VI/PI, and their common structure. GPI names that structure and prepares Week 4; no third algorithm catalog. |
| DP 32, 34, 40–46 | Omit detours; move future material to accepted placement | The award slide adds no necessary algorithm context. No live Q-value-iteration derivation, caveman homework or coding exercise. Asynchronous DP remains optional/unassigned. Retain only the known-model limitation from 43–45 as a bridge to Week 3's sampled prediction; no MC/TD derivation here. |

Proposed native reuse should preserve old equation/diagram objects where practical, with notation and model corrections. This is a reuse recommendation for the later renderer, not authorization to copy over existing deck slides.

### Slide-level sequence and timing

Provisional IDs continue after B16; actual slide splits can wait. Required spoken explanation, questions and answer discussion are included. Targets sum to **58 minutes**.

| ID | Content and reason | Student check / essential treatment | Min |
| --- | --- | --- | ---: |
| B17 | Improving the policy — section boundary and control motivation | Recall B14's result in one sentence. Ask why a better first action might justify a different policy at every visit. No full optimality recap. | 2 |
| B18 | Greedy policy improvement | Define the changed policy using the old policy's q values. Compare action scores at (2,1); explain “greedy” includes future return through v^π. | 4 |
| B19 | Why improvement works | **Protected:** one-step inequality, substitute it at every successor, show two steps and explain the vanishing discounted tail. Ask why improving only immediate reward would not establish this result. | 8 |
| B20 | Policy iteration | Evaluate the fixed policy, hold its values fixed to improve, then reevaluate. Explain ties and why a stable greedy policy satisfies the already known optimality equation. | 4 |
| B21 | PI on the familiar grid | **Protected:** supply solved old values; students choose the new arrows. Reveal the reevaluated values and check stability. This small example needs one improving round, not all problems. | 6 |
| B22 | Why shorten policy evaluation? | Evaluation itself may require many sweeps. Could useful action decisions be made before values settle? Preserve old DP 25's computational motivation without an unconditional speed claim. | 3 |
| B23 | Value iteration | Turn B16 into the synchronous Vₖ update; keep terminal entries zero. Show compact procedural steps and a separate greedy extraction from the final table. | 4 |
| B24 | VI sweeps and action choices | **Protected:** supply first sweep; students compute the second-sweep lower-left entry and choose its maximizing actions. Reveal the full second table, then briefly interpret a third. | 8 |
| B25 | Comparing PI and VI | Put their grid/table results beside each other. Compare what is held fixed, what each iteration costs and what intermediate values mean. A PI round and a VI sweep are different units of work. | 5 |
| B26 | Reward sensitivity | **Protected discussion:** predict changed behavior on the familiar 3×4 map, then reveal recomputed policies for −2, −0.04 and +0.6 living rewards. Explain the algorithm is optimizing the specified objective. | 8 |
| B27 | Generalized policy iteration | Name the evaluation/improvement interaction already seen. Full evaluation and shortened evaluation are different schedules; Week 4 reuses the idea with experience. | 4 |
| B28 | Planning limits and exit check | Which quantities require a model? How would behavior change if we changed rewards? Close on needing sampled experience when exact dynamics are unavailable. | 2 |
| | **Total** | | **58** |

### Improvement argument: the indispensable mathematics

Write π′ for the changed policy (a second policy, not a new kind of object). On nonterminal states,

\[
\pi'(s)=\arg\max_{a\in\mathcal A(s)}q^\pi(s,a),\qquad
q^\pi(s,a)=\mathcal R(s,a)+\gamma\sum_{s'\in\mathcal S^+}\mathcal T(s,a,s')v^\pi(s').
\]

Keep the old action when it is among the maximizers; otherwise choose the first maximizing action in the stated order up, right, down, left. For a deterministic old policy,

\[
q^\pi(s,\pi'(s))=\max_a q^\pi(s,a)\ge q^\pi(s,\pi(s))=v^\pi(s).
\]

The action value still means **new action once, then old policy**. The missing argument is why using the new policy repeatedly is safe. Because the inequality holds at every nonterminal successor and probabilities and γ are nonnegative,

\[
\begin{aligned}
v^\pi(s)&\le\mathbb E_{\pi'}[R_{t+1}+\gamma v^\pi(S_{t+1})\mid S_t=s]\\
&\le\mathbb E_{\pi'}[R_{t+1}+\gamma R_{t+2}+\gamma^2v^\pi(S_{t+2})\mid S_t=s]\\
&\le\cdots\longrightarrow v^{\pi'}(s).
\end{aligned}
\]

Explain the second inequality aloud, rather than replacing it with “repeat.” Use a finite MDP, bounded rewards and 0 ≤ γ < 1: the remaining discounted old-value tail vanishes. At termination continuation is zero; no terminal action is required. This is the central improvement argument, not a full contraction-proof sequence. With a stochastic old policy, the maximum similarly dominates its policy-weighted average; mention once, without a second proof.

PI with exact evaluation and tie retention improves until stable; at stability v^π equals the maximum one-step backup of itself, hence satisfies the optimality equation and equals v^*. Finitely many deterministic policies and strict value progress on a genuine change give finite policy termination. Numerical evaluation to a tolerance is approximate: do not promote an unchanged policy under a rough table into an exact optimality certificate.

### Concrete grid checks for cross-review

The numbers below are answer material, not instructions to display all answers at once. The 2×2 model is unchanged from B03: state order **(1,1), (1,2), (2,1)**; terminal (2,2); intended/perpendicular motion 0.8/0.1/0.1; blocked motion stays put; γ = 0.5; +1 total on goal entry, −0.04 otherwise, zero after termination.

**PI:** supply the solved always-right values `(0.050909, 0.836364, 0.116364)`, not the earlier third-sweep estimates. At (2,1), q^π for up/right/down/left is approximately `(0.800364, 0.116364, 0.014909, 0.090182)`. Up is genuinely the maximizing action. Students then determine the three greedy arrows: **up, right, up**. In particular, at (1,1), up scores 0.302909 whereas right scores 0.050909, because the old continuation policy handles the upper-left state much better.

Reevaluation yields `(199/550, 469/550, 469/550)`, approximately **(0.361818, 0.852727, 0.852727)**. At (1,1), up and right now tie; retaining up avoids a gratuitous policy change. Another greedy pass leaves the policy unchanged. Label the steps separately: one improving round followed by reevaluation and a stability check. The 0.800364 one-action score is not the new policy's value 0.852727. One improvement reaching optimality is special to this grid.

**VI:** for s ∈ 𝒮,

\[
V_{k+1}(s)\leftarrow\max_{a\in\mathcal A(s)}
\left[\mathcal R(s,a)+\gamma\sum_{s'\in\mathcal S^+}\mathcal T(s,a,s')V_k(s')\right].
\]

Initialize V₀ = 0; read every successor from the old table; update nonterminal states; replace the table after the sweep. Terminal entries stay zero. Extract a policy by maximizing the same expression using the **final stored table**. Do not label an arbitrary intermediate action score q^π or q^*: the current V table need not be a policy's infinite-horizon value.

| Computation | (1,1) | (1,2) | (2,1) | Terminal |
| --- | ---: | ---: | ---: | ---: |
| VI V₀ | 0 | 0 | 0 | 0 |
| VI V₁ | −0.04 | 0.792 | 0.792 | 0 |
| VI V₂ | 0.3144 | 0.8296 | 0.8296 | 0 |
| VI V₃ | 0.34904 | 0.8492 | 0.8492 | 0 |
| PI's reevaluated improved policy / optimal limit | 0.361818… | 0.852727… | 0.852727… | 0 |

At (1,1), the second VI sweep scores up/right **0.3144** each, and down/left **−0.0184** each. The maximizing action is tied; choose consistently. One calculation is
`−0.04 + 0.5[0.8(0.792) + 0.1(0.792) + 0.1(−0.04)] = 0.3144`.
Contrast with fixed-policy evaluation's second-sweep 0.0232 only after students identify the changed continuation values. No repeat 2.1 evaluation exercise.

With zero initialization and synchronous updates, Vₖ represents the optimal expected discounted sum of the next k rewards with zero remaining tail; an intermediate table is not generally an infinite-horizon evaluated stationary policy. The greedy choices can stabilize before the values; here the final greedy policy is already obtainable from V₁, while V₁ is far from v^*. Do not use policy stability alone as a universal VI stopping rule.

**Convergence/cost in B25:** in the finite discounted setting, action averaging and taking a maximum do not enlarge the worst input discrepancy; discounting bounds the new maximum discrepancy by γ times the old one. Use that single explanation for convergence, with a practical small-sweep-change stopping condition clearly approximate. A dense VI sweep considers every state/action/successor; a deterministic-policy evaluation sweep considers one chosen action per state; PI additionally pays for improvement and however many evaluation sweeps or a solve it uses. The grid has at most three distinct successors per action, so dense worst-case costs overstate its local work. No blanket VI/PI winner and no rederivation of 2.1's complexity formulas.

### Reward sensitivity without changing conventions

Return to B03a's **3×4 map**, wall (2,2), terminals (4,3) and (4,2). Keep γ = 0.5 and all transitions fixed. Entering those terminals pays +1 or −1 **total**, with zero continuation; the living reward applies only when the next state is nonterminal, including wall collisions. This changes the grid scenario for discussion, not the accepted recycling-robot rewards.

Propose three recomputed policy panels, with the same map orientation. Ask students to predict the action at **(3,2)**, immediately left of the negative terminal, before revealing:

| Living reward | Optimal action at (3,2) | Interpretation |
| --- | --- | --- |
| −2 | right | Ending quickly can be preferable even through the −1 terminal when remaining alive is very costly. |
| −0.04 (baseline) | up | Seek the positive outcome while accounting for slip risk and delay. |
| +0.6 | left, into the wall as the intended motion | Remaining in safe nonterminal states can beat the +1 exit; all slips and future policy choices still count. |

For +0.6, an optimal policy from the left side can avoid both terminals indefinitely, obtaining `0.6 + 0.5(0.6) + … = 1.2`. Discounting keeps this finite. A terminal label does not itself force eventual termination. The policy panel must show ties where relevant, not imply that a particular arrow is uniquely optimal everywhere.

The old −0.03 and −0.01 panels do not produce the old pictured contrast under the current model: recomputation gives the same optimal action sets as −0.04. The proposed positive case exposes a clear third behavior without silently changing γ. Alternative: use **−2, −0.4, −0.04** only; these distinguish urgency/risk in the lower row and avoid the positive-reward case, within the same eight minutes. This is a consequential example choice for cross-review/instructor selection, not an accepted reward change. Preserve at least the clear −2 versus baseline comparison.

### Source contributions and evidence limits

Local files were inspected on 2026-10-11. These are teaching references, not votes for inclusion. PDF locators below are physical pages; book printed pages are also supplied. The old decks supply the base; the latest redesigned deck supplies continuity.

| Source | Specific contribution / limit |
| --- | --- |
| [Sutton & Barto](../../sources/RLbook2020.pdf), §§4.2–4.4, printed 76–84 / PDF 98–106; §4.6, printed 86–87 / PDF 108–109 | One-action versus repeated-policy argument, PI, shortened evaluation motivating VI, and GPI. Exercise 4.4 (printed 82) motivates stable tie handling. Reuse explanations, not the book's different grids, undiscounted assumptions or notation. |
| [Silver lecture 3](../../sources/silver_rl/lectures/lecture-3-planning-by-dynamic-programming-.pdf), PDF 12–24, especially 16–19 and 23–24 | Improvement proof and stability, PI before VI, and the warning that intermediate VI tables may not correspond to policy values. Omit the car-rental setup and full contraction appendix. |
| [CS234 lecture 2, Winter 2026](../../sources/stanford_cs234/lectures/lecture2post.pdf), PDF 18–27, 33–43 | The explicit question about acting once versus following the new policy repeatedly is useful motivation; policy enumeration motivates iteration. Avoid copying its indexing and broad optimal-policy/convergence claims without finite discounted assumptions. No extra policy-counting exercise. |
| [CS285 lecture 7](../../sources/berkeley_cs285/lectures/lec-7.pdf), PDF 6–9 | Backup using a stored table and the shorter value-update picture. The slide's “approximates the new value” qualification matters. Its sample-fitting context does not turn this session into model-free control. |
| [Abbeel lecture 1](../../sources/foundations-deep-rl-abbeel/l1-mdps-exact-methods.pdf), PDF 22–25, 54–57 | Common grid and the comparison between maximization and fixed-policy evaluation; finite-policy termination sketch. Convert terminal conventions and successor indices; preserve only conditional speed claims. |
| [Sutton DP slides](../../sources/sutton/7-8-DP.pdf), PDF 8–12, 19–21, 24–27 | Alternating evaluation/improvement, tie issue, and GPI as an interaction at different granularities. The excerpted book page numbers differ from our local 2020 book; cite our book directly for the proof. |
| [CS224R tutorial](../../sources/stanford_cs224r/lectures/CS224R_Tutotial_Max.pdf), PDF 19–27 | Boundary check: optimal versus policy-dependent action values is relevant, while advantage/Monte Carlo/n-step material belongs later. No extra content added from these pages. |

Numerical checks used exact rational dynamics and policy evaluation: reproduced the inherited old-policy values, computed all greedy scores and VI sweeps, checked the improved 2×2 policy against all 64 deterministic policies, and verified each proposed 3×4 solution satisfies the optimality equation exactly. The reproducible checker is [check_bellman_session22_chatgpt.py](../../scripts/check_bellman_session22_chatgpt.py). New numbers are calculations under the explicitly stated adapted model, not facts extracted from the old slides.

### Time-budget audit, open choices and next step

`70 × 0.85 = 59.5` usable minutes; the proposed targets sum to **58**, leaving **1.5 usable minutes** and **12 physical minutes**. The accepted Week 2 estimates remain 60 + 58 = 118 against 119 usable; 2.1's accepted 61-minute slide targets do not consume 2.2's allocation. No carryover, added required work or changed assessment is assumed.

Arithmetic fit does not establish feasibility. Main risks are the first encounter with the improvement argument, confusion between a one-action score and a new policy's value, PI's inner/outer computations, and switching back to the larger grid. Supply solved PI values and protect the 8-minute argument, 6-minute PI activity, 8-minute VI activity and 8-minute reward discussion. The additional explanation displaces old duplicate optimality/DP recaps, the caveman setup, and live derivation of Q-value iteration; no accepted core topic is moved out. Use B25/B27's repeated summary language as the first place to shorten delivery, rather than removing the proof or student work. Keep asynchronous methods unassigned and optional, with no hidden workload.

Prerequisites are exactly 2.1's value relationships, expectation backups, solved-policy interpretation and optimality equations; no new probability, matrix or notation prerequisite is required. This prepares the accepted VI/PI implementation/comparison mastery, without specifying a new assignment or expecting both algorithms to be coded during class.

**Consequential choices for the normal cross-review:** PI-before-VI ordering; the three reward panels (especially the +0.6 alternative). No running-map, reward-entry, scope or minute decision needs reopening. Independent mutual cross-review is next, before instructor choices and any deck extension. This step stops at suggestions: no 2.2 rendering input, PPTX edit, new acceptance or resolution of R24–R28 is implied.
