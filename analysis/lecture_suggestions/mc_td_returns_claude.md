# Session 3.2 (`returns`): initial content suggestion (Claude)

**Claude's step-1 suggestion** (`docs/lecture_workflow.md`, pilot v2), 2026-10-22. Analysis only: nothing here is accepted. It becomes historical after step 3. The deck's status lives in [`decisions/lectures/mc_td.md`](../../decisions/lectures/mc_td.md).

**Scope of this file:**
- the 3.2 teaching sequence, to be appended to the accepted 3.1 deck (D1, one deck for 3.1–3.2);
- the old-deck delta for the slides 3.1 left to 3.2;
- the two choices left open from 3.1 (R08/R13: the 19-state plot) plus one new choice (a generated learning-curve figure).

All numbers are checked by `scripts/check_mc_td_returns_claude.py`.

**Corrected after ChatGPT's cross-review (R28–R34), 2026-10-22:** the TD-bias wording, the variance claims, the update-availability rule, the book figure references, the random-walk statistics and the evaluation baseline wording. The responses and the consolidated sequence are in the [shared review](mc_td_review.md).

## Accepted frame

From `decisions/topic_decisions.yaml` (`returns`) and `output/lectures/session_sources.md` §3.2:
- **Allocation:** 58 teaching minutes (range 50–65), no administration. Plan to 58 first; the delivery allowance up to 63 is for motivation and intuition only.
- **Worked activity:** trace n-step targets; inspect noisy learning curves and a baseline comparison.
- **Feasibility note:** includes **10 minutes of evaluation reasoning**; the λ mixture moves to Week 8.
- **Prediction group:** core; explain / derive / implement / analyze. "Derive n-step target." Implement representative MC/TD prediction, not all return variants.
- **Evaluation group:** core; analyze. Choose a baseline, separate training and evaluation, compare seeds and uncertainty, distinguish interaction and compute budgets, interpret ablations. 3.2 is the group's first session; 4.2 (project baseline and metric, 15 min) and 6.2 (replay/target ablations, 15 min) come later.
- **Deck decisions:**
  - D6: Example 6.2 (random walk) and Example 6.4 ("you are the predictor") are in 3.2. Batch setup comes before 6.4. The random-walk setup is counted outside the ten evaluation minutes (R12, R17).
  - R13 (agreed): 6.4 is a batch, Markov-information argument; neither batch answer is certified as the true value; the batch random-walk plot (old P33 figure) is omitted.
  - R08/R13 (deferred to this step): whether to keep the 19-state n-step plot.
- **A1 dependency:** A1 supplies checks for "n-step/terminal handling" and asks for "a compact interpretation of the comparison". So 3.2 must show the terminal rule for n-step targets and how to read a comparison.

## What students already have (accepted 3.1 deck, SHA `b1d2c2de…`)

- One update form V(S_t) ← V(S_t) + α[U_t − V(S_t)], with U_t the target (MT07, slide 9). Constant α versus 1/N(s), and the Robbins–Monro footnote.
- MC: U_t = G_t; first-visit and every-visit (MT05–MT07a). TD(0): U_t = R_{t+1} + γV(S_{t+1}), δ_t (MT09–MT09a).
- MT09: "The expected TD target is a Bellman backup of the current V; it need not equal v^π". This is the bias statement 3.2 makes explicit.
- **The shared trajectory** (1,1) → (1,1) → (1,2) → goal, returns 0.19, 0.46, 1; after one episode with α = 0.5: MC (0.095, 0.5), TD (−0.03, 0.5); exact values 14/275 ≈ 0.051 and 46/55 ≈ 0.836 (MT10–MT11).
- **MT11's open questions:** "Can this episode establish which method is better? What would we need to compare learning after many episodes?" 3.2 opens with them.
- Sampling versus bootstrapping and the three Silver backup diagrams (MT12). The data taxonomy, including online versus offline (fixed data) (MT03).
- MT14's announcement: "Next session: bias, variance, n-step targets and evaluating learning."

