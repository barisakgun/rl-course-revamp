# Model-free prediction — render-ready addition for session 3.2

**Frozen (historical):** first-render input for the 3.2 slides (MT15–MT25) of `course/lectures/week03/mc_td_claude.pptx`, rendered 2026-10-22. Not maintained: the PPTX is the source from that render on. Do not use this file to rebuild or overwrite the deck. Status: [deck decisions](../../../decisions/lectures/mc_td.md).

**Shared:** instructor, Claude and ChatGPT. Prepared by ChatGPT, 2026-10-22, under [lecture workflow step 4](../../../docs/lecture_workflow.md) and the instructor's request to prepare 3.2. Current status and accepted choices live in [mc_td decisions](../../../decisions/lectures/mc_td.md). This addition implements D12–D16 and the finalized C01–C10 sequence in the [shared review](../../../analysis/lecture_suggestions/mc_td_review.md), including R28–R37. It is the first-render input for the **new 3.2 slides only**. Freeze it at their first render; thereafter the saved PPTX is the teaching source.

## Renderer handoff

- Append the 21 slides below to the existing combined `course/lectures/week03/mc_td_claude.pptx`, after its accepted 20-slide 3.1 portion. Accepted baseline SHA-256: `b1d2c2dec74ada2066b8a6134340c22e6a49688dbaf4b7dd0e505504c08b3be1`. Preserve slides 1–20, their notes, objects, builds and instructor edits. Check the latest saved deck before appending and back it up. If the fingerprint has changed, reconcile that change rather than restoring this baseline over it.
- Do not rebuild from or edit the frozen `mc_td_content.md` or `mc_td_claude.yaml`. This separate addition follows the precedent of `bellman_improvement_content.md`. No second deck or new course title slide.
- New stable IDs: **MT15, MT16, MT16a, MT17, MT17a, MT18, MT19, MT19a, MT20, MT21, MT21a, MT22, MT22a, MT22b, MT23, MT23a, MT24, MT24a, MT24b, MT24c, MT25**. All are live. Titles, display text and equations below are the content specification. Source/reuse directions are production instructions, not student-facing text. Teaching notes and source citations go into speaker notes.
- Keep the existing template and editable objects. Reuse old PowerPoint equations natively where available, correcting them to the equations below. Equations use theme Accent 5 (`#4472C4`). Use the [notation guide](../../notation_guide.md): true value `v^π`, estimate `V`, reward `R_{t+1}`, target `U_t`, n-step target `G_{t:t+n}`, final episode time `T`. No new notation or notation-guide change is needed. Generic indices inside sums are local counting indices.
- Question slides precede answers. MT19/MT19a and MT22/MT22a/MT22b are explicit question/reveal sequences. For other answer cues use click reveals or a native answer panel, without adding teaching time. Keep the question and state/trajectory context visible. Answer reveals must not leak onto initial question builds.
- The course-generated evaluation figure and its data below are **explicitly shared render assets**, despite their authorship suffix. They may be embedded or converted into an editable chart by the renderer. They are not counterpart suggestion inputs. The standalone SVG preserves vector text/paths; the CSV permits native chart reconstruction. No other ChatGPT-specific artifact is needed for rendering.

## Sequence and timing

| Unit | Slides | Purpose | Minutes |
| --- | --- | --- | ---: |
| C01 | MT15 | Reopen the comparison question | 2 |
| C02 | MT16, MT16a | Meaning of bias/variance and the two targets | 2 + 3 |
| C03 | MT17, MT17a | Example 6.2 setup, curves and first-episode check | 3 + 2 |
| C04 | MT18, MT19, MT19a | Batch updating, Example 6.4 vote and explanation | 3 + 2 + 5 |
| C05 | MT20 | Motivation and backup diagrams for n-step targets | 2 |
| C06 | MT21, MT21a | Derivation, terminal rule and availability | 4 + 2 |
| C07 | MT22, MT22a, MT22b | Protected grid calculation and chronological trace | 4 + 2 + 3 |
| C08 | MT23, MT23a | 19-state experiment: setup, plot, mechanism | 2 + 4 |
| C09 | MT24, MT24a, MT24b, MT24c | Figure reading, then protected evaluation reasoning | 2 + 3 + 4 + 3 |
| C10 | MT25 | Method-choice reference and next session | 3 |
| | **Total** | | **60** |

Targets implement D16: 58-minute planning allocation unchanged; 60-minute delivery target, 0.5 minute above `70 × 0.85 = 59.5` usable and 10 physical minutes remaining. These are estimates, not rehearsal evidence. N-step motivation/derivation/practice receives 17 minutes; the nine-minute exercise and ten-minute evaluation activity are protected. Book setup and the new figure's two-minute reading have their own time. Detailed expectation bounds and the variance proof below are optional notes, not additional live obligations. No new homework, reading, implementation requirement or prerequisite is introduced. λ mixtures remain in Week 8. No 3.1 carryover is charged here.

