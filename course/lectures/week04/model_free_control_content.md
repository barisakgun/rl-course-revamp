# Model-free control — first-render content, sessions 4.1–4.2

> **Historical: frozen at the first render (Claude, 2026-10-27).** This file was the input to the first render of
> `course/lectures/week04/model_free_control_claude.pptx`. From that render on, the PPTX is the source. Do not
> rebuild over the deck or treat this file as its current content. Status: [deck decision file](../../../decisions/lectures/model_free_control.md).

**Shared** by the instructor, Claude and ChatGPT. Prepared by ChatGPT, 2026-10-27, under [workflow step 4](../../../docs/lecture_workflow.md), implementing [model_free_control D1–D5](../../../decisions/lectures/model_free_control.md) and the resolved [mutual review R01–R23](../../../analysis/lecture_suggestions/model_free_control_review.md). **Deck status lives only in the deck decision file.** This is the first-render input, not an accepted teaching deck. At the first render, mark this file historical: the saved PPTX becomes the teaching source; never rebuild over instructor edits from this file.

## Rendering and source conventions

- Preserve the accepted 18 units for 4.1 and 11 teaching units plus administration for 4.2. Four units split across two slides for legibility: C13/C13a, C15/C15a, P03/P03a and P09/P09a. **34 live slides**, with no additional appendix specified. A slide split does not add time. Session 4.1 ends at C17; P00 starts 4.2.
- **Display** is required visible teaching content. **Notes** supplies answers, qualifications and spoken explanations within the allotted time. Present questions before their answers; use click reveals or the specified answer slide. Do not put all notes on the slide. Preserve editable text, grids and equations.
- **Old Pn** means physical slide n in [5 – Model Free Control.pptx](../../../sources/current_course/5%20-%20Model%20Free%20Control.pptx), 61 slides, SHA-256 `7309376c0881a12c8eb47ad324f87044efd05b8a182c585504c5cf3ef50bc7bc`. The [PDF](../../../sources/current_course/5%20-%20Model%20Free%20Control.pdf) has 57 pages; its numbering differs. Relevant mapping: P8→PDF6, P10→7, P13→10, P14→11, P15→12, P16→13, P17→14, P19→16, P21→18, P23→19, P24→20, P40→36, P41→37, P42→38, P43→39, P44→40, P50–51→46–47.
- Reuse the old PPTX's native equations and diagrams where identified below, with the exact edits specified. P10, P13, P15, P16, P17, P21, P23, P40 and P41 contain native equation material. P24/P42 are raster algorithm boxes: use P23/P40 equation objects plus the new editable algorithm text instead of enlarging the raster boxes. Do not copy an entire old slide when only a diagram or equation is requested. Never retain stale old notes or excluded algorithm lists.
- Use [course notation](../../notation_guide.md): `q^π`, `q^*` for true action values; `Q` for estimates; `v^π` for true state values; `R_{t+1}` after action `A_t`; `b(a∣s)` for behaviour; `U_t` for a target. Remove old behaviour `μ`, return `H`, reward-index and true/estimate ambiguities. No new state-action counter is introduced. State-action sample averaging is described in words. In loop text, next-step variables keep their time indices.
- Native PowerPoint equations first, with LaTeX below as the correctness specification. No source equation overrides the displayed version here. Use established course formatting rather than inventing a new theme.
- The old control deck is the content base. The accepted Bellman/mc_td decks supply continuity only; recreate their simple grid from the specification below, without changing either deck. Current `mc_td` was accepted under D19, SHA-256 `b4ca75d4317a629ca7941888759a70ca926aae93d2c96baadde10e46f1ef72ba`; its forward-λ introduction is recalled verbally only.
- **Preparation references, not assigned reading:** [book](../../../sources/RLbook2020.pdf) §§5.2–5.4 printed 96–103 / PDF118–125; §§6.4–6.5 printed 129–132 / PDF151–154; [Silver L5](../../../sources/silver_rl/lectures/lecture-5-model-free-control-.pdf) PDF6–16, 20–22, 35–42; [CS234 L4](../../../sources/stanford_cs234/lectures/lecture4post.pdf) PDF17–21, 29–38; [Abbeel L2](../../../sources/foundations-deep-rl-abbeel/l2-deep-q-learning.pdf) PDF5–10; [Sutton TD slides](../../../sources/sutton/11-12-TD.pdf) PDF34–39. CS285/CS224R references in the initial suggestion support the policy/data distinction; their approximation and actor-critic sequences are not imported here.

## Timing and teaching order

| Session | Accepted unit | Slides | Minutes |
| --- | --- | --- | ---: |
| 4.1 | Title | C00 | 0.5 |
| 4.1 | What changes when we want better behaviour? | C01 | 2 |
| 4.1 | Brainstorm | C02 | 3 |
| 4.1 | Why Q? | C03 | 3 |
| 4.1 | Evaluation and improvement interleave | C04 | 2 |
| 4.1 | One MC control cycle | C05 | 3 |
| 4.1 | Greedy lock-in question | C06 | 3 |
| 4.1 | Exploration versus exploitation | C07 | 2 |
| 4.1 | Epsilon-greedy | C08 | 3 |
| 4.1 | On-policy MC control | C09 | 2 |
| 4.1 | Why not wait? | C10 | 2 |
| 4.1 | SARSA derivation | C11 | 6 |
| 4.1 | SARSA loop | C12 | 3 |
| 4.1 | Sampled Q-value iteration and Q-learning loop | C13, C13a | 3 + 3 |
| 4.1 | Behaviour and target policies | C14 | 2 |
| 4.1 | Protected target exercise | C15, C15a | 7 + 3 |
| 4.1 | Interpretation and synthesis | C16 | 3.5 |
| 4.1 | Recap | C17 | 1.5 |
| | **4.1 targets sum to** | | **57.5** |
| 4.2 | Section opener | P00 | 0.5 |
| 4.2 | Retrieve the target distinction | P01 | 3 |
| 4.2 | Cliff setup and prediction | P02 | 3.5 |
| 4.2 | Target and reset exercise | P03, P03a | 4 + 2 |
| 4.2 | Route returns | P04 | 4 |
| 4.2 | Curve interpretation and comparison question | P05 | 6 |
| 4.2 | Debug one loop | P06 | 5 |
| 4.2 | Diagnose learning behaviour | P07 | 5 |
| 4.2 | Data-access revisit | P08 | 3 |
| 4.2 | Project example and protected activity | P09, P09a | 3 + 12 |
| 4.2 | Synthesis and Week 5 | P10 | 2 |
| | **4.2 teaching targets sum to** | | **53** |
| 4.2 | Administration, instructor-led | P11 | 5 |