## Is the old material substantial?

**Yes.** `4 - Model Free Prediction.pptx` slides 22 and 29 (the parts 3.1 did not use), 30–36 and 41–44 cover 3.2 directly. Slides 37–40 were used in 3.1 (MT12); 45–59 belong to Week 8 or are cut. The evaluation block has no old-deck material: the old course assessed evaluation only through the project report. The delta below starts from the old deck.

**Other sources used:**
- Book §6.2 (Example 6.2, Exercise 6.3), §6.3 (batch updating, Examples 6.3–6.4), §7.1 (n-step TD, eq. 7.1 and the error-reduction property, eq. 7.3; Example 7.1).
- CS234 lecture 3, pp. 23–26: criteria for an estimation approach (consistency, compute, memory, statistical efficiency, bias/variance/MSE). This gives the "what makes an estimate good?" framing and links to budgets.
- Silver lecture 4, pp. 12–30 (bias/variance of targets); Sutton slides `11-12-TD` pp. 21–31 (batch) and `13-multistep` pp. 3–10 (n-step).

## Central idea and the motivation thread

3.1 showed **how** MC and TD update. 3.2 asks **how good** their estimates are, and **how we would know**.
- An estimate is computed from random experience: run again and it changes. Its quality has two parts. **Bias** is a systematic offset of the average. **Variance** is the spread across runs.
- The MC target has no bias but carries every later random event. The TD target sees one random transition but leans on the current table. **n-step targets** move between the two: n real rewards, then the table, weighted by γ^n.
- Claims like "TD learns faster" are statements about experiments. They need many runs, uncertainty, fair tuning, an equal budget and a stated measure. The session ends by making students check such claims.

**Explicit motivation time** (pilot v2 lesson). About 14 of the 58 minutes go to "why" before "how":
- S01: why one episode cannot settle the comparison;
- S02: why an estimate has a distribution;
- S05: why TD might do better (leads to batch updating);
- S08: why choose only between one step and all steps;
- S11: why an intermediate n can help.

## Teaching sequence for 3.2 (slide level, unpolished)

IDs S01–S13 are for this suggestion only; slide IDs come with the render-ready content. Times are planning estimates, not a rehearsal.