## Source and reuse key

**P** = [old Model Free Prediction PPTX](../../../sources/current_course/4%20-%20Model%20Free%20Prediction.pptx), positions including hidden slides. Its PDF pagination differs. Primary source chain:

- P29–31: comparison and bias/variance, with the overstatements corrected below.
- P32 / PDF29: Example 6.2, **unnumbered plots**, book printed p. 125 / PDF147. Preserve the plot labels and α values. The left plot is one TD run's state values; the right is mean RMS error over 100 runs. **Book Figure 6.2 is the different batch plot on p. 127 / PDF149; do not substitute it.**
- P33–35: batch updating and Example 6.4, book §6.3, printed pp. 126–128 / PDF148–150. Omit P33's extra batch random-walk curve. Correct its “certainty equivalent” claim: that describes the TD solution, not both methods' solutions.
- P36–38, P41–43: comparison, backup diagrams and n-step targets. Remove P42's superficial-coverage promise and the λ question. P43's reward indices/target notation must be converted. Book §7.1, printed pp. 142–144 / PDF164–166.
- P44 / PDF41: **Figure 7.2**, book printed p. 145 / PDF167, the 19-state α–n experiment. Preserve the original axes and all curve labels. The original figure is evidence, not newly simulated data.
- Supporting configured sources: [Silver lecture 4](../../../sources/silver_rl/lectures/lecture-4-model-free-prediction-.pdf), bias/variance pp. 17–18, batch/Markov example pp. 21–25, backup/n-step pp. 26–33; [CS234 lecture 3](../../../sources/stanford_cs234/lectures/lecture3post.pdf), pp. 23–26 for estimator quality and target-versus-estimator distinctions; [Sutton TD slides](../../../sources/sutton/11-12-TD.pdf), pp. 21–31 for batch learning; [Sutton multistep slides](../../../sources/sutton/13-multistep.pdf), pp. 3–10. The [session index](../../../output/lectures/session_sources.md) supplies the wider source mapping. These references support preparation and are not added reading assignments.

The accepted Bellman/3.1 grid supplies continuity, not the primary content. Its upper row is `(1,2), (2,2)=goal`; lower row `(1,1), (2,1)`. Always choose right. Entry to goal pays **+1 total**, every other pretermination transition pays −0.04, γ = 0.5, terminal continuation zero. Learners receive observed transitions, not the transition model. This session does not need the slip probabilities for any grid update.

## MT15 — Can one episode decide?

**Time:** 2 minutes. **Reuse:** P29's comparison question, with the familiar MT11 exercise as continuity. New opening within the existing deck.

**Display**

We evaluated a fixed policy from experience:

\[
U_t=G_t\quad\text{(MC)},\qquad
U_t=R_{t+1}+\gamma V(S_{t+1})\quad\text{(TD(0))}.
\]

Our grid episode gave different value updates.

> Does one episode tell us which method learns better?

Today: noisy targets, n-step prediction and evidence for a comparison.

**Notes:** Allow a response before the closing line. No: one episode illustrates mechanics, and the 3.1 first-visit MC and TD update schedules also differed. Accuracy requires a true-value benchmark or an appropriate independent evaluation procedure. Hold the policy fixed throughout this session. We ask why the targets behave differently and how to judge repeated learning. Do not redo the 3.1 arithmetic.

## MT16 — Bias and variance describe repeated samples

**Time:** 2 minutes. **Reuse:** P30's framing; replace its unconditional statements. Use plain definitions and a small numerical table rather than importing additional parameter symbols from CS234.

**Display**

At the same state, repeat the sampling experiment while holding the current table fixed.

- **Bias:** mean target minus the true value.
- **Variance:** spread of targets around their own mean.
- **Mean squared error = variance + bias².**

Illustration, true value 1.0:

| Equally likely targets | Mean | Bias | Variance |
| --- | ---: | ---: | ---: |
| 0.0 or 2.0 | 1.0 | 0.0 | 1.0 |
| 0.8 or 1.0 | 0.9 | −0.1 | 0.01 |

**Notes:** These are illustrative target distributions, not experiment results or labels for MC/TD. Ask which pair is less spread out, then reveal the last two columns. Zero bias alone need not mean lower squared error: here the MSEs are 1 and 0.02. One observed target cannot establish its mean or spread. Distinguish a random update target from the estimate after a history of updates. Sources: P30; CS234 L3 pp. 23–24. Keep this to meaning and the simple numerical illustration; no statistical derivation live.

## MT16a — What randomness enters each target?

**Time:** 3 minutes. **Reuse:** P30's native equations, rewritten as follows.

**Display**

| | MC | TD(0) |
| --- | --- | --- |
| Target | `G_t` | `R_{t+1} + γV(S_{t+1})` |
| Samples | Remaining episode | One transition |
| Uses the current value table in the target? | No | Yes |

\[
\mathbb E_\pi[G_t\mid S_t=s]=v^\pi(s).
\]

