# Policy gradients · shared cross-review

**Shared** review file for the `policy_gradients` deck (sessions 7.1–7.2); `docs/lecture_workflow.md` step 2. Findings,
responses and resolution status live here. Outcomes and the deck's status live in the
[deck decision file](../../decisions/lectures/policy_gradients.md).

## Claude review of ChatGPT's initial suggestion · 2026-11-21

Reviewed [ChatGPT's suggestion](policy_gradients_chatgpt.md), SHA-256 prefix `61c41996eaf4`, against the
[accepted sessions](../../decisions/topic_decisions.yaml), the instructor's choices made before this review
([D1–D4](../../decisions/lectures/policy_gradients.md)), [A3](../../decisions/assignment_decisions.md), the
[Week 6 handoff](../../decisions/lectures/deep_q_learning.md) (D13, D17) and the book (Chapter 13). Claude's own
suggestion is [policy_gradients_claude.md](policy_gradients_claude.md) (`04f5c4100688`); it is a step-1 file and stays
unchanged. Statuses are Claude's view; agreement between the AIs is not acceptance.

### Overall

**The two suggestions agree on the structure.** One deck `policy_gradients`; history → stochastic parameterization →
derivation in the accepted order; the trajectory (path) derivation with the dynamics dropping out, then causality and
reward-to-go; the policy gradient theorem as the conditional-mean form of the same result, without the book's proof;
the sample calculation set up at the end of 7.1 and finished in 7.2's first 8 minutes; the baseline identity from the
zero-mean score; a learned baseline whose prediction enters the actor update as a fixed number (A3's
"accidental baseline gradient"); a critic that bootstraps, and an example where its error turns the actor the wrong
way. Neither adds reading, video or assessment.

**The main difference is the worked example.** ChatGPT uses a constructed two-step fork (γ = ½) for every calculation
and the old aliased gridworld for the stochastic-policy motivation. Claude uses the book's short corridor (γ = 1) for
both. That choice (C04) is the one consequential decision left for the instructor.

**Numbers checked.** I recomputed ChatGPT's answer key; all values are correct:
- episode returns 3 and 2; reward-to-go sum 3(½) + ½·2(−½) = 1; preference 0 → 0.1 at α = 0.1; full-return sum 0;
- upper-state rows: mean 0.5, variance 2.25; centred at 3: variance 0; baseline 10: contributions −3 and 4, variance
  12.25;
- values: upper 3, lower 1; start q = 3.5 / 2.5, v = 3, A(right) = +0.5; the sample's centred return 0;
- wrong critic (upper 0, lower 1): targets 2 and 2.5, ranking reversed. I add one number for the answer key: the start
  state's expected actor contribution is −0.125 with the wrong critic against +0.25 with the true action values, so
  the direction flips, not only the ranking.

**Timing.** ChatGPT's targets sum to 59 (3 + 4 + 3 | 4 + 5 | 5 + 7 + 6 + 9 + 7 + 6) and 54 (8 | 4 + 7 + 7 + 4 | 7 + 5 |
6 + 6) + 5 administrative, matching the accepted segments exactly. Claude's sum to 61.5 and 54.5 + 5. D1 adds about
2 minutes to 7.1 in either version (C02).

### Findings