Budget: each session has `70 × 0.85 = 59.5` usable minutes. Targets are 57.5 and 58 including administration: **115.5 total**, leaving 3.5 usable minutes unallocated plus 21 minutes of configured slack. Accepted allocations remain 58 and 53 + 5. No delivery allowance is used. Protect the ten-minute target exercise, six-minute cliff exercise and fifteen-minute project activity; notes are included in these targets. Arithmetic fit is not proof of delivery feasibility.

## Common example specifications

**2×2 grid (4.1).** Coordinates are `(horizontal, vertical)`: top row `(1,2), (2,2) goal`; bottom row `(1,1), (2,1)`. Four intended actions: up, right, down, left. An intended move occurs with probability 0.8, each perpendicular slip with probability 0.1; an attempted move outside the grid leaves the state unchanged. Entry to the goal gives **+1 total**, other transitions −0.04; the goal terminates, continuation zero; γ = 0.5. These are the accepted Bellman grid's rules. They are available for instructor checking; learners need only the supplied transitions for the updates. On grid diagrams show coordinates, goal, action arrows and γ; do not repeatedly reteach the full model.

**Cliff (4.2).** A separate 4-row × 12-column deterministic task. For the worked calculation use coordinates with bottom row 0 and left column 0: start `(0,0)`, goal `(11,0)`, cliff cells `(1,0)` through `(10,0)`. Four actions move one cell; walls leave the agent in place. Every ordinary transition, including goal entry, gives −1. Stepping into the cliff gives **−100 total** and places the agent back at start **within the same episode**. Only the goal terminates. γ = 1, ε = 0.1. A reset caused by a fall is not a terminal event. Label this as a different task before changing γ or rewards.

## C00 — Model-free control

**Time:** 0.5 minutes. **Reuse:** old P1 title layout, replacing its text.

**Display**

COMP438/538 Reinforcement Learning  
**Model-Free Control**  
Barış Akgün · Fall 2026

**Notes:** One deck for both sessions. Today: learning to improve behaviour from experience. No extra agenda catalogue.

## C01 — What changes when we want better behaviour?

**Time:** 2 minutes. **Reuse:** old P7's prediction/control contrast; replace its algorithm list with these lines.

**Display**

- With a model: evaluate a policy, then improve it.
- Last week: evaluate a fixed policy from experience.
- Today: use experience to improve the policy too.

**Question:** Which half of generalized policy iteration did we hold fixed last week?

**Notes:** Answer: policy improvement; the acting policy stayed fixed while we learned its values. MC, TD, n-step and forward λ gave ways to form prediction targets. Today's additional questions are which actions receive data and whose future behaviour a control target represents. Do not repeat λ formulas, trace mathematics or the policy-improvement proof. The average-reward contrast introduced no control algorithm.

## C02 — How could we learn to act without the model?

**Time:** 3 minutes. **Reuse:** old P4–5's motivation in notes; add the editable familiar grid.

**Display**

Grid caption: **Model hidden. The agent now chooses its actions.**

1. What should the agent learn so it can choose better actions?
2. How do its choices affect the data it will see?

**Notes:** Allow about two minutes for suggestions, one to organize them. Expected answers: estimate outcomes/returns for actions; try alternatives; exploit good estimates; improve as evidence arrives. Learning a dynamics model is another valid route, revisited later; this deck learns action values directly. A simulator may supply experience without the learner using a transition model. No “online = RL, offline = planning” distinction. Return to students' exploration suggestions in C06–C08.

## C03 — Why learn action values?

**Time:** 3 minutes. **Reuse:** old P10's native lookahead/argmax equations, edited to course notation and the following forms. Remove the claim that MC and TD inherently estimate only state values.

**Display**

With state values, greedy improvement needs the model:

\[
\pi'(s)=\arg\max_{a\in\mathcal A(s)}\left[\mathcal R(s,a)+\gamma\sum_{s'\in\mathcal S^+}\mathcal T(s,a,s')v^\pi(s')\right].
\]

With learned action values, choose directly from the table:

\[
\pi'(s)=\arg\max_{a\in\mathcal A(s)} Q(s,a).
\]

**q^π(s,a): take action a now, then follow π.**  
**Q(s,a): our estimate. We need evidence about actions, not just states.**

**Notes:** Recall the meaning before reading the equations. The state-value MC/TD versions taught last week do not give an action comparison without a model; their sampling ideas can be used to estimate Q instead. Q does not replace exploration or supply values for untried actions by magic. A finite noisy table is not the true q^π. Terminal state value in the first equation is zero. Source: book §5.2 opening, PDF118; Silver PDF8.

## C04 — Evaluation and improvement interleave

**Time:** 2 minutes. **Reuse:** old P8/P13 GPI diagram; replace labels and remove the proof/coverage claim.

**Display**

**Collect experience with π → update Q from returns → change π using Q → collect more experience.**

- Evaluation changes the estimates.
- Improvement changes the policy being evaluated.
- We need not finish evaluation before changing the policy.

**One noisy update is not a guarantee of improvement.**

**Notes:** The improvement theorem concerns true values under the evaluated policy. It motivates the direction of improvement; it is not a guarantee for each sample update. Policy and estimates form moving targets for each other. An episode's return reflects the policy that generated that episode; averaging returns from changing policies is not exact evaluation of the newest policy. Keep this qualification short; no theorem or convergence proof. Source: book §§5.3–5.4, especially printed p. 103 / PDF125.