\[
\mathbb E_\pi[R_{t+1}+\gamma V(S_{t+1})\mid S_t=s]
-v^\pi(s)
=\gamma\mathbb E_\pi[V(S_{t+1})-v^\pi(S_{t+1})\mid S_t=s].
\]

MC has an unbiased **target**. TD's target can inherit error from the table.

> On the grid, which random transitions affect each target for the start state?

**Notes:** About 1 minute on the table, 1 on the expectation equation, 1 on the grid question. MC includes every later slip and reward; TD(0) includes the next transition and the fixed table. Random actions also enter in problems with a stochastic policy; the grid policy is deterministic. The TD expression is a Bellman expectation backup, not necessarily the true value. Correct successor values are sufficient for zero target bias, not necessary: successor errors can cancel. MC does not use V in its target, but a constant-α MC estimate can still depend on its initialization. In noisy problems constant α generally leaves estimates fluctuating.

Say: “Bootstrapping often reduces sampling variability, but a poor table can reverse that comparison.” No universal variance ordering for arbitrary learned tables. **Optional explanation if asked:** with fixed correct V in a Markov task under a fixed policy, and finite second moments, the TD target is the conditional expectation of the return given the first observed transition; total variance gives its variance no greater than the return's. Longer true-value targets condition on longer prefixes. This argument does not cover arbitrary inaccurate V. Counterexample: zero rewards throughout and equally likely nonterminal successors with V = +1/−1 yield a variable TD target but a constant zero return. Do not add a proof or counterexample slide. Sources: book §6.2; P30; CS234 L3 pp. 24–26.

## MT17 — Example 6.2: random-walk prediction

**Time:** 3 minutes. **Reuse:** P32's five-state chain, separated from its plots for legibility. Native labels may be placed over an unlabelled copy if necessary; preserve the source diagram's meaning.

**Display**

Five nonterminal states **A, B, C, D, E** between left and right terminals. Start at **C**. Each step moves left or right with probability 0.5.

- **New example:** γ = 1, +1 on right-terminal entry, 0 on every other transition.
- Both terminals have zero continuation value.
- Start with V(s) = 0.5 for each nonterminal state.

| State | A | B | C | D | E |
| --- | ---: | ---: | ---: | ---: | ---: |
| True value | 1/6 | 2/6 | 3/6 | 4/6 | 5/6 |

> Why is v^π(C) = 0.5?

**Notes:** One minute setup, one on return/probability interpretation, one on measurement. This is a Markov reward process, equivalent to holding a policy fixed; no action selection to optimize. Undiscounted return is 1 on a right exit and 0 on a left exit, so value is the probability of exiting right. Symmetry gives 0.5 at C. Supply the other values; do not add a linear-system exercise. Measure **RMS value error over the five states**, not episode reward. Explain RMS as square each prediction error, average over states, then take the square root. True values and the model are available to us for checking; the learning updates use experience only. Announce the changed rewards/discount explicitly. Source: book Example 6.2, printed p. 125 / PDF147; P32 / PDF29.

## MT17a — What the random-walk curves show

**Time:** 2 minutes. **Reuse:** P32's two plots from book Example 6.2, with their axes, α labels and single-run episode labels intact. Use the original plots, not the batch Figure 6.2.

**Display**

Left: **one TD(0) run**, α = 0.1, estimated values by state.

Right: **mean RMS error over 100 runs**, several α values, by training episode.

> After the first episode, only V(A) changed. Where did the episode end, and by how much did V(A) change?

**Reveal:** left exit. `V(A): 0.5 + 0.1(0 − 0.5) = 0.45`.

**Notes:** About 45 seconds for the two axes, 45 for the prompt, 30 for the answer/transition. Every nonterminal-to-nonterminal TD target during that first episode was 0 + 0.5, equal to the current estimate. The left-terminal transition alone gives target zero and a −0.05 change. The episode may have revisited states; its exact path cannot be inferred. With constant α the noisy estimates need not settle exactly on the true values. The right plot shows lower error for TD at the illustrated settings; defer the strength and fairness of that conclusion to evaluation. It has no uncertainty bands. Transition: “What does each method do with the same finite experience if we train on it repeatedly?” Sources: Example 6.2 and Exercise 6.3, pp. 125–126 / PDF147–148. Do not claim a first-visit convention for the book's plotted constant-α MC when the displayed source does not specify it.

## MT18 — Learning repeatedly from a fixed batch

**Time:** 3 minutes. **Reuse:** P33's finite-data question, rewritten with the book's precise update convention. Omit its batch random-walk curve and asymptotic-convergence preamble.

**Display**

We have a fixed set of complete episodes. No new experience arrives.

For each pass through the batch:

1. Hold V fixed while computing each visit's increment.
2. Add the increments for each state.
3. Apply those sums, then start the next pass.

\[
\text{increment}=\alpha[U_t-V(S_t)].
\]

MC uses the observed return. TD uses the reward and the next state's estimate.

> Can repeated learning from the same data lead to different answers?

