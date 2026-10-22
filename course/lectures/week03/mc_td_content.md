# Model-free prediction — first-render content for session 3.1

**Frozen (historical):** first-render input for `course/lectures/week03/mc_td_claude.pptx`, rendered 2026-10-22. Not maintained: the PPTX is the source from that render on. Do not use this file to rebuild or overwrite the deck. Status: [deck decisions](../../../decisions/lectures/mc_td.md).

**Shared** by the instructor, Claude and ChatGPT. Prepared by ChatGPT, 2026-10-22, under [lecture workflow step 4](../../../docs/lecture_workflow.md), implementing [mc_td D1–D8](../../../decisions/lectures/mc_td.md) and the resolved [mutual review](../../../analysis/lecture_suggestions/mc_td_review.md). **Deck status lives only in the deck decision file.** This file supplies the first render of the 3.1 portion of the combined `mc_td` deck. At that render, mark this input historical: the instructor-edited PPTX becomes the teaching source. Do not rebuild over it. Prepare/append 3.2 separately when authorized; no 3.2 slides are specified here.

## Rendering and source conventions

- The 15 accepted teaching units are retained in order. Units 8, 10 and 14 are split across slides for legibility, without adding time or content. All 19 slides below are live. Stable slide IDs are `MT00`–`MT14`, with suffixes for these splits.
- Use native editable PowerPoint equations from the old decks where available; correct them to the displayed equations below. Native equations use Accent 5 (`#4472C4`), per the accepted course convention. Use the [notation guide](../../notation_guide.md): `v^π` for the true value, `V` for estimates, `R_{t+1}` for the observed reward, `U_t` for a target, and `δ_t` only for TD error. Do not use DP sweep indices for MC/TD updates.
- “Display” specifies visible teaching content; “Notes” contains the required explanation, answers and timing cues. Count the required notes within the target. Keep prompts visible before answers. Use click reveals for the specified answers; if animation is impractical, reveal answer panels without adding separately timed teaching material. Do not shrink the exercise tables to fit extra prose.
- **P** below means `sources/current_course/4 - Model Free Prediction.pptx`, in presentation order, **59 slides**. Its PDF has **54 pages** and different numbering. Reuse references are PPTX slide numbers unless explicitly marked PDF. VFA means `sources/current_course/6 - Value Function Approximation.pptx`; its average-reward definition is **PPTX37 / PDF32**.
- Source paths/locators: [old prediction PPTX](../../../sources/current_course/4%20-%20Model%20Free%20Prediction.pptx); [old prediction PDF](../../../sources/current_course/4%20-%20Model%20Free%20Prediction.pdf); [old VFA PPTX](../../../sources/current_course/6%20-%20Value%20Function%20Approximation.pptx); [book](../../../sources/RLbook2020.pdf), §2.4–2.5 (incremental averages), §5.1 printed 92–93 / PDF114–115, §6.1 printed 119–123 / PDF141–145, §6.2 printed 124–126 / PDF146–148, §10.3 printed 249 / PDF271 and Exercise 10.6 / PDF273; [Silver lecture 4](../../../sources/silver_rl/lectures/lecture-4-model-free-prediction-.pdf), pp. 4–7, 11–16, 26–29; [CS234 lecture 3](../../../sources/stanford_cs234/lectures/lecture3post.pdf), pp. 10–29, 31–40. These are preparation references, not new assigned reading.
- The accepted [Bellman grid record](../../../decisions/lectures/bellman.md) supplies continuity. Recreate the simple grid natively from the specification below; no need to alter or rebuild the accepted Bellman deck. Old prediction slides remain the base for the new teaching content.

## Teaching order and targets