## C05 — Trace one Monte Carlo control cycle

**Time:** 3 minutes. **Reuse:** old P13/P17 cycle; new editable table with the previously used episode. No new sampled data or performance claim.

**Display**

**New Q table, initially zero.** Hold the collecting policy fixed during this episode:

`(1,1) → (1,1) → (1,2) → goal`, taking **right** each time; γ = 0.5.

| Time | State-action pair | Reward | Supplied return |
| --- | --- | ---: | ---: |
| 0 | ((1,1), right) | −0.04 | 0.19 |
| 1 | ((1,1), right) | −0.04 | 0.46 |
| 2 | ((1,2), right) | +1 | 1 |

**First-visit averaging: which returns enter the table?**

Reveal: `Q((1,1), right) = 0.19`; `Q((1,2), right) = 1`.  
The repeated first pair is skipped; unvisited entries remain zero.

**Notes:** One minute setup, one for responses, one for interpretation. These are the first included samples for the two pairs, so each sample average equals its first return. First visit means first **state-action-pair** visit in this episode, not first visit ever. No constant-α rule is mixed into this example. A collecting policy may try other actions even though this particular trajectory contains only right; this is the familiar episode used for mechanics, not evidence of broad exploration. After the episode we can change the policy to favour larger Q. This does not prove right is best, and is not a conversion of the old V table into Q. Sources: old P13/P17; book §5.4 algorithm, PDF123.

## C06 — Would pure greediness find the better action?

**Time:** 3 minutes. **Reuse:** old P13's “would this work?” question; replace the generic failure explanation with a new snapshot at `(2,1)` on the same grid.

**Display**

**Separate hypothetical snapshot at (2,1)**

| Action | up | right | down | left |
| --- | ---: | ---: | ---: | ---: |
| Current Q | 0 | 0.12 | 0 | 0 |
| Tried here? | no | yes | no | no |

**A greedy choice is right. What would make the learner try up?**

Reveal, labelled **known-model reference from Week 2, not supplied to the learner**:

`q^π((2,1), right) ≈ 0.116`  
`q^π((2,1), up) ≈ 0.800`, with π = always-right thereafter.

**An untried action's initial estimate is not evidence that it is poor.**

**Notes:** This is a new illustrative snapshot, not the result of C05, which never visited `(2,1)`. Values compare different first actions under the same continuation. Greed can prevent collecting useful evidence; this is not a proof the learner must remain stuck forever. Noisy sampled updates can lower the current winner and cause a switch. With negative living rewards, zero initialization can itself encourage untried actions. Do not turn that observation into the Week 9 optimism lesson. The up/right tie at `(1,1)` is why the diagnostic example uses `(2,1)`. Sources: old P13/P18; accepted Bellman B14 reference.

## C07 — Exploration and exploitation

**Time:** 2 minutes. **Reuse:** old P14's restaurant-choice cartoon, unchanged, retaining source attribution if present. Add the short labels below without crowding the image.

**Display**

**Exploit:** choose what current estimates say is good.  
**Explore:** obtain evidence that could change those estimates.

Ways to obtain action coverage:
- Start episodes at different state-action pairs, when the system allows it.
- Keep a chance of trying other actions while acting.

**Notes:** The cartoon contrasts a familiar restaurant with an untried one; exploratory choices can cost reward now. Exploring starts is an assumption used in MC control development, not a capability every robot has. Epsilon-greedy will implement the second option. Nonzero action probabilities at a visited state do not promise every state will be reached in a finite run. Source: old P14; book §§5.3–5.4. Spend about one minute on the trade-off, one on coverage.

## C08 — Epsilon-greedy action selection

**Time:** 3 minutes. **Reuse:** old P15's native equation, corrected to action-set notation and the explicit random-branch rule. Remove any implication the random branch excludes the greedy action.

**Display**

- With probability **1 − ε**, choose a maximizing action; break ties uniformly at random.
- With probability **ε**, choose uniformly from **all** available actions.

For a unique maximizing action:

\[
\pi(a\mid s)=\begin{cases}1-\varepsilon+\varepsilon/|\mathcal A(s)|,&a\text{ is the unique greedy action},\\\varepsilon/|\mathcal A(s)|,&\text{otherwise}.\end{cases}
\]

**Question:** Four actions, ε = 0.1, one maximum: what are the probabilities?

Reveal: **0.925 for the maximizing action; 0.025 for each other action.**

**Notes:** Spend a minute on the two branches, a minute calculating, a minute on ties. With multiple maxima, divide the greedy-branch mass uniformly among them and still add the random-branch probability to every action. With a zero table and four actions, each has probability 0.25. This differs from a fixed tie order in exact DP to avoid systematically favouring one action when ties reflect no data. Epsilon-soft means each action receives at least ε divided by the number of actions; epsilon-greedy places the remaining mass on maximizers. No new counter or decay formula. Sources: book §5.4 PDF122; old P15.

## C09 — On-policy Monte Carlo control

**Time:** 2 minutes. **Reuse:** old P17 loop, rewritten as editable text; old P16's result stated in words only. No proof slide.

**Display**

1. Initialize Q and an epsilon-greedy policy, ε = 0.1.
2. Generate a complete episode with this policy held fixed.
3. For each pair's first visit, add its return to that pair's samples and set Q to their average.
4. Make the next episode's policy epsilon-greedy with respect to the updated Q.
5. Repeat.

**Exact-value guide:** epsilon-greedy improvement using true q^π is no worse than the epsilon-soft policy π being evaluated.  
**Sampled updates can be noisy; they do not inherit a per-update guarantee.**

**Notes:** Connect the steps to C05 and C08, rather than tracing another episode. C05 and this loop use the same first-visit sample-mean estimator. No separate MC-control implementation requirement. Exact improvement is within the epsilon-soft policy class; fixed exploration retains exploratory cost. Do not assert this sampled, changing-policy loop converges merely because the exact result exists. Sources: old P16–18; book PDF123–125; review R12/R16/R20.