**Notes:** Set up the experiment before the puzzle. “Fixed V” lasts for one pass, not all passes; bootstrapped targets change on later passes. This is the batch convention of book §6.3, not online updates applied immediately on each visit, and not a first introduction to modern offline-control problems. Use sufficiently small α for stable batch iteration. In this small tabular example each method approaches its own fixed point. Repeating a batch changes computation, not the amount of collected experience. The next example asks about the converged batch answers, not one pass from zero. Source: book printed p. 126 / PDF148; P33; Sutton TD pp. 21–31.

## MT19 — Example 6.4: you are the predictor

**Time:** 2 minutes. **Reuse:** P34's data, with answers and inferred-model diagram removed from this question slide. Show explicit terminal endpoints.

**Display**

**New example:** states A and B, γ = 1, zero terminal continuation.

Eight observed episodes:

| Count | Episode, with rewards on transitions |
| ---: | --- |
| 1 | A →(0) B →(0) terminal |
| 6 | B →(1) terminal |
| 1 | B →(0) terminal |

> What should V(A) and V(B) be after repeated batch learning?

Vote for V(A): **0**, **0.75**, or **depends on the prediction rule**.

**Notes:** One minute to parse the counts and think, one minute for a vote and reasons. There are eight B observations, including B in the first episode. State names are local to this new example; they are unrelated to A/B in the five-state walk. Give no answer until MT19a. Sources: P34; book Example 6.4, printed p. 127 / PDF149; Silver L4 AB example.

## MT19a — Two batch answers from the same data

**Time:** 5 minutes. **Reuse:** P34's empirical Markov diagram and P35's two solution interpretations. Keep the 1/6/1 data table as a compact reference. Replace the old “see further reading” explanation with the worked reasoning below.

**Display**

| | Batch MC | Batch TD(0) |
| --- | --- | --- |
| B | `V(B) = 6/8 = 0.75` | `V(B) = 6/8 = 0.75` |
| A | Its only observed return was 0 | Its observed successor was B, with reward 0 |
| Answer at A | `V(A) = 0` | `V(A) = 0 + V(B) = 0.75` |

**MC:** fit the observed returns at each state.

**TD:** use the observed transitions and share the continuation estimate at B.

Empirical model diagram: A to B, reward 0, probability 1; B to terminal with reward 1 at probability 0.75 or reward 0 at probability 0.25. Both terminal branches have continuation zero.

> When is it reasonable to reuse all the B outcomes after arriving from A?

**Notes:** About 1 minute for B, 1 for the MC answer, 2 for the TD/model explanation, 1 for the question. Reusing B's outcomes assumes the future from B does not depend on arriving via A versus starting in B: the Markov property. Batch MC minimizes squared error on observed returns. It fits A's one return exactly, but that does not establish best future prediction. At B the observed targets include both 0 and 1, so neither method fits every return exactly. Batch TD's fixed point equals the value of the maximum-likelihood empirical Markov model in this example, often called the certainty-equivalence answer. TD itself need not build or solve that model.

The data do not prove this empirical model is the true environment. With only one A visit, both answers reflect limited evidence. If the label B hides relevant history, pooling all its continuations can mislead. MC avoids bootstrapping through that aliased state but does not repair partial observability. Do not present this as proof TD always wins or merely as a bias–variance illustration: the central distinction is **return fitting versus Markov structure in batch learning**. Ordinary online updates need not reach either batch answer after one pass. Sources: P34–36; book §6.3, pp. 127–128 / PDF149–150; Silver L4; Sutton TD pp. 21–31.

## MT20 — Between one transition and a complete return

**Time:** 2 minutes. **Reuse:** P37–38 backup endpoints, P41–42 framing. Add the middle sampled path using the same native node/edge style, guided by book Figure 7.1 (p. 142 / PDF164). Remove P42's superficial-coverage statement and any λ-mixture construction.

**Display**

Three sampled-path diagrams from the same starting state:

- **TD(0):** one reward, then V at the next state.
- **n-step TD:** n rewards, then V if the episode continues.
- **MC:** rewards through termination.

> How much experience should we use before trusting the remaining value estimate?

**Notes:** This is a change in how far the sampled backup reaches, not a model-based tree expansion or a new policy. Longer targets use more observed outcomes before bootstrapping, at the cost of waiting longer. Show termination without a value tail. No claim that adding samples always increases variance. The n-step method can update before a long episode ends. Sources: P41–43; book Figure 7.1; Sutton multistep pp. 3–10.

## MT21 — The n-step target

**Time:** 4 minutes. **Reuse:** P43's native equations and update form. Replace old target notation and reward indices. Show the first lines before the general case.

**Display**

Before termination, replace the unobserved tail by the current estimate:

\[
\begin{aligned}
G_{t:t+1}&=R_{t+1}+\gamma V(S_{t+1}),\\
G_{t:t+2}&=R_{t+1}+\gamma R_{t+2}+\gamma^2V(S_{t+2}).
\end{aligned}
\]