| Accepted unit | Slide IDs | Purpose | Minutes |
| --- | --- | --- | ---: |
| 1 | MT00 | Title | 0.5 |
| 2 | MT01 | Recall evaluation; hide the model | 4 |
| 3 | MT02 | Why use samples? | 3 |
| 4 | MT03 | Model, data and policy distinctions | 3 |
| 5 | MT04 | Shared observed trajectory | 2 |
| 6 | MT05 | MC and backward returns | 5 |
| 7 | MT06 | First versus every visit | 3 |
| 8 | MT07, MT07a | Incremental averaging and MC loop | 3 + 2 |
| 9 | MT08 | Driving home; motivate an earlier target | 5 |
| 10 | MT09, MT09a, MT09b | TD target, loop, driving-home arrows | 2.5 + 1.5 + 1.5 |
| 11 | MT10 | Protected MC/TD exercise | 9 |
| 12 | MT11 | Compare with model-derived values | 2.5 |
| 13 | MT12 | Sampling and bootstrapping | 4 |
| 14 | MT13, MT13a | Continuing service and objective contrast | 2 + 3 |
| 15 | MT14 | Exit check; 3.2 and control bridge | 1.5 |
| | | **Targets sum to** | **58** |

## MT00 — Model-free prediction

**Time:** 0.5 minutes. **Reuse:** P1 title layout; replace its course/instructor text with the following, preserving the course's established visual style.

**Display**

Reinforcement Learning  
**Model-Free Prediction**  
Barış Akgün · Fall 2026

**Notes:** This is the combined deck's title. Today is session 3.1: learning values from experience. Do not add a second title or an agenda catalogue before the problem.

## MT01 — Policy evaluation without the model

**Time:** 4 minutes. **Reuse:** P3 recap, P15's prediction question; replace repeated VI/PI details with the three lines below. Add the editable 2×2 grid.

**Display**

- With a model: evaluate a policy, then improve it.
- Today: evaluate the **same fixed policy** using observed experience.
- Next week: improve policies using experience.

Grid: upper row `(1,2)` and `(2,2): goal`; lower row `(1,1)` and `(2,1)`. Put a right-action arrow in each nonterminal cell. Caption: **Always choose right; γ = 0.5.** Mark transition probabilities as “?” rather than showing the known model.

**Question:** You can run this policy and observe what happens. How could you estimate `v^π((1,1))`?

**Notes:** About 1 minute recall, 2 minutes responses, 1 minute connecting answers. Evaluation is one half of generalized policy iteration; we are temporarily holding the policy fixed. Students may propose averaging returns, collecting transition counts or trying different actions. Identify return averaging as today's first route; fitting a model is a different possible route, and changing actions to improve the policy is control. Ask what DP needed that the learner no longer has: the expected rewards and transition probabilities. An observed transition is evidence, not the full distribution. Do not repeat the improvement proof or Q-value iteration.

## MT02 — Why learn from samples?

**Time:** 3 minutes. **Reuse:** P4 full-backup picture and P5 sample-backup picture, side by side; update equation labels to `V(s)`/`V(s′)` where applicable. Reuse P12's motivation in the shortened wording below. Remove the old “Offline (MDPs) / Online (RL)” labels and any unrelated future-method list.

**Display**

| Expected backup | Sample backup |
| --- | --- |
| Average over possible outcomes using the model | Use an observed transition |
| Need outcome probabilities and expected rewards | Receive `(S_t, A_t, R_{t+1}, S_{t+1})` |

- A robot's dynamics may be unknown or unreliable.
- A simulator may produce samples even when enumerating all outcomes is impractical.
- One cheap update can still require many samples to learn accurately.

**Notes:** A simulator is a source of experience; model-free describes how the learning method uses that experience. For a tabular one-step update, arithmetic/value-table accesses do not scale with the number of possible successors; sample generation itself need not be cheap. Sampling does not by itself solve large-state-space representation. Ask: does observing one transition tell us that it is the only possible outcome? Answer: no. Sources: P4–5/P12; book §8.5 for the expected/sample distinction.

## MT03 — Three different questions about the data

**Time:** 3 minutes. **Reuse:** P13–14; replace their definitions entirely with this table. No extra algorithm taxonomy.

**Display**