## C10 — Why wait for the episode to end?

**Time:** 2 minutes. **Reuse:** old P19's question, replacing windy gridworld with the accepted familiar-grid case. Native grid with left arrows in nonterminal cells.

**Display**

**Counterexample: deterministic always-left, ε = 0.**  
Starting at `(1,1)`, the agent stays in the left column and never reaches the goal.

**MC needs a completed return. TD can update during the episode.**

With fixed ε > 0, this grid terminates with probability 1—but MC still waits for completion.

**Notes:** Intended left bumps the wall; perpendicular slips only change vertical position in the left column. This is not the epsilon-greedy MC policy on C09. Positive fixed exploration repairs this specific nontermination case; it does not make the episode-end update immediate. TD can learn during long episodes, which is the general motivation. Do not claim SARSA escapes every bad initialization or policy. No windy-grid setup or plot is required. Source: old P19/P25's teaching purpose; book Example 6.5 PDF152; D2 and R19.

## C11 — SARSA: a sampled action-value target

**Time:** 6 minutes. **Reuse:** old P21/P23 native update equations, corrected to `R_{t+1}`, `Q` and `U_t`; delete Expected SARSA and the convergence schedule. Build the derivation progressively.

**Display**

For a fixed π, recall the action-value Bellman expectation equation:

\[
q^\pi(s,a)=\mathbb E_\pi\!\left[R_{t+1}+\gamma q^\pi(S_{t+1},A_{t+1})\mid S_t=s,A_t=a\right].
\]

Observe the next transition, choose the next action using π, and use current estimates:

\[
U_t=R_{t+1}+\gamma Q(S_{t+1},A_{t+1}),
\qquad Q(S_t,A_t)\leftarrow Q(S_t,A_t)+\alpha[U_t-Q(S_t,A_t)].
\]

**S–A–R–S–A:** `(S_t, A_t, R_{t+1}, S_{t+1}, A_{t+1})`.

**Terminal next state:** `U_t = R_{t+1}`; no next action is needed.

**Notes:** Two minutes recall the meaning, two derive the sample/estimate replacement, two discuss what must be available. The successor action is an actual choice from the behaviour policy, not an argmax substituted after sampling. In control, π is epsilon-greedy in the evolving Q table; evaluation and improvement interleave. For a fixed table the sample target has a conditional expectation determined by that table and policy; it need not equal the true value when Q is inaccurate. “Sampled Bellman target” is not a claim that the bootstrap is unbiased for the true q^π. This is on-policy because the continuation follows the acting policy. Sources: book §6.4 eq. 6.7, PDF151; Sutton slides PDF34–35.

## C12 — Trace the SARSA loop

**Time:** 3 minutes. **Reuse:** old P23's algorithm structure and native equation; replace both old prose variants and the P24 raster with one editable box.

**Display**

Initialize Q for nonterminal pairs. For each episode:

1. Observe S₀; choose A₀ epsilon-greedily from Q.
2. Execute A_t; observe R_{t+1} and S_{t+1}.
3. If terminal: use `U_t = R_{t+1}`. Otherwise choose **A_{t+1}** epsilon-greedily and use `U_t = R_{t+1} + γQ(S_{t+1}, A_{t+1})`.
4. Update `Q(S_t,A_t) ← Q(S_t,A_t) + α[U_t − Q(S_t,A_t)]`.
5. If terminal, end the episode. Otherwise advance one step and **execute the already-selected A_{t+1}**.

**Question:** Where are exploration and improvement happening?

**Notes:** Exploration occurs in the epsilon-greedy action choice; as Q changes, future epsilon-greedy choices change. The action selected in step 3 is retained; do not draw another action before execution. On a self-transition the table may change before that action is executed; preserve the algorithm's ordering. Terminal initialization can be represented by zero continuation, but an implementation need not invent an action at the terminal. Convergence qualifications are kept to P07. Source: book algorithm, printed130/PDF152; R14.

## C13 — Q-learning: sampled Q-value iteration

**Time:** 3 minutes. **Reuse:** old P40/P41 equations, edited; recall Q-value iteration from Week 2 without replaying its worked example.

**Display**

With a model:

\[
Q_{k+1}(s,a)\leftarrow\mathcal R(s,a)+\gamma\sum_{s'\in\mathcal S^+}\mathcal T(s,a,s')\max_{a'\in\mathcal A(s')}Q_k(s',a').
\]

With one sampled transition:

\[
U_t=R_{t+1}+\gamma\max_{a\in\mathcal A(S_{t+1})}Q(S_{t+1},a),
\qquad Q(S_t,A_t)\leftarrow Q(S_t,A_t)+\alpha[U_t-Q(S_t,A_t)].
\]

**Act exploratorily; compute a greedy continuation in the target.**

**Notes:** The first line is a recalled nonterminal lookahead; the contribution of a terminal successor is defined as zero, without taking a maximum over an empty action set. The sampled rule is also shown for a nonterminal successor; C13a gives the terminal branch. k counts DP sweeps, t counts environment steps. The observed next state is still random; taking a maximum over actions does not remove transition uncertainty or erase the observed reward. This is the Bellman optimality target, unlike SARSA's sampled behaviour continuation. Sources: old P40–41; Abbeel PDF5–7; book eq.6.8 PDF153.

## C13a — Q-learning still needs an acting policy

**Time:** 3 minutes, within C13. **Reuse:** old P42's algorithm content as new editable text, with the native update from P40. Do not reuse its raster box as the main text.

**Display**

Initialize Q. For each episode:

1. Observe the current nonterminal state S_t.
2. Choose and execute A_t **epsilon-greedily** from Q.
3. Observe R_{t+1}, S_{t+1}.
4. If terminal, `U_t = R_{t+1}`. Otherwise, `U_t = R_{t+1} + γ max_a Q(S_{t+1},a)`.
5. Update `Q(S_t,A_t) ← Q(S_t,A_t) + α[U_t − Q(S_t,A_t)]`.
6. If terminal, end the episode; otherwise advance and choose the next **behaviour** action.

