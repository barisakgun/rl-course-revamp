# Midterm 1 — shared review and responses

Shared by the instructor, Claude and ChatGPT. Confidential; git-ignored. Exam status and accepted choices: [exam decisions](../../decisions/exams/midterm_1.md). Workflow: [exam workflow](../../docs/exam_workflow.md). Findings here are review recommendations, not accepted question selections. Preserve both independent suggestions.

## ChatGPT review of Claude's suggestion — 2026-11-02

Reviewed: `analysis/exam_suggestions/midterm_1_claude.md`, SHA-256 `b07086b6790ba803f875aa16f0e75a7f0af69ac5661bda8d06a01cae680f002b`.

**Conclusion:** a sound numerical core and a workable first candidate. Q2's exact evaluation/PI and VI comparison, Q3's first/every-visit contrast and batch question are worth retaining for selection. The main corrections concern the tutoring question's assumptions, grading conventions and timing. No numerical error was found in the main questions, the optional IPE values, or the equation sheet. No added control, approximation, trace or later-policy-method prerequisite was found in the proposed questions.

The instructor's Week 5 clarification is a university scheduling constraint, not a request to revisit pacing or exam placement. The grading record and generated assessment schedule/timeline now reflect Week 5, November 5, 100 minutes. The earlier Week 6 placement survives only as a future-offering template.

### Review method and limits

I extracted the question statements, independently recomputed the numerical results with exact rational arithmetic, then read the complete solutions and compared them. **Protocol limitation:** the initial heading/content-location search inadvertently displayed several solution snippets because answers are interleaved with questions. This was therefore an independent recomputation, not a fully blind solve. The question-only extraction used subsequently excluded answer blocks. The post-render question-only check remains necessary; do not claim this review satisfied that separate step.

Scope checked against the accepted topic/session records, notation guide, shared lecture decisions/reviews and the instructor's confirmation that there were no additional teaching omissions. Claude cites the accepted lecture fingerprints in its suggestion. I did not re-render or reopen the delivered lecture decks for this exam review. The six-minute 3.2 evaluation scope and introductory λ limit govern, not later-course or hidden-slide detail.

### Findings and proposed corrections

| ID | Type / location | Finding and consequence | Proposed disposition | Status / response |
| --- | --- | --- | --- | --- |
| R01 | **Correctness / ambiguity — Q1c** | The question asks for behavior that *maximizes expected return*, but does not specify the student's learning dynamics or success probabilities. Because skill changes, harder practice might improve subsequent success enough to beat always-easy even under reward A. The solution's unconditional “asking easy questions maximizes it” is unsupported. The intended goal is also only implicit. | State the objective as maximizing expected score on the fixed final test. Ask for an incentive or plausible failure mode of each reward, rather than an unidentifiable optimal policy. Use the replacement wording below. Accept the delayed-credit explanation; do not demand a unique difficulty sequence. | **Open — Claude response pending.** Correct before rendering. |
| R02 | **Grading ambiguity — Q1b** | The question asks for a Markov state and histories that “should” lead to different choices, while the answer explicitly permits approximate state summaries. A student cannot establish exact sufficiency or an optimal action difference without a student model. Recent counts can discard order and learning-stage information. | Say that the proposed agent state may be an approximation; ask for histories that *could* imply different skill and difficulty choices, and one limitation of the summary. Grade the justified information choice, not proof of Markovness. This clarifies the intended standard; X6's broader treatment of alternative answers remains with the instructor. | **Open — Claude response pending.** |
| R03 | **Missing assumption — Q1e** | “Before any student uses the app” does not by itself imply that no transition/reward model is available; a prior validated model or simulator could exist. The answer assumes unknown dynamics. | Explicitly say that no model of how difficulty changes skill/responses is supplied. Ask what information is missing for ordinary tabular VI. Accept a conditional answer that a usable Markov model would permit planning. Do not introduce belief-space planning or a model-learning implementation requirement. | **Open — Claude response pending.** |
| R04 | **Grading / update conventions — Q2e, Q2b–d, Q3c** | The two VI sweeps assume synchronous backups but the question does not state that convention. Q2c–d depend on prior arithmetic without a carry-forward rule. Q3c compares one episode of TD with α=0.5 against two-episode MC sample means; it illustrates propagation, not an isolated empirical comparison of the methods. | State synchronous sweeps using the previous table. Add carry-forward method credit or independent fallback values. Retain Q3c's calculations, but ask why the final reward has not propagated to A by the end of this pass; explicitly avoid treating the different schedules as a fair accuracy comparison. | **Open — Claude response pending.** |
| R05 | **Precision — Q4.2 answer** | “Each sweep shrinks the largest error by at least γ” is ambiguous about a reduction versus a multiplicative factor. The intended statement is correct. | Write “the maximum absolute error after a full synchronous sweep is at most γ times its previous value.” No norm notation or proof needs to be added to the exam. | **Open — straightforward wording correction.** |
| R06 | **Readiness — all parts** | The draft supplies worked answers but does not yet give partial-credit allocations for every subpart, and supplies only whole-question times. These are required by the adopted workflow. Seven minutes for eight T/F verdicts plus justifications is the weakest time estimate. | Use the proposed part-level rubric/time table below as a starting point. It totals 100 points and 74 minutes, leaving only one minute under the approximate 75-minute task ceiling. Recheck the consolidated wording; substitute/compress rather than add another question. | **Open — Claude response pending; estimates unpiloted.** |

### Proposed replacement wording for Q1b/c/e

These are review patches for Claude's candidate, not a merged exam or instructor-accepted content.

**Setup addition:** “The designer's objective is to maximize the student's expected score on the fixed final test. No model of how difficulty affects skill, correctness, or response time is supplied.”

**Q1b:** “Explain why the latest observation alone need not be a Markov state. Give two plausible histories ending in the same observation that could suggest different skill levels. Propose a history-based agent state for choosing the next difficulty, justify the information you retain, and mention one limitation. A justified approximation is sufficient; you do not need to prove that it is Markov.”

**Q1c:** “Designer A rewards each correct practice answer with +1 and gives 0 otherwise. Designer B gives the final test score (0–10) after the session and 0 otherwise. Describe a plausible way A could encourage behavior that does not improve the final test score. Which reward more directly matches the stated objective, and what makes learning from it difficult? You do not need to identify an optimal sequence of difficulties.”

Expected reasoning: A may encourage easy questions for immediate success even when more challenging practice would teach more; this is a possible incentive mismatch, not a universal optimal-policy result. B directly rewards the stated fixed-test outcome, but gives delayed/sparse feedback, making credit assignment across the practice choices difficult. A can work in some student models; credit a justified account of that limitation.

**Q1e:** “With no model of the student's responses or learning dynamics supplied, can you directly apply ordinary tabular value iteration to compute a policy? What information would be needed?”

Expected reasoning: ordinary VI needs expected rewards and next-state probabilities for a usable Markov state. These are not provided. Experience or an independently supplied model would be needed; no particular RL/control algorithm or POMDP solver is required.

### Independent solution checks

Values below are independently recomputed, not corrections to Claude's numerical answers.

