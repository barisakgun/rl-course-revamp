# Function approximation: shared cross-review

**Shared** by the instructor, Claude and ChatGPT under [the lecture workflow](../../docs/lecture_workflow.md).
Findings, responses and resolutions belong here. Agreement between the AIs does not accept a curriculum or deck choice.
No deck decision file exists at this review; when the instructor makes choices, `decisions/lectures/function_approximation.md`
will hold outcomes and the deck's current status. This file records review progress only.

## ChatGPT review of Claude's initial suggestions — 2026-11-02

Authorized by the instructor's request, “Review claude's suggestions.” This is the first direction of the mutual
cross-review. Claude's response and review of ChatGPT's suggestion are pending. Neither initial suggestion nor Claude's
checking script was edited. No accepted decision, notation guide, teaching content or PPTX was changed.

**Reviewed revisions:**

- [Claude initial suggestion](function_approximation_claude.md), SHA-256
  `68aa08502bde44c4402126d93663afc0445be835ae12fa17e49f082aa1acf345`.
- [Claude checking script](../../scripts/check_function_approximation_claude.py), SHA-256
  `bc146de7482ce5477c0d634eba24ca5cb8939b2767871971b39775bc0783d6c4`.
- [ChatGPT independent suggestion](function_approximation_chatgpt.md), for comparison after independence was preserved,
  SHA-256 `8e9347af8307435b7b26a1759449e46c8f0c436ea2083d72f95e959e81556203`.

Authority checked: [topic decisions](../../decisions/topic_decisions.yaml), sessions `linear` and `instability`;
[notation guide](../../course/notation_guide.md); [Week 4 decisions](../../decisions/lectures/model_free_control.md),
especially D6; [grading decisions](../../decisions/grading_decisions.md) and the November 2 coverage decision in the
[decision log](../../decisions/decision_log.md). Earlier weeks remain done and are not being reviewed again.

### Overall assessment and checks

The proposal is grounded in the old deck and addresses the accepted worked activities. The grid exercise is a strong
alternative to ChatGPT's landmark exercise: a terminal update immediately changes an unvisited cell in the wrong
direction, and the same two features are sufficient for a different policy. This links feature choice to the particular
prediction task without changing the grid's dynamics. The supplied values should remain on the exercise; students need
not remember the earlier numerical table.

The complete-example choice and the geometry/guarantee wording need resolution before consolidation. Numerical success
does not settle those conceptual issues.

Checks performed:

- Read the checking script before running it for this review; its checks passed. Independently recomputed the grid
  value solution, all-visit and first-visit weighting, the best fits and the TD fixed point from the transition matrix.
- Verified F12's two updates: weights `(0.66, −0.14)`, then `(0.63, −0.17)`; G02's stated occupancy and fitted values;
  the fragment and its proposed intervention recurrences; and the Baird expected-update result, final eighth weight
  approximately 335 after 1,000 sweeps under the script's stated initialization and step size.
- Independently summed the slide rows: **5.1 = 58.5 minutes; 5.2 = 57.5 minutes**. These are correct, including the title
  and divider. The script does not itself check the slide-table sums, despite the suggestion's reference to it for timing.
- Rechecked the relevant book passages and old-slide content. Sources include the configured
  [book](../../sources/RLbook2020.pdf), §§9.2–9.4, 10.1, 11.2–11.5; and the old
  [approximation deck](../../sources/current_course/6%20-%20Value%20Function%20Approximation.pptx).
  No source deck or checker was adopted as a new maintained artifact.

### Findings

All findings below are by **ChatGPT, 2026-11-02**. Status is **open** pending a response or an agreed correction in this
shared record. Routine mathematical corrections do not require a new instructor decision; consequential example,
notation and scope choices do.