**The action used in the maximum need not be the action executed next.**

**Notes:** Have students point to data collection and target computation. Q-learning aims at q^*, while the behaviour policy determines which pairs receive updates and how efficiently learning progresses. Finite-tabular convergence requires continued coverage and suitable step sizes; it is not true for arbitrary finite datasets or every constant-step run. The behaviour need not become greedy merely to estimate optimal action values under the relevant conditions. Source: book §6.5, PDF153; old P43 qualified.

## C14 — Behaviour and target policies

**Time:** 2 minutes. **Reuse:** old P6/P32 definitions and P40's no-IS remark, replaced with this table and explanation.

**Display**

**Behaviour b generates actions in the data. Target π describes the continuation being learned about.**

| Method | Behaviour | Continuation in the target |
| --- | --- | --- |
| SARSA | epsilon-greedy | the same acting policy: sampled next action |
| Q-learning | epsilon-greedy here | greedy continuation: maximum next-action value |

**Why no importance ratio in this one-step Q-learning target?**  
We condition on the action already taken and compute the successor maximum.

**Notes:** One minute for the table, one for the explanation. Given `(S_t,A_t)`, the transition sample comes from the same environment dynamics regardless of how the behaviour selected that pair. There is no successor behaviour-action sample being substituted for a different target-action average: we compute the maximum. This is a one-step statement, not a rule that all off-policy learning needs no correction. Ratios are studied in Week 8. Off-policy need not mean optimal target in general, and it need not mean fixed data. Sources: old P6/P32/P40, book §§5.5/6.5; R04.

## C15 — Your turn: one transition, two targets

**Time:** 7 minutes, first part of the ten-minute activity. **Reuse:** old P21/P40 target equations; new grid and editable tables. This is a fresh illustrative Q snapshot, not a learned table from earlier slides.

**Display**

`γ = 0.5`, `α = 0.5`, `Q((1,1), right) = 0.1`.

| Action at (1,2) | right | up | down | left |
| --- | ---: | ---: | ---: | ---: |
| Q | 0.8 | 0.2 | 0.1 | 0 |

Observed transition: **(1,1), right, −0.04, (1,2)**.  
The next epsilon-greedy action is **up**.

1. Calculate each target and the updated entry for SARSA and Q-learning.
2. Which next action does each target use?
3. When can the two targets agree?

**Separate terminal case — reset the exercise:** `(1,2), right, +1, goal`. What is each target?

**Notes:** Two minutes to identify the entries, five for students to compute and explain. Both methods start from the same snapshot; never apply the second method to the first method's updated entry. The right action at `(1,1)` can reach `(1,2)` by a perpendicular slip, so the observed transition is valid. The terminal case is an independent transition, not the next step after selecting up. Keep the answer hidden until C15a. Source: accepted exercise; R14.

## C15a — Compare the updates

**Time:** 3 minutes, remainder of C15. **Reuse:** native target/update equation forms from P21/P40; show substituted numbers in editable math.

**Display**

| | SARSA | Q-learning |
| --- | --- | --- |
| Continuation | Q((1,2), up) = 0.2 | max Q((1,2), ·) = 0.8 |
| U_t | −0.04 + 0.5 × 0.2 = **0.06** | −0.04 + 0.5 × 0.8 = **0.36** |
| Updated Q((1,1), right) | 0.1 + 0.5(0.06 − 0.1) = **0.08** | 0.1 + 0.5(0.36 − 0.1) = **0.23** |

**Same snapshot, same observed reward and next state; different continuation.**

Separate goal transition: **both targets are 1**, with zero continuation.

**Notes:** Ask for the reasoning, not just the arithmetic. On this nonterminal example, the targets agree if the sampled next action has the maximum Q value, including a tie. In general γ = 0 also removes the continuation difference. A coinciding target does not make whole learning trajectories identical: action ordering and later estimates still matter, especially on self-transitions. The terminal target is 1, not the previous table's goal estimate or a bootstrapped extra reward.

## C16 — What is each update trying to learn?

**Time:** 3.5 minutes. **Reuse:** old P50–51 comparison purpose, rebuilt as one native table. No copied future-method columns or extra numerical table.

**Display**

| Method | Update target | Continuation represented | DP connection |
| --- | --- | --- | --- |
| MC control | G_t | episode's collecting policy | evaluation/improvement idea; complete return |
| SARSA | R_{t+1} + γQ(S_{t+1},A_{t+1}) | behaviour policy | sampled action-value evaluation plus improvement |
| Q-learning | R_{t+1} + γ max_a Q(S_{t+1},a) | greedy continuation | sampled optimality backup |

**SARSA estimates action values for the policy it follows. Q-learning aims at optimal action values while exploring.**

**Notes:** Two minutes read the contrasts, 1.5 minutes interpret. All rows use the common update form, but targets are not the only difference: MC waits for the episode and uses its declared visit/averaging convention. With control, policies and estimates change together. The DP column is a conceptual connection, not an equivalence of update schedules or an extra algorithm. MC's full-return target has no one-step DP counterpart. Terminal continuation is zero in the TD rows.

Reference numbers **in notes only**: for the accepted grid and fixed epsilon-greedy policy around up/up/right with ε = 0.1, q^π at the greedy pairs is 0.341369, 0.849121, 0.849121 in state order `(1,1),(2,1),(1,2)`; q^* at those same pairs is 0.361818, 0.852727, 0.852727. These are model-computed reference values, not a learning experiment. The values 0.331793/0.810622/0.810622 instead average over the first action and are v^π, so do not label them Q. The two reference policies have the same greedy actions; finite learning need not produce identical behaviour. No guarantee for constant α follows. Sources: book §§5.4/6.4/6.5; R15–R16.

## C17 — From target differences to behaviour