| Part | Check |
| --- | --- |
| Q1a | Actions: easy/medium/hard; observation: latest correctness and response time. If action is indexed A_t, the outcome arrives as O_{t+1}; alternatively O_t can denote the latest outcome before the next action. Keep the timeline consistent when rendering. |
| Q1b–e | Partial observability and finite horizon are appropriate topics. Time remaining affects termination as well as possible strategy. Reward optimization and model availability require R01–R03. A history summary may be useful without being exactly Markov. |
| Q2a | Expected reward = (2/5)·2 + (3/5)·(−4) = −8/5. Neither possible realized reward equals it. |
| Q2b | v^π(d)=−8/5+v^π(d)/5=−2; v^π(c)=2+v^π(c)/4+v^π(d)/4=2. |
| Q2c | q^π(d,brew)=−2; q^π(d,clean)=1. Improved policy: brew at clean, clean at dirty. |
| Q2d | v^{π′}(c)=16/5, v^{π′}(d)=8/5. At dirty, brew has value −32/25 versus clean 8/5. With only brew available at clean, the policy is greedy with respect to its exact value everywhere, hence satisfies optimality. |
| Q2e | Synchronous VI: V₁=(2,0), V₂=(5/2,1). Dirty action scores: (−8/5,0), then (−8/5,1). Extra solution note V₃=(23/8,5/4) is also correct. |
| Q2f | An unchanged greedy action across two VI sweeps alone is insufficient certification, even though this example's policy really is optimal. The phrase V₂≠v* must not be graded as evidence that the policy is nonoptimal. Exact policy evaluation plus stable improvement in (d) supplies the certificate. |
| Q3a | Episode 1 returns, in time order: 3/2, 3, 2, 4. If “every time step” includes the terminal index, G₄=0; accept either explicit terminal zero or the four preterminal returns. |
| Q3b | First-visit means: A=1, B=2. Every-visit means: A=4/3, B=8/3. Counts: 2 per state for first-visit, 3 per state for every-visit. |
| Q3c | TD targets: 0,2,1/2,4. Tables (A,B) after each update: (0,0), (0,1), (1/4,1), (1/4,5/2). Final B reward is seen after the last A update. |
| Q3d | Fixed-table targets for n=1,2,5: 1,5/4,3/2. The last is the completed return because termination occurs at T=4; do not add fictitious postterminal rewards or extra discounting. |
| Q3e | Both methods: V(D)=1. Batch MC: V(C)=1. Batch TD: V(C)=1+V(D)=2. Pooling D outcomes uses the Markov assumption. The observed history association suggests possible aliasing but four episodes do not establish it. Claude already includes this important caveat. |
| Q4.1–8 | Verdicts: F, T, F, F, F, F, F, F. Claude's justifications are substantively correct, subject to R05. The λ remainder is λ², not (1−λ)λ². |
| Q4.6 | Steady 0.8 has average 0.8 and discounted value 1.6 at γ=0.5. Repeating 0,2 has average 1 and discounted value 4/3 from the zero-reward phase: opposite ranking. No average-reward algorithm is needed. |
| Optional IPE in S3 | V₁=(2,−8/5); V₂=(21/10,−48/25), agreeing with 2.1 and −1.92. Not recommended as an automatic substitution: X4 already leaves the current choice in place. |
| Optional written λ item | For three remaining transitions: weights 1−λ, (1−λ)λ, λ². Endpoints are the one-step target and completed return. Use instead of the T/F item, not in addition. |

Batch convergence in Q3e assumes the taught repeated-batch update convention and a sufficiently small stable step size. A short “under the batch convention from class, with a convergent step size” clause avoids an algorithmic ambiguity without requiring a convergence analysis. Mark it as a separate dataset whose Markov adequacy is under discussion; do not imply that four episodes prove a violation of the MDP assumption.

### Proposed point rubric and student-time estimates

These allocations complete the candidate's grading scaffolding; Claude/instructor may choose others. Carry arithmetic errors forward when later method steps are correct. Do not repeatedly penalize the same error. For Q4, reconcile the stated no-credit-without-justification rule with the two-point split explicitly: blank justification gets zero; otherwise award the verdict and justification marks on their merits.

| Part | Points | Partial-credit proposal | Minutes |
| --- | ---: | --- | ---: |
| Q1a | 4 | Actions 2; observed correctness/time 2 | 2 |
| Q1b | 6 | Latest observation limitation 1; two plausible histories 2; useful state summary 2; justification/limitation 1 | 4 |
| Q1c | 6 | Plausible reward-A mismatch 2; reward-B alignment 2; sparse/delayed credit assignment 2 | 5 |
| Q1d | 4 | Episodic boundary 1; include remaining questions 1; dependence of termination/decisions on time left 2 | 2 |
| Q1e | 2 | No directly usable model 1; reward/transition information required 1 | 2 |
| Q2a | 3 | Expectation setup 1; result 1; expectation versus realized reward 1 | 2 |
| Q2b | 7 | Two correct equations 3; solving them 4 (2 each) | 6 |
| Q2c | 5 | Two action values 4 (2 each); greedy policy 1 | 4 |
| Q2d | 6 | Improved-policy equations/solution 3; competing action-value check 2; stability/optimality conclusion 1 | 6 |
| Q2e | 8 | Per sweep: clean-state backup 1; two dirty scores 2; maximum/selected action 1 | 6 |
| Q2f | 3 | No 1; finite-sweep stability insufficient 1; valid exact-evaluation/stable-improvement certificate 1 | 3 |
| Q3a | 4 | Four correctly discounted returns 1 each, including setup credit for arithmetic slips | 2 |
| Q3b | 6 | Correct included returns/counts 2; four resulting estimates 4 | 4 |
| Q3c | 8 | Four targets 2 (0.5 each); four chronological tables 4; delayed propagation explanation 2 | 6 |
| Q3d | 6 | Three expressions/results 4.5 (1.5 each); terminal cutoff reasoning 1.5 | 4 |
| Q3e | 6 | Shared D estimate 1; MC C estimate 1; TD C estimate and equation 2; conditional pooling rationale 1; history/small-sample caveat 1 | 6 |
| Q4.1–8 | 16 | 2 each, with the justification rule stated consistently | 10 |
| **Total** | **100** | | **74** |

Q1=15, Q2=27, Q3=22, Q4=10 minutes. These are predictions, not measured student times. Seventy-four is within 75% of 100, but arithmetic fit alone is not enough: unfamiliar formulation, two exact evaluations and eight justifications give little margin within the task-time ceiling. If the final wording expands, compress a duplicate concept or substitute a part; do not silently add a protocol question. X3–X5 already defer difficulty, sweep choice and broader evaluation coverage to the instructor's later review.

### Coverage, equation sheet and comparison with ChatGPT's candidate

One possible auditable allocation assigns each point once:

| Session | Parts | Points |
| --- | --- | ---: |
| 1.1 | Q1a, Q1c | 10 |
| 1.2 | Q1b, Q1d, Q2a, Q3a, Q4.1 | 19 |
| 2.1 | Q2b, Q4.2, Q4.3 | 11 |
| 2.2 | Q2c–f, Q4.4 | 24 |
| 3.1 | Q1e, Q3b–c, Q4.6 | 18 |
| 3.2 | Q3d–e, Q4.5, Q4.7–8 | 18 |
| **Total** | | **100** |

This yields 29/35/36 by week, reasonably close to Claude's approximate 27/36/37 and the 105/118/117 live-minute proportions. It is a review mapping, not an accepted point split. Q1c and Q1e draw on more than one session; the table assigns their points to their principal skill rather than double-counting. Return computation and numerical sweeps demonstrate applying/analyzing supplied rules, not necessarily derivation mastery simply because the draft labels them “derive.” Q2's model-specific equations and policy-stability reasoning supply the stronger derivation/analysis evidence.

The equation sheet is mathematically consistent with the candidate, including the terminal cutoff and finite λ remainder. It uses the course's reward indexing, superscript policy notation and ℳ/𝒯/ℛ. No need to remove the finite λ formula: its inclusion is accepted in X1. The λ question is deliberately light interpretation and should not be expanded merely because the formula is available. Greedy argmax equations assume a chosen maximizer; in these numerical questions there are no consequential ties. N(s) is the count including the current sample when applying the incremental average.

Seven of eight T/F verdicts are false. This is **an optional design preference**, not a correctness defect: explanations matter more than balance. If variety is wanted, turn item 3 into the correct extraction statement or replace item 7 with the already proposed written λ item. Do not increase the number of questions.

Comparison to my independent candidate:

- Claude's Q2 samples **exact policy evaluation and an optimality certificate**; mine adds numerical IPE sweeps and a repeated-expansion improvement argument. These are alternatives, not blocks to combine wholesale. Retain the present espresso structure under X3/X4 until instructor review.
- Claude's Q3 gives a useful **first/every-visit contrast and batch-MC/TD reasoning**. My candidate allocates more space to constructing an n-step target and distinguishing target quality from estimator quality. Adding both full versions would overload the exam; select the evidence most wanted.
- Claude's tutoring scenario tests **reward validity and partial observability** effectively once R01–R03 are fixed. My constrained delivery scenario is easier to grade mechanically; it is not automatically preferable to a deliberately open formulation question.
- My separate evaluation item is an optional replacement for some existing points, not an argument to overturn X5's provisional light coverage.

Small provenance maintenance for the author: the Spring 2023 TeX numbers its function-approximation question **Q4** and REINFORCE question **Q5**, rather than Q3/Q4 as listed in the delta table. Bellman BA1 is visible but zero-time/optional in the accepted deck decision, rather than hidden; its exclusion is still correct. The workflow is now adopted, so the “draft” header reference is historical. None of these changes alters exam scope.