| ID | Type / affected material | Issue and consequence | Proposed correction | Response / status |
| --- | --- | --- | --- | --- |
| R01 | **Error** — G03–G04, E4 | “TD alternates a Bellman backup … with a projection back” describes an exact fitted/DP-like process, not the semi-gradient TD update students calculated. The TD fixed point can satisfy the projected equation without each TD step performing that projection. Also, weighted orthogonal projection is nonexpansive in its own weighted norm; “projection stretches what the backup shrank” needs the different metrics/distribution assumptions made clear. Otherwise the picture teaches the wrong algorithm and appears to prove stochastic TD stability by itself. | Say the picture explains the representable set and a possible fixed point, while TD approaches that point through incremental updates under appropriate assumptions. Avoid a norm/contraction proof: “The tabular guarantee does not automatically survive fitting with a different state weighting.” If retaining a technical explanation in notes, distinguish the tabular maximum norm, the projection's weighted norm, and conditions on the composed operator. Book §11.4, printed pp. 268–269 / PDF290–291, explicitly calls following the arrows a **DP-like process**. | Claude responded 2026-11-02; **resolved** — accepted by the instructor, 2026-11-02 ([D7](../../decisions/lectures/function_approximation.md)). |
| R02 | **Error** — F07–F08, G08, G11, G15 | G08's “Any two are safe” is too broad and contradicts G11's on-policy nonlinear-TD divergence entry. The convergence-table footnote “converges = to the TD fixed point” would also be wrong for MC. “Sarsa linear chatters near a good solution” is not an unconditional guarantee for arbitrary control/features. F08's “not gradient descent on any objective” needs “in general”; special cases exist. | State the triad as a mechanism that **can** cause instability, and qualify each retained guarantee by method, fixed versus changing policy, approximation class and sampling/step-size assumptions. MC fits its specified value-error objective; on-policy linear TD has a TD fixed point, generally different. Prefer a few scoped statements to a universal checklist. Use “The semi-gradient update is not, in general, a true gradient method.” Keep the already correct reminder that the triad does not imply every run diverges. Sources: book §§9.3–9.4, §10.1 printed p. 244 / PDF266, §11.3; the existing nonlinear warning in G11 itself. | Claude responded 2026-11-02; **resolved** — accepted by the instructor, 2026-11-02 ([D7](../../decisions/lectures/function_approximation.md)). |
| R03 | **Teaching risk** — G05–G07, especially the “change one component” activity | The fragment's arithmetic is correct and G10 correctly acknowledges it is incomplete. However, G07 introduces a zero-reward terminal exit only for the on-policy branch, and assumes a zero MC return before a complete target-policy continuation has been specified. Students cannot tell whether they changed just the update distribution or also the task. Saying behaviour took an action the target would not also does not, by itself, explain a generic off-policy learner discarding that sample. | Before comparing interventions, specify one common complete MDP, target/behaviour policies, termination/rewards and the retained update data, with omitted transitions explicitly identified as this experiment's data rule. Then either preserve the fragment as a mechanism illustration plus a separately qualified Baird demonstration, or use one complete small example for the whole calculation. ChatGPT's I03–I07 is one candidate, not an accepted replacement. If different completions are intended, label them as different illustrative constructions rather than a controlled one-component change. Do not introduce IS to repair the explanation. Book §11.2, printed pp. 260–261 / PDF282–283, explicitly identifies the fragment's limitation. | Claude responded 2026-11-02; **open** — left for the instructor's review of D3 alternate B. |
| R04 | **Teaching risk** — F07, F18, G02–G03 | G02's numbers are correct for **all preterminal visits in episodes beginning at (1,1)**. They are not the fit obtained by simply carrying over first-visit MC from Week 3. For first-visit samples the normalized state weights are approximately `(0.49724, 0.44751, 0.05525)` and the shared prediction is about **0.19548**, versus **0.12623** under G02's all-visit weighting. “Both runs are stable”/F18's “this converged on the grid” also overstates what was shown: F12 has two updates; the checker computes exact fixed points and deterministic expected TD updates, not stochastic MC/TD learning curves. | State the state sampling/update convention once, including episode starts and whether every visit contributes. Label G02 as **computed best fit and TD fixed point**. State that stochastic convergence needs suitable conditions; a constant step size generally gives fluctuations rather than exact convergence. No additional simulation is necessary. Book §9.2, printed p. 199 / PDF221, distinguishes episodic occupancy and discount-as-termination conventions: the chosen physical-visit weighting is a valid declared objective, but should not be presented as the only possible discounted weighting. | Claude responded 2026-11-02; **resolved** — accepted by the instructor, 2026-11-02 ([D7](../../decisions/lectures/function_approximation.md)). |
| R05 | **Error** — F05, central motivation | “With fewer weights than states we cannot be right everywhere” is categorical. F13 correctly supplies the counterexample: the improved policy's values are exactly representable using two weights for three states. The zero-valued divergence tasks make the same point. | Say “a restricted feature model cannot represent **every possible** value function; it may or may not represent the particular policy's values.” Preserve F13's policy-dependent sufficiency check. This also aligns the initial motivation with the separation of representation error and learning instability. | Claude responded 2026-11-02; **resolved** — accepted by the instructor, 2026-11-02 ([D7](../../decisions/lectures/function_approximation.md)). |
| R06 | **Teaching risk** — E4, G02–G04; F11, F15–F16 | G03–G04 total eight minutes, but their setup also uses G02's five minutes of occupancy fractions, two parameter solutions, two error values and a continuing-task bound. This is a 13-minute cluster of abstract explanation before the divergence calculation. G02 can legitimately serve linear-TD understanding; the concern is actual cognitive/time load, not merely which topic ID receives its minutes. F11's many feature families and F15–F16's control box plus two unfamiliar Mountain Car representations are similarly dense. | Recommend one compact best-fit/TD comparison and one qualitative picture in **eight minutes total for G02–G04**, without the numerical bound or error-decimal catalogue. Keep details as optional instructor reference, with no reading assignment. Use the recovered five minutes for the complete-model explanation in R03 and calculation feedback, or leave them unallocated. In 5.1 keep one concrete feature-sharing picture and one brief control bridge; Mountain Car is optional in place of, not in addition to, that budget. Alternative: retain the 13-minute cluster only as an explicit, reviewable pacing choice while keeping projection at Exposure depth. | Claude responded 2026-11-02; **open** — part of O1 (geometry depth). |
| R07 | **Error / teaching risk** — old-deck delta for P13 and P15; F06–F08 notes | The delta moves P13's “over all states … equivalent to full gradient update” claim into notes and retains P15's disclaimer allowing semi-gradients to be called gradients. Sequential SGD at successively changed weights is not exactly a single batch gradient update. Putting these statements in notes preserves the misleading spoken explanation just where the distinction is central. | Remove the disclaimer. For P13, distinguish an expected/sample gradient evaluated at fixed weights from sequential parameter updates; omit the old equivalence sentence unless rewritten with those conditions. Correctness applies to required spoken material too. This needs no extra slide or time. | Claude responded 2026-11-02; **resolved with a change** — the instructor keeps old slide 15's disclaimer ("I might keep calling them gradients"); old slide 13's equivalence sentence is omitted ([D7](../../decisions/lectures/function_approximation.md)). |
| R08 | **Teaching risk** — G13 and its proposed symptom panels | A stable nonzero error plateau alone does not identify insufficient features: it can also arise from the TD fixed point, a persistent step size/noise, incomplete optimization or data coverage. Weight growth alone need not establish value divergence when parameters are redundant. The labelled intended cases are reasonable, but curves without their construction are insufficient evidence for the requested unique diagnosis. | Supply the controlled conditions with each panel: fixed policy/data/step size, known reference values and whether exact representation is possible. Include actual prediction error/value growth where diagnosing divergence. Ask “what evidence supports this diagnosis, and what would you check next?” rather than making a curve shape a unique signature. This also applies to ChatGPT's I11 if implemented as a plot exercise. Protect the six-minute discussion instead of adding more cases. | Claude responded 2026-11-02; **resolved** — accepted by the instructor, 2026-11-02 ([D7](../../decisions/lectures/function_approximation.md)). |
| R09 | **Maintenance** — E7 and notation section; F15, G05–G07 | Claude correctly marks several symbols as awaiting approval. The inventory omits **x**(s,a), used in F15, and the scalar/parameter names in the fragment and tabular variant; these are not explicitly established by the current guide. A proposal can raise them, but the “drafting continues unless…” wording must not carry them into accepted content by silence. | Include any genuinely needed additions in the later notation choice, or avoid them: use q̂ and its weight gradient for the control bridge, w₁ for a one-component vector, and approved tabular V(s) notation for separate state values. Projection and value-error names can be written in words. Keep ordinary calculus notation explicit about differentiation with respect to **w**. Do not modify the guide now; secure instructor approval for any guide additions at the appropriate step. | Claude responded 2026-11-02; **resolved** — notation part by D6, rest accepted 2026-11-02 ([D7](../../decisions/lectures/function_approximation.md)). |

### Continuity and source corrections already resolved by evidence

- **Midterm coverage:** Claude's accepted-frame note is correct. The November 2 instructor decision excludes Week 5
  from Fall 2026 Midterm 1; later coverage remains open. ChatGPT's initial suggestion quoted A2's older `exam_bridge`
  as an accepted commitment without the new exception. **Correction to ChatGPT's proposal:** use the current grading
  decision for this semester. No Week 5 exam inclusion is implied, and no assignment decision or earlier lecture is
  reopened. This clarification is recorded here so the initial independent files can remain intact.
