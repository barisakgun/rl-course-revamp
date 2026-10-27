# Shared review: `model_free_control` (sessions 4.1–4.2)

**Shared** by Claude and ChatGPT (`docs/lecture_workflow.md`, step 2 onward). It holds findings, responses and
resolution status. Deck status and accepted/open outcomes live only in
[`decisions/lectures/model_free_control.md`](../../decisions/lectures/model_free_control.md). Resolving a finding
here does not accept a curriculum decision.

**File name.** The instructor chose `model_free_control` (D1, 2026-10-27). Claude's suggestion was renamed from
`control_targets_claude.md` to `model_free_control_claude.md`, with its content unchanged (SHA-256 still
`049c5aea…`), and the links below were updated.

## Claude cross-review of ChatGPT's suggestion — 2026-10-27

**Reviewed:**
- [`model_free_control_chatgpt.md`](model_free_control_chatgpt.md), as on disk 2026-10-27;
- for comparison, [`model_free_control_claude.md`](model_free_control_claude.md), as on disk 2026-10-27.

**Numbers checked.** Every number in ChatGPT's suggestion is arithmetically correct. `scripts/check_control_claude.py`,
section 3, reproduces:
- ε-greedy with ε = 0.2 and four actions: 0.85 / 0.05;
- MC bridge returns 0.19 / 0.46 / 1, and first-visit entries 0.19 and 1;
- grid targets: SARSA 0.06 → 0.08; Q-learning 0.36 → 0.23;
- cliff targets: SARSA −101 → −60.5; Q-learning −11 → −15.5;
- budget: 2 × 59.5 = 119 usable minutes; 116 planned; 21 slack.

R06 concerns whether one cliff snapshot entry is *plausible*, not the arithmetic.

### Where the two suggestions agree (independently)

- **One deck for 4.1–4.2.** Both recommend `model_free_control`. The session break falls after the target comparison
  and its policy interpretation.
- **Accepted boundaries respected:**
  - importance sampling in Week 8;
  - maximization bias and Double Q in 6.2;
  - optimism, bonuses and regret in Weeks 9 and 11;
  - Expected SARSA and softmax unscheduled;
  - no Sarsa(λ) or backward traces;
  - neither proposes moving anything back from the provisional Week 4 list.
- **Same running examples:** the 2×2 grid for 4.1 mechanics; book cliff walking as a separate, explicitly introduced
  task in 4.2.
- **No repeated policy-improvement proof.** The ε-soft improvement result is stated, not proved live. MC averaging is
  described without an unapproved N(s, a).
- **Q-learning as sampled Q-value iteration** (B24a; Abbeel L2 pp. 5–10). ε-greedy behaviour, greedy target.
- **The one-step no-IS explanation.** Both make the same correction of old P40's "because we already took the
  action": Q(S_t, A_t) conditions on the action taken, and the successor maximum is computed, not sampled.
- **Same old-deck corrections:**
  - P18's coverage and improvement claims qualified;
  - P43's "doesn't matter how you select actions" qualified (coverage, step sizes);
  - P44's notes: optimal path learned, but falls during exploration;
  - Expected SARSA removed from P21;
  - notation fixes (R_t → R_{t+1}, μ → b, true q versus estimate Q).
- **The cliff curve measures exploratory training return,** not the greedy policy's return. "Which is better" depends on
  the measure; this is the bridge to the project activity.
- **Timing:** 4.1 at 58 or less; 4.2 at 53 plus 5 administrative minutes; no use of the delivery allowance.

### Findings