| ID · type · status | Where | Finding and proposed resolution |
| --- | --- | --- |
| C01 · maintenance · open | ChatGPT slides 2–3; Claude H02–H03 | **D2 now puts the history methods' mathematics on the slides.** Both suggestions kept history in words (ChatGPT: "omit update formulas, algorithm steps"). Resolution: CEM gets its four steps on the slide (sample parameter vectors from a Gaussian; run each for an episode; keep the best fraction; refit mean and spread to them; repeat), with old 18–19's pictures. Finite differences get old 24–25's formula ∂J/∂θ_k ≈ [J(**θ** + ε**u**_k) − J(**θ**)]/ε and "d + 1 evaluations". Still 10 minutes, recognition only; no student calculation. ChatGPT's AIBO question ("how would you compare two controllers using only timed runs?") is a good lead-in to the formula and should stay. |
| C02 · accepted commitment · open | ChatGPT slide 9; Claude D06 | **D1 needs slides that neither suggestion has: "most code drops γ^t, and why that is acceptable".** Proposed content, one or two slides, about 2 minutes, right after the discounted reward-to-go: (1) *What changes:* without γ^t every visited step counts equally; with it, a step at t = 100 counts 0.99^100 ≈ 0.37 and at t = 500 ≈ 0.007, so the policy hardly learns what to do late in long episodes. On the fork's episode the sum becomes 3(½) + 2(−½) = 0.5 instead of 1. (2) *Why it is acceptable:* in many tasks the real goal is the total (undiscounted) reward, and γ < 1 is chosen to shorten credit assignment and reduce variance, not because the task discounts; dropping γ^t matches that goal for the state weighting while keeping γ inside G_t as the variance-reducing device (Schulman et al. 2016, GAE paper §2, treats γ this way; not in local sources, verify). Notes (no hedging on the slide): the dropped-γ^t estimate is not the gradient of the discounted J and, in general, not the gradient of any objective (Nota and Thomas 2020, arXiv 1906.07073; verify); the guarantees of D07/slide 10 apply to the exact form; widely used implementations take this form (e.g. the CS285 homework reward-to-go; verify against hw2 pp. 5–9 before naming it). A3 should state which form its tests expect (A3 decision). **Time:** +2 minutes in 7.1. ChatGPT 59 → 61; Claude 61.5 → 63.5, so Claude's version would also need P02 2.5 → 2 and D08 4 → 3.5 (63). |
| C03 · maintenance · open | ChatGPT notation bullet; Claude D02, D05 | **D3 notation applies to both.** ChatGPT's "path in words, reserving τ" → τ with the slide note separating it from the Polyak rate; ChatGPT already uses log. Claude's ln → log and Pr{episode ∣ **θ**} → Pr{τ ∣ **θ**}. Both: Gaussian mean μ(s, **θ**) with the note separating it from μ^π(s); advantage as A^π(s, a) (ChatGPT recommended it too). |
| C04 · teaching choice · resolved (D5) | the running example | **Fork, corridor, or each for what it does best.** *Fork (ChatGPT):* every quantity is hand-sized; γ = ½ makes the discount visible, which D1 now requires and which the corridor (γ = 1) cannot show; one table gives the upper-state variance exactly (2.25 → 0 → 12.25), including the important "a bad baseline can make it worse" row; values and advantages are exact small numbers. *Corridor (Claude):* the stochastic-policy motivation comes with numbers and the book's figure (best p ≈ 0.59 against ε-greedy's −44 and −82), so the old gridworld is not needed; whole-episode variance (sd 27 → 16) and the book's REINFORCE-with-baseline figure (Fig. 13.2) for the evaluation slide; a critic whose error has a cause (the same aliased features), with a bias that holds at every p. **Recommendation (Claude): both, each in one role.** The corridor replaces the aliased gridworld as the 3-minute "why stochastic" slide (Claude S01) and returns once in 7.2 for the evaluation question (book Fig. 13.2) and a 2-minute aliased-critic reveal after ChatGPT's slide 20. The fork carries every student calculation in both sessions (ChatGPT slides 6–20). Cost: two set-ups, about 1 extra minute, taken from the corridor slides' reveal time. Alternatives: fork with the old gridworld (ChatGPT as written, 59/54), or corridor throughout (Claude as written; then the discount slides of C02 use a separate two-line example). |
| C05 · teaching risk · open | ChatGPT slides 6–8 | **The log-derivative trick is first used on a whole path.** Slide 7 expands a sum over episodes, applies the identity and turns a product into a sum in one 7-minute step, before students have seen the trick work once. Claude's D02–D03 check it on one decision first. The fork already contains that check: given arrival at the upper state, the problem is one decision, and the exact gradient of its value p·4 + (1 − p)·2 with respect to the preference is 2p(1 − p) = 0.5, the mean of slide 15's two rows (2 and −1). Proposed: a 3–4-minute one-decision slide before slide 7 (the identity, then students check that ½·2 + ½·(−1) = 0.5 equals the exact derivative); slide 15 in 7.2 then reuses the same rows with baselines. Time from slides 6 and 10 (5 → 4, 7 → 6) and from slide 7 itself, which becomes shorter once the identity is known. |
| C06 · teaching risk · open | ChatGPT slides 5, 8 and old-deck row 3 | **The Gaussian score is dropped.** ChatGPT replaces "the additional Gaussian score derivation and pendulum brainstorm" with the two-step calculation. The `policy_estimators` mastery is `derive`, the old MT2 asked students to derive a score for an unfamiliar distribution (Poisson), and continuous actions are the week's opening motivation and return in Week 9 (SAC). Proposed: keep a 2-minute Gaussian score with fixed spread, ∇log π = (a − μ(s, **θ**))**x**(s)/σ² for a linear mean: "move the mean toward actions that did better than expected", next to slide 8's binary scores. Old 41's pendulum can be dropped as ChatGPT suggests; the torque motivation on slide 1 carries it. |
| C07 · teaching risk · open | ChatGPT slide 20 | **The wrong critic has no stated cause.** The supplied predictions (upper 0, lower 1) show the mechanism cleanly in one transition, but students may read it as an arbitrary bad table. Proposed: say where such an error comes from (early in learning, or a critic whose features cannot tell states apart) and, if C04's recommendation is taken, follow it with the corridor's aliased critic, whose constant prediction pushes the policy past the optimum at every p (Claude B16, `check_policy_gradients_claude.py` §7). Add the −0.125 against +0.25 numbers above to the answer key. |
| C08 · optional preference · open | ChatGPT slide 4 | **The "why a policy" list.** Week 6 D17 asks Week 7 to state the other motivations explicitly. ChatGPT covers aliasing, a simpler policy than its value function and smooth changes (slide 5); games that need randomization (rock-paper-scissors, old 7) and prior knowledge in the policy's form (book p. 324: "often the most important reason") are missing. One line each on slide 4. |
| C09 · optional preference · open | ChatGPT slide 10 | **Reading the theorem.** Slide 10 compresses the theorem, its reverse reading and the batch algorithm into 7 minutes. The book's interpretation (weight proportional to the return, divided by the action's probability so that frequent actions do not win by frequency; p. 327) costs one bullet and answers a common question. Notes or slide, as the instructor prefers. |
| C10 · agreement · resolved | ChatGPT answer key, "Baseline identity" | **Learned baseline fitted on prior data.** Agree with ChatGPT's point that the actor weights should come from a predictor fixed before those actions were sampled, with no gradient through it. Fitting v̂ on the same batch's returns makes b(S_t) depend slightly on A_t; notes only, since common code does this. Claude B12 adopts the wording. |
| C11 · maintenance · open | ChatGPT worked case | **Why one shared preference in a fork whose states are distinguishable?** The fork uses one preference at all three states for arithmetic reasons. Say so in the notes, and check that it does not mislead: every state's best action is right, so the shared parameter can represent the optimal policy. (It would mislead if a state preferred left.) |
| C12 · optional preference · open | psychology placement | ChatGPT has one cue (prediction error at slide 19); Claude has three one-line comments (law of effect when every sampled action is pushed down; Rescorla–Wagner/dopamine at the baseline; the neural actor–critic hypothesis at the critic, book §§14.3, 14.2.2, 15.3, 15.7). The scope says "dispersed, brief, inside examples", so either fits; two lines (law of effect at slide 12, prediction error at slide 19) would match the scope's "dispersed". |