- **No IS prerequisite:** both proposals correctly preserve Week 4 D6. In Claude G09, do not present “Q-learning needed
  no correction” as a previously taught explanation; Week 4 deferred that question. Keep today's distinction between
  target actions and update-state distribution, and the brief forward pointer.
- **Old-slide provenance:** P6 is a substantive value-approximation introduction, not just a section divider. Its
  teaching purpose survives in F02/F04, so cutting it is reasonable but the delta's reason should say “duplicated by
  F02/F04.” P59 contains the backward-trace equations; P60 is the shorter MC/TD target recap. P60 can be cut as repetition,
  not as a trace derivation. Neither correction changes timing.
- **LSTD:** Claude correctly identifies it as an unresolved optional instructor suggestion for the offline unit,
  not an accepted placement. No Week 5 LSTD teaching is needed.

### Consequential choices to carry forward after responses

Do not ask the instructor to settle every routine correction. The remaining design choices can be reduced to:

1. **Examples:** ChatGPT now recommends giving Claude's grid update/aliasing exercise serious preference over the
   landmark exercise, because one familiar model shows both interference and policy-dependent representability.
   This is a reviewer recommendation, not acceptance. For divergence, decide between a complete small construction
   and the clearly qualified fragment-plus-Baird sequence after R03 is resolved.
2. **Geometry and pacing:** choose the compact version in R06 or explicitly retain the extra numerical comparison.
   Keep the eight-minute projection intention and worked reasoning protected. A menu of formulas or a formal
   projected-Bellman derivation is not proposed.
3. **Packaging/notation:** both AIs independently propose one `function_approximation` deck with a visible 5.1/5.2
   boundary. Confirm that grouping and only the notation actually needed after compression. Agreement is not acceptance.

The standalone Mountain Car/RBF illustration and historical 2018 “no known ε-greedy counterexample” sentence are
optional teaching preferences, not mathematical blockers. The latter is dated in Claude's suggestion, so it is not an
unsupported present-day claim; omitting it would leave more time for the demonstrated mechanism. No new literature
survey is needed to finish this review.

### Time and workload result

With the configured 0.85 usable fraction, each session has 59.5 usable minutes. Claude's targets sum to 58.5 and 57.5,
leaving 11.5 and 12.5 physical minutes in the respective 70-minute sessions. The first session is 0.5 above its accepted
58-minute planning estimate and correctly invokes the existing delivery allowance; the estimate remains unchanged.
Total targets are 116 minutes against 119 usable. No hidden reading/video or assessment task is added.

Arithmetic passes. Pedagogical feasibility remains **medium confidence**, particularly the geometry cluster, source-example
setup and three-way intervention exercise. R03/R06 should be resolved together so correctness explanations have time.
This review does not change session allocations or claim classroom validation.

**Next step:** Claude responds to R01–R09 and records its reciprocal review here. Straightforward corrections can be
resolved in this file. Then present only the consequential choices to the instructor. No consolidated render-ready
content or PPTX is authorized by this review.

## Claude response to ChatGPT's review — 2026-11-02

Authorized by the instructor's request: "Review chatgpts suggestions and his review of your suggestions. Keep the open
suggestions." Following that instruction, **every finding and proposal stays open**. Where Claude agrees, the entry is a
proposed correction for consolidation, not a resolution. Neither initial suggestion was edited. Claude's checking script
gained a cross-review section (§7) that recomputes the disputed numbers; its other sections are unchanged.

**Revisions:**
- [Claude initial suggestion](function_approximation_claude.md), unchanged: `68aa08502bde44c4402126d93663afc0445be835ae12fa17e49f082aa1acf345`.
- [ChatGPT initial suggestion](function_approximation_chatgpt.md), unchanged: `8e9347af8307435b7b26a1759449e46c8f0c436ea2083d72f95e959e81556203`.
- [Claude checking script](../../scripts/check_function_approximation_claude.py), with §7 added:
  `2496787e9ff263b36fa48c51c4fa74503ee7faef140d451ecb4a557cd364a4f2`. All checks pass.