**Time:** 1.5 minutes. **Reuse:** old P20/P45 recap function; replace the old text/placeholder.

**Display**

- Q lets us compare actions without a transition model.
- Exploration determines which estimates receive evidence.
- SARSA and Q-learning use different future-action assumptions.

**Next question: can the better greedy path earn worse rewards while exploring?**

**Notes:** Ask one student to distinguish the next-action assumptions, then leave the question for 4.2. This is the session boundary. Do not start the cliff setup in this allocation or move unfinished slides into 4.2's budget.

## P00 — When exploration has a cost

**Time:** 0.5 minutes. **Reuse:** new section opener, retaining the deck's style. No second course title.

**Display**

**When exploration has a cost**  
Control targets, behaviour and evidence

**Notes:** Start session 4.2. Today: interpret a target difference, diagnose behaviour, and choose a meaningful project comparison.

## P01 — Which continuation does the target use?

**Time:** 3 minutes. **Reuse:** C15's target distinction with a fresh small numerical retrieval, not a full repeat of its update exercise.

**Display**

A nonterminal transition gives reward 0. The chosen next action has Q = 2; the largest next-action value is 5. Let γ = 0.5.

**Which target is SARSA's, which is Q-learning's, and why?**  
Candidates: **1** and **2.5**.

**Notes:** One minute pair responses, two for reasoning and connection. SARSA uses 1, from the sampled behaviour action; Q-learning uses 2.5, from the maximum. Neither can choose which next state was sampled. On a terminal transition both would use reward 0 alone. This abstract retrieval does not change the familiar grid's rewards or pretend to be a new grid transition.

## P02 — Cliff walking: predict before seeing the result

**Time:** 3.5 minutes. **Reuse:** old P44's cliff-task image only, enlarged. Hide the learning curve until P05; retain the safer/shorter paths but initially hide their method attribution. Add the exact task rules in editable text.

**Display**

**A different task:** deterministic movement; four actions; γ = 1; ε = 0.1.

- Ordinary transition: −1, including arrival at the goal.
- Fall: −100 and return to start; **the episode continues**.
- Only the goal terminates.

**Vote:** Which path would you expect from each method? Which earns more reward while exploring?

**Notes:** About two minutes rules, 1.5 minutes vote. Distinguish random action selection from stochastic dynamics: here actions have deterministic consequences, unlike the earlier slip grid. A fall is not a terminal transition. The pictured shorter route takes 13 moves from start to goal; the top route takes 17 without exploration. Do not reveal the curve or claim a universal algorithm ranking. Source: book Example 6.6, printed132/PDF154; old P44/PDF40.

## P03 — Work a target beside the cliff

**Time:** 4 minutes, first part of the six-minute exercise. **Reuse:** P44 task diagram with the transition highlighted, plus editable sample table. New illustrative Q snapshot, not a converged table.

**Display**

On the cliff diagram, label the bottom row 0 and left column 0. Observe:

**(1,1), right, −1, (2,1)**; the selected next action is **down**.

`γ = 1`, `α = 0.5`, `Q((1,1), right) = −20`.

At `(2,1)`: **Q(down) = −113; max_a Q(a) = Q(right) = −10**.

**Compute each target and the updated Q((1,1), right).**

Reveal:
- SARSA: `U_t = −1 − 113 = −114`; updated Q = **−67**.
- Q-learning: `U_t = −1 − 10 = −11`; updated Q = **−15.5**.

**Notes:** One minute setup, two work, one explanation. At `(2,1)`, down enters the cliff; −113 is a supplied action-value estimate containing future return, **not the reward already observed**. It is interpretable as −100 plus a −13 continuation from start; that does not make the whole snapshot exact or a converged SARSA table. Optional complete successor row for notes: right −10, up −12, left −12, down −113. The common current value −20 is an in-progress estimate. The next slide actually executes the selected down action to make reset handling concrete. Sources: R06/R17; book eqs.6.7–6.8 and Example6.6.

## P03a — A fall resets the state, not the episode

**Time:** 2 minutes, remainder of P03. **Reuse:** same diagram, showing a reset arrow to start. Reuse P40's target equation with the correct observed reward.

**Display**

Now execute the selected **down** action: observe **−100**, next state **start**.

**Q-learning's target:**
\[
U_t=-100+\max_a Q(\text{start},a).
\]

**SARSA's target:** −100 plus Q at the next action selected from start.

**Question:** Is the continuation zero?

Reveal: **No. The goal, not a fall, terminates this task.**

**Notes:** Use a fresh local time t for this new update; this updates the pair at the cliff edge, not the earlier pair in P03. Both methods use the observed fall penalty. Q-learning omits averaging over the next exploratory action, not actual rewards or environment risk. An independent goal transition gives target −1 for both methods. This contrast is why the illustration used −113 rather than encouraging the interpretation that a fall must have value exactly −100. No additional arbitrary start Q values are needed to make the reset point.

## P04 — Compare fixed policies around the routes

**Time:** 4 minutes. **Reuse:** old P44 task diagram, with edge/top routes distinguished. Add the instructor-approved editable numbers; do not use a new simulated curve.

**Display**

**Fixed-policy expected returns from start**  
Exact model calculations for the policies below; γ = 1, ε = 0.1.

| Policy | Expected episode return |
| --- | ---: |
| Epsilon-greedy around the edge route | **≈ −52** |
| Epsilon-greedy around the top route | **≈ −22** |
| Greedy edge route, no exploration | **−13** |

**A shorter greedy route can be worse when exploration continues.**

**Notes:** A minute for routes, a minute for the comparison, two to connect targets to behaviour. These are evaluations of fixed policies, not SARSA/Q-learning learning curves or guaranteed limiting values of constant-step runs. At a cell immediately above the cliff, with down nongreedy, the random branch selects down with probability 0.1/4 = 0.025. The risk compounds over repeated visits and falls reset without ending the episode; do not compute the episode cost as simply 0.025 times 13 steps.