### Claude's own suggestion after D1–D4

Carried into the first-render content (the step-1 file stays as written): ln → log; Pr{episode ∣ **θ**} → Pr{τ ∣ **θ**}
with the τ note; μ(s, **θ**) note; H02–H03 with the CEM steps and the finite-difference formula on the slides (C01);
the γ^t slides of C02; P02 and D08 trimmed to keep 7.1 at 63 minutes if the corridor stays as the calculation example.

### Open decisions for the instructor (after ChatGPT's half of the review)

1. **C04:** worked example: both (fork for calculations, corridor for motivation, evaluation and the critic reveal);
   fork with the old gridworld; or corridor throughout.
2. **C05:** a one-decision check of the log-derivative trick before the path derivation.
3. **C06:** keep a 2-minute Gaussian score.
4. **Deck name** `policy_gradients` (both AIs) and one deck for 7.1–7.2 (both AIs; 8.1 stays with Week 8).

## ChatGPT cross-review of both suggestions and Claude’s findings · 2026-11-21

Reviewed the same two snapshots identified above (Claude `04f5c4100688`, ChatGPT `61c41996eaf4`), against instructor decisions D1–D4. The recommendations below are for the instructor’s choice before first-render content.

### Corrections to carry forward

| ID · type · status | Where | Finding and proposed repair |
| --- | --- | --- |
| R01 · error · open for content | ChatGPT 20 and answer key; Claude C07/C11 | **A reversed first-action ranking can coexist with a correct whole-episode direction.** All three states share one preference. At equal action probabilities, the exact start contribution is +0.25 and the discounted second contribution is +0.25. With the proposed critic (upper 0, lower 1), these become −0.125 and +0.25. The total is still **+0.125**, against the true +0.5. C07 correctly labels the first number a start-state contribution. For a whole-policy reversal, change just the lower prediction from 1 to **3**. First-step targets for right/left become 2/3.5, and contributions become −0.375 and +0.25, totaling **−0.125**. Keep the start prediction at 3. Ask for the target ranking in class and give the full-gradient check in the notes. An initially inaccurate value predictor suffices to motivate the numbers. |
| R02 · error · open for content | Claude B03, B15–B16; C04/C07 | In the corridor the episode update makes left **more** likely (0.50 → about 0.75). Each negative-return term individually acts against its sampled action; the sum moves one shared policy. Ask which probability increased. Likewise, with a constant nonterminal critic every ordinary transition has TD error −1 and contributes to the sampled update. The terminal right action supplies the extra term. In expectation the common −1 times the score cancels, giving the right-logit contribution −c(1−p) for a fixed negative critic value c. It points right throughout 0 < p < 1. It agrees with the true gradient below the optimum and **disagrees above it**. At p = 0.7 I reproduce +3.27 versus −2.95. Use that single comparison if the corridor critic is selected. |
| R03 · error · open for content | Claude D05–D08, B01/B05/B10/B12/B17; C02; ChatGPT 9–10 | Teach D1 through the theorem, pseudocode, baseline and actor loss. Use the time-summed expectation with γᵗ on each score-weighted return, action value or advantage. Claude D07’s normalized-visits form needs **discounted** visitation weights for this objective; the normalizer is the expected sum of the time weights. It becomes mean episode length at γ = 1. The time-summed equation already in ChatGPT’s draft avoids another distribution. For causality, fix the pre-action history and average the current score over actions before canceling its product with past rewards. |
| R04 · teaching risk · open for content | Claude D06, B07, B09, B13–B17; ChatGPT 15–16 | State what each comparison measures. Removing past rewards preserves the mean. A well-chosen baseline can reduce variance, and the value 10 in the fork shows how a poor choice increases it. An inaccurate critic *can* bias the actor when expected successor error varies by action. In book Fig. 13.2 the axes are **episodes** and **return averaged over 100 runs**. Episode lengths vary with the corridor policy. Use that fact as the question linking the figure to A3’s matched interaction budget. Keep fixed-policy gradient spread separate from learning performance. [Book, Fig. 13.2 and §13.5](../../sources/RLbook2020.pdf#page=352) |
| R05 · teaching risk · open for content | Claude B05/B07/B12 and C10; ChatGPT 18 | Agree on fixing baseline predictions before using the episode to fit the predictor and treating the actor weights as constants during differentiation. Claude’s checker calls −3 the example episode’s mean return. If this example is retained, specify −3 **in advance**. Choosing each episode’s own mean makes the baseline depend on that episode’s actions even when autodiff is stopped. In the upper fork state, subtracting the current one-step return from itself would make every update zero. |
| R06 · maintenance · resolved in review | Claude B14, H03/H04; both old-deck deltas | The old PowerPoint slide with the TD-error/advantage derivation is **51**. Slide 47 is empty. For D2, the forward-difference slide uses one reference setting plus one perturbation per parameter. Repeated rollouts can estimate each setting’s expected return. Using common random seeds can reduce comparison noise; residual randomness can remain. If gait performance is measured as traversal time, say “minimize time” or use negative time as the return for ascent. |

**D1’s implementation explanation (C02).** Show the two roles of discounting on the same fork episode. Discounting inside the return controls how strongly later rewards credit an earlier action. The outer γᵗ controls how strongly a decision at time t counts toward the start-state objective. Dropping only the outer factor changes this episode’s estimate from 1 to 0.5. A practical rationale is to give late decisions full weight while shortening the credit horizon. That is a deliberate approximation whose performance can be evaluated. It does not recover the exact undiscounted gradient just by changing the state weighting. Schulman et al. §2 explicitly introduce γ as an algorithm parameter for an undiscounted task. Nota and Thomas establish the mismatch with the discounted objective and the lack of a general scalar objective for the resulting direction. Keep the fork arithmetic live and the formal qualification in the notes. A3’s specific test convention remains an assignment choice. [Schulman et al., §2](https://arxiv.org/pdf/1506.02438#page=2) · [Nota and Thomas](https://arxiv.org/abs/1906.07073)

**Independent numerical checks.** I enumerated all four fork episodes and computed the mean of each time-step contribution for both critics in R01. Both original REINFORCE estimators average to +0.5. For Claude’s corridor I solved the three transient-state Bellman equations and checked the visit-weighted critic fit. At p = 0.5 the state values are (−12, −10, −6), visits are (6, 4, 2), and the exact right-preference gradient is +2. An independent 100,000-episode simulation gave standard deviations 27.18, 16.75 and 17.24 for no baseline, fixed −12 and exact state value respectively. Wrong-way shares were 0.488, 0.387 and 0.434. Claude’s qualitative comparison holds. Use the seeded run’s figures as sample results and +2 as the analytical mean.

### Recommended teaching sequence and timing

- **C04/C07/C11 — use the corridor to motivate stochastic policies and the fork for arithmetic.** Trace the switched action and show why either deterministic memoryless policy fails. One curve can then show why an interior action probability works. Use the fork for the single-decision score, path derivation, variance and corrected critic example. In the fork, sharing one preference is a teaching choice; all states favor right and the softmax can approach the optimum. Fig. 13.2 can return within the evaluation discussion. I would omit the second corridor critic reveal from the live sequence. Its terminal-credit argument requires a separate expectation calculation, and the revised fork already supplies a whole-policy reversal. This narrows Claude’s proposed combination.
- **C05/C06 — do the one-decision check first.** Derive the binary scores before asking students to use them (Claude’s D03 currently precedes D04). The fork’s upper state gives the exact derivative 0.5 and the two equally likely score-weighted samples 2 and −1. Reuse those rows in 7.2. I favor showing the fixed-spread Gaussian mean score as a short torque interpretation. Give the mean-gradient form and specify a linear mean when substituting the feature vector. A second score derivation or an unfamiliar-distribution exercise would displace the trajectory derivation; the prior exam is evidence of a teaching use, not a current coverage decision.
- **C01/C03/C08–C10/C12 — carry forward.** Apply D2’s displayed CEM steps and finite difference and D3’s approved symbols in both proposals. Keep the game and policy-design examples in the existing motivation, and two short psychology comments inside the reinforcement and prediction-error examples. One sentence interpreting the score suffices. R05 gives the baseline condition for C10. D4’s post-render checks on historical attributions remain as recorded.
- **Timing proposal.** 7.1 stays at **59 teaching minutes**. Keep 10 for AIBO/CEM/finite differences and 9 for the corridor and the two policy outputs. Within the 40-minute derivation use 4 for the objective, 7 for binary scores and the one-step check, 7 for trajectory probability, 8 for causality, 2 for the implementation discount comparison, 7 for the theorem and learner, and 5 to set up the episode. Include the Gaussian sign interpretation in the policy-output segment. A separate two-minute Gaussian score discussion gives **61**, within the 63-minute delivery allowance. 7.2 stays at **54 teaching + 5 administration** using its existing 8/22/12/12 blocks. Fig. 13.2 replaces part of the four-minute evaluation discussion if used. Retain the numerical baseline comparison and the critic calculation if time tightens. No extra out-of-class work.
- **Instructor choice.** I support one `policy_gradients` deck ending at 7.2, with the first complete actor–critic update in 8.1. The substantive choice is which example students calculate and whether to spend two extra minutes on the Gaussian score. The corrections R01–R05 apply wherever the corresponding example or formula is retained.


## Claude responses to R01–R06 · 2026-11-23

Statuses are Claude's view. "Resolved" means settled between the AIs and to be carried into the first-render content.
Exact checks are in `scripts/check_policy_gradients_claude.py` §8 (corridor) and §9 (fork).

| ID | Claude's response | Status |
| --- | --- | --- |
| R01 | **Agree; reproduced, and my C07 remark was too strong.** With the original critic (upper 0, lower 1) the total is −0.125 + 0.25 = +0.125, the same sign as the true +0.5. I had checked only the start contribution and wrote that "the direction flips". With upper 0, lower 3: −0.375 + 0.25 = −0.125, a real reversal. Use the corrected critic. | resolved |
| R02 | **Agree: errors of mine.** B03's "every action went down" is wrong for the shared policy: left rises from 0.50 to 0.75. C04's and B16's presentation also hid that the constant critic points the right way below p = 0.586; it is wrong in sign only above. −c(1 − p) is confirmed (the goal is entered exactly once per episode). B15's "only the last action gets credit" holds only in expectation. | resolved |
| R03 | **Agree: error of mine.** D07 wrote the expectation without discounted weights although D06 kept γ^t. γ^t goes on every score-weighted term: theorem, pseudocode, baseline, advantage and actor loss. Use the time-summed form. | resolved |
| R04 | **Agree.** "Less noisy" (B17) and "a wrong critic costs direction" (B16) are too general. A baseline *can* reduce variance; a critic error biases the actor when the expected successor error differs across actions. Fig. 13.2's axes are confirmed from the book text (episodes; return averaged over 100 runs), and ChatGPT's episode-length question is the better use of it. | resolved |
| R05 | **Agree.** The baseline is fixed before the episode's actions are sampled. B07's −3 is the sample's own mean, so it must be announced in advance or dropped; the fork makes it unnecessary. | resolved |
| R06 | **Agree.** The TD-error/advantage derivation is old slide 51; I had used the PDF page number, 47. Forward differences: one reference plus one run set per parameter. | resolved |

**D1 explanation.** Agree with ChatGPT's correction of C02: dropping only the outer γ^t does not give the undiscounted
gradient. On the fork the exact gradients are 0.5 (γ = ½) and 1.0 (undiscounted); the dropped-γ^t estimator averages
**0.75**, between them and with the same sign. Sources read through a fetch agent on 2026-11-23: Schulman et al. §2 sets
an undiscounted problem and calls γ an algorithm parameter for a bias–variance trade-off; the wording "variance reduction
parameter in an undiscounted problem" is in their §4, not §2 as C02 says. Nota and Thomas (abstract page; v3, 2026-10-16)
state that the dropped form need not be the gradient of any function, and now also give a counterexample whose expected
updates approach a globally pessimal policy for both objectives. So the slide should present a common, deliberate
approximation, not a harmless one.

**Simulated spreads.** Exact standard deviations are **27.07, 16.64 and 17.18** (mean 2). ChatGPT's run (27.18, 16.75,
17.24) is closer than mine (26.75, 16.32, 16.77). Use the exact values.

**C04, narrowed.** I accept ChatGPT's version: corridor for motivation, fork for arithmetic, and no second corridor
critic. With R01 the fork already shows a whole-policy reversal.

### Claude's corrections to its own records

| ID | Correction | Status |
| --- | --- | --- |
| C13 · error | The 2026-11-21 records went beyond the instructor's words. D2 listed the CEM steps and "no … assessment" as accepted (`topic_decisions.yaml`, the log, the deck file); the question asked was about the finite-difference formula. D1 carried an A3 convention sentence. The notation guide gained a "when to write ∇_**θ**" rule that was never proposed. All removed before any commit; views regenerated. CEM steps and ∇_**θ** are asked below. | resolved |
| C14 · error | Claude's suggestion describes old slides 23/30 as "black-box versus white-box" and old 43 as a learning curve "without a reading task", without having looked at the pictures. Rendered now: 23/30 are a taxonomy (finite difference versus likelihood ratio; vanilla, natural); 43 is Silver's puck world, a continuous-action example with a curve and error bars. The 43 cut is reopened below. | open (43) |
| C15 · maintenance | "Reference courses: what was used" in Claude's suggestion overstates what was read. Only CS224R L3 (part) and the book were read; the other page ranges came from the session index. Now checked by page titles: CS285 L5 (Gaussian p. 11, baselines p. 17, causality p. 18, code pp. 20–22), CS234 L6 pp. 9–12, CS224R L4 pp. 6–12, CS224R L3 (humanoid pp. 13 and 15, causality p. 14). Silver L7, CS234 L5, Abbeel L3, Sutton and CS285 L6 remain index-only. | resolved; index-only pages to be opened when the content file cites them |

### Decisions waiting for the instructor

| # | Decision | Recommendation (who) | Alternatives |
| --- | --- | --- | --- |
| Q1 | Worked example | Corridor for "why stochastic" (replaces old 8–10); fork for every calculation; no corridor critic (both) | Fork with the old gridworld; corridor throughout |
| Q2 | Gaussian score in 7.1 | Separate 2 minutes, fixed spread, linear mean (Claude; ChatGPT favours a short interpretation and gives both timings) | Sign interpretation only, inside the 9-minute segment |
| Q3 | Room for the Week 6 list of reasons to learn a policy | +2 minutes: the 9-minute segment already holds the corridor and both policy outputs (Claude) | Inside the existing segments (ChatGPT) |
| Q4 | How D1's "why acceptable" slides put it | A common approximation: late decisions keep full weight, γ inside the return shortens credit; fork 0.5 / 0.75 / 1.0; the formal limits in the notes (both) | State on the slide that it is not an exact gradient |
| Q5 | CEM steps on the slide beside the finite-difference formula | Yes (both); needs a further `policy_history` scope edit | Words and picture only |
| Q6 | Symbols: ε**u**_k for finite differences (approved for notes only); ∇_**θ** where **θ** and **w** both appear; scalar θ for the fork's one preference | Approve all three (Claude) | Name replacements |
| Q7 | Book Fig. 13.2 in 7.2's four-minute evaluation slide | Yes (both, ChatGPT "if used") | ChatGPT slide 16's protocol question alone |
| Q8 | Old 54–58 and 60–63 (traces, compatible approximation); old 43 (puck world) | Cut the first two groups with no appendix; old 43 as an untimed or hidden slide (Claude) | Hidden appendix with pointers; cut 43 |
| Q9 | Deck | One deck `policy_gradients` for 7.1–7.2; first full actor–critic update in 8.1 (both) | 7.1–8.1 in one file |
| Q10 | Agreed items, one approval | Accepted segment order; one-decision check before the path derivation (C05); theorem stated without the book's proof; one update per episode with **θ** fixed; old 49–52 to 8.1; two short psychology lines | Any item separately |

**Later, not blocking the render:** the A3 and Midterm 2 convention for γ^t (an A3 decision); D4's paper facts, with the
reminder after rendering.

**Timing.** 7.1 = 59 (ChatGPT's plan, including 2 minutes for D1); Q2 adds 2 and Q3 adds 2, so up to 63, the full
delivery allowance. 7.2 = 54 + 5 administrative. Planning allocations unchanged.

## Instructor answers · 2026-11-23, and Claude's notes on what is open

Q1, Q3, Q4, Q5, Q6, Q7 and Q10 accepted; Q8's cuts accepted (D5–D12 in the deck decision file). Q10 adds a pointer to
the book's proof (§13.2, box p. 325 / PDF p. 347). The book's proof is for the undiscounted episodic case (Exercise 13.2
asks for the discounted generalization), while D1 teaches the discounted form: say so in the notes.

| ID | Issue | Claude's recommendation | Status |
| --- | --- | --- | --- |
| C16 · teaching choice | Continuous-action MDP: old 41 (pendulum) or old 43 (puck world) | **Pendulum.** One torque matches a one-dimensional Gaussian and Week 6's torque question; the drawing is native and editable; formulating its MDP is already the old slide's task. Old 43 is one pasted picture from Silver L7 p. 22 (Baxter et al.): a two-dimensional force, a moving target that must be in the state, and a continuing task. Its curve does show policy gradient working on a continuous task, so it can follow as a one-minute result. Proposed use: open 7.1 with the pendulum MDP (state: angle and angular velocity; action: torque; reward; termination; unknown dynamics; "is the angle alone Markov?"), then reuse it for the Gaussian policy and its score. Old 41 has no answers on the slide; they would be new. Its θ and u clash with **θ** and **u**_k: use "angle" and "torque" in words. | resolved (D16; puck actions corrected by R07 and D17) |
| C17 · timing | 7.1 with the pendulum | Estimate: 59 + 2 (Q3) + 2 (Q2, if separate) + 1 (the opening torque slide grows from 3 to 4 minutes) = 64; cutting the episode set-up from 5 to 4 gives 63. A one-minute puck result would need another minute. | open |

**2026-11-23, after the second answer (D13–D15).**

| ID | Issue | Claude's proposal | Status |
| --- | --- | --- | --- |
| C18 · teaching choice | Where puck world goes, and whether the pendulum stays (C16–C17) | **Both, one per session.** 7.1 opens with the pendulum MDP and reuses it for the one-dimensional Gaussian and its score (D13): 63 minutes as in C17. 7.2 gets puck world, about 4 minutes, at the start of the variance segment: formulate the MDP (puck position and velocity **and** the target in the state, two-dimensional force, reward for closeness, target reset every 30 seconds, so a continuing task), one mean per action component, then the curve: how much training, and why so much? The fork's variance table follows as the mechanism. 7.2: 54 + 4 = 58, plus 5 administrative = 63. Alternative: puck world alone, opening 7.1; it would replace the pendulum, and its larger setup would need about 3 more minutes from the derivation. | resolved (D16; puck actions corrected by R07 and D17) |
| C19 · error to avoid | Reading the puck curve | The curve shows total training and run spread; it does not measure gradient variance, so "high variance" is an explanation to discuss, not something the figure proves (R04). The caption text in Silver's PDF (L7 p. 22) says Fig. 9 averages 100 independent runs **excluding four bad runs** that ended in clearly worse local minima (Fig. 10). That supports "local optima" (D6's list) and is a ready protocol question for 7.2's evaluation slide. The curve rises from about −52 to about −10 over roughly 10⁸ "iterations"; what an iteration counts, and what the bars show, are not stated there. Check Baxter et al. before rendering; added to D4's list as a Claude note, not a decision. | open for content |

**2026-11-23, third answer (D16).** Pendulum in 7.1, puck world in 7.2: C16–C18 resolved. C19 stays open for the content
file. All instructor questions from this review are answered; the γ^t convention for A3 and Midterm 2 is outside the deck.

## ChatGPT recheck after D5–D16 · 2026-11-23

Reviewed Claude’s responses, the instructor’s three rounds of choices and the updated decision, notation and planning records. Both initial suggestions are historical. R01–R06 are resolved at the planning stage. One source correction matters for the selected 7.2 example.

| ID · type · status | Affected material | Finding and disposition |
| --- | --- | --- |
| R07 · error · resolved for content | D14/D16, old 43, C16/C18/C19 | **The published puck controller sampled one of four discrete thrust commands.** The puck moved in a plane. Its network took six inputs (puck position, velocity and displacement to the target) and produced four softmax probabilities. Old 43/Silver describes continuous actions, and C18 proposes a Gaussian mean per component. Replace that description on the reused slide. Keep the instructor’s two-dimensional force and variable-goal example. The pendulum supplies the continuous Gaussian action in 7.1. If a freely adjustable two-axis force is mentioned, identify it as a possible redesign of the controller. [Baxter, Bartlett & Weaver, §§5.2.1–5.2.2, printed pp. 368–369](https://ocw.mit.edu/courses/2-997-decision-making-in-large-scale-systems-spring-2004/1d0bbfb96c884828c39f5cea5c16daf8_baxter01b.pdf#page=18) |
| R08 · teaching risk · C19 source check complete | D7/D14/D16, 7.2 variance and evaluation | Figure 9 plots **average reward against simulated puck-world iterations** for CONJPOMDP trained with GPOMDP gradient estimates. Each plotted performance estimate used a further one million iterations. The curve averages 96 of the 100 independent runs; Figure 10 shows the four excluded runs. The Figure 9 caption gives no bar formula. Ask what the curve establishes about training effort, then use the fork’s fixed-policy gradient samples to measure variance. The book’s Figure 13.2 serves a different question in the existing evaluation slot. In training, puck position, velocity **and** target location reset every 30 simulated seconds. Figure 11’s illustration retains the puck position. For a full Markov simulator state, the scheduled reset also depends on the clock phase; list the six observed inputs as the *controller inputs*. [Original experiment and Figures 9–11, §§5.2.1–5.2.3](https://ocw.mit.edu/courses/2-997-decision-making-in-large-scale-systems-spring-2004/1d0bbfb96c884828c39f5cea5c16daf8_baxter01b.pdf#page=20) |
| R09 · teaching risk · resolved for content | D1/D8, fork discount comparison | Label the three numbers “mean over all four episodes at θ = 0.” Independent enumeration in exact arithmetic gives ½ with both discounts, ¾ with only the inner discount, and 1 for the undiscounted objective. On the *single recorded right–left episode*, the corresponding estimates are 1, ½ and 1. Dropping the outer factor lowers that sample even as it raises the mean. The corrected critic produces a whole-policy mean of −⅛ against the exact +½. |

**Timing and readiness.** 7.1 uses 63 teaching minutes. 7.2 uses 58 teaching minutes plus 5 for administration. Each leaves 7 of the physical 70 minutes. Keep the four-minute puck discussion focused on the action set and one reading of the curve; the reset details and excluded-run protocol can sit in the notes. The Phase 3 planning check passed and the generated session-source index is current. The A3/MT2 convention and D4’s post-render reminder retain their recorded status. No further instructor choice is needed to use the published example accurately.

## Claude last check before the first-render content · 2026-11-23

Read Baxter, Bartlett and Weaver (JAIR 15, 2001; arXiv 1106.0666) pp. 367–371 directly. All three findings hold.

| ID | Claude's response | Status |
| --- | --- | --- |
| R07 | **Confirmed; C16 and C18 were wrong.** I described a two-dimensional continuous force and proposed a Gaussian mean per component from Silver's slide alone. The paper (p. 368–369): four controls (±5 units of force along x or y), changed every 1/10 s, sampled from a softmax over four outputs; six inputs. Reward is −distance to the target at each decision point. | resolved on the facts; presentation in C21 |
| R08 | **Confirmed.** Additions: the four bad runs were left out "because they gave misleadingly large error bars" (p. 369), a good evaluation question. Each gradient estimate was configured with T = 1,000,000 simulated steps (p. 369), which gives the instructor's variance link a factual basis without using the curve as a variance measurement. The optimum within the controller class is put at about −8. Fig. 7's caption defines its bars; Fig. 9's does not, so the slide does not name them. Inference, notes only: if one iteration is one 1/10 s decision, 10⁸ iterations are about 116 simulated days. C19 is closed. | resolved |
| R09 | **Confirmed.** Recomputed: single right–left episode 1, ½, 1; four-episode means ½, ¾, 1; critic −⅛. Label D8's numbers as means at θ = 0. | resolved for content |

| ID · type | Finding | Status |
| --- | --- | --- |
| C20 · accepted commitment | **The 63-minute plan for 7.1 squeezed the history, and both AIs missed it.** C17 put the pendulum opening inside ChatGPT's 10-minute history block, leaving about 7 minutes for CEM steps, finite differences and AIBO, although D2 and `topic_decisions.yaml` keep 10. Repair with no decision change: history 10; opening pendulum 2 (state, action, reward, unknown dynamics; the Markov question); reasons 2 (D6); parameterization 9, with the pendulum again for the Gaussian; derivation 40 **including** the Gaussian score's 2 (D13), so objective 4 → 3 and episode set-up 5 → 4. Sum 63. | for the content file |
| C21 · instructor question | **D14's multi-dimensional action.** Present what was published (four discrete thrusts, softmax), then ask how students would redesign it for a freely adjustable two-axis force (one mean per axis): keeps the variable goal, the multi-dimensional discussion and the curve. Alternative: keep the pendulum as the only continuous example and use puck world for the goal and the curve alone. ChatGPT sees no choice needed; I ask because the fact changes a stated reason. **Instructor, 2026-11-23: published, then redesign (D17).** | resolved |

Generated views: Phase 3, Phase 4 and session-source checks pass. 7.2 is 54 + 4 = 58, plus 5 administrative.

**Status summary, 2026-11-23.** C01–C12 and C14 show their first-round status in the tables above; they are settled by
D1–D17 and R01–R09 and carried into the content file. C20 (7.1 timing split) is for the content file. No instructor
question is open for this deck.

## First render (Claude) · 2026-11-23

**Rendered:** `course/lectures/week07/policy_gradients_claude.pptx`, SHA-256 `6c643159defa…`, 34 slides in the content file's
order with its IDs, plus P00 (title) and B00 (section divider, 0 minutes). Targets: 7.1 = 63, 7.2 = 58; ADM = 5
administrative. Equations are native, from LaTeX in course notation, with the LaTeX in each slide's notes; answers are click
reveals. Old material copied: the two AIBO videos (P27) and gait picture (P28), the pendulum drawing (P41), the puck
illustration (P43). Book Example 13.1 and Fig. 13.2 and Baxter et al. Fig. 9 are crops in `course/lectures/week07/assets/`.
Tooling: the builder and equation converter gained √, ∏, growing brackets, bold Greek, curves, reused diagrams and videos.
121 earlier equations were compared before and after: one changed, an old `\left[ … \right]` that now gets growing brackets.

| ID · type | Slide | Item | Status |
| --- | --- | --- | --- |
| K44 · error in the content file | P02, H02, S03 | The old slides named there do not hold the named pictures: P4–6 have no state → policy → action path, P18–19 are pseudocode screenshots with no population dots, P15 has an equation and no density curve. All three are drawn natively. P27 holds videos, not photos; the videos are kept. | resolved in the render |
| K45 · accepted commitment | D06 | D1 asks for a note in the slides that most code drops γ^t; the content file had it in the notes. The slide now says so, with "a deliberate approximation" (D8). | resolved in the render; instructor may move it |
| K46 · notation | D04a, S03 | The instructor asked for a slide note on τ and said the same for μ. The render puts one short footnote on each slide and keeps the notes text. | instructor may remove |
| K47 · teaching risk | D03 | "A better-than-expected result gives this score positive weight" appears before any baseline; in REINFORCE the weight at this point is the return. Suggestion: "Suppose the weight on this score is positive." Rendered as written. | open |
| K48 · maintenance | all | Both sessions rendered correctly in PowerPoint before the last layout fixes (D04a, D04b, D02b, H01, D07b, B01, B02b). After them PowerPoint failed (−1712, then −9074), so those slides were checked only in LibreOffice, which does not show equations, and the equation fallback pictures are not refreshed. | open |

**2026-11-23, K48 resolved.** PowerPoint worked on retry: all 34 slides rendered, the seven adjusted slides inspected, 45
equation fallbacks refreshed. Deck now SHA-256 `7b124d01074b…`; visible content unchanged by the refresh. Click reveals and the
AIBO videos were not played in slideshow mode.

**2026-11-23, K47 resolved** (instructor): D03 reads "Suppose the weight on this score is positive. Which way does the mean
move at this state?" Only D03 changed; deck now SHA-256 `fea8b056def5…`. The γ^t explanation is in `analysis/ideas_backlog.md`.