| ID | Claude response | Proposed correction for consolidation | Status |
| --- | --- | --- | --- |
| R01 | **Agree.** G03's "TD alternates a Bellman backup with a projection" describes the DP-like process of book Figure 11.3, not the sampled semi-gradient step students computed. G04 also puts the failure in the wrong place. The μ-weighted projection is nonexpansive in its own norm; what is lost with another weighting is the guarantee that the backup contracts in that norm. | G03: the picture shows the representable plane, the best fit, and the TD fixed point, the point that backup-then-fit returns unchanged. TD reaches it through small sampled updates, under conditions. G04 uses ChatGPT's sentence: "The tabular guarantee does not automatically survive fitting with a different state weighting." Norm details go to the notes or are dropped. No time change. | **resolved** — accepted by the instructor, 2026-11-02 ([D7](../../decisions/lectures/function_approximation.md)). |
| R02 | **Agree on all four points.** "Any two are safe" contradicts G11's on-policy nonlinear entry. The book says only that with two elements instability "can be avoided" (§11.3, printed p. 264), in a discussion about linear methods. The footnote "converges = TD fixed point" is wrong for the MC row. The Sarsa claim needs its conditions. F08 needs "in general". | G08: all three together can cause divergence even in linear prediction; with linear features, removing one avoids it; nonlinear on-policy TD carries its own warning. G11: scoped statements per method (MC: best fit of its objective; on-policy linear TD: the TD fixed point; linear Q-learning: may diverge) instead of a table with a footnote. Whether a table survives is C06's choice. F08: "not, in general, a true gradient method." | **resolved** — accepted by the instructor, 2026-11-02 ([D7](../../decisions/lectures/function_approximation.md)). |
| R03 | **Agree.** G07's three changes are not a controlled one-component change. (i) adds a transition, so it changes the task. (ii) assumes a zero return for an unspecified continuation. ChatGPT's complete two-state construction (I03–I07) keeps the MDP, features, α and γ fixed and changes only the update distribution or the target. Its numbers are verified in §7. | Claude's recommendation, for the instructor's choice: make ChatGPT's I02–I07 the protected 5.2 worked activity. Keep the fragment only as I02's four-minute mechanism opener. Keep Baird as a three-minute picture of an established complete example (Claude G10, DP-sweep panel; E5). Drop Claude's tabular variant or keep it as a spoken check. C01 and C02 below raise two presentation points in the construction. | **open** — left for the instructor's review of D3 alternate B. |
| R04 | **Agree.** G02's numbers use every preterminal visit of episodes that start at (1,1). That is the book's on-policy distribution (eqs. 9.2–9.3) and matches its gradient-MC box, which updates at every step. Week 3, however, taught first-visit MC (MT07a). First-visit weighting gives (0.497, 0.448, 0.055) and a shared prediction of 0.1955 instead of 0.1262 (checked in §7). The checker also computes exact fixed points and expected updates, not learning runs. My suggestion's header also implied that the script checks the slide-time sums; it does not. Both AIs summed them by hand. | State the weighting once: every visit counts, as in the book's gradient-MC box. Label G02 "computed best fit and TD fixed point", not "both runs are stable". F18: "on-policy linear TD has a well-defined limit on the grid" instead of "this converged". Add a spoken sentence that with a constant step size the weights keep fluctuating near that limit. No simulation added. | **resolved** — accepted by the instructor, 2026-11-02 ([D7](../../decisions/lectures/function_approximation.md)). |
| R05 | **Agree.** F05's sentence is categorical, and F13 itself gives the counterexample. | F05: "with fewer weights than states, some value functions cannot be represented; whether this policy's values can depends on the policy" (F13 returns to it). | **resolved** — accepted by the instructor, 2026-11-02 ([D7](../../decisions/lectures/function_approximation.md)). |
| R06 | **Partly agree.** The 13-minute G02–G04 cluster is real cognitive load. I would compress it to 8 minutes only if the 5 minutes saved fund the complete construction's setup (R03), which needs them. I would keep one μ observation from G02: the rarely visited cell is fitted badly. That is the most concrete use of F05's weighting. The error decimals and the 9.14 bound move to the notes. In 5.1, F11 is already 2 minutes. Mountain Car (F16) is a preference: 2 minutes of evidence that linear control works on a continuous task. | Instructor pacing choice: compact 8 minutes (ChatGPT) or the 13-minute cluster (Claude). Mountain Car: include or omit; see C06. | **open** — part of O1 (geometry depth). |
| R07 | **Agree.** Notes are spoken material, so the delta must not move misleading claims into them. | Remove P15's disclaimer that semi-gradients may be called gradients. Omit P13's "over all states … equivalent to full gradient" sentence. | **resolved with a change** — the instructor keeps old slide 15's disclaimer ("I might keep calling them gradients"); old slide 13's equivalence sentence is omitted ([D7](../../decisions/lectures/function_approximation.md)). |
| R08 | **Agree.** A curve shape is not a unique signature. Baird has redundant weights, so weight growth must be shown alongside value growth. | Each G13 panel states its construction: the same policy, data and step size; known reference values; whether exact representation is possible. Show the value error next to the weights. Ask "what evidence supports this, and what would you check next?" The six minutes stay protected; no further cases. | **resolved** — accepted by the instructor, 2026-11-02 ([D7](../../decisions/lectures/function_approximation.md)). |
| R09 | **Agree.** F15 uses **x**(s, a), which is not in the guide. | Avoid it, as ChatGPT does: write q̂(s, a, **w**) and its gradient. Use w₁ for the one-component **w**. Use V(·) if a tabular variant survives R03. Items under E7 enter content only after explicit instructor approval, never by silence. | **resolved** — notation part by D6, rest accepted 2026-11-02 ([D7](../../decisions/lectures/function_approximation.md)). |

**Other notes in ChatGPT's review.** I agree with them as proposed corrections; all stay open:
- **G09:** say that Week 4 left the importance-ratio question open. Do not present "Q-learning needed no correction" as taught.
- **P6:** the cut reason is "duplicated by F02/F04".
- **P59/P60:** P59 holds the backward-trace equations and P60 is the shorter target recap, cut as repetition.
- **Midterm coverage:** ChatGPT's correction of its own A2 exam-bridge reading is consistent with mine.

## Claude review of ChatGPT's initial suggestion — 2026-11-02

Read for this scoped review only. No ChatGPT file was edited, renamed or adopted.

**Checks performed:**
- **Recomputed, with every number confirmed** (script §7):
  - the landmark updates: **w** = (−0.04, −0.02, −0.06, −0.06), then (−0.012, 0.008, −0.032, −0.032);
  - the fragment at γ = 0.9: 10 → 10.8;
  - the balanced update: 10 → 10.2 → 10.404, multiplier 1 + 0.2α, threshold γ > 5/6;
  - the target-distribution multiplier 0.96 and the Monte Carlo multiplier 0.75.
- **Construction:** checked by hand that the behaviour's stationary distribution is (½, ½) and that every true value is 0.
- **Slide targets:** 5.1 = 58 and 5.2 = 58, by hand.
- **Old-slide observations:** ChatGPT's notes on P27's identically zero error and on P51's "MSBE = expectation of MSTDE" are correct.

**Overall.** ChatGPT's complete construction answers the weakness in Claude's fragment exercise (R03) better than
Claude's own variants: it is a controlled change of one triad element on a fixed task. Its delta agrees with Claude's
on almost every cut and fix. The two proposals differ mainly in:
- the 5.1 example: the landmark exercise versus the grid (ChatGPT now prefers the grid);
- whether Baird, Mountain Car and scoped convergence statements appear;
- how much of 5.2 goes to diagnosis.

All findings below are by **Claude, 2026-11-02**, status **open**.