Full policy specification for reproducibility: use the cliff coordinates in the common specification. For the edge policy, the travel row is 1; for the top policy it is 3. In the last column choose down. In all other columns choose up below the travel row, right on it, and down above it. This defines a designated greedy action at every reachable nonterminal state, including states away from the pictured route. Assign it probability 0.925 and each other action 0.025; the random branch may also choose it. The goal has zero continuation, falls give −100 and reset to start, and ordinary/goal-entry rewards are −1. Linear policy evaluation gives −51.813188 and −22.272817; the deterministic edge policy returns −13. These are designated fixed policies, not an invocation of random tie-breaking on an unspecified Q table. For reference only, optimizing over epsilon-soft policies on this task gives start value approximately −20.707677; keep it in notes, not as another displayed comparison.

SARSA's sampled continuation reflects the behaviour policy's exploratory costs; Q-learning's maximum represents greedy continuation. Repeated backups propagate those differences to earlier choices. If asked about motion slips: optimal values change and the preferred route **can** change, depending on probabilities/costs; no unconditional route-switch claim. D4 controls display of these numbers; sources: book Example6.6 and §5.4 epsilon-soft construction; review's independent computations.

## P05 — What did the learning curve measure?

**Time:** 6 minutes. **Reuse:** old P44's published learning-curve image, enlarged, preserving axes and method labels. Caption it separately from P04's computed values; no invented error band or rerun claim.

**Display**

Caption: **Sutton & Barto, Example 6.6: reward during exploratory learning, ε = 0.1.**

**Which question are we asking?**
- How much reward is collected while learning?
- How good is the final greedy policy in separate evaluation?
- How many falls occur during learning?

**A simulator where only the final policy matters; a robot learning near stairs; a policy trained in simulation for deployment. Would you report the same measure?**

**Notes:** Two minutes read the plot, two discuss cases, two explain. Horizontal axis is episodes, vertical axis sum of rewards during each episode: a control measure, not prediction RMS error. The shown SARSA curve is less negative than Q-learning's during exploratory learning. A greedy policy extracted from Q-learning can take the shortest path without its training exploration, which is a different evaluation condition. The historical curve is an illustration, not a multi-seed uncertainty estimate or proof of a universal winner; do not claim these data establish which learns the optimal path faster. P04's exact-policy numbers explain the scale but are not a reproduction of this learning trace.

Possible answers: final greedy return is central in the simulator-only case; online falls/reward matter for the learning robot; simulation-to-deployment also requires representative evaluation dynamics and explicit exploration choices. A simulator success alone does not establish physical deployment performance. Distinguish learning run variability from evaluation variability, freeze updates for evaluating a learned policy, and state whether exploration is enabled. Match training interaction budgets and separate tuning from final comparisons. Sources: old P44; book Example6.6; mc_td MTE1–MTE2 continuity.

## P06 — Debug one shared control loop

**Time:** 5 minutes. **Reuse:** editable loop text from C12/C13a, with three short deliberately incorrect excerpts. Label them **bugs**, not alternative algorithms.

**Display**

**For each bug, name the mismatch and repair it.**

| Bug | What happens? |
| --- | --- |
| SARSA chooses A_{t+1} for its target, then draws another action to execute. | ? |
| Q-learning always executes the maximizing target action instead of its intended epsilon-greedy behaviour choice. | ? |
| A goal transition includes γ times an initialized terminal Q value. | ? |

**Notes:** Three minutes pair reasoning, two answers. (1) The target's sampled action no longer matches the action used for the next step; retain and execute the selected A_{t+1}. (2) This silently changes the behaviour to greedy, potentially losing coverage; compute the max for the target but choose behaviour actions separately. Greedy behaviour is not categorically an invalid Q-learning update; it is a bug relative to the intended exploratory loop and cannot supply a general coverage guarantee. (3) True termination has zero continuation; use only the observed reward. In the cliff example a fall is not termination. Do not add time-limit/truncation API conventions as a new lesson. These checks prepare A1's common loop without adding a new assignment requirement.

## P07 — Diagnose what is fluctuating

**Time:** 5 minutes. **Reuse:** old P18/P43 caveats and P53's exploration question; replace unconditional claims with the symptom/check table. No algorithm catalogue.

**Display**

| Observation | What would you check? |
| --- | --- |
| Some actions have no data | State-action visits and exploration |
| Good greedy evaluation, poor training reward | Exploratory cost; whether evaluation freezes learning |
| Episode returns fluctuate | Action/environment randomness; compare Q and policy changes separately |
| Q estimates keep changing substantially | Step sizes, target correctness, visitation and changing policy |
| One run looks better | Repeated runs, tuning effort and interaction budget |

**Coverage and suitable step sizes matter. A noisy return curve alone does not diagnose nonconvergence.**

**Notes:** Two minutes students choose a check, three for explanations. Constant ε keeps behaviour exploratory, even if the table and greedy policy are stable; constant α can retain estimate noise. Do not automatically prescribe decaying ε when ongoing exploration is deliberate. For standard tabular optimality claims, every relevant pair must keep receiving updates and step sizes must shrink appropriately. SARSA's usual optimality conditions also make behaviour greedy in the limit; Q-learning need not make its behaviour greedy to estimate optimal action values. A schedule name alone does not prove coverage. Finite data, initialization and reward validity also matter. Brief pointer only: smarter exploration returns in Weeks 9/11; maximization bias in 6.2; approximation changes the stability story in Week 5. No proof, formulas for schedules or new assessed method.

## P08 — Learning from someone else's data

**Time:** 3 minutes. **Reuse:** old P6/P32 policy distinction and current mc_td MT03's conceptual table; create editable text rather than copying its deck.

**Display**

| Question | Distinction |
| --- | --- |
| Are we using a transition model in the update? | Model-based / model-free |
| Can we gather more interaction? | Online / fixed-data offline |
| Does behaviour match the target policy? | On-policy / off-policy |

**Q-learning can use transitions from another behaviour policy. This does not supply missing state-action experience.**