For a positive integer n and a visit t < T:

\[
G_{t:t+n}=
\begin{cases}
\displaystyle\sum_{i=1}^{n}\gamma^{i-1}R_{t+i}+\gamma^n V(S_{t+n}), & t+n<T,\\[4pt]
\displaystyle\sum_{i=1}^{T-t}\gamma^{i-1}R_{t+i}=G_t, & t+n\ge T.
\end{cases}
\]

Same update form when the target becomes available:

\[
V(S_t)\leftarrow V(S_t)+\alpha[G_{t:t+n}-V(S_t)].
\]

**Notes:** One minute expanding the first two targets, two for deriving the general/terminal cases, one for the update. Split the complete return into n observed rewards and its remaining discounted tail; replace that tail by V. The last observed reward has weight γ^(n−1), and the continuation has weight γⁿ. At or past termination there is no continuation, no fictitious extra reward and no state lookup beyond T. The terminal-entry payoff is already included once. `V` means the table available **when computing the delayed update**, immediately before that update, unless a frozen snapshot is explicitly requested. Thus these equations do not silently mean the old table from the original visit time t. Use the in-place form to avoid a new update-clock symbol. Source: book §7.1 eqs. 7.1–7.2, printed pp. 143–144 / PDF165–166; P43.

## MT21a — When can the update happen?

**Time:** 2 minutes. **Reuse:** new timing explanation from book §7.1, retaining the preceding update equation in a small reference strip.

**Display**

For the visit at time t, wait until **n further transitions or termination, whichever comes first**.

For n = 2:

| Experience observed | Earliest eligible work |
| --- | --- |
| One transition | Wait, unless it terminated |
| Two transitions | Update the visit at time 0 |
| Later transitions | Update visits as their targets become available |
| Episode terminates | Complete all remaining visits in their original order |

Terminal completion needs **no further environment transitions**.

**Notes:** Distinguish environment interaction from processing pending updates. Before n rewards arrive, the target usually needs data we have not seen. If the episode ends sooner, the complete return is already known. Finish pending visits before starting the next episode. A repeated state may receive multiple updates. A target equal to the complete return does not by itself make the update schedule first-visit MC; n-step prediction updates each visit. Source: book p. 144 / PDF166 algorithm, expressed without its auxiliary τ notation. The next exercise shows the terminal flush explicitly.

## MT22 — Your turn: targets on the grid

**Time:** 4 minutes of the protected nine-minute exercise. **Reuse:** familiar editable 2×2 grid and trajectory, newly specified here; P43's formula as a small reference. Preserve existing 3.1 objects in place.

**Display**

Always choose right. γ = 0.5, α = 0.5. Observe:

\[
(1,1)\xrightarrow{-0.04}(1,1)\xrightarrow{-0.04}(1,2)\xrightarrow{+1}\text{goal},\qquad T=3.
\]

Use this **frozen starting snapshot**, the table after 3.1's TD pass:

| State | (1,1) | (1,2) | (2,1) | goal |
| --- | ---: | ---: | ---: | ---: |
| V | −0.03 | 0.5 | 0 | 0 |

1. At t = 0, calculate the targets for n = 1, 2, 3 and 5.
2. Using n = 2, make **one isolated update** to V((1,1)).

Hold every table entry fixed while calculating part 1. Part 2 starts from the same snapshot.

**Notes:** About 30 seconds setup, three minutes student calculation/pair comparison, 30 seconds collecting answers. The time-0 successor is the same grid state, so the one-step target uses −0.03. The two-step target uses 0.5 at the upper-left state. No transition probabilities or true values are needed. Keep the numerical answer off this slide. Next slide supplies the answers; the final exercise slide resets and performs chronological updates.

## MT22a — Grid targets and one isolated update

**Time:** 2 minutes. **Reuse:** MT22's trajectory/snapshot as a compact header, with this answer table.

**Display**

| n | Target for the time-0 visit |
| ---: | --- |
| 1 | `−0.04 + 0.5(−0.03) = −0.055` |
| 2 | `−0.04 + 0.5(−0.04) + 0.5²(0.5) = 0.065` |
| 3 | `−0.04 + 0.5(−0.04) + 0.5²(1) = 0.19` |
| 5 | `0.19` because the episode already ended |

One isolated n = 2 update:

\[
V((1,1))\leftarrow-0.03+0.5[0.065-(-0.03)]=0.0175.
\]

> For n = 5, why is there no extra discounting after the goal?

**Notes:** The same realized rewards remain at their original time indices. Extending the requested horizon cannot push the terminal payoff later or create a bootstrap from a nonexistent state. The equal n = 3/5 targets are complete returns. These frozen-snapshot targets compare backup horizons on one trajectory, not expected accuracy. Repeated-state updates have not yet been applied in part 1.

## MT22b — Reset, then update in time order

**Time:** 3 minutes. **Reuse:** same trajectory/snapshot. Reveal the answer rows after asking when each visit becomes eligible.