| ID | Author, date | Where | Label | Issue and consequence | Proposed fix | Status |
| --- | --- | --- | --- | --- | --- | --- |
| R01 | Claude, 10-27 | ChatGPT C04, C07; Claude C05 | teaching risk | **Where pure greed is shown to fail.** ChatGPT's MC trace leaves Q((1,1), right) = 0.19 with the other actions at 0, so greedy keeps choosing right at (1,1). That costs nothing there: under q\* up and right tie at (1,1) (both 0.362). Students could conclude that greed was harmless. At (2,1) the loss is real: right scores 0.116 under always-right, up 0.800 (B14 numbers students already know). | Keep ChatGPT's MC trace (R12). Then ask "greedy now?" and move the lock-in question to (2,1), as in Claude C05: Q((2,1), right) ≈ 0.12, the other actions 0 and untried, while choosing up once is worth ≈ 0.80. Say "can lock in", not "must": a sampled target after a left slip, −0.04 + 0.5·Q((1,1), ·), can be negative. | resolved; ChatGPT response below |
| R02 | Claude, 10-27 | ChatGPT P25 "omit windy gridworld"; Claude C09 | teaching risk | **Why TD control rather than MC control.** ChatGPT cuts the windy gridworld, saying its purpose survives in the SARSA loop. But the book's main point there (Example 6.5) is not online updating in general. MC control is hard to use when a policy may never reach termination, because the episode never ends. Without that point, "why not wait for the episode?" has only MT25's variance and online arguments, which apply to prediction too. Claude kept windy at 3 minutes, which costs a second task setup, as ChatGPT notes. | Make the point on our own grid, with no new task: **always-left never terminates**. From (1,1), left either bumps the wall or slips up or down; from (1,2), left bumps, slips up into the wall, or slips down to (1,1). Neither column-2 cell is ever entered (checked in section 3). An MC control learner whose greedy policy becomes always-left waits forever. SARSA updates at every bump, so the estimates for left fall and the policy changes during the episode. About 2 minutes. The windy picture becomes optional (hidden backup). | open |
| R03 | Claude, 10-27 | ChatGPT C05 "state tie handling"; Claude C07 | teaching risk | **Tie-breaking at learning time.** A zero-initialized Q table is all ties. Both suggestions say "state the tie rule" but neither chooses one. Week 2 used a fixed order for DP improvement (B18 notes: keep the current action, otherwise up, right, down, left). In control, a fixed order makes the greedy branch systematically favour "up" while the table is flat. That biases early exploration and can mask the lock-in effect students are meant to see. The book's experiments break ties randomly (stated in the Figure 6.5 caption, §6.7, printed 135 / PDF 157, quoted in old P47's notes). | Use **random tie-breaking** among maximizing actions for ε-greedy action selection, stated on the ε-greedy slide. Say why it differs from Week 2's DP convention (there, ties only selected among exactly equal values; here early ties come from no data). The A1 starter should match; flag this to whoever prepares A1. | resolved; ChatGPT response below |
| R04 | Claude, 10-27 | ChatGPT 4.2 (no unit); Claude P08 | teaching risk (scope) | **The accepted 4.2 groups include `prediction`,** whose scope says the data-access taxonomy is "brief and revisited". ChatGPT's 4.2 has no revisit. Week 4 is where off-policy first becomes concrete: Q-learning can, in principle, use data from others or from older policies, but only covered pairs are learned. Week 5 (deadly triad) and Week 12 (fixed-data Q-learning failure) build on this. | Keep a 3-minute revisit of MT03 in 4.2 (Claude P08), paid for as in the consolidated sequence below. | resolved; ChatGPT response below |
| R05 | Claude, 10-27 | ChatGPT C05 (ε = 0.2), P02 (ε = 0.1) | optional preference | Two ε values in one deck. The book's examples, the old slides and the likely A1 default use 0.1. | Use ε = 0.1 throughout (0.925 / 0.025 with four actions). | resolved; ChatGPT response below |
| R06 | Claude, 10-27 | ChatGPT P03 | teaching risk | **The cliff snapshot's Q(S′, down) = −100.** ChatGPT correctly warns that a fall is not terminal. But −100 is what the action would be worth if it *were* terminal. Under the reset rule its value includes the continuation from the start: q\*(edge, down) = −100 + v\*(start) = −113 (γ = 1, v\*(start) = −13). The snapshot may confuse the very point the note makes. | Use Q(S′, down) = −113 (or "about −113"). SARSA target −114, giving −67.0; Q-learning unchanged, −11 giving −15.5 (checked). A one-line check question: why is it not −100? | resolved; ChatGPT response below |
| R07 | Claude, 10-27 | ChatGPT C12 + P03; Claude C14 + P03 | optional preference | Both suggestions have a single-transition calculation in each session; ChatGPT asks whether that is redundant (its choice 3). The purposes differ: 4.1 isolates the continuation action; 4.2 adds exploration cost and reset. | Keep both, but make the 4.2 calculation shorter (6 minutes) and follow it with Claude's exact route values (4 minutes): ε-greedy along the edge −51.8, the top path −22.3, best ε-greedy −20.7, greedy edge path −13. Those numbers explain the book's curve (about −50 vs about −25) quantitatively. For 4.1, adopt ChatGPT's simpler snapshot (0.06 → 0.08 vs 0.36 → 0.23); Claude's (0.085 / 0.385) is not needed. | open |
| R08 | Claude, 10-27 | ChatGPT 4.1 end; Claude C15 | teaching risk | **What each method converges to.** ChatGPT's 4.1 ends with the right question ("can the better greedy path have worse exploratory return?") but never says what each method learns with constant ε. SARSA approaches the best ε-greedy policy's values; Q-learning approaches q\*. Without that, 4.2's cliff explanation has to introduce it under time pressure. On the grid the difference is visible in values only: SARSA (1,1) 0.332, others 0.811; Q-learning 0.362, 0.853, with the same greedy actions. That is exactly why a cliff is needed. | 2–3 minutes in 4.1 (Claude C15), merged into ChatGPT's C13 synthesis. | open |
| R09 | Claude, 10-27 | ChatGPT P49–52 synthesis; Claude C16 | optional preference | Both replace Silver's DP/TD comparison images (old P50–51) with a native synthesis in course notation. ChatGPT: MC / SARSA / Q-learning only. Claude: each sampled method next to its DP counterpart (iterative policy evaluation ↔ TD(0); Q-policy iteration ↔ SARSA; Q-value iteration ↔ Q-learning). | One table: rows are MC, SARSA and Q-learning; columns are target, which policy's values, what is sampled, and the DP counterpart. That is one extra column, not an extra slide. | resolved; ChatGPT response below |
| R10 | Claude, 10-27 | ChatGPT P10; Claude E3 | **instructor choice** | ChatGPT's administrative minutes present the proposal due 1 November as upcoming. Week 4 started on 26 October, 29 October is a holiday, and lecture weekdays are unresolved (`schedule_decisions.yaml`). 4.2 may fall after the deadline, which would make "proposal expectations" stale and change the P08/P09 project activity's framing. | If after the deadline: the same 15 minutes refine the submitted baseline and metric toward the Week 7 formulation/design milestone, and the 5 administrative minutes cover that milestone and the A1 release. Planning minutes are unchanged either way. | open |
| R11 | Claude, 10-27 | ChatGPT P06; Claude P06–P07 | optional preference | **Two kinds of failure in 4.2.** ChatGPT debugs *implementation* errors in one loop: SARSA redraws its selected action; Q-learning executes the maximizer instead of the exploratory action; a goal transition bootstraps. Claude tabulates *learning-behaviour* failures by symptom, cause and check: no coverage, exploration cost, constant ε or α, seed variance, reward specification. Both serve A1, and they complement each other. | Keep both, shortened: ChatGPT P06 (5 minutes) and Claude's symptom table merged with ChatGPT P07's convergence-claim caveats (5 minutes). Claude's separate diagnosis exercise (P07, 4 minutes) is dropped to pay for this. | resolved; ChatGPT response below |
| R12 | Claude, 10-27 | Claude C04–C08 | maintenance (self) | Claude's MC bridge has no worked step: it states the loop and its result. ChatGPT's C07 traces one MC control cycle on the episode students already know (returns 0.19 / 0.46 / 1; the repeated first pair is skipped). That serves the bridge's `explain` mastery better and costs no new numbers. | Adopt ChatGPT's trace, then continue with R01's lock-in question. | resolved; ChatGPT response below |
| R13 | Claude, 10-27 | Claude E4; ChatGPT C03 | optional preference | The ε-soft improvement proof (book eq. 5.2, old P16). ChatGPT omits it; Claude proposed a hidden appendix slide. | Either. A hidden appendix costs no live time; omitting it removes one slide to maintain. | resolved; ChatGPT response below |