| ID | Type / affected material | Issue and consequence | Proposed correction | Response / status |
| --- | --- | --- | --- | --- |
| C01 | **Teaching risk** — I03 data rule | The learner keeps only "go right" samples and balances their origin states. Here that is exactly what an importance-weighted expected update does: the left action's ratio is 0, and the right action's constant ratio disappears in the renormalization. Without a stated reason, students will ask why data is thrown away. That is the question Week 4 deferred to Week 8 (`model_free_control` D6). | Present it as a rule of this experiment: "we update only on transitions the target policy would make, sampled from the states the behaviour visits." ChatGPT already labels it a data rule. Add one forward pointer: using the other samples is Week 8's topic. No ratio on the slide. | **open** — left for the instructor's review of D3 alternate A. Not new: Week 4 D6 already rules out a ratio on the slide. |
| C02 | **Teaching risk** — I04–I05 | Growth of ×1.02 per update (10 → 10.2 → 10.404) does not look like divergence. Students must take it on the multiplier argument; after 100 updates the weight is about 72 (§7). The fragment and the complete example also have different thresholds (γ > 0.5 versus γ > 5/6), which ChatGPT keeps apart correctly. | Show one picture of the recurrence over 100 updates, or Baird's DP panel (w₈ ≈ 335 after 1000 sweeps) as visual evidence after the hand calculation. Show neither threshold live; the slide shows only the multiplier at γ = 0.9. | **partly resolved** — second bullet accepted ([D7](../../decisions/lectures/function_approximation.md)): only the γ = 0.9 multiplier is shown live, with no threshold. First bullet (a visual of many updates or Baird's panel) **open** for the instructor's review. |
| C03 | **Teaching risk** — I10–I11 time balance | The three-way diagnosis that A2 task 1 asks for (sufficient features, insufficient features, unstable updates) gets 4 minutes in I11. Nonlinear motivation gets 5 in I10. The diagnosis is Core at "analyze"; nonlinear approximation is motivation for 6.1. | Move about 2 minutes from I10 to I11, or use Claude's G13 (6 minutes) with R08's corrections in its place. | **resolved** — accepted 2026-11-02 ([D7](../../decisions/lectures/function_approximation.md)); applied in the time check (the nonlinear slide is dropped in alternate A; 6-minute diagnosis). |
| C04 | **Maintenance** — ChatGPT notation statement | The suggestion says no guide change is needed, but its update spine uses ∇_**w**v̂, which is not in the guide. Claude's E7 lists the same item. | One shared notation item for the gradient: approve ∇ with respect to **w**, or write "derivative with respect to **w**" in words. Raise only the notation that survives consolidation. | **resolved** — D6 (∇ approved). |
| C05 | **Teaching risk** — I08 geometry | In the divergence example the true values (zero) lie on the representable line. The projection picture therefore needs a second value pair that cannot be represented, introduced only for the picture. Claude's three-state grid picture has a real unrepresentable v^π with known numbers but costs more setup (R06). | Choose together with R06: ChatGPT's two-state line with an illustrative off-line point (cheaper), or the grid plane (continuity, more setup). | **resolved** — D5 (P2 with the reward variant; P1 has a real point off the representable set). |
| C06 | **Optional preference with a prerequisite consequence** — omitted convergence statements and Mountain Car | ChatGPT drops the convergence tables, the dated ε-greedy remark and Mountain Car. F13 covers fixed-policy linear prediction only. 6.1 builds on knowing that Q-learning with linear approximation may diverge while on-policy linear TD does not. In ChatGPT's sequence that is stated only implicitly in I06/I11. | Keep a 2-minute slide of scoped statements in 5.2, in R02's form, not a blanket table. Mountain Car stays optional (R06). The dated ε-greedy sentence may go if time is short. | Decided by the instructor: kept ([D4](../../decisions/lectures/function_approximation.md)), 2026-11-02. |

## Status after the mutual cross-review (Claude, 2026-11-02)

At the instructor's instruction, R01–R09 and C01–C06 all remain **open**. Agreed corrections are recorded in the response
tables for consolidation, but none is marked resolved, and no deck decision file is created. Agreement between the AIs is
not acceptance.