| ID | Slide(s) | Content and teaching purpose | Source | Min |
| --- | --- | --- | --- | ---: |
| S01 | Can one episode decide? | Re-open MT11's questions. Students answer: many episodes, many runs, a measure of error, the same conditions for both. That gives the session its two halves: what makes an estimate good, then how to compare learners. | 3.1 MT11 | 2 |
| S02 | What makes an estimate good? | Run the same learner again and the estimate changes: it has a distribution. **Bias:** how far its average is from v^π(s). **Variance:** how much it spreads between runs. Dartboard picture. One line on the other criteria an estimator is judged by: does it converge with more data (consistency), and what it costs in data, computation and memory. These come back in the evaluation block. | old 30 (picture); CS234 L3 pp. 23–24 | 3 |
| S03 | Bias and variance of the two targets | **MC:** 𝔼_π[G_t ∣ S_t = s] = v^π(s), so the target is unbiased; it depends on every later action, transition and reward, so it varies a lot. **TD:** 𝔼_π[R_{t+1} + γV(S_{t+1}) ∣ S_t = s] is the Bellman backup of the current V (MT09). It need not equal v^π(s): its bias at s is γ times the expected error of V at the next state, so it is at most γ times V's worst error (errors at different successors can also cancel). It depends on one random transition and the table, while G_t depends on all of them; with a correct table its variance is never larger than the return's, but a poor table can make it vary more. **Grid question:** which random events affect G_0 on the shared trajectory? (Every slip on the way.) And the TD target at t = 0? (Only the first transition.) Notes: the variance statement with a correct table follows from the law of total variance (G_t = R_{t+1} + γG_{t+1} and 𝔼[G_{t+1} ∣ S_{t+1}] = v^π(S_{t+1})). Counterexample for a poor table: two equally likely successors with estimates +1 and −1 and all later rewards 0 give a random TD target but a constant return. In noisy problems, constant α keeps both estimates fluctuating (the MT07a caveat). | old 30 (fixed), old 31 (part); book §6.2; Silver L4 | 5 |
| S04 | Random walk: one task, many runs | **Setup (counted here, outside the evaluation minutes, R17):** five states A–E, start at C, each step left or right with equal chance, +1 for leaving on the right, 0 otherwise; γ = 1; V starts at 0.5. Ask why the true values are 1/6, …, 5/6 (the chance of leaving on the right). **Quick check (Exercise 6.3):** after the first episode only V(A) changed. Why, and by how much with α = 0.1? (The episode left on the left; only the last transition had a nonzero TD error: −0.05.) **Curves:** TD's estimates after 0, 1, 10, 100 episodes; RMS error over the states, averaged over 100 runs, for MC and TD at several α. Read the axes first. Claim, scoped: on this task, for the α values tried, TD's averaged error is lower. | old 32 (book Example 6.2 figures); book §6.2 | 5 |
| S05 | Why might TD do better? Batch updating | Take a **fixed** set of episodes (the offline, fixed-data case from MT03). Sweep it repeatedly; accumulate the increments and apply them after each sweep, until the table stops changing. With small α both methods converge to one answer each, but to **different** answers. Which answers? Next slide. | old 33 (text; plot omitted, R13); book §6.3 | 4 |
| S06 | You are the predictor | Eight episodes: A,0,B,0; B,1 six times; B,0. Students vote on V(B) and V(A) before the answer. V(B) = 3/4 by both. **Batch MC:** V(A) = 0, the average of the one return seen from A; it fits the observed returns best (minimum squared error on this data). **Batch TD:** V(A) = 3/4. It gives the values of the model that best explains the data (A → B always with reward 0; B ends with +1 three times in four): certainty equivalence. TD reaches this answer without building that model. **Which would you expect to predict better on new episodes?** If the process is Markov, 3/4: TD uses everything seen from B to value A. Neither answer is certified as the true value (A was seen once). | old 34–35 (fixed); book Example 6.4 | 6 |
| S07 | MC or TD: when to prefer which | Corrected summary table. TD: lower-variance target, uses the Markov property, learns before the episode ends, more sensitive to initial values. MC: unbiased target, does not rely on the Markov property. It avoids bootstrapping through a state that does not capture everything relevant (seen in 1.1–1.2); it does not repair that partial observability. It is simple. These are tendencies, not a universal selection rule. "TD usually learns faster" is an observation on many tasks; there is no general proof (book §6.2). Function-approximation claims wait for Week 5. Answers old 29's "Is MC useless?": no. | old 22, 29, 31, 36 (fixed); book §§6.2–6.3 | 3 |
| S08 | Between one step and a whole episode | MC waits for every reward; TD trusts the table after one. Question: why choose only these two? Backup diagrams for 1-step, 2-step, 3-step, …, ∞-step (= MC). One line: averaging several n is the λ mixture, Week 8. | old 41 (orientation), old 42 (picture; book Fig. 7.1) | 2 |
| S09 | The n-step target | **Derive** from G_t = R_{t+1} + γG_{t+1}: unroll n times, then replace the unseen remainder G_{t+n} by V(S_{t+n}): G_{t:t+n} = R_{t+1} + γR_{t+2} + ⋯ + γ^{n−1}R_{t+n} + γ^n V(S_{t+n}). n = 1 gives the TD target. **Terminal rule:** if t + n ≥ T, there is nothing left to estimate, and G_{t:t+n} = G_t. Update: the same form with U_t = G_{t:t+n}. **Availability:** the target for S_t is known after n more transitions or at termination, whichever comes first. At termination the pending updates are completed in visit order, with no further environment steps. Point to the book's pseudocode (§7.1). | old 43 (fixed: indexing, MC line, terminal rule); book §7.1 eq. 7.1–7.2 | 5 |
| S10 | **Your turn: n-step targets on our episode** (protected) | Same trajectory as 3.1. Starting table, labelled as a frozen snapshot for (a)–(b): the table TD(0) left after 3.1, V(1,1) = −0.03, V(1,2) = 0.5, V(2,1) = 0; γ = 0.5. **(a)** Targets from t = 0 for n = 1, 2, 3: **−0.055, 0.065, 0.19** (n = 3 reaches the goal, so it is G_0). **(b)** From t = 1 for n = 1, 2: **0.21, 0.46** (the second already ends at the goal). **(c)** Chronological n = 2 trace from the same starting table, α = 0.5: nothing after the first transition; after the second, the time-0 visit of (1,1) is updated to **0.0175**; at the goal, the time-1 visit to **0.23875** (target 0.46, no tail) and (1,2) to **0.75**. The repeated state is updated twice. **(d)** Which target uses the most real rewards? Which depends most on the table? Note: reaching the complete return as a target does not reproduce first-visit MC's update schedule. | new; numbers checked | 8 |
| S11 | Choosing n | **Mechanism:** the table enters the target with weight γ^n, and only if the episode is still running after n steps. So a larger n leans less on a poor table, including in undiscounted tasks such as the 19-state walk (γ = 1), where only the second factor acts. It also adds sampled rewards and transitions, which often (not always) adds noise. So an intermediate n often works best, and n interacts with α. Notes only: for a fixed table, the expected target's error at s is at most γ^n × P(still running after n steps) × V's worst error (book eq. 7.3 without the running factor); on our grid the post-3.1 table's worst error 0.336 becomes 0.067, 0.025, 0.011 for n = 1, 2, 3 (model-computed expectations, for checking only). *If kept (Q1):* the 19-state α–n plot, announced as a changed experiment (19 states, −1 on the left, values start at 0, error over the first 10 episodes, 100 runs). | old 44 (Q1); book §7.1, eq. 7.3, Example 7.1 | 3 |
| S12 | **Can we conclude that TD is better?** (protected evaluation reasoning) | No new setup: reuse S04's random walk (and S11's plot if kept). Five checks, each tied to the figure. **(1) Runs and uncertainty:** the book's curve shows means over 100 runs and no uncertainty. Single runs overlap: in a course simulation (notes), about 3 in 10 cross-pairs of single runs at episode 100 rank MC (α = 0.02) below TD (α = 0.1), though the means differ clearly. **(2) Fair tuning:** each method at its own best α, with the same tuning effort; show sensitivity instead of one α. **(3) Budget:** the x-axis counts episodes (interaction). Batch updating spends more computation per episode. Say which budget a claim is about. **(4) Learning, tuning and evaluation:** here the error against true values can be computed because the task is solved (MT11's benchmark). Choosing α on the same runs that are then reported makes the result optimistic. Without true values, evaluate a frozen estimator against independent return data; for control (Week 4 on), evaluate the policy on separate runs. **(5) Baseline:** compare against a simple reference under the same protocol. Here MC is TD's baseline; the starting table's error (0.236) is a reference level, which a useful learner should improve on, on average. **Format (R33):** the activity carries the checks rather than a separate list. Three claims; students vote supported or not, then discuss which check decides it. Example claims: "TD learns faster than MC on this random walk." (Supported, scoped: these α, per episode, mean of 100 runs.) "With a wider range of α, MC would win." (Book Exercise 6.4: the plot cannot say; it needs a sensitivity sweep with equal tuning effort.) "In my run MC beat TD, so MC is better." (Not supported: one run.) Book Exercise 6.5 (TD's error goes down, then up at large α) is a backup prompt. One line: changing one component at a time (n = 1 versus n = ∞) is an ablation; 6.2 develops it. | new; book Example 6.2 right-hand plot (p. 125), Exercises 6.4–6.5, Fig. 7.2; CS234 L3 p. 23 | 10 |
| S13 | Summary and next | One update form, three targets: G_t, R_{t+1} + γV(S_{t+1}), G_{t:t+n}. n trades the table's bias against sampling variance. A comparison needs runs, uncertainty, fair tuning, a stated budget and a baseline: the same checks apply in A1 and the project. Next week: control, with these targets for action values (Sarsa, Q-learning). The λ mixture comes in Week 8. | old 6 (roadmap line) | 2 |
| | | | **Total** | **58** |

**Protected time:** S10 (8) and S12 (10). The random-walk setup (S04) and the 19-state announcement (S11) are counted outside the ten evaluation minutes, as R17 asks.

**If the instructor wants more motivation time** (allowance up to 63): S06 and S12 benefit first (vote and discussion), not new topics.

## Choices for the instructor

**Q1 (R08/R13, deferred from 3.1): keep the 19-state α–n plot (old 44)?**
- **Recommendation: keep it** (originally inside S11's 3 minutes; after review R32, about 6 minutes, see the consolidated sequence in the shared review). It is the only evidence for "intermediate n often works best" and for the n–α interaction. S12 then reuses it for "show sensitivity, not one α", with no second setup.
- Its experiment differs from S04's random walk (19 states, −1 on the left, values start at 0, error over the first 10 episodes). It must be announced as a changed experiment, and its claims scoped to it (R13).
- Alternative (ChatGPT's earlier preference): omit it. The bias/variance argument and the eq. 7.3 numbers still motivate n; S12 makes the sensitivity point with the α values in Example 6.2's right-hand plot.

**Q2 (new): a course-generated learning-curve figure for S12?**
- The book's Example 6.2 plot (p. 125, right) shows averages over 100 runs without error bars, so it cannot show S12's first check.
- **Recommendation (conditional, R35):** one generated panel that replaces part of S12's explanation, not an addition: the same random walk, MC (α = 0.02) and TD (α = 0.1), the mean over 100 runs with a pointwise 95% interval for the mean, plus two or three single runs per method chosen before looking at results. Declared protocol in `scripts/check_mc_td_returns_claude.py`: every-visit constant-α MC, TD seeds 1000–1099, MC seeds 2000–2099. At episode 100 the means are 0.057 (TD) and 0.088 (MC), with interval half-widths 0.005 and 0.009. It could be a native PowerPoint chart, so you can edit it.
- Alternative: keep only the book figure and say the caveat aloud.

**Not reasons to pause (listed for cross-review):**
- Starting S10 from the table TD left in 3.1, not from V = 0. With V = 0 the bootstrapped term vanishes, and the trace would hide what n changes.
- Ordering: bias/variance and examples first, then n-step, then evaluation last, so the evaluation block reuses both figures without new setup.
- The old-deck fixes below.
- The evaluation scope: ablations get one line here; 4.2 and 6.2 develop baselines, metrics and ablations further.

## Delta against the old deck `4 - Model Free Prediction.pptx` (PPTX slide numbers)

| Old slides | Action | Where / what |
| --- | --- | --- |
| 22 (rest) | fix | S07. "Unbiased", "high variance", "applicable to non-Markovian problems". "Inefficient for Markovian problems – why?" is answered by S06 |
| 29 (rest) | fix | S07. "TD usually converges faster than MC (no mathematical result)" kept, scoped as in book §6.2. "Is MC useless? Let's brainstorm" becomes S07's closing question. "Better suited for exploration" stays cut (3.1) |
| 30 | fix | S02 picture (dartboard) and S03 text. V̄^π becomes V; r_t becomes R_{t+1}. "V̄^π(s_{t+1}) can be anything" becomes "biased while V is wrong at the successors". Keep "R_{t+1} + γv^π(S_{t+1}) is an unbiased (but unavailable) target" |
| 31 | fix | S07. "Zero bias" becomes "unbiased target" (a constant-α estimate still depends on its start). The two function-approximation lines move to Week 5 |
| 32 | keep | S04. Book Example 6.2 figures, caption "constant α, no discounting". Add the RMS definition in words |
| 33 | fix | S05. Text kept; the batch-training plot is cut (R13). "Converge deterministically (given small α)" kept |
| 34 | keep | S06. Episodes and MRP picture; votes before the answer |
| 35 | fix | S06. "Minimum mean-squared error" becomes "minimum squared error on the observed returns". "TD(0)" becomes "batch TD(0)". Further reading (book §6.3, Silver's notes) kept in the notes |
| 36 | keep | S07, merged |
| 37–40 | — | Used in 3.1 (MT12) |
| 41 | keep | S08, orientation only. The λ axis gets a Week 8 pointer |
| 42 | fix | S08. Backup-diagram picture kept. "Smoothed-out prediction" becomes the Week 8 pointer. The note that the rest of the deck is covered superficially is cut |
| 43 | fix | S09. G_t^{(n)} = R_t + … becomes G_{t:t+n} = R_{t+1} + ⋯ + γ^{n−1}R_{t+n} + γ^n V(S_{t+n}). The MC line's γ^T R_T becomes γ^{T−t−1}R_T. Add the terminal rule and the update delay. Keep the pseudocode pointer (book §7.1) |
| 44 | keep or cut | S11, per Q1. If kept, add the changed-experiment caption |
| 45–59 | — | Week 8 or cut (unchanged from the 3.1 delta) |

## Notation (`course/notation_guide.md`)

- **Available:** G_t, G_{t:t+n}, V(s), v^π, 𝔼_π[·], α, γ, T, U_t, δ_t, 𝒟.
- **No new symbol needed.** Bias is written 𝔼_π[U_t ∣ S_t = s] − v^π(s). Variance, RMS error and confidence intervals are said in words. If the render-ready content wants Var[·] or a standard-error symbol, that needs a guide entry first.
- **Time-indexed tables:** the book writes V_{t+n−1} in the n-step target. The slides say "the table when the update is made" instead. V_k stays reserved for DP sweeps (C6).
- **"Baseline":** S12 uses the word for a reference method in an experiment. In Week 7 b(s) is a policy-gradient baseline (guide item O2). Say once that these are different uses.

## Correctness notes for whoever writes the first-render content

- **Unbiasedness is about the target given S_t = s.** The first-visit MC sample average is unbiased; the every-visit average is biased but consistent (CS234 L3 p. 26). A constant-α estimate of either method depends on its starting value. Do not write "MC estimates have zero bias" without that scope.
- **The TD target's expectation is the Bellman backup of the current table** (MT09). It is unbiased for v^π(s) when V is correct at the successors. Correct successor values are sufficient for this, not necessary (3.1 review R14).
- **Batch convergence needs a small enough α** (book §6.3). Batch MC fits the observed returns; batch TD gives the certainty-equivalence values. Neither is the true value in general.
- **Eq. 7.3 is about the expected n-step target**, worst case over states. Single n-step targets can be further off. The grid numbers in S11 are expectations under the model, computed for checking only; the learner never sees them.
- **Random-walk curves:** RMS over the five states, then averaged over 100 runs (Example 6.2's right-hand plot; Figure 6.2 is the batch version and is not used). TD's curves at larger α go down and then up slightly; book Exercise 6.5 asks why, and the answer involves the constant step size and the initialization. That is not divergence.
- **Single-run statistic in S12:** a descriptive cross-pair share from two independent sets of 100 runs (0.29 at episode 100, 0.006 at episode 25), not 10,000 independent trials: each run appears in 100 pairs. State it with the episode and the protocol, or leave it out of the live content.
- **The 19-state plot (if kept):** left exit −1, so the true values range from −0.9 to 0.9; values start at 0; the error is averaged over the first 10 episodes and 100 runs (book Example 7.1). Its "best n" applies to that experiment only.