### Assumptions both suggestions share (step-2 check)

- **The Bellman equations for q.** The expectation form (B07) and the optimality form (B16) are taught and accepted, so
  "SARSA samples the expectation equation" and "Q-learning samples the optimality equation" rest on taught material.
  No gap.
- **Estimates of a moving target.** Both treat SARSA's Q as an estimate of q^π for "the current policy". But the
  policy changes whenever Q changes, so the target itself moves. Neither suggestion says this. It is the reason for
  constant α (MT07 already said "better for non-stationary problems") and the reason the policy improvement theorem
  only guides the method rather than guaranteeing each update. One sentence in C04 or C11, and in the notes.
- **Convergence conditions.** GLIE and Robbins–Monro step sizes appear only as spoken qualifications. MT07's footnote
  named Robbins–Monro, so the reference is not new. Neither suggestion examines it; keep it that way.
- **"Off-policy" without ratios.** Both say Q-learning needs no correction ratio and that ratio methods come in Week 8.
  Students must not infer that *all* off-policy learning is ratio-free. ChatGPT's C13 and Claude's C13 both say
  "one-step"; keep that word on the slide.
- **No live experiment.** Both rely on the book's published cliff curve. Claude's exact route values are computed, not
  simulated, so the declared-protocol requirement that 3.2 adopted for generated learning curves (D13) does not apply.

### Consolidated sequence proposal (for instructor comments)

Uses the findings above. Minutes are planning targets.

**4.1: targets sum to 57.5.**

| ID | Unit | From | Min |
| --- | --- | --- | ---: |
| C00 | Title | both | 0.5 |
| C01 | What changes when we want better behaviour? (GPI half fixed last week) | ChatGPT C01, Claude C01 | 2 |
| C02 | Brainstorm: learning to act without a model | Claude C02 | 3 |
| C03 | Why Q, not V (Q = take this action, then follow a specified policy) | ChatGPT C02, Claude C03 | 3 |
| C04 | Evaluation and improvement interleave; moving target (shared assumption) | ChatGPT C03, Claude C04 | 2 |
| C05 | Trace one MC control cycle | ChatGPT C07 (R12) | 3 |
| C06 | Would greedy work? Lock-in at (2,1) | Claude C05 (R01) | 3 |
| C07 | Exploration vs exploitation; exploring starts vs soft policies | Claude C06 | 2 |
| C08 | ε-greedy, ε = 0.1, random ties | ChatGPT C05, Claude C07 (R03, R05) | 3 |
| C09 | On-policy MC control with ε-greedy improvement (result stated) | ChatGPT C06, Claude C08 | 2 |
| C10 | Why not wait for the episode? Always-left never ends | R02 | 2 |
| C11 | SARSA: TD on action values (derivation) | both | 6 |
| C12 | Trace the SARSA loop | ChatGPT C10 | 3 |
| C13 | Q-learning: sampled Q-value iteration; behaviour vs target | both | 6 |
| C14 | Behaviour and target policies; one-step, no ratio | Claude C13, ChatGPT C13 | 2 |
| C15 | Your turn: same transition, two targets (ChatGPT numbers) | both (R07) | 10 |
| C16 | What each learns, and one synthesis table with DP counterparts | R08, R09 | 3.5 |
| C17 | Recap; question: can the better greedy path have worse exploratory return? | ChatGPT C13, Claude C17 | 1.5 |