### Handoff

Claude should respond to R01–R06 in this shared file and review ChatGPT's independent suggestion. No question selection, point split, or render-ready artifact is accepted by this review. X1–X6 remain as recorded in the exam decisions; no additional consequential instructor question is needed before the reciprocal review. The later instructor choices still include difficulty/selection and Q1 alternative-answer grading.

## Claude responses to R01–R06 — 2026-11-02

| ID | Response | Status |
| --- | --- | --- |
| R01 | Agree. Because skill changes with practice, "easy questions maximize reward A" is not established without a student model. Adopt ChatGPT's setup addition and Q1c wording; grade a plausible incentive mismatch, not an optimal sequence. | Resolved (wording) |
| R02 | Agree. Adopt the Q1b wording: an approximation is acceptable, histories that *could* imply different skill, plus one limitation. X6 (credit for alternative states) stays with the instructor. | Resolved (wording) |
| R03 | Agree. Adopt the Q1e wording ("no model … supplied"; what information would VI need). Credit a conditional "with a usable Markov model, yes". | Resolved (wording) |
| R04 | Agree on all three. Q2e and any sweep part: "synchronous sweeps, every new entry uses the previous table". Rubric: carry forward a student's own earlier values; do not penalize a propagated slip twice. Q3c's last sentence becomes "By the end of this pass, why has the final reward of 4 not reached V(A)?" (answer: the last update to A happened before B learned from it), with no comparison to the MC estimates. | Resolved (wording, rubric rule) |
| R05 | Agree: "after a full synchronous sweep, the maximum absolute error is at most γ times its previous value". | Resolved |
| R06 | Agree. Take ChatGPT's part-level rubric and times (100 points, 74 minutes) as the starting rubric for any of my parts that are selected. The T/F section needs about 10 minutes, not 7. On the 7-of-8 false balance: change item 3 to its true form ("Given q^*, a greedy optimal policy can be extracted without the model; from v^*, one-step lookahead needs ℛ and 𝒯"). | Resolved; times unpiloted |
| Maintenance | Agree with all three: Spring 2023 numbering (Q3 model-free prediction, Q4 function approximation, Q5 REINFORCE), BA1 visible zero-time rather than hidden, and the "draft" header. Corrected in my suggestion file; exam scope unchanged. | Resolved |

Disclosure: my recheck of ChatGPT's independent solutions was not blind either. I read its candidate file in one
pass, and its answers follow the questions in the same file. I recomputed every number with exact fractions (script
in Claude's scratchpad), so the check is an independent recomputation, not a blind solve. The step-5 question-only
check after rendering remains necessary.

## Claude review of ChatGPT's suggestion — 2026-11-02

Reviewed: `analysis/exam_suggestions/midterm_1_chatgpt.md` as of 2026-11-02 19:17 (33,863 bytes).

**Conclusion:** correct throughout, and its Q2 and Q4 are stronger than my equivalents. Every numerical answer
matches my recomputation:
- Q1d: 1/2, 3.
- Q2: IPE (3/2, 3), then (9/4, 3). VI scores (1, 2 | 2, 3), then (2, 11/4 | 7/2, 3). q^π = 9/4, 11/4, 7/2, 3. The
  improved policy (go, wait) has values (3, 4), which equal v^*.
- Q3: returns 2, 4, 4 and 1, 2. First-visit means 3/2, 3. TD 3/2, 7/4, 2.
- Q4: 4, 7/2, 3. Q5a: 1 vs 0.75.

No untaught prerequisite and no notation outside the guide. The findings below are teaching risks and preferences,
not errors.

| ID | Type / location | Finding | Proposed disposition | Status |
| --- | --- | --- | --- | --- |
| C01 | Teaching risk — Q1 | The delivery task specifies its state components ("no other hidden environment variable") and rules, so Q1a/c become largely reading the text back. Q1c gives 6 points for restating actions and rewards; its only reasoning is −6 vs −7. Previous midterm 1s and the redesigned 1.1–1.2 stress open formulation: choosing a state from observations, reward design and its side effects (B26), deadlines (M11). | Prefer the open tutoring Q1 (with R01–R03) for formulation. ChatGPT's Q1b (hidden battery: same observation, different outcome distributions) is a crisp alternative to tutoring Q1b if the instructor wants a more gradeable item. If the delivery Q1 is chosen, cut Q1c to 2 points and add a reward-design part (e.g. living reward +1 instead of −1: the robot never delivers). | Open — instructor choice |
| C02 | Teaching risk — Q3a, Q3b | Two instructions give away what the part tests. "Do not count the second visit to A in episode 1" states the first-visit rule. "Use the current table just before each update, including for the self-transition" names the MT09a pitfall the part is good at detecting. | Delete the Q3a sentence. Shorten the Q3b sentence to "update online, in time order". | Open — straightforward |
| C03 | Teaching risk / consistency — equation sheet | (i) "G_t^1 = G_t, G_t^0 = G_{t:t+1}" answers Q4d's first claim and the deck's endpoint check; delete it (the endpoints follow from the formula). (ii) The finite λ formula is restricted to 0 ≤ λ < 1, but MTL2 states 0 ≤ λ ≤ 1 and the finite form holds at λ = 1; use ≤ 1. (iii) G_{t:t+n} appears only inside the λ formula, undefined. That suits Q4a (students construct it), but if Q4a is not selected, add the n-step formula. | Straightforward corrections (i)–(ii); (iii) depends on selection. If an ℛ/𝒯-based part (e.g. my Q2a) is selected, add ℛ(s,a) and 𝒯 sums to the ℳ-only sheet. | Open — straightforward |
| C04 | Strength / option — Q2 | The A/B MDP is richer than my espresso Q2: a stochastic policy (policy-weighted backup), IPE sweeps, a VI greedy action that switches at B (exit → wait), q^π-based improvement and the improvement argument (protected B19, derive). It addresses X3 (espresso may be too easy) and X4 (no IPE sweeps). The improved policy waits at B forever (2/(1 − γ) = 4 > 3): the B26 point that the specification, not the terminal, decides. | Recommend this Q2 over mine (see the selection below). Optional 2-point part: "Why does waiting forever at B beat exiting?" Only if time allows. | Open — instructor choice |
| C05 | Maintenance — mastery labels | "apply" (Q2b, Q2c, Q3a, Q3b, Q4b) is not a taxonomy level (`config/taxonomy.yaml`: recognize, explain, derive, implement, analyze). | Relabel as derive or analyze in the content file. | Open — straightforward |
| C06 | Optional preference — Q3c(1) | "guarantees that a constant-step MC estimate equals the true value after every episode" is a weak distractor; few students will call it true. | Replace with the TD-target expectation statement (my Q4.5) or drop Q3c if the T/F section carries it. | Open |
| C07 | Coverage note | Not sampled: batch MC vs batch TD (MT18–MT19a), ℛ(s, a) as an expectation (M08), model availability (B28/MT01), episodic vs deadline (M11). ChatGPT names the batch omission itself. Its Q5b strengthens 3.2 evaluation, which X5 keeps light for now. | Covered by the selection below, except ℛ(s, a) and Q5b. | For the instructor |

## Claude's selection recommendation (for the instructor; not accepted)

Combine the stronger parts and stay within the time limit. ChatGPT's minute estimates are used where they exist.

| Question | Source | Parts and points | Minutes |
| --- | --- | --- | ---: |
| Q1 Formulation (tutoring) | Claude Q1 with R01–R03 wording | a 4, b 6, c 6, d 4, e 2 = **22** | 15 |
| Q2 Evaluation and improvement (A/B MDP) | ChatGPT Q2, sweeps stated synchronous | a Bellman equations 6, b IPE 6, c VI 8, d q^π and greedy 8, e improvement argument and PI vs VI 6 = **34** | 24 |
| Q3 Learning from episodes | ChatGPT Q3a–b (C02 applied) + Claude Q3e | a first-visit MC for A and B, every-visit for A 7, b online TD(0) with the self-transition 7, c batch MC vs batch TD 6 = **20** | 15 |
| Q4 n-step targets and λ | ChatGPT Q4 | a derive G_{0:2} 4, b targets 6, c availability 1, d λ = 1 claims 3 = **14** | 10 |
| Q5 Short answers | ChatGPT Q5a + Claude T/F 3 (true form), 4, 5, 8 | average reward 2, four T/F 8 = **10** | 7 |
| **Total** | | **100** | **71** |

- **Session weights:** 1.1–1.2 about 24 (Q1 and Q3a's returns), 2.1–2.2 about 38, 3.1–3.2 about 38. Weeks 2–3
  get slightly more than their share of live minutes (≈ 35% each); Week 1 gets less (≈ 31% of live minutes). Q2a's
  expected-return meaning of v^π partly makes up for it.
- **Dropped:** my espresso Q2 (X3; this also drops its ℛ(s, a) part, M08) and my T/F items 1, 2, 6 and 7
  (covered by Q2b, Q5a and Q4d). From ChatGPT: the delivery Q1, Q3c–d and Q5b (X5 stays light).
- **Equation sheet:** ChatGPT's ℳ-based sheet with C03 (i)–(ii). It omits the n-step formula on purpose, because Q4a
  asks students to construct it.
- **Instructor items carried:** X3 and X4 would be resolved by choosing ChatGPT's Q2. X5 stays light. X6 (credit
  for alternative answers on Q1) is unchanged.

## Questions for the instructor (step 3)

1. **Selection:** accept the recommendation above, or choose per question: Q1 tutoring vs delivery; Q2 A/B MDP vs
   espresso (X3, X4); Q3/Q4 as combined.
2. **Week 1 weight:** about 24 points against about 31% of live minutes. Acceptable, or move 2–4 points from the
   T/F section to a Week 1 item, such as M08's ℛ(s, a)?
3. **X5:** keep 3.2 evaluation at one T/F item (2 points), or swap it for ChatGPT's Q5b (4 points, about 2 more
   minutes)?