| Question | Distinction |
| --- | --- |
| Do we use or learn an environment model? | Model-based / model-free |
| Can we collect more interaction data while learning? | Online / offline (fixed data) |
| Does the behaviour generating data match the policy being evaluated? | On-policy / off-policy |

**Today: tabular, model-free, on-policy prediction of a fixed π.**

**Notes:** For on-policy prediction, actions in the experience follow the policy being evaluated. Off-policy prediction evaluates a target policy using data generated by a different behaviour policy; the target need not be optimal. Do not introduce correction ratios. A fixed dataset can have been collected under the target policy; fixed data and off-policy are not synonyms. Likewise, MC can collect episodes online and update after each one: waiting for termination does not make the overall learning setting offline. These distinctions return in Weeks 4, 11 and 12; no formal offline-RL method is taught now.

## MT04 — One observed episode

**Time:** 2 minutes. **Reuse/build:** P5's transition-tuple structure; new editable grid and three-row transition table. The grid is specified in MT01; preserve its coordinates and goal.

**Display**

`(1,1) → (1,1) → (1,2) → goal`

| t | S_t | A_t | R_{t+1} | S_{t+1} |
| --- | --- | --- | ---: | --- |
| 0 | (1,1) | right | −0.04 | (1,1) |
| 1 | (1,1) | right | −0.04 | (1,2) |
| 2 | (1,2) | right | +1 | goal |

**γ = 0.5. The +1 is paid on entry; continuation after the goal is zero.**

**Notes:** The learner observes states, chosen actions, rewards and termination. Intending right need not mean moving right. No transition probabilities are needed to compute any MC/TD update. For instructor verification only: intended direction has probability 0.8, each perpendicular slip 0.1; hitting a wall leaves the state unchanged. This path has probability `0.1 × 0.1 × 0.8 = 0.008` under always-right. It is deliberately selected to show repeated visits in a short episode, not a representative performance sample. Entry payoff +1 is total, not +1−0.04. `(2,1)` is not visited. These rules are the accepted Bellman MDP, not a new grid.

## MT05 — Monte Carlo: value as a mean return

**Time:** 5 minutes. **Reuse:** P16–17's native value/return equations; replace old indices and value-estimate notation. Keep the MT04 trajectory visible in compact form.

**Display**

\[
v^\pi(s)=\mathbb{E}_\pi[G_t\mid S_t=s].
\]

**Monte Carlo prediction:** follow π, observe complete episodes, and average returns after visits to each state.

\[
G_T=0,\qquad G_t=R_{t+1}+\gamma G_{t+1}.
\]

**Your turn:** calculate `G_2`, then `G_1`, then `G_0` for our episode.

**Answer reveal**

\[
G_2=1,\qquad G_1=-0.04+0.5(1)=0.46,\qquad
G_0=-0.04+0.5(0.46)=0.19.
\]

**One observed return is a sample, not the expectation.**

**Notes:** About 1 minute rationale, 2 minutes student calculation, 2 minutes discussion. `T=3` here; the terminal entry reward is in `G_2`, not in `G_3`. The unknown quantity is the expected return; an episode supplies an observed target. This complete-return MC method needs the relevant episode to terminate. A truncated partial sum is not the same target. The book writes `v_π`; course notation is `v^π`. Sources: book §5.1; Silver pp. 4–7; CS234 pp. 10–14.

## MT06 — Which visits count?

**Time:** 3 minutes. **Reuse:** P18's repeated-state question and P21's first/every-visit distinction. Use a new editable table, not the old pseudocode image.

**Display**

| Visit to (1,1) | Return following that visit |
| --- | ---: |
| First, t = 0 | 0.19 |
| Second, t = 1 | 0.46 |

- **First-visit MC:** include only the first visit to a state in each episode.
- **Every-visit MC:** include every visit to that state.

**Question:** what sample mean does each produce after this one episode?

**Answer reveal:** first-visit `0.19`; every-visit `(0.19 + 0.46)/2 = 0.325`.