**Display**

**Reset to V((1,1)) = −0.03, V((1,2)) = 0.5. Use n = 2 and α = 0.5.**

| When | Visit updated | Target | New estimate |
| --- | --- | ---: | ---: |
| After transition 1 | None | — | No change |
| After transition 2 | t = 0, (1,1) | 0.065 | 0.0175 |
| At termination, after transition 3 | t = 1, (1,1) | `−0.04 + 0.5(1) = 0.46` | 0.23875 |
| Finish pending work, no new transition | t = 2, (1,2) | 1 | 0.75 |

\[
0.0175+0.5(0.46-0.0175)=0.23875,\qquad
0.5+0.5(1-0.5)=0.75.
\]

**Notes:** One minute for eligibility predictions, one for the repeated-state update, one for terminal completion and questions. The second update to (1,1) uses its new estimate 0.0175, not the frozen −0.03. Its target contains only observed rewards because t+n = T. The final pending visit uses the complete one-reward return. State (2,1) remains 0, the goal remains 0. Finish with “Same trajectory, delayed information, multiple visits.” These are mechanics, not a ranking of learning methods. The first-visit MC schedule from 3.1 updates the repeated state only once, whereas this trace updates both visits.

## MT23 — A larger random walk tests the choice of n

**Time:** 2 minutes. **Reuse:** P44's experiment framing, expanded to state the book's changed conventions. Keep the full graph for MT23a.

**Display**

| | Earlier five-state walk | New 19-state walk |
| --- | --- | --- |
| Start | C | Middle state |
| Moves | Left/right with probability 0.5 | Same |
| Terminal-entry rewards | Left 0, right +1 | **Left −1, right +1** |
| Other rewards / γ | 0 / 1 | 0 / 1 |
| Initial nonterminal V | 0.5 | **0** |

Both terminal continuation values are zero.

The plot measures RMS error over 19 states at each episode end, then averages over **the first 10 episodes and 100 runs**.

**Notes:** This is the book's distinct experiment in Example 7.1, not a new run of the grid and not a continuation of the five-state training curve. Same sampled walks are reused across all parameter settings. The true values are −0.9, −0.8, …, 0.9, including 0 at the middle; give this in notes if asked, no second derivation. Average the per-episode RMS errors; do not take one square root after pooling all runs/episodes. Announce the metric because the next graph's horizontal axis is α, not episodes. Source: book p. 145 / PDF167, Figure 7.2; P44 / PDF41.

## MT23a — n and step size interact

**Time:** 4 minutes. **Reuse:** P44's complete Figure 7.2. Preserve α axis, error axis and each n label; remove the old “best of all n?” bridge to λ mixtures.

**Display**

Full book graph, with a compact caption: **Each curve fixes n. Horizontal axis: α. Lower error is better.**

> Is the best n the same at every α? What can we conclude from the low points of these curves?

**Reveal:** intermediate n performs best in this experiment. Step size matters too.

The target uses the table only if the episode is still running after n steps. A longer horizon reaches a complete return more often, but can also add sampling variability and delay.

**Notes:** Two minutes to read axes/curves, two for discussion and the mechanism. The plot reports early learning over ten episodes, not asymptotic performance. For this undiscounted walk γⁿ = 1: discounting does not reduce the bootstrap weight. The chance that the target reaches termination instead of the table changes with n. With an imperfect table, more sampled rewards often increase variability but there is no universal ordering. A shrinking bias bound does not prove monotonic bias reduction or that some intermediate n must win. Large finite n curves such as 256/512 are not literally MC on every possible episode. This plot motivates a sensitivity check, not a universal n recommendation.

**Optional notes only:** for a fixed table and starting state s, the absolute error of the expected n-step target is bounded by γⁿ × probability the episode is still running after those n transitions × the largest absolute error in V. The probability is conditional on the starting state and policy. Terminal errors are zero. For γ = 1 only the survival factor changes this bound. This is a statement about the expected target with a fixed table, not each noisy sample or the evolving online learning curve. The grid's model-based expected-error calculations from the review are unnecessary live. Sources: book §7.1 eq. 7.3 and Example 7.1; the survival refinement follows by separating terminated and nonterminated trajectories in the expectation.

## MT24 — Mean error and individual runs

**Time:** 2 minutes, **additional to** the ten-minute evaluation activity. **Reuse:** the shared course-generated figure below. Keep its source identity separate from the book plot.

**Display**

Full-width figure: [vector SVG](assets/mc_td_returns_evaluation_chatgpt.svg), [PNG fallback](assets/mc_td_returns_evaluation_chatgpt.png).

Caption: **Course simulation of the five-state task. TD(0), α = 0.1; every-visit MC, α = 0.02.**

> Do the mean-error intervals overlap at episodes 25 and 100? What does the individual-run panel tell us that the mean alone cannot?