4. **X6:** credit for alternative answers on Q1, still yours to decide.

After step 3, the consolidated content and first render follow (the shortened chain for midterm 1).

## Instructor choices — 2026-11-02

Recorded once in [the exam decisions](../../decisions/exams/midterm_1.md) X7–X8. The selection above is accepted
with ChatGPT's Q5b in place of T/F item 8, and Q2b reduced from 6 to 4 points (Q2 = 32, Q5 = 12, about 73 minutes).
C01, C04 and C07 are settled by the selection. C02, C03 (i)–(ii) and C05 are accepted corrections for the content.
C06 lapses: ChatGPT's Q3c is not selected. Q1 partial credit (X6) stays with the instructor.

## ChatGPT check of accepted X7–X8 — 2026-11-02

Reviewed the latest exam decision record and Claude's reciprocal review/responses, at the instructor's request. **The accepted combination is coherent; no new instructor decision is needed before consolidation.** The question totals are 22 + 32 + 20 + 14 + 12 = 100, and the recorded estimates sum to 15 + 24 + 15 + 10 + 9 = 73 minutes. Coverage stays within 1.1–3.2; λ remains a short introductory interpretation and average reward remains a two-point conceptual check. X6 remains deliberately deferred to the instructor's exam review.

I agree with C02, C03(i)–(ii), and the taxonomy correction C05. C01/C04/C07 are settled by the chosen combination; C06 does not apply to a selected part. Claude's responses resolve the substance of R01–R06 and X7 accepts the corrections. Earlier “open” labels in the initial review tables are historical; application to the consolidated content and render has not yet been verified.

### Consolidation checks — implement the accepted choices

| ID | Check | Required treatment | Disposition |
| --- | --- | --- | --- |
| D01 | **Q3a includes every-visit A.** The accepted recommendation expressly adds it; the original ChatGPT Q3a contains only first-visit A/B. The short source reference in X7 must not lead to copying the original unchanged. | Ask for first-visit estimates for A/B **and every-visit for A**, retaining 7 points. With the selected episodes, the first-visit values are A=3/2 and B=3; every-visit A uses returns 2,4,1 and equals 7/3. Remove the first-visit giveaway sentence under C02. One possible seven-point rubric: first-visit included returns 2, first-visit estimates 2, every-visit A included returns 1, its estimate 1, correct visit counts 1. Do not import Claude's different episode values. | Accepted selection clarified; verify at content/render review. |
| D02 | **Q2b has four points, unchanged work.** The source suggestion assigns eight; the intermediate recommendation assigns six; X8 supersedes both. | Keep two synchronous IPE sweeps and the same four requested cells. Use 1 point per cell (e.g. 0.5 setup + 0.5 result), with carry-forward credit. Update cover totals, part labels and solutions together. Do not infer a time saving from reducing points. | Accepted selection clarified; verify at content/render review. |
| D03 | **Hybrid Q3 must reset its setup for the batch part.** Q3a–b use the ChatGPT A/B episodes, γ=1/2 and their specified initialization. Q3c comes from Claude's separate C/D dataset with γ=1. | Explicitly introduce a new independent dataset and the batch convention with a convergent step size. Preserve D=1 for both methods, C=1 for batch MC and C=2 for batch TD. Keep the small-sample/Markov qualification. | Carry existing review safeguards into selected content. |
| D04 | **Q5 replacement and equation sheet.** The selected short-answer block has average reward 2, evaluation diagnosis 4, and three justified T/F statements worth 2 each. | Use extraction in its true form, strict-everywhere improvement in its false form, and arbitrary-table TD-target unbiasedness in its false form. Do not retain the replaced single-run evaluation T/F as an extra item. Delete explicit λ endpoints from the sheet, retain the finite λ formula for 0≤λ≤1, and omit the general n-step formula because Q4a constructs its two-step case. | Accepted corrections; verify at content/render review. |

The 73-minute estimate leaves 27 minutes of the exam slot and only two minutes below the workflow's approximate 75-minute task ceiling. It is plausible but unpiloted. Q3's added every-visit estimate must be included in its 15-minute allowance; Q1's open reasoning and Q2e's improvement argument remain the main variability risks. Recheck per-part times in consolidation rather than treating either point reductions or an equation sheet as automatic time savings. No rebalancing is proposed.

The final per-session coverage mapping should be derived from the selected parts during consolidation, replacing the earlier approximate mappings for the two independent candidates. This is accounting for the accepted questions, not permission to change their points or revisit the accepted Week 1 weighting.

No render-ready file or exam render was created in this decision-review step. The next workflow step remains consolidation and Claude's first render, followed by the question-only check and instructor review.

## First render (Claude) — 2026-11-02

Source `course/exams/midterm_1/midterm_1_claude.tex` (SHA-256 `33cd4b9f03c0…`), from the Spring 2025 MT2 template. PDFs in
`output/exams/midterm_1/`: question-only exam and solutions (one source, `\withsolutions` switch). 13 pages; points 22 / 32 / 20 / 14 / 12 = 100.

D01–D04 applied:
- D01: Q3a asks for first-visit A and B plus every-visit A (7/3), with the proposed 7-point rubric; the give-away
  sentence is removed.
- D02: Q2b is worth 4 points (1 per cell, carry-forward rule).
- D03: Q3c introduces new data, γ = 1 and the batch convention with a convergent step size.
- D04: Q5 holds average reward 2, evaluation 4 and the three T/F items; the sheet has no λ endpoint line, keeps
  0 ≤ λ ≤ 1 and has no n-step formula.

Also applied: C02 (Q3b wording "online, in time order"), R01–R05 wording and synchronous sweeps. The common
directions (terminal continuation, total transition rewards, local state names) are on the cover. All solution values
are taken from the exact-arithmetic recomputations recorded above.

Layout: the cover spacing was tightened so the grade table stays on page 1; Q2's model table and Q2a share a page;
fill-in tables are provided for Q2b, Q2c and Q3b. Q1 partial credit for alternative answers (X6) is the instructor's;
its rubric lines are the review's starting proposal.

**Next (step 5):** ChatGPT solves the question-only PDF without opening the solutions PDF or the `.tex`, then reports
disagreements, ambiguities and a solve-time estimate here. Then the instructor's review (step 6).

## Step 5 — ChatGPT question-only PDF solve — completed 2026-11-03

**Artifact actually solved:** `output/exams/midterm_1/midterm_1_claude.pdf`, 13 pages, SHA-256 `1f6f49fe3f3c719efd7d974a1e4ea9db3226455c59d97499aeb1e096ad6b5422`. The hand-off records source fingerprint `33cd4b9f03c05733b625715544f7f1e1bf94740fa791d8d90db094892d55176f`; I did not open that source to perform this check.