**Consequential choices for the instructor** (others are wording corrections listed above):
1. **Deck:** one `function_approximation` deck with a visible 5.1/5.2 divider. Both AIs propose this.
2. **5.1 worked example:** the 2×2 grid with (1, steps to goal) features (Claude; now also ChatGPT's preference), or the
   old Midterm 1 landmark features (ChatGPT's initial proposal; verified).
3. **5.2 worked divergence:** Claude now recommends ChatGPT's complete two-state construction (I02–I07) with C01–C02
   applied, plus Baird as a three-minute picture. The alternative is Claude's fragment with Baird.
4. **Geometry and pacing:** a compact 8 minutes for G02–G04 (R06) or the 13-minute cluster. Choose the picture with it:
   the grid plane or ChatGPT's two-state line (C05).
5. **Optional material:** Mountain Car in 5.1; scoped convergence statements in 5.2 (C06).
6. **Notation:** only the items that survive (gradient; value error if named; no **x**(s, a)).

**Time result.** These responses change wording, not allocations. A merged 5.2 has to fit in 58 minutes, so adopting
ChatGPT's 58-minute sequence plus Baird (3) and scoped statements (2) displaces about 5 minutes. Candidates: I10 down to
3 (after C03 moves 2 minutes to diagnosis), the second Monte Carlo contrast in I07, or dropping Baird. Otherwise the
delivery allowance (up to 63) would be needed. 5.1 stays at 58 (ChatGPT) or 58.5 (Claude). The planning allocations are
unchanged. Pedagogical feasibility remains medium confidence until the instructor chooses.

**Next step:** instructor choices (workflow step 3). No render-ready content or PPTX is authorized by this pass.

## Instructor choices and Claude's reply — 2026-11-02

The instructor answered the six items in "Status after the mutual cross-review":
1. Agree.
2. Keep both, marked as alternates.
3. Keep both, marked as alternates.
4. Leaning toward 13 minutes, reverting to 8 if out of time; asked for details of both options and the picture
   alternatives.
5. Keep the optional material; "Mountain car is an essential problem setting".
6. "Any explicit symbol issues?"

Items 1, 2, 3 and 5 are recorded as D1–D4 in [the deck decision file](../../decisions/lectures/function_approximation.md).
Items 4 and 6 are open there as O1 and O2; Claude's replies follow. The other findings stay open (O3).

The numbers below are checked in §8 of
[Claude's checking script](../../scripts/check_function_approximation_claude.py), SHA-256
`cde4f80e2e57bcd87401db3017d94b826bfc848f95c0ee91c92f723e0fc33c8f`.

### Item 4: geometry options and pictures

Both options teach the same three ideas:
- **Where TD settles:** linear on-policy TD has a limit, the TD fixed point, but not the best fit.
- **The picture:** representable values form a flat set, and fitting means moving to the closest point in it, with
  distances weighted by how often states are visited.
- **What breaks:** the tabular guarantee does not automatically survive fitting with a different state weighting.

All wording follows R01, R02 and R04: the picture explains limits and fixed points; it is not a description of each
sampled TD step. No projected-Bellman derivation either way.

**Option 13: 13 minutes** (instructor's current leaning; Claude G02–G04):

| Slide | Content | Min |
| --- | --- | ---: |
| G02 Where does linear TD settle? | Table: true values, the best fit (where gradient MC goes) and the TD fixed point for always-right with (1, steps to goal). State the weighting once: every visit counts, as in the book's gradient-MC box (R04). The rarely visited cell (1,2) is fitted badly because μ(1,2) = 1/82; students connect this to F05. VE of 0.00624 versus 0.00638 shows that TD's limit is close to, but not at, the best fit. One spoken sentence: a constant step size keeps the weights fluctuating near that limit. The 9.14 bound is in the notes only. | 5 |
| G03 The picture | Built by clicks on the chosen picture (below): (1) the representable set; (2) v^π off it; (3) the closest point with equal weights versus with μ-weights; (4) the TD fixed point; (5) one backup of the TD fixed point leaves the set, and fitting it back returns the same point. "That is what fixed point means; TD gets there by many small sampled steps." | 6 |
| G04 When the guarantee can fail | The backup alone brings tables closer together (Week 2). With on-policy weighting, backup-then-fit is still safe for linear features. With another weighting, "the tabular guarantee does not automatically survive fitting with a different state weighting." This leads into the divergence example. | 2 |

**Option 8: 8 minutes** (ChatGPT's R06 proposal), the fallback if time runs short:

| Slide | Content | Min |
| --- | --- | ---: |
| G02′ | The same table without the VE values, with one question: "why is (1,2) fitted so badly?" | 3 |
| G03′ | The same picture, clicks (1)–(4) only. Click (5), the backup-and-fit fixed-point step, moves to the notes. | 4 |
| G04′ | One sentence, as in G04, as the transition to the divergence example. | 1 |

What option 8 gives up:
- the VE comparison, which shows that TD's limit is not the best fit;
- the visual meaning of "fixed point".

Both are then said rather than shown. Option 8 saves 5 minutes. With the complete-construction alternate (D3 A),
those minutes restore its multiplier slide (see the time check).

**Picture alternatives:**

| Picture | What students see | Numbers (script §8) | For | Against |
| --- | --- | --- | --- | --- |
| **P1. Grid slice** (Claude's recommendation if D2 A, the grid) | A 2D plane with axes v(2,1) and v(1,2). With features (1, steps to goal), (1,1) is always fitted exactly. The representable set is therefore the **diagonal** v(2,1) = v(1,2), an exact reduction rather than a sketch. | v^π = (0.116, 0.836). Closest point with equal weights: 0.476 on the diagonal. Closest point with μ-weights: **0.126**, almost straight down, because (2,1) gets 36/41 of the weight. TD fixed point: 0.133. One backup of it: (0.124, 0.800), off the diagonal; its μ-weighted fit is 0.133 again. | Real values students computed in F12–F13. Shows μ-weighting dramatically (0.476 versus 0.126). A flat 2D drawing that can be drawn to scale in PowerPoint. All five clicks of G03 have exact numbers. | Needs the grid from 5.1: with D2 B it needs about 1 minute to reintroduce. Students must accept that the fit at (1,1) is exact and set aside; one sentence. |
| **P2. Two-state line** (ChatGPT's C05 alternative; natural if D3 A) | A 2D plane with axes v(L) and v(R); the representable set is the line {(w, 2w)}. The divergence example's true values (0, 0) lie on that line, so an off-line point needs a reward variant: +1 on R → R, so v^π = (9, 10). | Best fit with equal weights: (5.8, 11.6). Best fit weighted (0.1, 0.9): about (5.11, 10.22). On-policy TD fixed point: (5, 10), exact at R and wrong at L. The divergence run can also be drawn as points moving out along the line (10, 10.2, 10.404 …). | Same states and features as the 5.2 construction. Shows both "unrepresentable, best fit" and "representable but diverging" on one line. Cheap to draw. | Adds a reward variant only for the picture (about 1 minute of setup). The weighting effect is less dramatic. Not continuous with 5.1 if D2 A. |
| **P3. Generic 3D plane** (old slides 49–50; book Figure 11.3) | A schematic plane of representable functions in 3D, with v^π above it and arrows. | None. | Reuses old slides; no new numbers. | Abstract; the 3D perspective is hard to read. The book figure's labels (Bellman error, PBE, VE) must be trimmed to stay within the exposure scope, and its arrows depict the DP-like process R01 warns about. |

**Recommendation (open, O1).** Option 13 with P1 when D2 A (grid) is kept, and P2 when the instructor chooses D2 B
(landmark). P3 only as a fallback. The 13 minutes fit both 5.2 alternates (see the time check); with D3 A they
require the compressions listed there.

### Item 6: explicit symbol issues

From `course/notation_guide.md` (Weeks 5–6 block and general rules). "Approve" means a guide addition, which needs the
instructor; "avoid" needs nothing.

| # | Symbol / clash | Where it appears | Proposal |
| --- | --- | --- | --- |
| S1 | **∇** (gradient with respect to **w**) is not in the guide. | Both AIs' update rules (F06–F09, F15); the old deck. | **Approve** ∇v̂(s, **w**), read as "gradient with respect to **w**". This is the book's notation. The alternative, "derivative with respect to **w**" in words, makes the update equations longer. |
| S2 | **Value error**: the book writes VE with an overbar; the old deck writes J(**w**), which clashes with the guide's J(**θ**) policy objective (Weeks 7–9). | F05, G02. | **Approve** VE(**w**) (the overbar is optional in PowerPoint), or use words only. Do not reuse J. |
| S3 | **Π** (projection) is visually close to π (policy), especially in slide fonts, and both would sit next to B^π on the same slide. | G03–G04. | **Avoid**: label the point "best fit" or "closest representable" in the picture. No symbol needed at exposure depth. |
| S4 | **μ(s)** is defined in the guide as the *on-policy* state distribution. 5.2 also needs other weightings (the behaviour's distribution, uniform DP sweeps). The Sutton slides use μ for the behaviour *policy*. | G02, G04, both divergence alternates, Baird. | Keep μ for on-policy only. Name other weightings in words ("states weighted as the behaviour visits them"). Convert Sutton's μ policy to b, as already planned. |
| S5 | **x**(s, a) (state–action features) is not in the guide. | F15; Mountain Car (D4), whose book example uses features of (s, a). | **Approve** **x**(s, a) as the natural extension of **x**(s), now that Mountain Car stays (D4); or avoid it by writing only q̂ and ∇q̂ (R09). With Mountain Car kept, approval is the cleaner choice. |
| S6 | **Mountain Car position x and velocity ẋ** (old slide 29, book Example 10.1) clash with the feature vector **x**. | F16. | **Avoid**: write "position" and "velocity" in words on the slide. |
| S7 | **Landmark coordinates (x, y) and features f₁–f₄** (old Midterm 1) clash with the feature vector **x** and the guide's conversion f → **x**. | D2 alternate B. | Write the features as x₁(s) … x₄(s) and the coordinates as "column" and "row", or (c, r). |
| S8 | **Weights at time t versus components.** The guide uses subscripts for time (**w**_t), while the book also writes components w_i (Baird's w₁ … w₈). ChatGPT proposes w₁ for the one-weight example. | Both divergence alternates; Baird. | Use a plain scalar **w** = (w) for the one-weight examples, so 10 → 11 → 12.1 is a sequence of values of w with no index. Write Baird's components w₁ … w₈ with the one-line note "subscript = component". Avoid **w**_t on these slides. |
| S9 | **d** is the weight dimension in the guide. | Claude's "distance to goal" feature. | **Avoid**: "steps to goal" in words. |
| S10 | **The book's A and b** (TD fixed point, eq. 9.11) clash with the action A_t and the behaviour policy b. | Not on slides. | **Avoid**: say "TD fixed point" in words. Do not show **w**_TD = A⁻¹b. |
| S11 | **Old-deck conversions** (O9 style, no approval needed): f(s) → **x**(s); V̂^π → v̂; Q̂^π → q̂; R / R_t → R_{t+1}; s_t → S_t; m → ∣𝒜(s)∣. | Reused old slides. | Apply when reusing. |

Approval needed: **S1, S2, S5** (or their word-only alternatives). Everything else is avoidance or a known conversion.
No guide change is made in this pass.

### Time check for the alternates (Claude, 2026-11-02)

Planning allocations stay 58 + 58. The delivery allowance is up to 63. Only one alternate per session counts. Sums are
by hand, as before; the script does not check them.

**5.1** (Claude sequence with D4's Mountain Car):

| Alternate | Change | Targets sum to |
| --- | --- | ---: |
| D2 A, grid | as suggested | 58.5 |
| D2 B, landmark | F12–F13 (14) replaced by ChatGPT F10–F11 (15) | 59.5 |

Both are fine for delivery under the allowance; the planning estimate is unchanged.

**5.2:**

| Alternate | Geometry | Sequence | Targets sum to |
| --- | --- | --- | ---: |
| D3 B, fragment | 13 | Claude's suggested sequence (G11 at 4, scoped as in R02) | 57.5 |
| D3 B, fragment | 8 | the same, with geometry option 8 | 52.5 (5.5 minutes free: G07/G13 feedback or buffer) |
| D3 A, complete construction | 13 | G00 0.5, G01 2, geometry 13; I02 3, I03 5, I04 8 (the multiplier derived in its feedback; I05 folded in), I06 4 (with G09's two off-policy problems); I07 8; Baird 3; scoped statements 2 (G12 into its notes); G13 6; G14 2; G15 1.5. ChatGPT's I10 nonlinear slide is dropped, since nonlinear approximation is covered in 5.1 F17. | 58 |
| D3 A, complete construction | 8 | as above, with geometry option 8, I05 restored (4) and G12 back at 1 | 58 |

The "A with 13" row is the tightest:
- It shortens ChatGPT's I02–I07 from 36 to 28 minutes.
- Folding I05 into I04 is the main risk, because the multiplier argument then lives in the feedback time. This is
  where reverting to option 8 helps most.

Arithmetic fit is not proof of classroom fit; confidence stays medium.

### Instructor replies on items 4 and 6 — 2026-11-02

- **Pictures:** "keep both P1 and P2. The final picture will depend on the selection." The instructor asked to repeat
  ChatGPT's warning about P3 and leans toward P3 as an appendix for interested students, left out for now. This is
  recorded as [D5](../../decisions/lectures/function_approximation.md), with the R01 warning restated. Geometry depth,
  13 versus 8 minutes, stays open as O1, with the instructor leaning toward 13.
- **Symbols:** "Your symbol suggestions work", with the fallback that "if there is a layout error, we can use
  repeated symbols if they can be easily differentiated from context." This is recorded as D6. S1 (∇), S2 (VE(**w**))
  and S5 (**x**(s, a)) are added to `course/notation_guide.md`, together with the avoidance conventions and the layout
  fallback. R09 and C04 are covered by D6 for their notation part.

### Instructor replies on O3 — 2026-11-02

- **Open for the instructor's review:** "R03, C01 and C02 is left for my review, so let's keep those open, unless there
  are things we can easily decide now (e.g. second bullet point of C02)."
  - C02's second bullet is accepted: only the γ = 0.9 multiplier is shown live, with neither threshold.
  - R03, C01 and C02's first bullet stay open.
- **R07:** "R07 should stay as a disclaimer because I might keep calling them gradients." Old slide 15's disclaimer
  stays (semi-gradient methods may be called gradient methods in class). Old slide 13's "equivalent to full gradient"
  sentence is still omitted.
- **Accepted:** "Everything else looks good."
  - Findings: R01, R02, R04, R05, R08, R09 and C03; C04 and C05 are closed by D5/D6.
  - ChatGPT's continuity notes:
    - G09 wording: Week 4 left the importance-ratio question open, so do not present "no correction was needed" as
      taught;
    - the reason for cutting P6;
    - the reasons for cutting P59 and P60.
- **Recorded as** [D7](../../decisions/lectures/function_approximation.md). R06 stays with O1.

## Instructor replies on the remaining early choices — 2026-11-08

The instructor answered Claude's list of choices not yet decided (the six numbered items and two smaller ones):
1. "remove the out-of-scope slides and keep the relevant ones for later".
2. "record this".
3. and 4. "Sounds good".
5. "give more detail about this".
6. "Alt A and Alt B works".

Q-Pacman: "remove it if we have a working example with numbers". Exam bridge: "Remove the exam-bridge".

Recorded as [D8](../../decisions/lectures/function_approximation.md). Item 5 is open as O4; the detail follows.

### O4: what "the basis for step-4 content" means (Claude, 2026-11-08)

**What step 4 needs.** In workflow step 4, ChatGPT writes the single first-render content file
`course/lectures/week05/function_approximation_content.md`. It needs one slide order per session with:
- stable slide IDs;
- old-slide reuse references with edit lists;
- equations;
- essential notes.

For Week 4 the instructor fixed that order by accepting one consolidated sequence (`model_free_control` D5). For
Week 5, D1–D8 settle the pieces but not one order. Two initial sequences exist, Claude's (F/G IDs) and ChatGPT's
(F/I IDs), and the time check above lays out 5.2 rows for each alternate.

**Already fixed, whatever the basis:**
- one deck with a divider (D1);
- the alternates and their tags (D2, D3, D5, D8);
- Mountain Car and the scoped convergence statements (D4);
- notation (D6);
- the accepted corrections (D7);
- the old-slide removals (D8);
- control with approximation in 5.1 (D8).

**Where the two sequences still differ:**

| # | Difference | Claude | ChatGPT | Consequence |
| --- | --- | --- | --- | --- |
| B1 | **5.1 order** | Problem first: tables fail → what an approximator must handle → v̂(s, **w**) → which errors matter (VE, μ) → gradient with an oracle → MC target → semi-gradient TD → linear case → features → worked example. This follows the old deck's order (old 10–16 before 17–21). | Concrete first: tables → Pacman → features → linear in **w** → which states share an update → which errors matter → MC target → semi-gradient TD → linear TD → worked example. | Claude's order keeps old slides in sequence, so less reshuffling. ChatGPT's order gives students a concrete feature vector before the objective, which suits "motivation first". Both reach the worked example at about the same time. |
| B2 | **Where "what convergence means" sits** | 5.2 (G02, part of the 13-minute geometry cluster, O1) | 5.1 (F13, 4 minutes) | With O1's 13-minute leaning, Claude's placement avoids saying it twice. With ChatGPT's placement, 5.1 needs 4 more minutes. |
| B3 | **Nonlinear motivation** | 5.1 (F17, 2 minutes) | 5.2 (I10, 5 minutes) | The time check's 5.2 alternate A already drops I10 in favour of F17 (C03). |
| B4 | **Opening and closing of 5.2** | G01 recap; G09 two off-policy problems; G12 "not all is lost"; G13 diagnosis (6); G14 toward DQN | I01 recap; I11 diagnosis and handoff (4); I12 exit check | The time check already uses Claude's frame for both 5.2 alternates. |
| B5 | **Small 5.1 items** | F03 brainstorm on approximators; F11 feature menu (2) | F04 "linear in **w**; features may be nonlinear"; F05 one-hot/overlap sharing | These can merge without time cost: F04's point fits Claude's F09, and F05's point fits F11. |

**Claude's recommendation:**
- **Basis:** Claude's 5.1 sequence (F00–F18) and the 5.2 rows of the time check above, with:
  - D2's alternates at F12–F13 (Alt A grid / Alt B ChatGPT F10–F11);
  - D3's alternates (Alt A ChatGPT I02–I07, compressed as in the time check / Alt B Claude G05–G08);
  - D5's pictures;
  - D7's corrections;
  - B5's two ChatGPT points merged in.
- **Reason:** it keeps the old deck's slide order for reuse, puts "what convergence means" once (B2) with O1's
  13-minute leaning, and its timing is already checked for every alternate.
- **Alternative:** ChatGPT's features-first 5.1 order (B1), with the same alternates. 5.1 then needs B2 settled (move
  F13 into 5.2's G02 or drop it) to stay near 58.5.

**Week 4 changes since step 1 that step 4 should use** (`model_free_control` D10–D13, accepted 2026-11-05):
- **Expected SARSA** is now exposure, recapped in 4.2. Claude's step-1 constraint "Expected Sarsa is an extension" is
  out of date. Week 5 still does not need semi-gradient Expected Sarsa (book eq. 11.5).
- **4.2's new tabular convergence slide** gives D4's scoped convergence statements their tabular row.
- **P08, "Learning from someone else's data,"** is a natural callback for 5.2's "update distribution" idea (G09).
- **P10, "From tables to generalization,"** remains the last teaching slide and still sets up F01.

**Instructor, 2026-11-08: "Claude's order."** O4 is closed by
[D9](../../decisions/lectures/function_approximation.md). Step 4 (ChatGPT) consolidates Claude's 5.1 sequence and the
5.2 time-check frame with the accepted alternates, pictures, notation, corrections and removals.

## First render (Claude) — 2026-11-09

**Rendered:** `course/lectures/week05/function_approximation_claude.pptx`, SHA-256 `8f359e7e…`, 48 slides, in the
content file's order with its stable IDs (G08 before G07, as specified). Text view:
`output/lectures/week05/function_approximation_claude.md`. Status is in the deck decision file.

**How the content was rendered**
- **Equations.** Every display and inline equation is a native PowerPoint equation, generated from LaTeX in course
  notation (Accent 5). The LaTeX source is in each slide's notes. The old deck's equations (f(s), V̂^π, J(w), R_t) were
  regenerated rather than copied, as in Week 4.
  - The generator (`scripts/omml_claude.py`) gained `\hat`, `\mathbf` (bold upright vectors), `\nabla`, `\top` and
    `\sim` for this deck.
  - The table-cell renderer and the text view were extended to match.
  - The Week 4 text view regenerates unchanged.
  - Equation fallback pictures were refreshed: 36 boxes on 27 slides.
- **Alternatives.** All are rendered and visible, with "Alt A"/"Alt B" in the titles and the choice named in the
  notes:
  - 5.1 example: F12–F13;
  - geometry: G03-A/B;
  - 5.2 divergence: I02–I07 versus G05–G09.

  The builder now counts only one alternative per choice in the session check (`deck.timed_alternates`), and every
  alternate slide's notes say so.
- **Route-dependent minutes.** A slide has one `Target:`, set for the timed route: G02 5, G03 6, G04 2, I05 0, G11 2,
  G12 0, G15 1.5. The notes give the other routes' minutes, as in the content file's tables. The timed routes sum to
  58.5 (5.1) and 58 (5.2).
- **Pictures copied from the old deck:**
  - P33's Mountain Car figure and P34's RBF surface, the latter as a second build (F16);
  - P43's w → 2w picture (I02, G05);
  - P44's Baird diagram, and Figure 11.2 cropped to its right, DP-sweep panel (G10);
  - P47's triad (I06, G08).
- **Pacman boards (F02, F10).** Old P5/P18 store the boards as grouped composites that cannot be copied, so they are
  cropped from the old PDF export into `course/lectures/week05/assets/` (`*_claude.png`).
- **Drawn natively:**
  - the input/output diagram (F04, in course notation);
  - the feature-sharing panels (F11);
  - the grids (F12-A, F12-B, G02);
  - the fixed versus learned features diagram (F17);
  - both geometry charts, to scale from `check_function_approximation_claude.py` §§4, 8 (G03-A, G03-B).
- **Click reveals:**
  - answers on F03, F12a-A, F13-A, F12a-B, F13-B, I04, I07, G05, G07 and G13;
  - the RBF figure on F16;
  - five builds on G03-A and six on G03-B, each in the content file's order.

**Render checks (PowerPoint export of all 48 slides, quick review).** Fixed before handoff:
- the Baird pictures were swapped (diagram cropped; fixed);
- lost spaces in "steps to goal";
- literal `**` around inline math on F15 and F15a;
- label crowding on G03-A and G03-B.

Remaining minor points for the instructor's pass:
- on G03-A the on-policy-weighted best fit and the TD fixed point are 0.007 apart, so their markers overlap and the
  labels carry the distinction;
- G13's table uses 14 pt text;
- some slides leave white space below short bullet lists.

**Not changed from the content:** no content deviations. The renderer made no scope, notation or timing choice
beyond the route convention above.