**Notes:** One minute to identify mean, band and single-run traces; one for the questions. The intervals do not overlap at either checkpoint. The right panel shows different trajectories despite the fixed task/method/α, including crossings at some episodes. The two runs per method were selected by seed order before inspecting results; they do not estimate the full distribution. A narrow interval for a mean is compatible with noisy individual runs. The shaded intervals are approximate **pointwise 95% intervals for the mean RMS error**, not 95% of single runs and not a simultaneous interval for the whole curve. Overlap/non-overlap of separate marginal intervals is not itself a calibrated 5% test of their difference. No significance-testing lesson is added. Continue the reasoning on MT24a–c.

**Figure provenance / speaker-note detail:** generated by independent `scripts/build_mc_td_returns_figure_chatgpt.py`. NumPy `default_rng` (PCG64), TD seeds 1000–1099, MC seeds 2000–2099, 100 episodes per run; each method starts from its own independent run set. The displayed individual runs are seeds 1000/1001 and 2000/2001. Every-visit MC applies constant-α updates in visit order after termination; each visit's return is 0 or 1. TD updates online after each transition. Nonterminal initialization 0.5, terminal values 0, γ = 1, start C, equal left/right moves, right-entry +1 and every other reward 0. The two α values are prespecified illustrations, not the result of tuning on these runs. The figure is not a reconstruction of the book's random sample or a paired-seed comparison.

For each episode compute each run's RMS across five states, then average those 100 RMS values. Band = mean ± 1.96 × sample standard deviation / √100, with sample variance denominator 99. Data and exact provenance: [CSV](../../../output/lectures/week03/mc_td_returns_evaluation_chatgpt.csv), [JSON](../../../output/lectures/week03/mc_td_returns_evaluation_chatgpt.json). The generator and CSV hashes are in the JSON. These numbers supersede the illustrative simulation numbers in the historical cross-review **for this figure only**; seeds alone do not specify a random-number implementation.

| Episode | TD mean RMS ± interval half-width | MC mean RMS ± interval half-width |
| ---: | ---: | ---: |
| 25 | 0.055807 ± 0.003840 | 0.156691 ± 0.006439 |
| 100 | 0.053623 ± 0.004322 | 0.085858 ± 0.009466 |

Initialization error is √(1/18) ≈ 0.235702, shown as a dotted reference. Do not reuse the earlier review's cross-pair reversal percentage or interpret reused cross-pairs as independent experiments. No cross-pair statistic is needed here.

## MT24a — Claim 1: “TD learns better”

**Time:** 3 minutes of the protected ten-minute activity. **Reuse:** MT24's figure or its mean panel with both method labels and band meaning intact.

**Display**

> “This figure proves TD is the better algorithm.”

Vote: **supported**, **unsupported**, or **needs a narrower claim**.

**Reveal:** TD has lower mean prediction error at these checkpoints for **this task, these α values, initialization and episode budget**.

> What changes if one individual MC run has lower error than one TD run?

**Notes:** 30 seconds vote, one minute evidence, one minute for individual runs and the baseline, 30 seconds summary. A single favorable or unfavorable run does not overturn a population-mean comparison; the figure does not prove every TD run wins. MC is a meaningful comparison because it solves the same fixed-policy prediction problem with completed-return targets. The dotted initialization error is another reference; it is not a threshold every noisy run must improve on. State that the object evaluated is V, the value estimator, not a control policy. Do not expand “better” to all environments, all α or all resource budgets. Sources: generated figure; book Example 6.2 and its limitations; CS234 L3 p. 23.

## MT24b — Claim 2: “One setting settles the comparison”

**Time:** 4 minutes of the protected ten-minute activity. **Reuse:** the book's Example 6.2 right-hand multi-α plot from P32 and, if space permits, the already-taught Figure 7.2 from P44. Keep them legible; a small labelled reference to MT23a is sufficient if two full graphs do not fit.

**Display**

> “With a wider α search, MC would win.”

Vote, then identify the missing evidence.

**Reveal:** these plots do not establish that counterfactual. Compare sensitivity and give both methods equal tuning effort.

**Learning:** fit V using experience.

**Tuning:** choose α and n on separate development runs.

**Final evaluation:** report performance on fresh runs after those choices.

> In the 19-state experiment, how could we isolate the effect of n?

**Notes:** One minute vote/evidence, one minute sensitivity, one minute learning/tuning/evaluation, one minute the ablation. This adapts book Exercise 6.4: neither “MC would win” nor “no wider search could change anything” follows from the displayed settings. Each method may need a different α. The generated figure used declared illustrative α values, not claimed optimal ones. For an ablation, hold the task, initialization, walk sets, evaluation and α fixed while varying n; report several α settings to expose interactions. A separate best-tuned-method comparison uses equal search effort per method. Figure 7.2 is valuable precisely because it varies both parameters visibly.