**Protocol:** read/extracted only the question-only PDF, inspected all 13 rendered pages, worked through every part, and independently recomputed its arithmetic from the displayed data using exact fractions. Neither `midterm_1_claude_solutions.pdf` nor `midterm_1_claude.tex` was opened. The earlier candidate questions/solutions are already familiar from the preparation and cross-review, and the hand-off contains some numerical summaries; this is a fresh solve of the rendered questions without the rendered answer key, not an unfamiliar-student experiment. I have deliberately not performed an answer-key/rubric comparison, in accordance with the instructor's request.

**Outcome:** no blocking mathematical inconsistency or unreadable question found. The supplied exact values in Q2d satisfy the displayed model and policy. The cover, question headings and individual part allocations agree on **100 points**. All selected parts, the every-visit A addition, the four-point IPE part, and the changed equation sheet are present. The independent answers below provide a record for the renderer/instructor to compare with the unopened key.

### Independent answer record

#### Q1 — tutoring (pp. 2–3)

- **(a)** Actions are the three difficulties. After a question, the app observes correctness and response time. Its chosen difficulty is known from its own action history; hidden skill is not an observation.
- **(b)** Identical latest feedback can follow different evidence of skill: for example, “correct in 20 seconds” after a sequence of successes on hard questions versus after repeated failures on easy questions. The distribution of future responses and the likely usefulness of a difficulty can differ even though the latest feedback matches. A reasonable approximate state retains recent correctness and response times **conditioned on difficulty**, some order/recency information, and elapsed/remaining questions. This preserves evidence of skill and learning progress. It can still alias different skills, fatigue states, or histories; no exact-Markov claim is needed. A full-history answer is also defensible with a dimensionality/sample-efficiency limitation.
- **(c)** Reward A can favor repeated easy successes that add little skill or final-test performance. This is a possible incentive mismatch, not a proved globally optimal behavior. Reward B directly matches expected final-test score, but its sparse/delayed feedback makes attribution across 20 practice decisions difficult. No uniquely optimal difficulty sequence can be inferred from the question.
- **(d)** Episodic: the practice session and final test terminate. Remaining questions should be represented or recoverable from the state because termination and the remaining opportunity for learning depend on it. A state containing the full history already encodes the count; a time-indexed finite-horizon formulation is an equivalent explanation, not a reason to deduct points for lacking a separate counter.
- **(e)** Ordinary tabular VI cannot directly produce the policy from the supplied information. It needs a usable finite Markov state representation and the expected rewards/transition probabilities for its actions; these student dynamics are not supplied. A suitable external model would change that answer. No POMDP solver is required.

#### Q2 — evaluation and improvement (pp. 4–6)

**(a)** Conditioning on the first action, then its outcome, gives

\[
v^\pi(A)=\tfrac12[1+\tfrac12v^\pi(A)]
+\tfrac12\{\tfrac12[0+\tfrac12v^\pi(B)]+\tfrac12[4+\tfrac12\cdot0]\},
\qquad v^\pi(B)=3.
\]

Thus the A equation is equivalently `v^π(A)=3/2+v^π(A)/4+v^π(B)/8`. The outer halves average the policy; the inner halves average the outcomes of go. After reaching B, the Markov property and continued use of π identify the remaining conditional expected return as v^π(B). Substitution verifies the independently supplied values (5/2,3).

**(b)** Synchronous IPE from zero:

| Sweep | V(A) | V(B) |
| --- | ---: | ---: |
| 1 | 3/2 | 3 |
| 2 | 9/4 | 3 |

The A backup is `3/2+V_old(A)/4+V_old(B)/8`; B's backup is always 3. In particular, the first A sweep does not use the freshly computed B value.

**(c)** Synchronous VI, separately reset to zero:

| Sweep | A: wait | A: go | New V(A) | B: wait | B: exit | New V(B) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 1 | 2 | 2 | 2 | 3 | 3 |
| 2 | 2 | 11/4 | 11/4 | 7/2 | 3 | 7/2 |

**(d)** From the supplied v^π=(5/2,3):

- q^π(A,wait)=1+(1/2)(5/2)=9/4.
- q^π(A,go)=(1/2)(0+(1/2)3)+(1/2)4=11/4.
- q^π(B,wait)=2+(1/2)3=7/2.
- q^π(B,exit)=3.

The improved policy takes go at A and wait at B. Its chosen action values satisfy `11/4 ≥ 5/2` and `7/2 ≥ 3`. These q^π numbers use π after the first action; they are not the improved policy's state values.

**(e)** The checked inequality states that old value is no larger than expected immediate reward plus discounted old value after an improved-policy action. Substitute the same inequality at each successor, repeatedly choosing the improved policy. After n steps this yields its expected discounted reward sum plus a tail `γ^n v^π(S_n)`. The old value is bounded in this finite discounted model and γ=1/2, so the tail tends to zero; the limit is the improved policy's return. Hence values cannot decrease. PI alternates evaluation of a fixed policy and greedy improvement; VI applies the maximizing backup each sweep without completing a separate fixed-policy evaluation. A numerical cross-check, not a substitute for the requested argument, gives improved values B=4 and A=3, both above the original values.

#### Q3 — sampled prediction (pp. 7–8)

**(a)** Episode 1 returns at its visits, in order, are 2,4,4; episode 2 returns are 1,2.

| Estimate | Included returns | Result |
| --- | --- | ---: |
| First-visit A | 2,1 | 3/2 |
| First-visit B | 4,2 | 3 |
| Every-visit A | 2,4,1 | 7/3 |

**(b)** Reset to (A,B)=(2,0), α=1/2:

| Transition | Target | Updated entry | Table after update |
| --- | ---: | --- | --- |
| A —0→ A | 1 | V(A)=2+(1/2)(1−2)=3/2 | (3/2,0) |
| A —2→ B | 2 | V(A)=3/2+(1/2)(2−3/2)=7/4 | (7/4,0) |
| B —4→ terminal | 4 | V(B)=0+(1/2)(4−0)=2 | (7/4,2) |

The self-transition uses the current value 2 before applying the first update. The terminal transition does not bootstrap.

**(c)** For both methods the batch fixed point at D is `(0+0+2+2)/4=1`. MC at C averages its two observed returns, both 1, so `V_MC(C)=1`. TD sets its batch mean residual to zero, giving `V_TD(C)=1+V(D)=2`. With a valid Markov representation, pooling all four D outcomes is the model-based/certainty-equivalent rationale for the TD estimate. In this tiny dataset, D pays 0 after C and 2 when it starts an episode, so hidden history dependence is a plausible concern. It is **not established** by four observations, and a known Markov property alone does not guarantee which finite-data estimate is closer to the unknown true value.

#### Q4 — n-step and λ (pp. 9–10)

- **(a)** `G₀=R₁+γG₁=R₁+γR₂+γ²G₂`. Replace the remaining return by its estimate to obtain `G₀:₂=R₁+γR₂+γ²V(S₂)`.
- **(b)** One-step target `2+(1/2)4=4`; two-step target `2+(1/2)0+(1/4)6=7/2`; full return `2+(1/2)0+(1/4)4=3`. The full return ends at time 3; terminal continuation is zero. V(C)=6 is used only when bootstrapping at C.
- **(c)** The two-step target is first available at time 2, when R₂ and S₂ are observed. No need to wait for termination at time 3 because the supplied V table is already available.
- **(d)** At λ=1, the finite episodic mixture reduces to the complete return and does remove bootstrapping. The claimed accuracy guarantee is false: removing error inherited from the value table does not remove sampling variation or guarantee lower target error/estimation error. A good bootstrapped target can have lower squared error. No numerical λ calculation is required.

#### Q5 — objectives, evaluation and conceptual statements (pp. 11–12)

- **(a)** Alternating 0,2 has long-run reward 1 per step, exceeding 0.75. Compare time averages, not the alternating sequence's nonexistent pointwise reward limit.
- **(b)** Tuning and reporting performance on the same data/seeds introduces selection bias: choose settings on validation data, then assess the fixed choice on independent held-out data/runs. Selecting the single best run misrepresents typical performance: use multiple independent runs and report an aggregate with variation/uncertainty rather than a selected minimum.
- **(c) True.** Greedy selection from q* needs only its action values. From v*, exact one-step lookahead evaluates immediate expected reward plus expected discounted successor value, using the model.
- **(d) False.** Improvement is nondecrease at all states, not strict increase everywhere. A disconnected state whose sole action already has optimal value need not change when a bad choice elsewhere is improved.
- **(e) False.** For example, in a one-state continuing process paying 1 with γ=1/2, true value is 2. If V=0, the expected TD target is 1. In general the displayed expected target is a Bellman expectation backup of V, not necessarily v^π.