**Notes:** Ask students which returns belong in each average before revealing it. At `(1,2)`, either convention includes the single return 1. `N(s)` counts included returns: first visits for first-visit MC, all visits for every-visit MC. Returns from repeated visits within an episode are correlated; do not call them independent episodes or assert that every finite-sample MC estimate is unbiased. Under the usual fixed-policy/visitation assumptions both visit conventions are consistent. These numbers are **sample means**; later we explicitly switch to constant-step updates. Sources: book §5.1, CS234 p.26.

## MT07 — From an average to an incremental update

**Time:** 3 minutes (unit 8, part 1). **Reuse:** P18–19 native running-mean equations, with `V̄` replaced by `V`, DP-like visit indices removed and approved `N(s)` retained. Do not copy the old notation for MC “error” as `δ`.

**Display**

For one newly included return `G_t`, first increment `N(s)`:

\[
N(s)\leftarrow N(s)+1,
\qquad
V(s)\leftarrow\frac{(N(s)-1)V(s)+G_t}{N(s)}
=V(s)+\frac{1}{N(s)}[G_t-V(s)].
\]

**A common update form**

\[
V(S_t)\leftarrow V(S_t)+\alpha[U_t-V(S_t)].
\]

`U_t`: target. `α`: fraction of the discrepancy used for this update.

| Step size for MC | Meaning |
| --- | --- |
| `1/N(s)` | Exact sample mean of included returns |
| Constant `α` | Recency weighting; initialization can still matter |

**Notes:** The right-hand `V(s)` is its old value; after incrementing the count, `N(s)−1` returns contributed to that old mean. Show the algebra, not just the final rule. Constant α weights recent targets more and can be useful when the policy changes later; here π is fixed. For this presentation take `0 < α ≤ 1`. A first-visit sample mean and a constant-step estimate are different estimators even when fed the same return. No gradient aside or convergence-sum derivation. Sources: P18–20; book §§2.4–2.5; Silver p.11.

## MT07a — First-visit MC prediction

**Time:** 2 minutes (unit 8, part 2). **Reuse:** P21 / book §5.1 algorithm structure. P21 is a picture: rebuild this shorter loop as editable text with native equations rather than importing its unapproved bookkeeping symbols.

**Display**

1. Fix π. Initialize `V(s)=0` and `N(s)=0` for nonterminal states.
2. Generate a complete episode following π.
3. Compute its returns backwards: `G_T=0`, then `G_t=R_{t+1}+γG_{t+1}`.
4. Scan the episode in time order. At the **first visit** to each state:
   - increment `N(S_t)`;
   - update `V(S_t) ← V(S_t) + [G_t−V(S_t)]/N(S_t)`.
5. Repeat with another episode.

For constant-step MC, replace `1/N(S_t)` by `α` in step 4. The first-visit rule stays.

**Notes:** “First” means earliest in the episode, not first encountered in the backward return calculation. Students need to understand this order before implementing an update kernel. No list of returns need be retained across episodes; the current episode still needs enough information to compute its returns. For every-visit MC omit the first-visit restriction. Spoken caveat: fixed-policy tabular convergence requires sufficient visits and suitable step sizes; constant α generally leaves fluctuations in noisy problems. The Robbins–Monro step-size conditions are one source of such guarantees, not a proof that every constant-step process must fluctuate. We will compare mechanisms today, not prove convergence.

## MT08 — Driving home: must learning wait?

**Time:** 5 minutes. **Reuse:** P28's driving-home table (book Example 6.1, printed 122 / PDF144). Recreate as an editable table if the old object is raster. Save the arrow panels for MT09b; this is the first of **two** book-illustration slides.

**Display**

**Predict the minutes remaining until home**

| Situation | Elapsed minutes | Predicted minutes remaining | Predicted total minutes |
| --- | ---: | ---: | ---: |
| Leave office | 0 | 30 | 30 |
| Reach car; raining | 5 | 35 | 40 |
| Exit highway | 20 | 15 | 35 |
| Behind slow truck | 30 | 10 | 40 |
| Enter home street | 40 | 3 | 43 |
| Arrive home | 43 | 0 | 43 |

