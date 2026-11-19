# Week 6 (`dqn_loop` and `dqn_diagnosis`, sessions 6.1–6.2): initial content suggestion (Claude)

**Claude's step-1 suggestion** (`docs/lecture_workflow.md`, pilot v2), 2026-11-15. Analysis only: nothing here is
accepted. It becomes historical after step 3. No deck decision file exists yet. The instructor's choices will go to
`decisions/lectures/<deck>.md`; E1 below proposes the deck name. I have not read any ChatGPT file for this deck.

**Scope of this file:**
- the teaching sequences for 6.1 `dqn_loop` and 6.2 `dqn_diagnosis`;
- the old-deck delta for `8 - Deep QL.pptx` (24 slides, 1 hidden), for slides 46–48 of
  `5 - Model Free Control.pptx` (maximization bias and Double Q-learning, moved here by `model_free_control`) and
  for slides 57–58 of `6 - Value Function Approximation.pptx` (incremental versus batch, offered by
  `function_approximation` D8);
- early choices for the instructor (E1–E11).

All numbers are checked by `scripts/check_deep_q_learning_claude.py` (§ numbers below refer to its sections).

## Early choices for the instructor

Each has a recommendation; drafting continues with the recommendation unless the instructor says otherwise.

| # | Choice | Recommendation | Alternative |
| --- | --- | --- | --- |
| E1 | Deck split and name | One deck for 6.1 and 6.2, as in Weeks 2–5. Name: `deep_q_learning` (the old deck's title). | `dqn`; `dqn_loop` (first session id); two decks. |
| E2 | 6.1 worked trace (accepted: "trace replay, target construction and parameter updates in one loop") | **A three-position corridor with two actions and four weights** (A12–A13). q̂(s, a, **w**) = **w**_a · (1, position), so one output per action and a gradient students can compute by hand. One loop: act, store, sample three transitions, targets from **w**⁻ with one terminal transition, TD errors, one minibatch step, the copy. The step makes a prediction rise although its own error was negative, which is the reason targets move. | The 2×2 grid (four actions): network outputs supplied as a table, targets and errors computed, no weight-level update. Keeps the running example, loses "parameter updates". |
| E3 | 6.1 "recorded example" (feasibility note: small-task or recorded, no live long run) | The Atari results from Mnih et al. (2015) as the recorded example: old 15 plus one result figure. | A course-generated learning curve from a small task. It needs a learner that does not exist yet, and it must not be A2's own replay/target comparison. |
| E4 | Where Atari goes | **At the start (A02), as the motivation**: what a network buys, before any mechanism. | The old deck's place, after the algorithm (old 15). |
| E5 | Fitted Q-iteration and "incremental versus batch" (old 7–8; old Value Function Approximation 57) | One bridge inside A06: store experience and fit to it, with the batch extreme named in one line. Old 7's "we have seen the linear version as Least Squares Q-Learning" is removed, because LSTD/LSPI were cut in Week 5. | Old 7 as its own slide (+3 minutes in 6.1, taken from A15–A16). |
| E6 | Target-network update rule | **Hard copy every C updates** is the taught rule (Mnih 2015, book §16.5). Polyak averaging gets one line on A16. The lecture and A2's "target-network update" hook should use the same rule; I recommend the hard copy for both. | Polyak averaging as a second loop slide (old 14). It needs a symbol for the rate: τ is open item O5 in the notation guide. |
| E7 | Notation not in the guide | Needs approval before rendering (details under "Notation"): replayed transition (s_j, a_j, r_j, s′_j) with target U_j; TD loss L(**w**); copy period C; the two tables Q₁, Q₂; "minibatch" and "done" in words. | Keep the old deck's y for the target and N for the copy period. N clashes with N(s). |
| E8 | 6.2 single example for the 20-minute block | **Coin-flip estimates, then one table with two rows of estimates** read three ways: max of one row (Q-learning), select with one row and evaluate with the other (Double Q-learning), online row selects and target row evaluates (Double DQN). Book Example 6.7 stays as a three-minute figure (old Model Free Control 47). | Book Example 6.7 as the main worked example. It is a simulation result, with no hand calculation. |
| E9 | 6.2 ablation material (accepted: "small environments or supplied traces") | The Mnih 2015 replay × target table (local copy: Silver L6 p. 41, CS234 L4 pp. 74–76) plus two constructed toy traces (§§2–3). | Course-generated runs. Same objection as E3: this is A2's own experiment. |
| E10 | Old-deck extensions | **Cut** prioritized replay (old 19–20), dueling networks (old 21) and parallel Q-learning (old 6); one pointer line to Rainbow (old 23) on B13. This is the accepted feasibility note for 6.2. Prioritized replay also needs importance weights, which are out until 8.2. | Hidden appendix slides. |
| E11 | Delivery allowance | 6.1 slide targets sum to 57.5 minutes, 2.5 above the 55-minute allocation: fine for delivery under the 63-minute allowance, planning estimate unchanged. The extra time is motivation (A02, A05, A08). 6.2 sums to 53.5. | Drop A15 (does it work?) to 1 minute and A16 to 1 minute: 6.1 = 54.5. |

## Accepted frame

From `decisions/topic_decisions.yaml` and `output/lectures/session_sources.md` §6.1–6.2.

**6.1 `dqn_loop` (DQN as approximate Q-learning).** 55 teaching minutes (range 50–65), delivery allowance up to 63.
Requires 5.2 `instability` and 4.1 `control_targets`.
- Worked activity: trace replay, target construction and parameter updates in one loop.
- Feasibility note: small-task or recorded example, not a live long training run.
- Groups:
  - `deep_value` (core; explain / implement / analyze; live): one DQN loop and replay/target ablations using small
    environments or supplied traces. Topics: `dqn`, `experience_replay`, `target_networks`.
  - `approximation` (core): nonlinear approximation motivates DQN; no separate neural-network course.

**6.2 `dqn_diagnosis` (Double estimators and experimental diagnosis).** 55 teaching minutes (range 48–65).
Requires 6.1.
- Worked activity: bias / Double Q / Double DQN contrast (20 minutes), then replay/target ablation reasoning
  (15 minutes). Within the same example, map online selection versus target evaluation to the Double DQN patch
  (3–5 minutes inside the double-estimator segment).
- Feasibility note: Rainbow and the extension catalog are removed; protect the main DQN mechanism.
- Groups:
  - `maximization_bias_core` (core; explain / analyze): explain and diagnose maximization bias in Q targets; connect
    action selection and evaluation to Double DQN. No extra lecture block.
  - `double_dqn_core` (core; explain / implement): only the target-selection patch inside the supplied DQN learner;
    no benchmark study and no performance-win requirement.
  - `double_estimators` (exposure; explain): tabular Double Q-learning as a contrast; no implementation.
  - `evaluation` (core; analyze): baseline, training versus evaluation, seeds and uncertainty, interaction versus
    compute budgets, interpreting ablations.
  - `deep_value`, as above.

**Constraints from other decisions.**
- **No importance sampling** before 8.2 (`model_free_control` D6). One-step Q-learning from replay needs none.
  Prioritized replay would; it is cut (E10).
- **Expected Sarsa** is exposure only. It appears in one notes sentence (A07).
- **No hedging on slides** (2026-11-12): conditions and "this is not…" statements are in the notes column of the
  tables below, marked "Notes:".
- **Readings:** none assigned in current planning. Paper and book pointers stay optional.
- **Midterm 2** coverage is decided before that midterm. A2's `exam_bridge` says it may assess DQN/replay/target
  reasoning; the old Spring 2025 MT2 Q2 did exactly that (effect of a replay buffer and a target network on bias,
  variance, non-stationary targets and correlated samples). A14 and B09 prepare that kind of question.

**Assessment link.** A2 (release Week 6, due Week 9; prerequisites `linear`, `instability`, `dqn_diagnosis`):

| A2 hook | Prepared by |
| --- | --- |
| DQN TD loss | A10, A12 (errors and loss by hand) |
| Terminal mask | A10, A12 (sample 5), B07 (third transition), B12 |
| Target-network update | A09, A13 (the copy), B12 |
| Replay sampling | A06, A12 (sampled indices) |
| Double DQN target-selection switch | B06–B07 |
| One controlled replay/target comparison, diagnosis from traces | B08–B10 (method and protocol; a different task from A2's) |

The lecture uses a hand-sized corridor and a published table, so it does not hand out A2's code or its result. No
slide says that Double DQN wins.

## What students already have

- **Week 4** (`model_free_control`): Q-learning's target R_{t+1} + γ max_a Q(S_{t+1}, a); behaviour b and target π;
  the one-step Q-learning target needs no correction; ε-greedy; cliff walking; a one-line forward pointer to
  maximization bias (P06).
- **Week 5** (`function_approximation`, done, D20):
  - q̂(s, a, **w**), the semi-gradient update and the two targets (F15); terminal target U_t = R_{t+1};
  - "treat the target as fixed for this step" (F08);
  - one output per discrete action (F04, right panel); learned features feeding a value head (F17);
  - I02: one update raises its own target (10 → 10.8, target 18 → 19.44); the deadly triad (I06); Baird (G10);
  - G12b: nonlinear Q-learning is ✗ (can diverge); its notes say DQN is nonlinear Q-learning;
  - G14: "We want richer value functions, reusable experience and more stable targets. Next: DQN…".
- **Weeks 3–4 evaluation** (MTE1–MTE2, P06): narrower claims, intervals over seeds, comparable tuning, budgets in
  transitions, fresh final runs.
- **Entry background** (`config/course.yaml`): basic machine learning. Minibatch SGD, backpropagation and
  train/test separation are assumed; A03 spends no time on them.

## Is the old material substantial?

**Yes for 6.1, partly for 6.2.** `8 - Deep QL.pptx` gives the 6.1 mechanism slides (old 3–15) and the Double DQN
slides (old 16–18). Its other slides are extensions that the accepted plan removed. The maximization-bias half of
6.2 comes from `5 - Model Free Control.pptx` 46–48. The ablation and evaluation half of 6.2 has no old slides: it is
new, built from the Mnih table and the Weeks 3–4 evaluation slides. The old deck has no worked activity; both
protected activities are new. I did not need to ask.

## Central idea and the motivation thread

**6.1: DQN is Week 5's semi-gradient Q-learning with two changes to what it learns from.** The update rule is
F15's. What changes is the data fed to it and the target it chases:
1. **Which transitions?** Not the last one, used once, but a random minibatch from a buffer of stored transitions.
2. **Which target?** Not one computed from the weights being changed, but from a copy that is held still for a while.

Each change answers one named problem from Week 5 (G14's three wishes): the network gives richer values, replay
gives reusable and mixed experience, the target network gives more stable targets. The trace (A12–A13) then shows
all three in numbers: a shared-weight step that raises a prediction whose own error was negative, a target that
would have jumped from 0.30 to 0.43, and a target that stays at 0.20 until the copy.

**6.2: two questions about a working loop.**
1. **Is the target right on average?** The max of noisy estimates is too high on average, even when every estimate
   is unbiased. Selecting and evaluating with the same numbers is the cause; splitting the two jobs is the fix. DQN
   already has two networks, so the fix is one line.
2. **How do we know which part helps?** Remove one part at a time, keep the rest fixed, and report it so that
   someone else could believe it.

The two halves share one statistical idea, and B10 says so: picking the best run, checkpoint or learning rate and
then reporting its score is the max of noisy estimates again.

**Explicit motivation time** (memory "motivation first").
- **6.1:** about 20 of 57.5 minutes before or between mechanisms: A01–A02 (what we want and what it buys), A04–A05
  (what breaks), A07 (why replay is allowed at all), A08 (the moving target, on Week 5's own numbers), the first
  half of A09.
- **6.2:** about 15 of 53.5: B01–B01a (the puzzle in real DQN curves), B02–B03 (a bias students compute before it
  is named), B08's "predict the table before reading it", B10's "would you believe this?".

## Teaching sequence for 6.1 `dqn_loop` (slide level, unpolished)

Slide IDs are proposals. Minutes are planning targets. "Old N" means `8 - Deep QL.pptx` slide N in PPTX numbering
(the PDF omits hidden slide 24). "VFA N" and "MFC N" are the old Value Function Approximation and Model Free
Control decks.

| ID | Slide | Content and reason | Sources | Min |
| --- | --- | --- | --- | ---: |
| A00 | Title | Title Slide layout: course name; **Deep Q-Learning** / instructor / Fall 2026. | deck title format; old 1 | 0.5 |
| A01 | Three wishes from last week | G14's line, split in three: richer value functions, reusable experience, more stable targets. G12b's bottom-right cell (nonlinear Q-learning ✗). Today each wish gets one mechanism. Replaces old 2 ("Notes"). Notes: the mechanisms reduce the problems; none restores a convergence guarantee. | G12b, G14; old 2 (rewritten) | 2 |
| A02 | What a network buys: Atari from pixels | Old 15 moved to the front (E4). One agent, one architecture and one set of hyperparameters for 49 games; input is pixels, not hand-made features (contrast F10–F11, Mountain Car's tiles). State = last four frames: ask why (old 15's "why?"). Answer: one frame has no velocity; link to 1.1 observation versus state. Reward = change in score. Notes: results with their scope and date (Mnih et al. 2015: at or above 75% of the human tester's score on 29 of 46 games, book p. 438; some games near random, e.g. Montezuma's Revenge, book p. 441); stacking does not remove partial observability in every game (book p. 438). | old 15; book §16.5 printed 436–441 / PDF 458–463; CS234 L4 pp. 71–73; Silver L6 pp. 39–40 | 4 |
| A03 | The network: one output per action | q̂(s, ·, **w**): state in, one value per discrete action out (old 3's right panel, F04's right panel). Why this form: one forward pass gives max_a and argmax_a. It needs a finite, small action set (Week 7 picks up continuous actions). No neural-network teaching. | old 3 (picture; text cut to this point); F04, F17; book p. 439 | 2 |
| A04 | First try: F15's update with a network | Old 4's loop in course notation: act ε-greedily, observe one transition, U = r + γ max_a q̂(s′, a, **w**) (U = r at a terminal), **w** ← **w** + α[U − q̂(s, a, **w**)]∇q̂(s, a, **w**), with ∇ by backpropagation. Old 5 merged: the target is treated as a constant. Ask old 4's question, "what could go wrong?", and collect: (1) consecutive transitions look alike and each is used once; (2) the target changes with every step; (3) the target is not differentiated. (3) is the semi-gradient choice from F08 and stays; today is about (1) and (2). | old 4–5 (merged, notation fixed); F08, F15; book eq. 16.3 p. 439; CS234 L4 p. 63 | 4 |
| A05 | Problem 1: the data arrive in the wrong order | One episode's transitions come from one part of the state space; the next minutes of data come from another. Toy with one shared weight (§3): targets +1 for group A, −1 for group B, α = 0.5. In blocks AAAA BBBB the weight goes to 0.94 and then to −0.88: it tracks whatever came last and forgets the rest. Mixed, it stays at the best fit. Second cost: each transition is used once and thrown away, while environment steps are the expensive part. Notes: with a network the same effect is called catastrophic interference; the toy is supervised regression, not RL. | new (§3); old 3 ("states are correlated"), old 4; CS285 L8 p. 3 (figure idea); VFA 57 ("not very sample efficient") | 3 |
| A06 | Experience replay | Keep the last N… transitions in a buffer 𝒟 (bounded, oldest out first: old 12's "indirect point" made direct). Each step: store the new transition, then sample a minibatch uniformly from 𝒟 and update on it. VFA 57 as the bridge: incremental methods update once per transition; batch methods store and refit; replay sits between (E5). Old 9–10 merged, with Levine's buffer picture (old 10). Fixes: "samples are no longer correlated" → "a random minibatch mixes old and new experience"; "does use a single explorative policy" removed (the buffer holds data from many past policies). | old 9–10, 12 (footer); VFA 57; book p. 440; Silver L6 p. 38; CS234 L4 p. 64 | 4 |
| A07 | Why are we allowed to replay? | Check: "the transitions in 𝒟 were generated by older, different policies. Why can Q-learning still use them? Could Sarsa?" Answer: Q-learning's target needs (s, a, r, s′) only; the max supplies the next action, whoever generated the data (Week 4 C13). A stored Sarsa target would use the action an old policy took. Book: replay "requires an off-policy algorithm" (p. 438). Notes: Expected Sarsa could recompute the expectation under the current policy (exposure only). Replay does not make the data on-policy: updates follow the buffer's mix of states, which is the "other state weighting" row of G12a, so the off-policy leg of the triad is still present. No importance sampling appears. | Week 4 C13; G12a; book pp. 438, 440; CS234 A2 written question (replay) | 3 |
| A08 | Problem 2: the target moves | I02 again: one update, 10 → 10.8, and the target went from 18 to 19.44. Repeat it: 10 → 10.8 → 11.664 (factor 1.08 per update, §2). The learner chases a target that runs away at the same time. CS234's wording: the update uses the target as a number, but the weights change on the next round and change the target. | I02 (Week 5); §2; old 4 ("fast changing"); CS234 L4 p. 65; book p. 440 | 2 |
| A09 | The target network | Keep a second copy of the weights, **w**⁻, used only to compute targets: U = r + γ max_a q̂(s′, a, **w**⁻). Hold it still; every C updates copy **w**⁻ ← **w** (old 11, w′ → **w**⁻). Between copies the problem is ordinary regression on fixed labels. Same example with C = 5 (§2): the target stays 18 for five updates, w goes 10.8, 11.52, …, 13.28 toward 18; then the copy moves the target to 23.9. Ask CS285's two questions: why is this good, why is this bad? Good: a stable problem between copies. Bad: targets are up to C updates out of date, so new information spreads more slowly. CS234 check: it doubles the memory, not the computation. Notes: in this example w still grows across copies (×1.33 per period against ×1.47 for five moving-target updates): freezing slows the feedback, it does not remove it. Convergence is not guaranteed. | old 11; §2; CS285 L8 pp. 4–7; CS234 L4 pp. 66, 68–69; book p. 440 | 4 |
| A10 | Target and loss for a minibatch | For each sampled (s_j, a_j, r_j, s′_j): U_j = r_j if s′_j is terminal, else r_j + γ max_a q̂(s′_j, a, **w**⁻). L(**w**) = mean over the minibatch of ½[U_j − q̂(s_j, a_j, **w**)]². One gradient step on L with U_j held constant gives F15's update, averaged. Only the output for the action taken, a_j, has an error. Old 13 ("mini mini-batching") merged, sum → mean. Notes: in code the terminal case is a mask, r + γ(1 − done)·max; the network returns numbers for any input, including a terminal state, so the mask is required; U_j is computed without gradient tracking. | old 13 (fixed); F15; CS234 L4 p. 67 (terminal case); Silver L6 p. 38 (loss) | 3 |
| A11 | The DQN loop | Old 12 rebuilt in course notation as a five-step box: (1) act ε-greedily on q̂(s, ·, **w**); (2) store (s, a, r, s′) in 𝒟; (3) sample a minibatch from 𝒟; (4) targets from **w**⁻, one gradient step on **w**; (5) every C updates, **w**⁻ ← **w**. Three clocks in one loop (CS285's three processes): collecting data, updating **w**, updating **w**⁻. Fixes to old 12: add the terminal case to the target; "if D is not big enough: repeat" → "start learning after a warm-up"; w′ → **w**⁻; N → C. | old 12 (rebuilt); CS234 L4 p. 67; CS285 L8 pp. 8, 10–12; Abbeel L2 pp. 33–34; book §16.5 | 3 |
| A12 | **Your turn: trace one loop (targets and errors)** | **Protected (with A13): 14 minutes.** Corridor: positions 1, 2, 3; goal to the right of 3 (terminal, +1 on entry, 0 otherwise); a wall to the left of 1; actions L and R; γ = 0.5. q̂(s, a, **w**) = **w**_a · (1, position). Given tables of the six online outputs and six target outputs (§1). (a) Act: at position 3 the online outputs are L 0.40, R 0.60; the greedy action is R; store (3, R, +1, goal, done) as transition 5. (b) The sampled minibatch is transitions 2, 4, 5: (2, L, 0, 1), (2, R, 0, 3), (3, R, +1, goal, done). (c) Targets from **w**⁻: 0.10, 0.20, 1. (d) TD errors: −0.20, −0.20, +0.40; loss 0.04. (e) What would transition 5's target be without the terminal case? 1.25. About 2 minutes setup, 4 work, 2 discussion. | constructed (§1); A2 hooks | 8 |
| A13 | **Your turn: the update and the copy** | (f) One step with α = 0.3 on the mean (0.1 per sample): **w**_L (0.1, 0.1) → (0.08, 0.06); **w**_R (0, 0.2) → (0.02, 0.28). (g) New online outputs for R: 0.30, 0.58, 0.86. The prediction for (2, R) rose from 0.40 to 0.58 although its own error was −0.20: the goal transition outvoted it through the shared weights. Position 1's R output moved without being in the minibatch. (h) Recompute transition 4's target: from **w**⁻ it is still 0.20; from the online weights it would have gone from 0.30 to 0.43. (i) Now copy **w**⁻ ← **w**: the target becomes 0.43 in one jump. About 3 minutes work, 3 discussion. Notes: the corridor is linear so that the gradient is the feature vector; with a network backpropagation supplies ∇ and everything else is unchanged. q^\* for R is (0.25, 0.5, 1), which this model cannot represent exactly; the trace shows mechanics, not convergence. | constructed (§1); F12a (two samples pull shared weights) | 6 |
| A14 | What each part changed | Three rows read off the trace: network → richer values (shared weights, and their side effect in g); replay → mixed and reused experience (b); target network → targets that move in jumps (h, i). The old exam's four words (bias, variance, non-stationary targets, correlated samples) as a check: which part acts on which? Notes: answers from Spring 2025 MT2 Q2: replay acts mainly on correlation and reuse, and averages over a minibatch; the target network acts on non-stationary targets; neither removes bootstrapping bias. | A12–A13; old 10, 22; `exams/spring25/mt2` Q2 | 2 |
| A15 | Does it work? | Recorded example (E3): Mnih 2015's results figure, or a short clip. One reading question: what is on the vertical axis, and what was it compared with? (A linear learner on hand-made features, a human tester, random play.) Old 22's "need to be patient". | old 15, 22; book pp. 437–438; CS234 L4 pp. 72–73 | 3 |
| A16 | The rest of the recipe | One slide, no formulas: ε decays from high to low; rewards and errors are clipped to keep step sizes comparable across games; a warm-up before learning; typical sizes (minibatch 32, a buffer of about a million transitions, C in the thousands) with their source. Old 22's tuning list. Polyak averaging as one line (E6). Fix: old 14's "init: random or all zeros" is wrong for a network (all-zero weights keep hidden units identical). | old 14, 22; book pp. 439–440; CS285 L8 pp. 19–20; Abbeel L2 p. 34 | 2 |
| A17 | Summary and the question for 6.2 | DQN = semi-gradient Q-learning + a network + replay + a target network. Question: every target takes a max over estimates that are noisy. Is the target right on average? | old 22 (first half) | 2 |

**Targets sum to 57.5 minutes** (§8; E11). Protected: A12–A13 (14 minutes).

## Teaching sequence for 6.2 `dqn_diagnosis` (slide level, unpolished)

| ID | Slide | Content and reason | Sources | Min |
| --- | --- | --- | --- | ---: |
| B00 | Session opener | Section divider "Double estimators and experimental diagnosis" (same deck). | — | 0.5 |
| B01 | Recap and two questions | The loop in five steps (A11). Today: (1) are the targets right on average? (2) how do we find out which part of the loop helps? | A11, A17 | 2 |
| B01a | A puzzle in real learning curves | van Hasselt et al. (2016): DQN's value estimates on Atari games next to the discounted returns its policy actually obtains. The estimates are higher. CS285 shows the same figure under "Are the Q-values accurate?". Ask: an unbiased, noisy estimate would be too high half the time. Why always too high? Notes: figure and claim from the Double DQN paper; that paper is not in the local sources, so the figure and its caption must be checked before rendering. | CS285 L8 pp. 15–16; CS224R L6 p. 19; van Hasselt et al. 2016 (arXiv 1509.06461) | 3 |
| B02 | **Your turn: all the true values are zero** | **Protected block B02–B07: 20 minutes.** A state with two actions, both worth exactly 0. Each estimate is the truth plus a coin flip: +1 or −1. (a) List the four cases and the max in each. (b) Average: E[max] = 0.5, though the true max is 0. (c) With three actions? 0.75. Four? 0.875 (§4). MFC 46's wording as the reveal ("our estimation involves a maximization step… maximization leads to positive bias"). | MFC 46; book §6.7 printed 134 / PDF 156; §4 | 4 |
| B03 | Why: selecting and evaluating with the same numbers | The max picks whichever action had the luckiest error, and then reports that same lucky number as its value. In symbols: 𝔼[max_a Q(a)] ≥ max_a 𝔼[Q(a)]. In Q-learning this max is inside every target (MFC 46's update, R_t → R_{t+1}), and bootstrapping passes the excess to earlier states. More actions and more noise give more bias: with standard normal errors, 0.56 for 2 actions, 1.03 for 4, 1.82 for Atari's 18 (§4). Notes: the estimates need not be biased individually; MFC 46's question "are MC control methods affected?": greedy selection over noisy estimates is, but an MC target contains no max, so the excess is not fed back through targets. Sarsa with ε-greedy also selects with a max (book p. 134). | MFC 46; book §6.7; Sutton 11-12-TD pp. 44–45; CS285 L8 p. 17; §4 | 3 |
| B04 | It changes behaviour: the book's example | MFC 47 (book Figure 6.5). From A, right ends with 0; left goes to B, whose many actions each pay a reward with mean −0.1 and variance 1. Vote first: how often will ε-greedy Q-learning go left early on? Reveal the curve: about 90% at the peak, against the 5% that ε = 0.1 forces. Our reproduction with 10 actions in B: 93% at episode 25, 12% at episode 300; Double Q-learning 24% and 7% (§6). | MFC 47; book Example 6.7 printed 134–135 / PDF 156–157; Sutton 11-12-TD p. 46; §6 | 3 |
| B05 | Double Q-learning: two estimates, two jobs | Keep two tables, Q₁ and Q₂, learned from different samples. One selects, the other evaluates: Q₂(s′, argmax_a Q₁(s′, a)). On each step a coin decides which table is updated (book eq. 6.10; MFC 48's box, exposure). Back to B02 with a second, independent coin-flip estimate: the selected action's second estimate averages 0 (§4). One table with two rows for a three-action state, true values 0: Q₁ = (0.6, −0.3, −0.1), Q₂ = (−0.2, 0.4, −0.4). Max of each row: 0.6 and 0.4. Crossed: Q₂ at Q₁'s choice = −0.2; Q₁ at Q₂'s choice = −0.3 (§5). Notes: the double estimate is unbiased for the value of the *selected* action, which can be below the best action's value: with true values (1, 0) and coin-flip noise, the single estimator averages 1.25 and the double estimator 0.75 (§4). It doubles memory, not computation per step (book p. 135). | MFC 47 (text box), 48; book §6.7 printed 135–136 / PDF 157–158; Sutton 11-12-TD pp. 45–47; §§4–5 | 3 |
| B06 | Double DQN: we already have two networks | DQN's target, U = r + γ max_a q̂(s′, a, **w**⁻), selects and evaluates with **w**⁻. Double DQN: select with the online network, evaluate with the target network: U = r + γ q̂(s′, argmax_a q̂(s′, a, **w**), **w**⁻). Same loop, same two networks, one line changed (old 16–17; old 18's contrast with the two symmetric tables). Read B05's table again with row 1 = online outputs and row 2 = target outputs, r = 0, γ = 0.9: DQN target 0.36, Double DQN target −0.18 (§5). Fixes: old 16's Q^T → q̂(·, **w**⁻); "due to noise, this is an overestimate (and thus biased)" → "too high on average"; old 17 gets the terminal case. Notes: **w**⁻ is an old copy of **w**, so the two are not independent as Q₁ and Q₂ are: the bias is reduced, not removed. No claim that Double DQN scores higher; A2 awards nothing for that. | old 16–18; CS285 L8 pp. 17–18; CS224R L6 pp. 20–21; van Hasselt et al. 2016; §5 | 3 |
| B07 | **Your turn: two targets for a minibatch** | Three sampled transitions, γ = 0.9, with online and target outputs at s′ given (§5). (1) r = 0; online (1.0, 2.0, 1.5), target (1.2, 1.4, 1.8): DQN 1.62, Double DQN 1.26. (2) r = 1; online (0.5, 0.2, 0.1), target (0.9, 0.3, 0.4): both 1.81. (3) r = −1, terminal; any outputs: both −1. Questions: when do the two agree? (Same argmax in both networks, or a terminal transition.) Can the Double DQN target be the larger one? (No: it evaluates one action with **w**⁻; DQN takes the largest **w**⁻ output.) This is A2's switch and A2's terminal test, by hand. | constructed (§5); A2 task 4; CS285 hw3 (format) | 4 |
| B08 | **Ablation: remove one part at a time** | **Protected block B08–B10: 15 minutes.** The 2 × 2 design: replay on/off × target network on/off, everything else fixed. Predict first: which cell is worst, and which single part helps more? Then the table for five games (Mnih 2015 as in Silver L6 p. 41). Reading tasks: the full method is best in all five; replay alone beats the target network alone in four of five, and Seaquest reverses it (823 against 1003); Breakout: ×76 from replay alone, ×3 from the target network alone (§7). | Silver L6 p. 41; CS234 L4 pp. 74–76; book p. 441; §7 | 4 |
| B09 | **Explain the table from the mechanisms** | For each cell, students say what the learner is fed and what it chases, using 6.1's two toys as supplied traces. Trace 1 (§3): blocks against mixed samples, the weight swings 0.94 → −0.88 against staying at 0. Trace 2 (§2): moving against frozen target, 14.69 against 13.28 after five updates, with a jump at the copy. Then three short symptom descriptions to match to a removed part: (i) evaluation return rises, then collapses whenever the agent spends a long time in one region; (ii) predicted values climb steadily while evaluation return stays flat; (iii) learning is slow but steady, and each environment step is used once. CS234's question: beyond correlation, what else does replay give? (Reuse: many updates per environment step.) Notes: suggested matches are (i) no replay, (ii) no target network, or maximization bias, (iii) no replay with a small step size; real runs can show the same symptom for other reasons (step size, exploration, a bug), so a symptom suggests a check and does not prove a cause. | §§2–3; A05, A09; CS234 L4 p. 76; CS285 L8 pp. 10–12; `exams/spring25/mt2` Q2 | 6 |
| B10 | **Would you believe this table?** | Vote, as in MTE1: "replay matters more than the target network": supported, unsupported, or needs a narrower claim? Then the protocol questions from the accepted `evaluation` scope: What is the baseline? Were scores measured on separate evaluation episodes or on ε-greedy training episodes? How many seeds, and how large is the run-to-run spread? Were all four cells given the same environment steps, and the same tuning effort? Was one thing changed at a time? Link to B02: reporting the best checkpoint or the best learning rate is a max over noisy scores. Notes: narrower claim: five games, one architecture, one budget. Mnih 2015 report, for this table, the highest evaluation score over checkpoints and over three learning rates after 10 million frames per agent; this protocol detail is from memory of the paper's Extended Data Table 3 and must be verified against the paper before rendering (it is not in the local sources). CS285: results are "very inconsistent between runs", so run several seeds. Replay changes compute, not interaction: more gradient steps per environment step (MTE2's budget point). | MTE1–MTE2 (Week 3); P06 (Week 4); CS285 L8 p. 20; Mnih et al. 2015 | 5 |
| B11 | Is my DQN learning? What to plot | Four curves and what each can tell: evaluation return of the greedy policy on separate episodes (the result); training return (includes exploration); average max_a q̂ over a fixed set of held-out states (smoother than return; compare its level with actual discounted returns, as in B01a); TD loss. Ask: should the TD loss go to zero? Notes: the loss is measured against targets that move, and against a changing data mix, so it need not fall while the agent improves; a falling loss does not show a good policy either. Rising value estimates with flat returns suggest overestimation or instability (G13's weight-norm and error diagnosis, now for a network). | G13 (Week 5); B01a; Mnih et al. 2013 (average-Q curve; not local, verify); CS285 L8 pp. 15–16, 19 | 5 |
| B12 | Four places where DQN code goes wrong | The A2 hooks as a symptom table, without code: terminal case missing (values near the goal too high; A12e's 1.25); target computed from **w** or with gradients flowing through it (A13h); the copy never happens, or happens every step; sampling the most recent transitions instead of uniformly (A05). Each has a fixed-input test: known outputs in, known target out, as in B07. CS285's advice: test on an easy, reliable task first. | A2 tasks 2 and 4; A10–A13, B07; CS285 L8 p. 19 | 4 |
| B13 | What DQN leaves open | The max over actions needs a small discrete action set: continuous actions lead to policy methods (Week 7). Other improvements exist (prioritized replay, dueling networks, multi-step targets, Rainbow): names and one pointer only (old 23). | old 23; CS234 L4 p. 77; Abbeel L2 p. 45 | 2 |
| B14 | Summary | A max over noisy estimates is too high on average; split selection from evaluation. Change one part at a time; state the baseline, the budget, the seeds and what was measured. A2 opens: the loop's four hooks and the Double DQN switch. | old 22 | 2 |

**Targets sum to 53.5 minutes** (§8). Protected: B02–B07 (20 minutes; the Double DQN mapping is B06–B07's
selection/evaluation reading, about 4 minutes of the 7) and B08–B10 (15 minutes).

## Old-deck delta

### `8 - Deep QL.pptx` (PPTX numbering; H = hidden)

| Old slides | Decision | Where / why |
| --- | --- | --- |
| 1 | **Fix** | A00: new title format. |
| 2 ("Notes") | **Fix** | A01: its point ("the groundwork is there; today is the tricks") becomes the three-wishes opener. |
| 3 | **Keep picture, cut text** | A03: the one-output-per-action panel. The left panel (state and action in) was F04. "Divergent behaviour (states are correlated, single step gradients, …)" is taken apart in A04–A05, A08. |
| 4 | **Keep, fix** | A04: the loop and "what were some issues?". Q_w(s, a) → q̂(s, a, **w**); α_w → α; y → U; "f(s, a) if V is linear" → **x**(s, a). |
| 5 | **Merge** | A04: "treating U_t as a constant" in one line; it is F08's semi-gradient. |
| 6 | **Cut** | Parallel Q-learning: another way to mix data, outside the accepted scope. Its purpose (decorrelation) is served by A05–A06; parallel actors can return with actor-critic in Week 8. |
| 7 | **Compress** | A06, one line (E5). "We have seen the linear version as Least Squares Q-Learning" is removed (LSTD/LSPI cut in Week 5). "Policy must have broad support" goes to the notes of A07 and returns in the offline unit (12.1). |
| 8 | **Cut** | The two GPI pictures: they motivated "don't go over the entire batch every time". A06 says it directly; the pictures were used in Weeks 2 and 4. |
| 9–10 | **Keep, merge, fix** | A06: steps and Levine's buffer picture. Fixes: "no longer correlated" → mixes old and new; "does use a single explorative policy" removed; "(I will stop mentioning this from now on)" removed. |
| 11 | **Keep, fix** | A09: w′ → **w**⁻; "OR do Polyak averaging" → A16 (E6); "helps with fast-changing targets!" kept, with the cost added. |
| 12 | **Keep, rebuild** | A11: loop box in course notation; terminal case added; warm-up wording; N → C; circular buffer stated on A06. |
| 13 | **Merge, fix** | A10: minibatch update, sum → mean, "mini mini-batching" name dropped. |
| 14 | **Compress, fix** | A16, one line. The rate's convention differs from most sources (old: w′ ← τw′ + (1 − τ)w with τ near 1); "init: random or all zeros" is wrong for networks. |
| 15 | **Keep, move** | A02 (motivation) and A15 (results). "Superhuman performance in many games!" gets its scope and date in the notes. |
| 16–17 | **Keep, fix** | B06: the two targets; Q^T → q̂(·, **w**⁻) throughout; terminal case; wording of the bias sentence. Old 17's full loop is not repeated: only the changed line is shown. |
| 18 | **Keep, compress** | B05–B06: the contrast in one sentence; the paper's Algorithm 1 image is replaced by the book's box (MFC 48). |
| 19–20 | **Cut** | Prioritized replay (E10): accepted feasibility note; needs importance weights (D6). |
| 21 | **Cut** | Dueling networks (E10). The advantage it "remembers" is introduced in Week 7. |
| 22 | **Keep, split** | A14, A16, A17, B14: the summary lines and the tuning list. "Double Q-learning: reduce the effect of maximum bias" → B14. |
| 23 | **Keep, compress** | B13: one pointer line; "Q-learning with continuous actions" → the Week 7 question. Multi-step Q-learning is not taught here. |
| 24 (H) | **Cut** | Planning note ("Include rainbow in lectures?"): answered by the accepted plan. |

### `5 - Model Free Control.pptx` 46–48 (moved here by `model_free_control`)

| Old slides | Decision | Where / why |
| --- | --- | --- |
| 46 | **Keep, rebuild** | B02–B03: its four-line argument becomes the coin-flip exercise and its explanation. R_t → R_{t+1}. "Are MC control methods affected?" answered in B03's notes. |
| 47 | **Keep** | B04: book Figure 6.5 with a vote before the reveal. The two update equations at the bottom are dropped (they are F15's). |
| 48 | **Keep (exposure)** | B05: the Double Q-learning box. "The FA version is similar" is replaced by B06, which is the version actually used. |

### `6 - Value Function Approximation.pptx` 57–58 (offered by `function_approximation` D8)

| Old slides | Decision | Where / why |
| --- | --- | --- |
| 57 | **Keep, compress** | A06: incremental / batch / growing batch / limited buffer as the bridge to replay. "Find the best fitting value function" is dropped (least squares was cut). |
| 58 (H) | **Cut** | Shorter duplicate of 57. |

**Teaching purpose of cut material** (workflow step 1):
- **Prioritized replay, dueling, Rainbow:** "what came after DQN". Kept as one pointer (B13); the accepted plan
  removed the catalog to protect the main mechanism.
- **Parallel Q-learning:** a second answer to correlated data. Replay answers it in scope; parallel collection fits
  Week 8.
- **Fitted Q-iteration as its own slide:** the batch view of Q-learning. One line now (E5); the offline unit (12.1)
  is its accepted home.
- **Polyak averaging as its own loop:** one line (E6); Week 9's SAC can show it if needed.

## Reference courses: what was used

Evidence, not authority. Page numbers are in the local copies under `sources/<id>/lectures/`.
- **CS285 L8** (pp. 3–20): regression view of the target network and its "why good / why bad" questions (A09); the
  three-process picture (A11); overestimation and the selection/evaluation split (B01a, B06); practical tips,
  including multiple seeds (B10–B12). Its n-step and continuous-action parts are not used.
- **CS234 L4** (pp. 63–77): the two named problems and two fixes (A04); pseudocode with the terminal case (A10–A11);
  the memory-versus-computation check (A09); the ablation table and "what else does replay do?" (B08–B09). Maximization
  bias is reading-only there.
- **CS224R L6** (pp. 7–25) and the Q-learning tutorial (pp. 32–39): target networks and Double DQN in the same
  order as here; its n-step part is not used.
- **Silver L6** (pp. 38–41): replay and fixed targets in six lines (A06, A09), the loss (A10), the ablation table (B08).
- **Abbeel L2** (pp. 33–34, 45): DQN details and the Rainbow list (A16, B13). Image-based slides; not re-inspected
  beyond the session index's description.
- **Sutton 11-12-TD** (pp. 44–47): maximization bias and double learning (B03–B05).
- **Book:** §16.5 for DQN's own description (A02, A06, A09, A16); §6.7 for B02–B05.

Not in the local sources and needed for B01a, B10 and B11: Mnih et al. (2013, 2015) and van Hasselt et al. (2016).
The claims that rest on them are marked "verify" above.

## Notation

From `course/notation_guide.md`: **w**, q̂(s, a, **w**), ∇q̂, **w**⁻, 𝒟, U_t, δ_t, α, ε, γ, b, π. Conversions from the
old decks (O9 style):
- Q_w(s, a) → q̂(s, a, **w**); Q_w′ and Q^T → q̂(·, **w**⁻); w′ → **w**⁻;
- y → U; D → 𝒟; α_w → α; f(s, a) → **x**(s, a); R_t → R_{t+1} (MFC 46);
- Q^A, Q^B (old 18's paper image) → Q₁, Q₂ (book).

**Missing, needs approval (E7):**

| Item | Needed by | Proposal |
| --- | --- | --- |
| A replayed transition and its target | A10–A13, B06–B07 | (s_j, a_j, r_j, s′_j) with index j for the position in the minibatch, and U_j for its target. Lower case because these are stored values; the guide's R_{t+1} indexing stays for the time-indexed update on A04. |
| TD loss | A10, B11 | L(**w**). Not VE(**w**) (a different quantity) and not J (policy objective). |
| Copy period | A09, A11 | C, as in the book and Mnih. The guide's c is the UCB coefficient (lower case, Week 9). The old deck's N clashes with N(s). |
| Minibatch and its size | A10 | Words only ("mean over the minibatch"). B would clash with B^π. |
| Terminal indicator | A10, B07 | Two-case target on slides; "done" appears only in code-style text and notes. |
| Two tabular estimates | B05 | Q₁, Q₂ as in the book, labelled "subscript = which table" on first use (the guide uses subscripts for time and sweeps). |
| Polyak rate | A16 | Words on the slide ("move **w**⁻ a small step toward **w** after every update"). A symbol waits for O5. |
| Buffer capacity | A06 | Words only. |

## Prerequisite and timing checks

- **No forward references.** 6.1 uses Weeks 4–5 and entry-level machine learning. 6.2 uses 6.1 and the Weeks 3–4
  evaluation slides. No importance sampling, no n-step targets, no advantage function.
- **Worked activities protected:** A12–A13 (14 minutes) in 6.1; B02–B07 (20) and B08–B10 (15) in 6.2, as accepted.
- **Totals:** 6.1 targets sum to 57.5 (allocation 55; fine for delivery under the 63-minute allowance; planning
  estimate unchanged). 6.2 targets sum to 53.5 (allocation 55).
- **Density:** 6.1 has four new objects (network output form, buffer, target network, minibatch loss) and each is
  used in the trace. 6.2 has two (double estimator, ablation protocol). No slide introduces a method that is not
  used again.
- **Hidden workload:** none. No reading or video is assigned.
- **Scope claims:** no state-of-the-art claim. Atari results are given with their paper and year. Convergence is
  not claimed anywhere; the notes of A01, A07 and A09 say what the mechanisms do not guarantee.
- **Week 7 interface:** B13 ends on continuous actions, which 7.1 `reinforce` opens with.

## Open points to carry into the cross-review

1. E2: corridor or grid for the trace.
2. E6 and A2: one target-update rule, and the same loss (squared, as on A10, or Huber), in lecture and assignment.
3. E7: notation approvals.
4. B01a, B10, B11: three facts to verify against papers that are not in `sources/`.
5. B09: whether the three symptom descriptions should be replaced by course-generated curves in a later offering
   (`analysis/ideas_backlog.md` candidate; not proposed for now).