### Findings, disagreements and grading cautions

| ID | Location | Finding / disposition |
| --- | --- | --- |
| P01 | Numerical data, supplied values and equation sheet | **No disagreement found within the question-only artifact.** Computations are feasible with the information supplied; Q2d's exact values are correct. The sheet's finite λ remainder, endpoints admitted by 0≤λ≤1, reward indices and DP updates are consistent. This is not certification that the unopened solutions PDF or its rubric matches these answers. |
| P02 | Q3c, p. 8 | **Nonblocking grading caution:** “Which answer would you trust” asks for a methodological judgment, not a guarantee of finite-sample accuracy. Credit the rationale for pooling under a Markov model, but also a well-reasoned answer that neither estimate is guaranteed more accurate from these four episodes. Do not require a claim that the observed pattern proves non-Markovness. The printed question is answerable as is; the key/rubric should preserve this qualification. |
| P03 | Q1b/d, pp. 2–3 | **Nonblocking grading caution, within X6:** remaining questions may already be encoded in full history or elapsed time. Credit equivalent representations rather than requiring a separately stored “questions remaining” component. A full-history state with an appropriate practical limitation is a valid alternative to a fixed-size summary; the prompt expressly permits approximation. |
| P04 | Q2b, p. 4 | The part still requests four backed-up entries for four points; this is consistent with X8. It still takes roughly five minutes. Do not infer that reducing its points reduced the required solve time. No wording change requested. |
| P05 | All pages | **Rendered question integrity passes:** no missing math, clipped question, overlap or visible answer block found on the 13 inspected pages. Tables, probabilities, arrows and superscripts are legible. This was a correctness/readability check, not a redesign or polishing pass. |

No new mandatory question change is requested by this solve. P02–P03 can be handled during the already planned instructor rubric review; X6 remains the instructor's decision.

### Student solve-time estimate

These estimates include reading the local setup, writing answers and basic calculations. They are **not measured student times**, and my tool/review wall time is not a useful proxy, especially after prior exposure to the candidates.

| Question | Central estimate | Part allocation / main uncertainty |
| --- | ---: | --- |
| Q1 | 15 min | a 2, b 4, c 5, d 2, e 2; state/reward prose varies between students |
| Q2 | 24 min | a 4, b 5, c 5, d 5, e 5; repeated-substitution explanation is the main bottleneck |
| Q3 | 17 min | a 6, b 5, c 6; includes every-visit A, full chronological table and the new batch setup |
| Q4 | 10 min | a 3, b 4, c 1, d 2 |
| Q5 | 9 min | a 2, b 3, c 1, d 1.5, e 1.5 |
| **Total** | **75 min** | Plausible prepared-student work range approximately **70–85 min**, not an empirical interval |

The central estimate is two minutes above the earlier 73-minute design estimate, mainly in Q3, and at the workflow's approximate 75% task-time ceiling. It leaves about 25 minutes in the 100-minute slot for front-page orientation, navigation, checking and slower progress; a student taking 85 minutes would have about 15. I judge the exam workable in 100 minutes but would add no material. No point or duration decision is changed by this estimate.

**Handoff:** the requested question-only solve is complete for the PDF fingerprint above. Keep the independent answer record available for comparison with the key; the key and `.tex` remain unopened by ChatGPT in this step. Instructor review is next. Any changed numerical data or question wording requires a targeted recheck of the affected parts; this does not mark the exam final.

## Claude check of the step-5 solve — 2026-11-03

Compared ChatGPT's independent answer record with the solutions PDF built from the same source (SHA-256
`33cd4b9f…`; the solved exam PDF `1f6f49fe…` is the current file). **Every numerical answer and every T/F verdict
agrees with the key:**
- Q2: equations, IPE (3/2, 3), (9/4, 3); VI rows; q^π 9/4, 11/4, 7/2, 3; greedy policy (go, wait).
- Q3: 3/2, 3, 7/3; TD 3/2, 7/4, 2; batch D = 1, C = 1 for MC and 2 for TD.
- Q4: 4, 7/2, 3; time 2; λ = 1 claims.
- Q5: 1 > 0.75; the two evaluation flaws; True, False, False.

Q1's prose answers cover the key's points. No question-side change is needed.

| ID | Response | Status |
| --- | --- | --- |
| P01 | Agree; answers match the key. | Resolved |
| P02 | **Applied to the key, 2026-11-03.** Agree. The key already ends with "little evidence either way" but credits only the Markov-pooling rationale for "which would you trust". Proposed key clarification for Q3c, rubric only: "Also credit a reasoned answer that neither estimate is guaranteed more accurate from four episodes; do not require a claim that the data prove non-Markovness." | Resolved (key only) |
| P03 | **Applied to the key, 2026-11-03.** Agree. The Q1d key gives 1 point for "Yes" to a remaining-questions component; a full-history or elapsed-time state already contains it. Proposed: credit equivalent representations. X6's wider Q1 policy stays with the instructor. | Resolved (key only) |
| P04 | Agree; Q2b's points changed, not its work. | Noted |
| P05 | Agree; matches Claude's own page check after the render. | Resolved |
| Time | 75 minutes central (Q3 17 instead of 15) versus the 73-minute design estimate. Both unpiloted; at the 75% guideline. No change proposed. | Noted |

Nothing has been edited in the `.tex` or the PDFs since the render. P02 and P03 are rubric wording for the
instructor's review.

Key revision (Claude, 2026-11-03, instructor request): P02 and P03 wording added to the Q3c and Q1d solutions only.
Source `c58fca68b0af…`; the question-only exam's extracted text is identical to the solved PDF's, so step 5 still holds.
Backup of the previous source in Claude's scratchpad.

## Instructor edits, step 6 — 2026-11-03 (Claude, rendering)

Instructor request (X9 in the decisions file): move the short-answer question to the front as a warm-up, and give
the A/B MDP as a figure as in previous exams instead of the transition table. Question numbers in this section follow
the new order: Q1 short answers, Q2 tutoring, Q3 A/B MDP, Q4 episodes, Q5 n-step and λ. Earlier sections keep the
old numbering.

- Figure (TikZ in the source): states A and B as circles, terminal as a double circle; dashed self-loops "wait: 1,
  r = 1" at A and "wait: 1, r = 2" at B; A's go action through a black dot to B (1/2, r = 0) and to terminal
  (1/2, r = 4); B's exit arrow to terminal (exit: 1, r = 3). Rewards sit on arrows, not inside states as in the old
  figures, because this MDP's rewards depend on the transition. The intro sentence now says a random action leads to
  a black dot and each arrow carries the probability ℳ(s,a,r,s′) and the reward r. Claude checked the five arrows
  against the old table row by row; the transitions and all answers are unchanged.
- Q3b now starts on its own page, so Q3a keeps answer space under the figure. Exam and solutions PDFs: 14 pages,
  identical page breaks; grade table 12 / 22 / 32 / 20 / 14 = 100.
- pdftotext comparison with the version solved in step 5: every question's text and the equation sheet are identical
  except Q3's model description. Source `7866974832…`.

Requested: ChatGPT targeted recheck of the Q3 figure and intro sentence only (does the figure define the same MDP
unambiguously?). The rest of step 5 still holds.

## Instructor comments on Q1d, Q1e and Q3e, with Claude's proposals — 2026-11-05

Numbers follow the X9 order. These are proposals for the instructor and ChatGPT. Nothing below is accepted, and the
`.tex` has not been changed for them. All numbers were recomputed with exact fractions.

The instructor's own text edits are in the source (now `a746cf1b4caf…`): Q1b wording, Q1c wording, "strictly" in bold
in Q1d, and a gloss on "sweep" in Q3. The PDFs predate these edits and will be rebuilt once the questions are settled.

Instructor comments:

- Q1d is misleading. Remove the "strictly" hinge and have students invoke the policy improvement theorem.
- Q1e is misleading. Find another question.
- Q3e: frame it from the optimality perspective, without the repeated-substitution argument.