**At the car, would you revise the office prediction now, or wait until home?**

Small convention line: **Standalone prediction example: rewards are elapsed minutes; γ = 1.**

**Notes:** About 1 minute setup, 2 minutes discussion, 1 minute the numeric contrast, 1 minute transfer to the grid. This predicts positive travel time under a fixed behaviour; it is not a reward-maximizing driving-control problem. Explain elapsed versus remaining time before interpreting total-time changes. At the car we have spent 5 minutes and predict 35 more: the office target can already be 40. MC must wait for the realized 43. Reveal the rows from “exit highway” downward only after the question so students do not get the outcome prematurely. Then pause the grid after its first observed transition: what can replace the unseen return? The next state's current value estimate. It can be wrong; the point is that it is available earlier. Do not introduce a second driving scenario or all six updates here.

## MT09 — A sampled Bellman target

**Time:** 2.5 minutes (unit 10, part 1). **Reuse:** P25–26 native equations; replace old reward indices, barred values and policy marks. P24's bootstrapping explanation supplies the final line. Sources: book §6.1, printed 119–121 / PDF141–143.

**Display — reveal in this order**

1. Recall the Bellman expectation equation:
\[
v^\pi(s)=\mathbb{E}_\pi[R_{t+1}+\gamma v^\pi(S_{t+1})\mid S_t=s].
\]
2. Use one observed transition and the current next-state estimate:
\[
U_t=R_{t+1}+\gamma V(S_{t+1}).
\]
3. Compare the target with the current estimate, then update:
\[
\delta_t=U_t-V(S_t),\qquad
V(S_t)\leftarrow V(S_t)+\alpha\delta_t.
\]

**Bootstrapping:** use an existing value estimate in a new update target.

Small caption: **The expected TD target is a Bellman backup of the current V; it need not equal v^π.**

**Notes:** The two approximations are sampling the expectation and replacing the unknown true successor value with `V`. For a fixed table under π, averaging this target gives the DP evaluation backup of that table. Correct successor values are sufficient, not necessary, for that expectation to equal the true value at a given state: successor errors may cancel. Do not use “unbiased only if the whole table is exact.” A single target is not guaranteed closer to truth. This is one-step TD, called TD(0); the zero is part of the method's name, not α=0. At a terminal successor `V=0`, so the target is just the observed entry reward. No maximization: this is fixed-policy prediction.

## MT09a — TD(0) prediction

**Time:** 1.5 minutes (unit 10, part 2). **Reuse:** P27 / book §6.1 algorithm structure. P27 is a picture: rebuild this compact loop with the approved notation.

**Display**

Fix π and choose α. Initialize the nonterminal estimates; set `V(terminal)=0`.

At each transition:

1. Take `A_t` according to π; observe `R_{t+1}` and `S_{t+1}`.
2. Form `U_t = R_{t+1} + γV(S_{t+1})`.
3. Update `V(S_t) ← V(S_t) + α[U_t−V(S_t)]`.
4. Advance to the next state; if terminal, end the episode.

**Update after observing the transition. Read the current table before changing it.**

**Notes:** This matters for self-transitions: calculate the target before overwriting the same table entry. Keep the terminal value at zero. In a continuing discounted task, continue taking transitions without an episode-end test. This does not make the displayed TD rule an average-reward algorithm; the objective contrast later changes the question, not this algorithm. The fixed-policy, tabular, adequate-visitation and suitable-step-size qualifications apply to convergence. No theorem or function-approximation guarantee is added here.

## MT09b — Driving home: what each update changes

**Time:** 1.5 minutes (unit 10, part 3). **Reuse:** P28's MC/TD arrow panels, sourced from book Figure 6.1, printed 123 / PDF145. Copy the existing panels as figures, keeping axes and attribution; remove the table from this second illustration. Do not import duplicate shape IDs from P28 when copying objects. Correct captions as below.