MC bridge: C04, C05, C07 (the exploring-starts half) and C09, about 8 minutes.

**4.2: targets sum to 53, plus 5 administrative minutes.**

| ID | Unit | From | Min |
| --- | --- | --- | ---: |
| P00 | Section opener | — | 0.5 |
| P01 | Retrieve the target distinction | both | 3 |
| P02 | Cliff task; predict first (reset vs termination stated) | both | 3.5 |
| P03 | Work a target beside the cliff (−113 snapshot) | ChatGPT P03 (R06) | 6 |
| P04 | Why the routes differ: exact ε-greedy route values | Claude P03 (R07) | 4 |
| P05 | What did the curve measure? Which one "wins"? | ChatGPT P05, Claude P04–P05 | 6 |
| P06 | Debug one shared loop | ChatGPT P06 (R11) | 5 |
| P07 | Failure modes and what the convergence claims promise | Claude P06, ChatGPT P07 (R11) | 5 |
| P08 | Learning from others' data: MT03 revisited | Claude P08 (R04) | 3 |
| P09 | Project: question, baseline, metric (protected) | both | 15 |
| P10 | Synthesis; Week 5 boundary | both | 2 |
| P11 | Administration (R10) | both | (5) |

### Consequential choices for the instructor

1. **Deck name and split** (both recommend one deck, `model_free_control`).
2. **R02:** the always-left grid argument in place of the windy gridworld (which becomes optional), versus cutting the
   point (ChatGPT) or keeping windy (Claude's original).
3. **R10:** the project activity and administrative minutes if 4.2 falls after the 1 November proposal deadline.
4. **R11 / R04:** 4.2's mix (loop debugging, failure-mode table, data-access revisit), as in the consolidated sequence.

Everything else is a straightforward correction or preference that the AIs can settle.

## ChatGPT cross-review of Claude's suggestion — 2026-10-27

**Reviewed revisions:**
- [Claude's independent suggestion](model_free_control_claude.md), SHA-256 `049c5aeac4d27a20f10d624556a4380da48c64773558a5f5107ac592862c782c`.
- [ChatGPT's independent suggestion](model_free_control_chatgpt.md), SHA-256 `114e2ee5bc038b3ef542eedc5c7c70b1c2a66bf6710221aa4fc4bd4b2fc92a62`.
- Claude's R01–R13 and consolidated proposal above, as present in this shared file on 2026-10-27 (before this addition). References below explicitly distinguish original slide IDs from consolidated IDs.

This is the requested cross-review, not acceptance of the consolidated sequence. Both initial suggestions and Claude's checking script were left unchanged. The script's model/policy definitions were read for this review only; calculations below were checked independently, without executing or adopting that script. Accepted scope is [topic_decisions.yaml](../../decisions/topic_decisions.yaml); `mc_td` D18–D19 and O6 remain closed/unchanged as appropriate. No deck-status record is created here.

**Overall judgment.** The proposals agree on the essential progression: why Q, why exploration, a short MC bridge, SARSA/Q-learning, then cliff interpretation and evaluation. Claude's explicit grid lock-in example and sampled Q-value-iteration bridge are useful. The major corrections concern quantities being compared, the difference between exact policy evaluation and learning guarantees, and preservation of the next action in SARSA. Keep a concrete cliff target exercise; three computed route returns cannot replace it. The current consolidated sequence remains a proposal pending the open findings below.

### Checks completed

- Claude's original targets sum to **57.5** minutes for 4.1 and **52.5 teaching + 5 administration** for 4.2. The consolidated proposal above sums to **57.5** and **53 + 5**. ChatGPT's original targets are **58** and **53 + 5**. These fit the unchanged allocations; none needs the delivery allowance. Target sums do not establish teaching feasibility.
- Claude C14's arithmetic is correct: targets 0.085 / 0.385 and updated entries 0.1425 / 0.2925. R14 concerns the trajectory, not arithmetic. Both proposals' terminal targets are correct for independent goal transitions.
- Independently evaluating all 64 deterministic greedy choices on the accepted 2×2 model, with ε = 0.1, reproduces the state values **0.331793, 0.810622, 0.810622**, in state order `(1,1), (2,1), (1,2)`. Greedy actions can be up/up/right. The corresponding **greedy-action q^π values** are **0.341369, 0.849121, 0.849121**. Optimal state values/maxima of q^* are **0.361818, 0.852727, 0.852727**. This establishes R15.
- Independent linear policy evaluation on the book's 4×12 cliff reproduces start returns **−51.813188** (edge-row policy) and **−22.272817** (top-row policy), with ε = 0.1. The epsilon-soft optimal start value is **−20.707677**. For these route policies, actions go up to the chosen row, right along it, down if above it, and down in the goal column. This specification includes actions away from the displayed route. These are exact-policy benchmarks, not simulated learning results or a reproduction of the book's curve.
- Sources checked against the claims: the old control deck/PDF; configured book §5.4, printed pp. 100–103 / PDF122–125 (including the exact-evaluation qualification on p. 103); §6.4, pp. 129–130 / PDF151–152; §6.5/Example 6.6, pp. 131–132 / PDF153–154. The source coverage in ChatGPT's suggestion also supplies relevant CS285/CS224R comparisons missing from Claude's short source list; this is not a requirement to add their advanced topics.

### New findings

All entries below are by **ChatGPT, 2026-10-27**. Open entries await Claude's response or the indicated instructor choice. Resolution of a technical finding does not accept a curriculum or example choice.

#### R14 — error — Claude original C14: the terminal case changes the selected action

C14 selects `A′ = down` at `(1,2)`, then calls `(1,2), right, +1, goal` the **next transition**. In the SARSA loop just taught, down must actually be executed next. This example would teach the redraw bug that ChatGPT's P06 is meant to expose. The same ambiguity should be avoided in ChatGPT C12's terminal variant.

**Fix:** label the goal case **a separate terminal transition, reset the exercise**, rather than a continuation of the first trajectory. No number or time change is necessary. Source: book §6.4 algorithm, PDF152, `S ← S′; A ← A′`. **Response:** pending. **Status: open.**

#### R15 — error — Claude original C15, R08 and consolidated C16: state values are labelled as learned Q values

The 0.332 / 0.811 numbers are **v^π for an epsilon-greedy policy**, averaging over its first action. SARSA learns action values **q^π(s,a)**, which condition on the first action; at the specified greedy actions these are 0.341369 / 0.849121. The 0.362 / 0.853 Q-learning column consists of maxima over q^*, not a complete Q row. Presenting these as “which values each learns” hides the distinction that motivated Q. Moreover, matching greedy actions in these benchmark policies does not guarantee identical finite-time behaviour during learning.

**Fix:** preferably retain the qualitative policy distinction and omit this extra numerical table. If retained, compare q^π and q^* at the **same named state-action pairs**, with the corrected numbers, and label them exact reference values under stated policies, not demonstrated learning limits. Alternatively show v^π versus v^* and explicitly explain that these are derived state values. **Response:** pending. **Status: open.**

#### R16 — error — Claude C04/C08/C11/C15 and R08: an exact improvement result is being used as a learning guarantee

The delta correctly qualifies old P18, but C04 says the theorem applies unchanged and C08 infers that the proposed **constant-α** MC loop approaches the best epsilon-soft policy. The book's improvement statement assumes exact q^π (printed p. 103); finite sampled updates do not guarantee improvement at every step, and constant α is not a general sample-path convergence guarantee. C11's GLIE-plus-step-size qualification is useful and should remain. A bare `ε_k = 1/k` example must not substitute for the actual condition of persistent state-action coverage in a sequential MDP.

**Fix:** distinguish the exact improvement result, the practical sampled loop, and the conditions of a convergence claim. Say the result motivates moving toward greediness; estimates and the policy change together, and a noisy update may make behaviour worse. Present fixed-policy numbers as benchmarks (R15/R18), not outcomes guaranteed for constant-step learning. Keep conditions in plain language; drop the decay formula and extra proof rather than adding a convergence lesson. **Response:** pending. **Status: open.**

#### R17 — error — Claude original P03–P04: scope the cliff mechanism

“Q-learning's max never [includes falls]” can imply that Q-learning ignores observed penalties. It still uses the **actual** −100 reward and continuation from the reset state on a fall. What its target omits is averaging over the *next exploratory action*; the maximum represents greedy continuation. Likewise, adding unspecified motion slips does not necessarily make the optimal path move away: that depends on slip probabilities and costs. The 0.025 fall probability applies to states immediately above cliff cells when down is a nongreedy action, not every state on the whole route.

**Fix:** make those qualifications explicit in the calculation/route discussion. Change the slip answer to “the optimal values change; the preferred route **can** change.” Keep the fall/reset versus terminal check from ChatGPT P03. Source: book eq. 6.8 and Example 6.6. **Response:** pending. **Status: open.**

#### R18 — teaching risk — Claude original P03–P04, R07 and consolidated P03–P05: fixed-policy returns do not replace a worked target

Original P03 gives three full-episode expected returns and calls them the worked target difference, without an actual SARSA/Q-learning target calculation. The consolidated six-minute target exercise addresses that gap. The subsequent route values are numerically correct, but require the complete policy away from the route, ε, tie handling and reset convention. They are not what a finite learning run must attain; approximate agreement with a published curve is illustration, not validation of a learner.

**Fix:** retain the concrete six-minute target/reset exercise. Prefer the diagram and qualitative route explanation within the following four minutes, with exact values in notes. If numbers are displayed, label them fixed-policy computations, specify the complete route policies in notes, and start with the two route comparisons; the third “best epsilon-soft” number introduces an optimization result that is not needed to explain the target. This is the remaining teaching choice behind R07, not a failed arithmetic check. **Response:** pending. **Status: open.**

#### R19 — teaching risk — Claude C09, R02 and consolidated C10: distinguish nontermination from long exploratory episodes

The proposed always-left **deterministic** policy on the accepted grid indeed cannot leave the left column. It is a useful counterexample to assuming all policies terminate. It is not the epsilon-greedy MC policy just introduced: with fixed ε > 0, right/up actions remain possible and this finite grid reaches the goal with probability one. Describing the current exploratory MC learner as necessarily waiting forever would undermine the preceding exploration explanation. The same qualification matters when adapting the book's windy-grid warning, which concerns termination under arbitrary policies.

**Fix:** keep the familiar-grid example if desired, explicitly label ε = 0 for the nonterminating counterexample, then say exploration repairs that particular coverage problem while MC still must wait for episode completion; TD can update during long episodes. Do not promise SARSA escapes every improper initialization/policy. I support this qualified two-minute example over introducing a second grid solely for this point; no backward or multi-step control content is needed. **Response:** pending. **Status: open.**

#### R20 — error — Claude E4 and the paragraph after the original 4.1 timing sum: allowance does not authorize a live proof

The main sequence and R13 correctly avoid a proof. E4 nevertheless offers a four-minute live derivation from the allowance, and the timing paragraph repeats that option. The accepted `control_targets` pacing note says **“No repeated policy-improvement proof.”** Extra delivery minutes do not waive accepted exclusions.

**Fix:** withdraw that live alternative; keep the statement/intuitive connection. An optional hidden reference is a separate choice and must create no required reading or assessment. No instructor question is needed merely to obey the existing exclusion. **Response:** pending. **Status: open.**

#### R21 — teaching risk — Claude P06/P07 and R11: noisy returns are not evidence that Q failed to converge

A constant-ε **return curve** can fluctuate even when estimates/policy are stable, because actions and episodes vary. Constant α affects estimate noise; constant ε affects behaviour and ongoing exploratory cost. “Never settles → use GLIE decay” blurs these quantities and can recommend removing exploration when it is intentionally retained.

**Fix:** identify what is fluctuating, inspect visitation and Q/policy changes separately, and distinguish training return from frozen-policy evaluation. Keep the symptom table as a diagnosis exercise with multiple possible causes, not an automatic schedule prescription. This strengthens the proposed combination of loop debugging and behaviour diagnosis without adding minutes. **Response:** pending. **Status: open.**

#### R22 — teaching risk — Claude P09 and consolidated P09: the worked project example needs an interaction budget

The worked example gives “episodes, seeds” as its budget. In cliff walking, methods produce different episode lengths and resets do not end an episode. Equal episode counts therefore need not mean equal interaction budgets, exactly the issue `mc_td` MTE2 introduced. Seeds count independent runs; they do not define the per-run interaction budget.

**Fix:** model the expected answer using a transition budget per run, number of independent runs, and separate evaluation episodes; report computation as relevant. Distinguish training falls/return from final greedy-policy return and name the primary question. Students may choose another budget if they justify it. The 15-minute activity stays unchanged. **Response:** pending. **Status: open.**

#### R23 — maintenance — ChatGPT old-deck delta P53–61: correct the later placement of bonuses

My initial suggestion incorrectly grouped **exploration bonuses** with Week 9. Accepted `model_exploration` places them in **11.2 `model_limits`**, alongside model uncertainty and corrective data; bandit optimism/UCB/regret are in 9.2. Claude's distinction is correct. This review records the correction without rewriting the independently reviewed suggestion or changing curriculum state.

**Response:** ChatGPT accepts the correction; use the accepted placements in subsequent content. **Status: resolved.**

### ChatGPT responses to Claude's R01–R13

“Resolved” here means the reviewer accepts the technical fix or a common recommendation is available. It does **not** mean the instructor has selected the sequence, examples, deck name or assignment conventions.

| Finding | ChatGPT response, 2026-10-27 | Disposition |
| --- | --- | --- |
| R01 | Agree to use `(2,1)` and the known 0.116 versus 0.800 continuation comparison for the exploration question. My C04 did not specify the state; the MC trace alone was never evidence of a suboptimal greedy choice. Keep the distinction explicit: same grid, a new hypothetical Q snapshot, and possible failure to obtain evidence rather than guaranteed permanent lock-in. | resolved |
| R02 | The always-left observation is correct for a deterministic policy; the conclusion about the epsilon-greedy learner needs R19. I support the qualified familiar-grid version. | open; see R19 |
| R03 | Agree to recommend uniform random tie-breaking among maximizing actions, with the four-action probability example explicitly assuming a unique maximum. For ties, split the greedy-branch mass among maximizers. Communicate the convention to later A1 preparation; this review does not edit or accept its starter. | resolved |
| R04 | Support a brief MT03 revisit, funded within the consolidated 53 teaching minutes. Its function is to distinguish fresh/fixed data and behaviour/target, not to teach the deadly triad or offline RL early. A group reference alone does not require reteaching every topic in that group. | resolved |
| R05 | Agree to use ε = 0.1 consistently (0.925/0.025 with a unique maximum); 0.2 was an arithmetic convenience, not a substantive choice. No A1 default is accepted here. | resolved |
| R06 | −100 is valid as the explicitly arbitrary in-progress estimate I proposed; it need not equal a converged action value. Still, −113 makes the reset continuation easier to explain. Support that illustrative replacement, giving −114 → −67, without relabelling the whole supplied snapshot a converged SARSA table. | resolved |
| R07 | Agree that the two exercises have different purposes and support the simpler 4.1 numbers. Exact route returns versus a qualitative route explanation remains open under R18. | open |
| R08 | Agree that students need the distinction between the behaviour policy's action values and optimal action values before the cliff. Do not adopt the displayed numbers or unconditional convergence language; R15–R16 give the corrections. | open |
| R09 | Support one compact synthesis. Mark the DP relation as an analogy, not identical update schedules; MC's complete-return target has no one-step DP counterpart, so a blank/brief GPI note is better than forcing one. Omit the extra column if it crowds the policy/target distinction. | resolved |
| R10 | Agree that the real session date is unresolved. My initial P10 already called for rechecking the decision record. Keep the accepted allocation now; if delivery is after November 1, ask the instructor about milestone framing before producing dated content. Do not move the deadline or transfer class minutes automatically. | open; instructor/calendar |
| R11 | Support the mix of concrete loop debugging and a short symptom/check discussion, with R21's distinction between behaviour noise and estimate instability. The consolidated 5 + 5 minutes is a reasonable recommendation, not established delivery feasibility. | resolved as a sequencing recommendation; R21 still open |
| R12 | Agree to keep a worked MC cycle. Specify first-visit **state-action pairs**, hold the episode's policy fixed, then improve. Choose either sample averaging in words or a clearly labelled constant-step example; do not change estimator halfway through the trace. No N(s,a) addition is required. | resolved |
| R13 | Prefer omitting the appendix proof, but either omitted or explicitly optional is compatible with the scope. No live derivation: R20 corrects the original alternative. | resolved for the optional-reference preference; R20 still open |

### Remaining choices and handoff boundary

The main remaining design choices are the combined deck/name and familiar-grid continuity; whether exact cliff-policy benchmarks earn live time (R18); and project framing once the actual delivery date is known (R10). The qualified always-left example (R19) and the 4.2 debugging/data-access mix now have ChatGPT support, subject to the corrections and instructor selection. Routine arithmetic, quantity labels, trajectory consistency and source-placement fixes should be resolved by the AIs rather than presented as instructor preferences.

Claude's original C04–C08 contains less worked MC reasoning than ChatGPT's bridge; the proposed consolidation repairs that. Its end-of-4.1 synthesis also combines policy interpretation, numerical comparisons and a DP correspondence table in 3.5 minutes: omit the extra C15 numbers first if that is too dense, protecting the ten-minute target exercise. In 4.2 protect the 15-minute project activity and five administrative minutes. No hidden appendix becomes prerequisite work, and no time is borrowed from accepted 3.1–3.2 or Week 8.

Small provenance correction for later reuse: old P44 shows **Example 6.6, printed p. 132**; Claude's limitations section calls it the Figure 6.4 region. Figure 6.4 is the backup-diagram comparison on printed p. 134. Use Example 6.6 as the cliff citation.

This completes ChatGPT's requested review pass and responses. New open findings await Claude's response; the consolidated sequence is not yet a mutually cleared or instructor-accepted result. No render-ready content, PPTX, curriculum changes, notation-guide edits or calendar changes were made.

## Claude responses to ChatGPT's R14–R23, and closing check — 2026-10-27

**Reviewed:** this file as on disk 2026-10-27 (SHA-256 `273ff060…`, after ChatGPT's addition); Claude's suggestion
unchanged (`049c5aea…`). R15's corrected values are reproduced in `scripts/check_control_claude.py` (last line):
q^π at the greedy pairs 0.341369 / 0.849121 / 0.849121; q\* at the same pairs 0.361818 / 0.852727 / 0.852727.

| Finding | Claude response, 2026-10-27 | Status |
| --- | --- | --- |
| R14 | Accepted. My C14 selected A′ = down and then continued with (1,2), right: that is the redraw bug. The goal case becomes a separate terminal transition with its own reset. The consolidated C15 uses ChatGPT's numbers and needs the same label. | resolved |
| R15 | Accepted. 0.332 / 0.811 are v^π of the ε-greedy policy, not Q entries; the Q-learning column was max_a q\*. Consolidated C16 keeps the qualitative statement (SARSA estimates q^π of the ε-greedy policy it follows; Q-learning estimates q\*) and moves the corrected same-pair numbers to the notes, labelled as exact reference values for stated policies. The 3.5 minutes then go to interpretation and the synthesis table. | resolved |
| R16 | Accepted. Slides and notes will separate (1) the exact improvement result, which motivates moving toward greedy; (2) the sampled loop, where estimates and policy change together and a noisy update can make behaviour worse; and (3) convergence conditions, in plain words (every pair keeps being tried; step sizes shrink suitably; for SARSA, exploration fades in the limit). The ε_k = 1/k formula is dropped. This also covers the "moving target" assumption above. | resolved |
| R17 | Accepted, all three points. Q-learning's target does use the observed −100 and the continuation from the start; what it omits is averaging over the next exploratory action. The slip answer becomes "the optimal values change; the preferred route *can* change". The 0.025 applies at cells directly above the cliff, where down is nongreedy. | resolved |
| R18 | Accepted in its conditional form. The six-minute target/reset exercise stays (consolidated P03). In P04 I still recommend *showing* two numbers, because they make the book's curve readable at a glance: ε-greedy around the edge route ≈ −52, around the top route ≈ −22 (greedy edge route −13). Label them fixed-policy expected returns, with the full route policies and the reset convention in the notes. The best-ε-soft value (−20.7) goes to the notes. ChatGPT preferred notes only; this is a presentation preference, listed below for the instructor, not a correctness question. | resolved technically; minor preference open |
| R19 | Accepted. The always-left example is labelled ε = 0, a deterministic policy, and is used to show that MC needs episodes to end. With ε > 0 this grid terminates with probability 1, so exploration repairs that particular case; MC still waits for completion, while TD updates during long episodes. No claim that SARSA escapes every bad initialization. | resolved |
| R20 | Accepted. The live-derivation alternative in E4 and the timing paragraph of my suggestion are withdrawn: the delivery allowance does not override "No repeated policy-improvement proof". With R13, the default is no proof slide at all; an optional hidden reference remains possible, with no reading or assessment. | resolved |
| R21 | Accepted. The failure-mode table becomes a diagnosis exercise with several possible causes per symptom. It separates what fluctuates (return, Q estimates, greedy policy, visit counts), separates training return from frozen-policy evaluation, and does not prescribe decaying ε when exploration is deliberate. | resolved |
| R22 | Accepted. The worked project example uses a transition budget per run, a number of independent runs, and separate evaluation episodes, with the primary question named. That ties to MTE2's "same episodes, different cost". | resolved |
| R23 | Agreed (ChatGPT's own correction). | resolved |
| Provenance | Accepted: old P44 shows Example 6.6 (printed p. 132); Figure 6.4 is the backup diagrams (p. 134). Cite Example 6.6. | resolved |

**ChatGPT's responses to R01–R13.** I accept them, including its qualifications:
- R03: split the greedy mass among tied maximizers;
- R04: the revisit distinguishes fresh vs fixed data and behaviour vs target only;
- R06: −113 as an illustrative replacement, not a converged table;
- R09: the DP column is an analogy, with no one-step counterpart for MC;
- R12: first-visit *state–action pairs*, policy held fixed during the episode, one estimator throughout.

R02, R07 and R08 are now settled by R19, R18 and R15–R16.

**Effect on the consolidated sequence.** No unit, order or minute changes: 4.1 targets sum to 57.5; 4.2 to 53 plus 5
administrative minutes. The fixes change content and labels inside units:
- C10 (ε = 0 label);
- C15 (separate terminal transition);
- C16 (qualitative plus notes);
- P03 (−113 entry);
- P04 (two labelled numbers);
- P07 (diagnosis framing);
- P09 (transition budget).

### Status after this pass

Every technical finding (R01–R23) is resolved between the AIs. Agreement is not acceptance. These items need the
instructor:

1. **Deck:** one deck for 4.1–4.2, named `model_free_control` (both AIs recommend).
2. **Running examples:** the 2×2 grid for 4.1 (MC trace, lock-in at (2,1), the ε = 0 always-left case in place of the
   windy gridworld, the target exercise), and book cliff walking for 4.2. Both AIs recommend. This is a cross-session
   example choice.
3. **R10, project framing:** whether 4.2 is delivered before or after the 1 November proposal deadline. After it, the
   15-minute activity refines the submitted baseline and metric toward the Week 7 formulation/design milestone, and the
   5 administrative minutes cover that milestone and the A1 release. Allocations are unchanged either way.
4. **R18, minor:** show the two fixed-policy route returns on the cliff slide (Claude), or keep them in the notes
   (ChatGPT).
5. **Basis for first-render content:** the consolidated sequence with the R01–R23 fixes, as `mc_td` D8 and D15 did.

**A1 note (not a lecture decision):** random tie-breaking among maximizers (R03) should reach whoever prepares the A1
starter.

## Instructor choices — 2026-10-27

Recorded as D1–D5 in [`decisions/lectures/model_free_control.md`](../../decisions/lectures/model_free_control.md):
- one deck;
- the AIs' example recommendations;
- project timing handled by the instructor outside the deck, which closes R10;
- the cliff route returns shown initially (R18);
- the merged sequence with the R01–R23 fixes as the basis for first-render content (step 4).

No finding remains open.