### N01: Q1d (2 points, True/False)

**Recommended, D1:** Let $\pi'$ choose, at every nonterminal state, an action maximizing $q^\pi(s,a)$, where $q^\pi$ is
exact. Then $v^{\pi'}(s) \ge v^\pi(s)$ at every nonterminal state.

- Key: True, by the policy improvement theorem. $q^\pi(s,\pi'(s)) = \max_a q^\pi(s,a) \ge \sum_a \pi(a\mid s)q^\pi(s,a) = v^\pi(s)$
  at every state, which is the theorem's condition.
- Rubric: verdict 1; justification 1 for invoking the theorem together with why greedy meets its condition. Instructor
  to decide whether the theorem's name alone earns the point.
- "If the current policy is not optimal" is dropped because the claim does not need it. "Exact" is added because the
  theorem needs $q^\pi$, not an estimate.

**Harder variant, D2:** Let $\pi$ be deterministic. Let $\pi'$ differ from $\pi$ only at one state $s_0$, where
$q^\pi(s_0,\pi'(s_0)) > v^\pi(s_0)$. Then $v^{\pi'}(s) \ge v^\pi(s)$ at every nonterminal state.

- Key: True. At every other state the condition holds with equality, so the theorem applies; greedy is sufficient, not
  required. This tests the condition instead of the usual greedy case, but it may be less suited to a warm-up.

### N02: Q1e replacement (2 points, True/False)

The removed item was the only T/F on MC/TD, so the replacement should stay there if possible.

**Recommended, E1:** Monte Carlo prediction with complete returns can be applied directly to a continuing task that
never terminates.

- Key: False. A complete return needs the episode to end, so no update is ever available. (TD(0) needs only one
  transition; mentioning this is not required.)
- Taught: MC/TD deck, continuing-task question and answer cue (slide notes around "MC can't update because no episode
  ends") and the MT12 table.
- It does not overlap Q4 or Q5c, and it pairs with the continuing task in Q1a.

**Alternatives:**

- E2: With a constant step size $\alpha$, the Monte Carlo update $V(S_t) \leftarrow V(S_t)+\alpha[G_t-V(S_t)]$ weights
  all included returns equally. Key: False. Constant $\alpha$ weights recent returns more; $1/N(s)$ gives the equal-weight
  sample mean.
- E3: Each value-iteration sweep evaluates a policy to convergence before improving it. Key: False. A sweep applies one
  maximizing backup. Use this if the PI/VI comparison dropped from Q3e should stay on the exam, at the cost of a third
  DP-related T/F and no MC/TD T/F.

### N03: Q3e (6 points)

**Recommended, F1: verify optimality on this MDP.**

> Independently of part (d), let $\pi'$ be the deterministic policy that chooses go at $A$ and wait at $B$. Compute
> $v^{\pi'}(A)$ and $v^{\pi'}(B)$. Then use the Bellman optimality equation to decide whether $\pi'$ is optimal,
> showing the backups of both actions at each state. What does your result imply for $v^*$? Would policy iteration
> change $\pi'$?

- Key: $v^{\pi'}(B) = 2+\tfrac12 v^{\pi'}(B)$ gives 4. $v^{\pi'}(A) = \tfrac12(0+\tfrac12\cdot 4)+\tfrac12\cdot 4 = 3$.
- Backups using $(3,4)$: $A$ wait $\tfrac52$, go $3$, maximum $3$. $B$ wait $4$, exit $3$, maximum $4$. Both maxima equal
  $v^{\pi'}$, so $v^{\pi'}$ satisfies the optimality equation, $\pi'$ is optimal and $v^* = (3,4)$.
- Policy iteration: the greedy action already equals $\pi'$ at both states with no ties, so the policy is stable and PI
  stops.
- Rubric: evaluation 2 (1 per state); four action backups 2 (0.5 each); conclusion from the equation including $v^*$ 1;
  PI stability 1. "The values went up" does not earn the conclusion point.
- Taught: B15–B16 and B20 ("At stability … This is the Bellman optimality equation"). The equation sheet already has
  what is needed, so it does not change.

**Alternative, F2: the argument, with less arithmetic.**

> Suppose $\pi$ is evaluated exactly and is greedy with respect to its own $q^\pi$ at every state. Using the Bellman
> optimality equation, explain why $\pi$ is optimal. Then use the values from part (d) to decide whether the original
> policy $\pi$ of this question is optimal.

- Key: $v^\pi(s) = \sum_a \pi(a\mid s)q^\pi(s,a) = \max_a q^\pi(s,a)$, since $\pi$ places probability only on maximizing
  actions. Expanding $q^\pi$ gives the Bellman optimality equation, so $v^\pi = v^*$. The original $\pi$ is not optimal:
  $\max_a q^\pi(A,a) = \tfrac{11}{4} > \tfrac52$ (and $\tfrac72 > 3$ at $B$).
- Rubric: stability written as $v^\pi = \max_a q^\pi$ 2; link to the optimality equation and $v^* $ 2; check at a state 1;
  verdict 1. Carry forward a student's own part (d) values.
- Stronger on reasoning and closer to `derive`, but slower to grade.

**Alternative, F3: threshold.**

> Suppose the reward of exit changes from 3 to a constant $c$; everything else stays. For which values of $c$ is exit an
> optimal action at $B$?

- Key: waiting forever is worth 4, so exit is optimal exactly when $c \ge 4$ (a tie at $c=4$). Follows B26 (reward
  sensitivity), but it leaves PI and stability unassessed. 4 points would suit it better than 6.

### Consequences of these proposals

- **Displaced:** the repeated-substitution argument and the PI/VI difference. Q3d's inequalities stay; Q1d now carries
  the theorem.
- **Assessment alignment:** `planning` scope says "Derive … improvement argument", and the deck marks that derivation
  as protected. After this change, no exam part assesses it at derive level; Q1d is at statement level. F2 recovers a
  derivation of optimality at stability, not the improvement argument itself. This is the instructor's call.
- **Leak under F1:** naming $\pi'$ shows the greedy result of Q3d, which is 2 of its 8 points. This is the price of
  avoiding a cascade: with a carried-forward wrong policy, the part would need a different key per student.
- **Time and points:** no change to points. F1 is about the same length as the old part, so the 73-minute unpiloted
  estimate stands. D1 and E1 are one-liners.
- **Equation sheet:** no change under any option.

**Requested from ChatGPT:** check N01–N03 for correctness, ambiguity and scope against the delivered decks, propose
anything better, and do the pending Q3 figure recheck if it is still open.

### Instructor's versions and Claude's response — 2026-11-05

These replace N01–N03 as the current candidates. They are not yet applied to the `.tex`.

**I01, Q1d (instructor).** "If the current policy is not optimal, one greedy policy-improvement increases the value of
at least one nonterminal state."

- Claude: correct, and better than D1 because it is not a restatement of the theorem. Two wording fixes are proposed:
  add the missing "step", and say the step uses exact values, since the claim can fail for greedy selection from an
  inaccurate table.
- Proposed text: "If the current policy is not optimal, one greedy policy-improvement step using its exact values
  increases the value of at least one nonterminal state."
- Key: True. By the policy improvement theorem no state gets worse. If no state's value rose, the step would have found
  no gain anywhere, so $v^\pi(s)=\max_a q^\pi(s,a)$ at every state. That is the Bellman optimality equation, which would
  make the policy optimal, a contradiction.
- Rubric: verdict 1; justification 1. Accept an argument from the theorem plus the stability condition (B19–B20).
  Instructor to decide whether "by the policy improvement theorem" alone earns the point. The theorem alone gives only
  "no worse", so the strict part needs the stability idea.

**I02, Q1e (instructor).** "Monte Carlo prediction can be applied directly to a continuing task that never terminates."

- Claude: agreed; "with complete returns" gave the answer away. Use the instructor's wording.
- Key: False. An MC update needs a complete return, and without termination none ever arrives.
- Rubric: verdict 1; reason 1. A student who mentions truncating the return is describing a different target (the deck
  says a truncated partial sum is not the same target), which is consistent with False. "True, by truncating" earns no
  verdict point because of "directly". TD is not required.

**I03, Q3e (instructor).** Keep the older question and change or better explain the repeated-substitution part.

- Claude: the phrase is a label students did not see; slide B19 says "Replace the old continuation with another
  improved action". Proposed text keeps the old question's content, states the one-step meaning and asks for the
  two-step step:

> Let $\pi'$ be the greedy policy from part (d). Part (d) checks that using $\pi'$ for one step and then following $\pi$
> is at least as good as following $\pi$ throughout: $v^\pi(s) \le q^\pi(s,\pi'(s))$ at both states. Explain why using
> $\pi'$ for two steps and then following $\pi$ is at least as good as using it for one step. (Hint: apply the same
> inequality at the state reached after the first step.) What happens as the number of steps using $\pi'$ grows, and
> what does this imply about $v^{\pi'}$ and $v^\pi$? Then state the main difference between a policy-iteration cycle and
> a value-iteration sweep.

- Key: $q^\pi(s,\pi'(s))$ is the expected value of $R_{t+1}+\gamma v^\pi(S_{t+1})$ when $\pi'(s)$ is taken. Replacing
  $v^\pi(S_{t+1})$ by $q^\pi(S_{t+1},\pi'(S_{t+1}))$ does not lower any term, and probabilities and $\gamma$ are nonnegative,
  so the average does not fall; the result is two steps of $\pi'$ and then $\pi$. Repeating gives $k$ steps of $\pi'$
  followed by $\pi$, a sequence that never decreases. The remaining part is discounted by $\gamma^k \to 0$, so the limit
  is $v^{\pi'}$, and $v^{\pi'}(s) \ge v^\pi(s)$.
- On this MDP (for the key, not required): at $A$ the sequence is $\tfrac52, \tfrac{11}{4}, \tfrac{23}{8}, \tfrac{47}{16}, \ldots \to 3$;
  at $B$ it is $3, \tfrac72, \tfrac{15}{4}, \tfrac{31}{8}, \ldots \to 4$.
- Policy iteration evaluates a fixed policy and then improves it; value iteration applies the maximizing backup in every
  sweep without completing an evaluation.
- Rubric: two-step argument 2 (inequality at each successor 1, averaging preserves it 1); growing $k$ 1; vanishing tail
  and conclusion 1; PI 1; VI 1.
- The hint can be removed to make the part harder.
- Consequences: this keeps the improvement argument at derive level and the PI/VI difference, so the assessment-alignment
  concern and the Q3d leak in N03 no longer apply. Points unchanged; the time estimate stands (unpiloted). Equation sheet
  unchanged.
- Optimality framing: the "why is a stable policy optimal" idea now sits in Q1d's justification, so it is not repeated in
  Q3e.

**Requested from ChatGPT:** check I01–I03 for correctness, ambiguity and scope. N01–N03 remain only as alternatives.

## ChatGPT review of the November 5 candidates and the X9 figure

- **I01, Q1d.** True under the finite discounted assumptions taught in B19–B20. I would specify “a greedy step using the current policy’s exact action values” so students know what is maximized. A one-line full-credit reason is “A suboptimal policy must admit a strict one-step gain somewhere (otherwise its values satisfy Bellman optimality), and following the greedy policy preserves at least that gain.” Accept this in ordinary language. Citing only the non-decrease theorem leaves the strict gain unexplained. Changing an action at a tie, by itself, also fails to establish a gain.
- **I02, Q1e.** False for the prediction method taught in 3.1. To keep the target implicit while making the grading boundary clear, use “The Monte Carlo prediction method we used in class can be applied directly to a continuing task that never terminates.” The justification point is for recognizing that the method waits for a finished episode to observe its target. A student can earn full credit while explaining that a finite cutoff would change the target. This follows the complete-return example and continuing-task comparison in the MC/TD deck.
- **I03, Q3e.** Keep the successor-state hint. It asks for the same reasoning as B19 while leaving students to explain why averaging preserves the inequality. At a terminal successor both continuations are zero. The remaining continuation vanishes because values are bounded and the discount is 1/2. I independently obtain the first two replacements as (11/4, 7/2) and (23/8, 15/4), with limit (3, 4). The PI/VI comparison and six-point split are sound. Accept a verbal argument, and award the reasoning points independently of a mistaken action choice in (d) when the student correctly uses the supplied inequality.
- **X9 figure, question-only PDF p. 6.** I traced all five outcome arrows. Waiting loops to A for reward 1 and to B for reward 2. From A, go leads equally often to B for 0 and to terminal for 4. From B, exit leads to terminal for 3. This reproduces the previous model and the policy probabilities are given separately below it. One wording ambiguity remains in the introduction: “a random action” could describe how the policy chooses an action. Suggested replacement: “The black dot shows the possible outcomes after choosing go. Each arrow gives the probability and reward of its outcome.” The diagram itself needs no change.
- **Timing and render status.** I retain the prior independent estimate of about 75 minutes (roughly 70–85 for a prepared student, unpiloted). I03 unpacks an existing derivation and requires no additional calculation. The question PDF checked here is the X9 render (`d4fbfd089964…`). The editable source is already newer (`a746cf1b4caf…`). I01–I03 remain candidates for the instructor and renderer. Verify the question text and matching key together after the next render.

## Claude response to ChatGPT's November 5 review, and render — 2026-11-05

| Item | Response | Status |
| --- | --- | --- |
| I01 wording | Agree: "using its exact action values" states what is maximized. | Applied |
| I01 rubric | Agree: the strict gain needs a reason; a tie change or the non-decrease theorem alone does not give it. In the key as the default. Whether the theorem's name alone earns the point is the instructor's. | Applied; instructor to confirm |
| I02 wording | Agree: "the Monte Carlo prediction method we used in class" keeps the target implicit. | Applied |
| I02 rubric | Agree: a finite-cutoff explanation earns full credit. | Applied |
| I03 | Agree: hint kept; terminal-successor note, verbal arguments and independence from a wrong (d) added to the key. | Applied |
| X9 intro | Agree on the ambiguity of "random action". ChatGPT's replacement is used, except that $\mathcal{M}(s,a,r,s')$ is kept because the equation sheet uses it. | Applied |
| Figure, timing | Figure recheck noted. About 75 minutes stands, unpiloted. | Noted |

Render: source `3bca03635510…`, exam PDF `514bf735967f…`. Both PDFs are 14 pages with the same page breaks as before; grade
table 12 / 22 / 32 / 20 / 14 = 100. Text comparison with the X9 render shows only the instructor's edits (Q1b, Q1c, the
"sweep" gloss) and the X10 changes. The previous source is backed up in Claude's scratchpad. Applied for instructor review;
acceptance is recorded under X10 in the decisions file.

**Requested from ChatGPT:** recheck the changed question text and its key in this render (Q1d, Q1e, Q3 intro, Q3e) only.

Instructor, 2026-11-05: Q1d rubric set. Naming the policy improvement theorem without the strict-gain reason earns 0.5 of
the reason point; this replaces the key default above. X6 will be decided after seeing a few student answers. Key only:
source `c8bf949d539c…`, and the exam's extracted text is identical to the previous render.

## ChatGPT recheck of the X10 render and Q1d rubric — 2026-11-05

Checked the four items in Claude’s handoff against the current rendered questions (`db594b7353f8…`) and key (`020217247c85…`). Both PDFs have 14 pages.

| Item | Finding |
| --- | --- |
| Q1d, p. 3 | The prompt specifies exact action values and a gain in at least one state. The key correctly justifies True. A correct verdict plus the theorem’s name alone earns 1.5/2 under the instructor’s latest rule. A correct strict-gain explanation earns the full reason point. |
| Q1e, p. 3 | The wording identifies the method taught in class. The False key correctly distinguishes waiting for a completed return from cutting it off at a finite horizon, which changes the target. |
| Q3 introduction, p. 6 | The text identifies the black dot as the outcome branch after choosing go. Its two branches show B with reward 0 and terminal with reward 4, each with probability ½. The policy’s action probabilities appear separately below the figure. |
| Q3e, p. 9 | The successor-state hint matches the two-step argument. The key treats terminal continuation as zero, justifies the limit using bounded values and discount ½, and distinguishes PI from VI. The six rubric points add up and allow a correct verbal argument even after an error in (d). |

All four items match the accepted decisions. The targeted recheck is complete.

Claude, 2026-11-05: ChatGPT's recheck raised no findings and its PDF hashes match the current render. Exam marked final
in the decisions file (step 7); decision log updated. X6 stays open for grading.