**Display**

Two panels: **MC: toward the final outcome** and **TD: toward the next prediction**.

Retain y-axis label **Predicted total travel time**. Convention: **γ = 1; α = 1 for the full arrows.**

Highlight only the first arrow in each panel:

- MC at the office: `30 → 43`, after reaching home.
- TD at the office: `30 → 5 + 35 = 40`, after reaching the car.

**Notes:** The table's state value is remaining time; the graph adds elapsed time to plot total predicted duration. That is why adjacent graph heights show the TD discrepancy with γ=1. Full arrows illustrate α=1, not a recommended universal step size. This is the explanation time reserved in unit 10; do not narrate every arrow. Return explicitly to the grid's γ=0.5 and reward units for MT10.

## MT10 — Your turn: MC and TD on the same episode

**Time:** 9 minutes, protected student reasoning. **Reuse/build:** P21/P27 algorithm structures, the MT04 trajectory and a new editable answer table. No new environment setup.

**Display**

`(1,1) → (1,1) → (1,2) → goal`  
Rewards `−0.04, −0.04, +1`; returns `0.19, 0.46, 1`.

**Reset each method independently: V = 0, γ = 0.5, constant α = 0.5.**

1. First-visit MC: update each state's first visit using its completed return.
2. TD(0): update after each transition, in time order.
3. Why does the goal reward affect the estimates differently?

Initial display: table values below replaced by “?”. Reveal after students work.

| Method / event | Target U_t | Estimate being changed | Value after update |
| --- | ---: | --- | ---: |
| MC, first (1,1) visit | 0.19 | V((1,1)) | 0.095 |
| MC, first (1,2) visit | 1 | V((1,2)) | 0.5 |
| TD, t = 0 | −0.04 | V((1,1)) | −0.02 |
| TD, t = 1 | −0.04 | V((1,1)) | −0.03 |
| TD, t = 2 | 1 | V((1,2)) | 0.5 |

Footer: **MC and TD have different targets and update schedules; this is not a performance ranking.**

**Notes / complete answers:** Allow roughly 1 minute instructions/reset, 4 minutes students calculate, 3 minutes answer discussion, 1 minute interpretation.

- Constant-step first-visit MC: `0 + 0.5(0.19−0) = 0.095`; skip the second `(1,1)` visit; `0 + 0.5(1−0) = 0.5` at `(1,2)`. These differ from MT06's sample means because α is now fixed at 0.5.
- TD t=0: target `−0.04 + 0.5(0) = −0.04`, error `−0.04`, new `V((1,1))=−0.02`.
- TD t=1: `V((1,2))` is still zero, so target `−0.04`; error `−0.04−(−0.02)=−0.02`; new `V((1,1))=−0.02+0.5(−0.02)=−0.03`.
- TD t=2: target `1+0.5(0)=1`; error 1; new `V((1,2))=0.5`. No update to the terminal state. `(2,1)` stays zero in both tables because it is unvisited.
- MC uses the realized goal reward immediately in the earlier completed-return target. Online TD's earlier updates happened before the successor estimate learned from the goal. Later visits can propagate this information; there is no extra backward TD sweep at the end of this pass.
- Equal α does not isolate only target choice: first-visit MC updates `(1,1)` once; TD updates it twice. Do not interpret a negative estimate after one episode as proof of failure or positive estimates as proof of optimism.

## MT11 — One episode versus an expected value

**Time:** 2.5 minutes. **Reuse/build:** P29's comparison question, with the new exact-value table. Values below follow the accepted grid and always-right policy; they are not the old DP deck's terminal-boundary numbers.

**Display**

| State | First-visit MC after this episode | TD(0) after this episode | True v^π from the known model |
| --- | ---: | ---: | ---: |
| (1,1) | 0.095 | −0.03 | ≈ 0.051 |
| (1,2) | 0.5 | 0.5 | ≈ 0.836 |