Separate sources of data: training episodes fit V within a run; development runs select settings; fresh final runs assess the selected procedure. Here we know exact values, so we compute value error directly at checkpoints without collecting evaluation episodes. Without exact values, freeze V and compare predictions with independent return samples under the same policy and specified evaluation-state distribution. Squared error against sampled returns also contains irreducible return noise, so it is not automatically the same quantity as squared error against true values. Repeated evaluation returns can estimate conditional means more accurately. Choosing settings using the reported test runs makes the result optimistic. No new statistical estimator or implementation assignment is introduced.

Optional response to Exercise 6.5 if raised: with larger constant α, the early improvement can give way to fluctuation as the favorable initialization is forgotten; this pattern depends on the task/initialization and is not universal. Do not add this as a fourth live claim. Sources: book Exercises 6.4–6.5, p. 126 / PDF148; Figure 7.2; CS234 L3 p. 23.

## MT24c — Claim 3: “Same episodes means same cost”

**Time:** 3 minutes of the protected ten-minute activity. **Reuse:** a compact copy of the mean curve's episode axis and MT18's batch-versus-new-data distinction. New claim text.

**Display**

> “Both methods used 100 episodes, so their interaction and computation costs were equal.”

Vote: **supported or unsupported?**

**Reveal:** specify the budget.

| Budget | What to count |
| --- | --- |
| Interaction | Environment transitions, not only episodes |
| Computation | Updates, data passes, and time under a stated implementation |
| Tuning | Configurations and runs used to choose them |

> What does another pass through a fixed batch cost?

**Notes:** One minute vote and variable episode lengths, one minute batch/compute, one minute consolidation. Episode lengths vary. Our two independently seeded methods need not see equal transition totals at the same episode count, even though they use the same start and transition distribution. Under the generated every-visit protocol both methods make one update per visited nonterminal state, but their timing, storage and total sampled transitions can differ. MC waits for episode completion; TD updates online. Repeating the same batch adds data-processing cost without new interactions. For stronger interaction-matched claims, compare at matched cumulative transitions; wall-clock claims need measurements. Figure 7.2 reused the same walks across settings, helping control interaction variability, but that does not prove equal compute costs.

Close by asking students to name the checks actually used: meaningful baseline, multiple runs/uncertainty, fair tuning/sensitivity, separate final evaluation, declared budgets. These checks recur in A1 and the project; this slide adds no deliverable. Source: book §6.3 batch setup; generated CSV transition/update counts; CS234 L3 p. 23.

## MT25 — Choosing between MC, TD and n-step targets

**Time:** 3 minutes. **Reuse:** P29/31/36's reference-table purpose, rewritten with qualified claims. This replaces a separate plain closing summary.

**Display**

| Question | MC | TD(0) | n-step TD |
| --- | --- | --- | --- |
| Target | Complete return | One reward + V | n rewards + V if still running |
| Earliest update | Episode end | Next transition | n transitions or episode end |
| Target error | Unbiased under the fixed policy | Can inherit table bias | Horizon changes reliance on the table |
| Sampling variability | Often high | Often lower with a useful table | Often grows with horizon; not guaranteed |
| Useful when | Complete episodes are available; avoid a bootstrap target | Need immediate updates or discounted continuing prediction | Can wait for more evidence before bootstrapping |
| Dependence on V in the target | None | Direct | Through a surviving continuation |

TD shares continuation estimates using the Markov assumption. MC's completed target avoids that bootstrap; it does not solve partial observability.

**Choice needs evidence:** compare runs, tuning and budgets on the task.

Next: control with sampled targets. λ mixtures: Week 8.

**Notes:** About two minutes to revisit the practical choices and one to connect forward. The variability row states common tendencies, not a theorem for arbitrary V. For n reaching the episode end, the target is the full return; every-visit versus first-visit scheduling can still differ. MC's target has no V, but finite-data/constant-α estimates can retain initialization effects. TD/n-step targets can inherit errors from initial tables. For continuing tasks, the methods discussed here are ordinary discounted prediction; do not imply the same formula solves average-reward differential prediction. The earlier five-minute objective contrast introduced no such algorithm. No function-approximation convergence promises, universal MC/TD ranking or new λ derivation. Sources: P29/31/36, corrected under R28–R29; book §§6.2–6.3 and §7.1.

## Handoff checks

- Preserve accepted 3.1 and frozen inputs. This addition and its explicitly shared assets are the new first-render inputs; source status remains in the deck decision file.
- Check source plots against P32/P44, especially online versus batch identity, axes and α/n labels. Keep five-state and 19-state conventions distinct from the grid.
- Keep all worked answers, reset instructions and terminal-flush timing visible at their intended reveals. Retain the nine-minute exercise and the ten evaluation minutes plus two figure-reading minutes.
- Validate the generated figure at its final slide size. Its data, protocol and answer values must stay together if it is reconstructed natively. Do not substitute old cross-review statistics.
- Confirm displayed qualifications survive summarization, especially the final method table and the γ = 1 explanation. No unresolved content decision is being delegated to the renderer; raise new substantive issues in the shared review if rendering exposes one.