**Question:** If an action never appears in the dataset, what evidence updates its tabular Q entry?

**Notes:** Answer: none; its entry can retain an unsupported initial value, and a max can select it. Off-policy does not imply an unlimited fixed dataset can support every target. We may collect fresh off-policy experience or use old data; the axes are distinct. A dataset collected under the target policy can be on-policy despite being fixed. Keep this a taxonomy/coverage revisit; detailed fixed-data failures and methods belong to Week 12, and the approximation interaction to Week 5. Sources: accepted `prediction` revisit, old P32/P40.

## P09 — A meaningful project comparison

**Time:** 3 minutes, first part of the protected fifteen-minute activity. **Reuse:** new native table, grounded in the accepted activity and project evaluation scope. No proposal deadline or calendar framing.

**Display**

**Example question:** Which learner incurs fewer falls during a fixed amount of cliff interaction?

| Item | Example plan |
| --- | --- |
| Compared methods | Q-learning versus SARSA baseline |
| Primary metric | Number of training falls within the interaction budget |
| Secondary question | Frozen greedy-policy return, stopping at the goal or after 200 transitions |
| Per-run budget | 10,000 environment transitions per method |
| Repetitions | Three independent training runs per method |
| Separate evaluation | 20 rollouts per trained policy from start; no updates, ε = 0; report how often the cap is reached |

**Same number of episodes need not mean the same amount of interaction.**

**Notes:** This is a hypothetical small planning example, not an assigned experiment, recommended universal run count or reported result. Other defensible primary measures include accumulated training reward. Falls reset the state but remain within an episode; use transitions to count interaction. Three seeds count independent runs, not a guarantee of precision. Evaluation retains uniform random tie-breaking among maxima, with no exploratory branch. With unique maximizing actions in this deterministic task, repeated rollouts from the same start may repeat; variability across separately trained policies still matters. The declared evaluation cap keeps an unsuccessful greedy policy from running forever; the measured return is capped, unlike P04's full-episode expectation. Report cap hits separately. No training terminal-handling convention is changed. For real projects, adapt initial conditions/evaluation to the question. Separate hyperparameter tuning from the final runs and report computation as relevant. Do not infer deployment safety or robust uncertainty from these small counts. Sources: accepted evaluation scope, D3, R22.

## P09a — Choose your baseline, metric and budget

**Time:** 12 minutes, remainder of P09. **Reuse:** new editable activity template. Leave the prompt visible during the work and reports.

**Display**

**Eight minutes, with your team or a partner:** use a candidate project, or use cliff walking if needed.

1. What question are you trying to answer? What does the agent control?
2. What simple baseline would make the comparison informative?
3. What is the primary metric, and when is it measured?
4. What interaction/computation budget and repeated runs are feasible?
5. What result would *not* support your claim?

**Four minutes: share and challenge two or three plans.**

**Notes:** The activity chooses a comparison, not a required new handout or submission. A random or heuristic baseline may be more informative than another RL algorithm. A baseline must address the same task/objective; compare budgets and distinguish training behaviour from frozen evaluation. Ask whether the metric reflects the stated question, whether tuning reuses the final evidence, and whether a negative result would still be informative. Students need no implementation or complete proposal. Example challenge: fewer falls after fewer interactions is not evidence of greater learning efficiency; better greedy return does not establish fewer training failures. The instructor handles project timing separately under D3; do not frame this as before/after a specific deadline. Preserve all fifteen minutes across P09/P09a.

## P10 — From tables to generalization

**Time:** 2 minutes. **Reuse:** old P45's recap purpose; new concise synthesis and Week 5 pointer.

**Display**

- Specify the policy represented by the target.
- Distinguish learned values, acting behaviour and the performance measure.
- Check coverage, terminal handling and comparison budgets.

**Next:** a separate estimate for every state-action pair is impractical in large spaces. How can experience generalize?

**Notes:** Ask for one example of confusing behaviour performance with the target policy's values. Then motivate approximation without a gradient update or an instability theorem. This is the end of the 53-minute teaching allocation.

## P11 — Course announcements and assignment questions

**Time:** 5 administrative minutes, separate from teaching. **Reuse:** new simple announcement slide, not old administrative dates.

**Display**

**Course announcements**

**A1 preparation:** planning backups, MC/TD prediction, and a shared SARSA/Q-learning control loop.

**Assignment and project questions**

**Notes:** Instructor-led logistics under D3. No release date, deadline, proposal-timing assumption or schedule change is printed. The instructor may use these minutes for A1 logistics and current questions. A1's accepted design is one supplied-MDP value-iteration solver with supplied policy-iteration comparison; MC/TD prediction kernels and supplied n-step/terminal checks; one epsilon-greedy control loop with two target choices. This is a scope reminder, not the assignment handout. No separate MC-control, lambda, Expected-SARSA or Double-Q implementation task is introduced. The possible release move mentioned by the instructor is not an accepted schedule change in this file.

## First-render handoff checks

- Render in the listed order, with the C17/P00 session boundary. Stable IDs are in headers; suffix slides share the parent unit's time.
- Reuse old P44's two images separately: task diagram in P02/P04, learning curve in P05. Do not show the curve before the prediction vote or label P04's exact-policy values as learning results. Source caption is **Example 6.6**, not Figure 6.4.
- Check native equations, terminal branches, reward indices and random-tie wording. Keep C15's goal transition explicitly separate and P03a's fall explicitly nonterminal. Do not silently use old notes that contradict those conventions.
- Keep reference-value calculations and the best epsilon-soft cliff value in notes. Show D4's two route-return comparisons and greedy −13 reference initially. No hidden proof/reading dependency is introduced.
- Confirm timing and questions in notes; no automatic expansion beyond the accepted units. Layout may split a dense display only if its unit time and teaching purpose remain unchanged.
- At first render freeze this content file, update the deck decision file's workflow status, and generate review views through Claude's workflow. This file itself makes no claim about rendered visual quality, animations or acceptance of a future PPTX.