**The right-hand column is a checking benchmark; the learner did not use it.**

**Questions:** Can this episode establish which method is better? What would we need to compare learning after many episodes?

**Notes:** Exact benchmark values are `14/275` and `46/55`, respectively. Answer: one illustrative path cannot rank the methods. Repeated datasets/runs, step sizes, initialization, a stated error metric and comparable data budgets matter. More episodes can improve estimates under the appropriate conditions, but 1,000 episodes is not a guarantee or a ranking. Leave full bias/variance and evaluation reasoning to 3.2. Do not rederive the Bellman solution. This table makes the difference between an outcome and an expectation visible.

## MT12 — Sampling and bootstrapping

**Time:** 4 minutes. **Reuse:** P37–39 backup pictures (original attribution: David Silver, lecture 4) and P40's classification, consolidated on one slide. Copy diagram objects only; remove the old claims that a diagram proves which method is better for non-Markov problems. Label terminal leaves “terminal”, not `T` (reserved for the final time step). If the labels are embedded in a picture, redraw that simple diagram natively with the same branching structure and attribution. Use the caption/table below.

**Display**

| Method | Uses sampled experience? | Bootstraps from value estimates? | What supplies the target? |
| --- | --- | --- | --- |
| DP expected evaluation backup | No | Yes | Model-weighted reward and successor values |
| Complete-return MC | Yes | No | Observed return through termination |
| TD(0) | Yes | Yes | One observed reward and next-state estimate |

**Sampling:** use observed outcomes in place of a full expectation.  
**Bootstrapping:** use a value estimate in the target.

**Check:** Which needs a model? Which must wait for the completed return? Which can update before the episode ends?

**Notes:** Answers: the displayed DP backup; complete-return MC; TD(0). Samples can come from real interaction or a simulator. For a fixed table, one sample TD target averages to a DP evaluation backup; the current table itself may be inaccurate. No claim that each sampled update reduces error. The classification concerns these three specific methods, not every possible algorithm called DP or MC. Detailed bias/variance, batch learning and n-step targets belong in 3.2. Do not add the old full unified-method diagram, λ axis or eligibility traces.

## MT13 — A task that keeps running

**Time:** 2 minutes (unit 14, part 1). **Reuse/build:** VFA PPTX37's continuing-objective motivation only; build a new editable two-state diagram from accepted D7. Do not copy its stationary-limit line or the later differential-value slides.

**Display**

**A continuing service system — equal-duration time steps**

Diagram with two states, **ready** and **busy**:

- ready → ready: **steady service; reward 0.8**.
- ready → busy: **start large job; reward 0**.
- busy → ready: **complete job; reward 2** (only available action).

Starting from ready:

| Fixed policy at ready | Reward sequence |
| --- | --- |
| Always steady service | 0.8, 0.8, 0.8, … |
| Always start a large job | 0, 2, 0, 2, … |

**There is no terminal state. What should good long-run performance mean?**

**Notes:** This is a separate continuing example, not a restart of the grid. Both policies use forced completion at busy. Discounted return is already one meaningful objective for such a task. We now contrast it with average reward. All rewards are received on the stated transitions and each transition consumes one equal unit of time. Students identify the two reward sequences before the next slide. No policy learning algorithm is introduced.

## MT13a — Discounted return and average reward

**Time:** 3 minutes (unit 14, part 2). **Reuse:** VFA PPTX37's average-reward definition as conceptual source, restricted to the time-average form; replace its display with the equation and table below. Book §10.3, Eq. 10.6; do not import Eq. 10.7. Use `t` as the length of the averaging prefix, already an approved time index.

**Display**

**Average reward: expected reward per step over a long run**

For the policies in this service example, starting from ready:

\[
r(\pi)\doteq\lim_{t\to\infty}\frac{1}{t}
\mathbb{E}_\pi[R_1+R_2+\cdots+R_t\mid S_0=\text{ready}].
\]

Ask for the average-reward entries first; reveal the full table afterward.

| Policy | Average reward per step | Discounted return from ready, γ = 0.5 |
| --- | ---: | ---: |
| Steady service | 0.8 | 1.6 |
| Large jobs | (0 + 2)/2 = 1 | 4/3 ≈ 1.333 |

**The objective changes the ranking:** discounted return prefers steady service; average reward prefers large jobs.

**Notes / answers:** About 1 minute students compute rates, 1 minute discounted comparison, 1 minute interpretation. Show the rates as the proportion of total reward to elapsed steps. Supply the discounted values with the short arithmetic spoken or in notes:

- Steady: `0.8 + 0.5×0.8 + … = 0.8/(1−0.5) = 1.6`.
- Large jobs: `0 + 0.5×2 + 0.5³×2 + … = 1/(1−0.5²) = 4/3`.
- The job pays more per step in the long run but delays its first payment. This is an objective choice; neither objective is universally correct.
- The alternating policy is periodic. Its time average exists, but its individual expected rewards oscillate; do **not** write `r(π)=lim 𝔼[R_t]` or claim convergence to a stationary distribution. No ergodicity lesson is required. The displayed definition is scoped to this example, avoiding a claim that every MDP has a start-independent average reward.
- The discounted TD(0) rule taught earlier does not by itself learn this average-reward objective. No differential returns, differential Bellman equations, average-reward algorithm or approximation teaser here. These two slides together retain exactly the accepted five-minute contrast.

## MT14 — What can we learn before the episode ends?

**Time:** 1.5 minutes. **Reuse:** P6's roadmap reduced to the lines below; P29's availability question. Do not restore the broad algorithm catalogue.

**Display**

- MC updates toward a completed observed return.
- TD updates toward an observed reward plus estimated continuation.
- Both can evaluate a fixed policy from experience.

**Exit check:** Which needs the next state's estimate? Which needs the completed return?

**Next session:** bias, variance, n-step targets and evaluating learning.  
**Week 4:** improve policies using learned action values.

**Notes:** TD uses the next estimate; complete-return MC waits for the return. Both methods here are model-free and on-policy; episode-based MC can still learn while collecting fresh data. The service example changed the objective, not these answers. Link back to GPI: greedy improvement using state values alone ordinarily needs a model for action lookahead; learning action values provides the next route. Do not give SARSA/Q-learning rules yet.

## Handoff checks and session boundary

- The targets sum to **58 minutes**: 53 for MC/TD/data access and five for average reward. This is one minute below the accepted 59-minute planning allocation, 1.5 below `70 × 0.85 = 59.5`, leaving 12 physical minutes. The minute below the allocation is buffer, not a slot for another topic. No 63-minute delivery allowance or earlier-session carryover is used.
- Protect MT05's student return calculation, MT06's visit-selection check and all nine minutes of MT10. MT07–MT09b carry substantial explanation in 10.5 minutes after the separate five-minute motivation block; check pacing during delivery rather than treating the arithmetic total as feasibility proof. MT13/MT13a remain Exposure and total five minutes.
- Routine cross-review corrections are built in: observer/model distinction; correct source numbering and notation; first-visit versus constant-step reset; current-table chronological TD; nonexclusive unbiasedness condition; qualified convergence; different update counts; time-average-only service definition. No first-render input or deck from an earlier session is changed.
- **3.2 boundary:** reserve Examples 6.2 and 6.4, with batch setup before 6.4; count random-walk environment setup outside its protected ten evaluation-reasoning minutes. The 19-state plot stays deferred, n-step work remains protected, and λ mixtures remain in Week 8. This file does not attempt to establish 3.2's timing fit or implement its content.
- Claude's next workflow step is the first PPTX render and quick gross-layout check. In particular inspect native equation conversions, the two driving-home panels' axes/units, reveal order, terminal payoff labels and the exercise answer table. Preserve attribution on the book/Silver figures. This Markdown handoff does not certify a rendered layout or classroom pacing. At first render, freeze this input and record the current deck in the deck decision file.
