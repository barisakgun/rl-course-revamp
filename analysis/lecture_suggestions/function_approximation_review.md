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
| R03 | **Teaching risk** — G05–G07, especially the “change one component” activity | The fragment's arithmetic is correct and G10 correctly acknowledges it is incomplete. However, G07 introduces a zero-reward terminal exit only for the on-policy branch, and assumes a zero MC return before a complete target-policy continuation has been specified. Students cannot tell whether they changed just the update distribution or also the task. Saying behaviour took an action the target would not also does not, by itself, explain a generic off-policy learner discarding that sample. | Before comparing interventions, specify one common complete MDP, target/behaviour policies, termination/rewards and the retained update data, with omitted transitions explicitly identified as this experiment's data rule. Then either preserve the fragment as a mechanism illustration plus a separately qualified Baird demonstration, or use one complete small example for the whole calculation. ChatGPT's I03–I07 is one candidate, not an accepted replacement. If different completions are intended, label them as different illustrative constructions rather than a controlled one-component change. Do not introduce IS to repair the explanation. Book §11.2, printed pp. 260–261 / PDF282–283, explicitly identifies the fragment's limitation. | resolved — lapsed: fragment slides hidden as alternatives (D14) |
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
| R03 | **Agree.** G07's three changes are not a controlled one-component change. (i) adds a transition, so it changes the task. (ii) assumes a zero return for an unspecified continuation. ChatGPT's complete two-state construction (I03–I07) keeps the MDP, features, α and γ fixed and changes only the update distribution or the target. Its numbers are verified in §7. | Claude's recommendation, for the instructor's choice: make ChatGPT's I02–I07 the protected 5.2 worked activity. Keep the fragment only as I02's four-minute mechanism opener. Keep Baird as a three-minute picture of an established complete example (Claude G10, DP-sweep panel; E5). Drop Claude's tabular variant or keep it as a spoken check. C01 and C02 below raise two presentation points in the construction. | resolved — lapsed: fragment slides hidden as alternatives (D14) |
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
| C01 | **Teaching risk** — I03 data rule | The learner keeps only "go right" samples and balances their origin states. Here that is exactly what an importance-weighted expected update does: the left action's ratio is 0, and the right action's constant ratio disappears in the renormalization. Without a stated reason, students will ask why data is thrown away. That is the question Week 4 deferred to Week 8 (`model_free_control` D6). | Present it as a rule of this experiment: "we update only on transitions the target policy would make, sampled from the states the behaviour visits." ChatGPT already labels it a data rule. Add one forward pointer: using the other samples is Week 8's topic. No ratio on the slide. | resolved — closed by instructor 2026-11-15: covered by I03's rule wording and Week 8 notes pointer |
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

## First-render correctness check (ChatGPT) — 2026-11-09

**Version examined:** `course/lectures/week05/function_approximation_claude.pptx`, SHA-256
`8f359e7e20f753af406c9466cbb79bb90b202aeb82291271930f3388b37606aa`, 48 slides. The generated text view has the same
fingerprint. This is the single correctness-focused pre-instructor pass in workflow step 5, not final acceptance.
Current deck status remains in the [deck decisions](../../decisions/lectures/function_approximation.md).

**Result:** no blocking mathematical, factual or rendering error found. No deck changes requested before the
instructor's first review. The PPTX, frozen first-render inputs and generated text view were not changed.

**Evidence checked:**
- Read all slide text and speaker notes against D1–D9, the shared content and the notation guide. The 5.1/5.2 boundary
  is at slide 26 (G00); both example alternatives and both geometry pictures remain visible. Expected SARSA is a
  continuity note, not an added approximate algorithm. No excluded average-reward, gradient-TD or least-squares
  block was restored.
- Independently recomputed the grid's true values, weighted best fit and TD fixed point, their value errors, the
  landmark updates, and the complete-example and fragment interventions. The grid geometry correctly treats the
  start-state coordinate separately rather than claiming it is always exact. The two-state geometry explicitly
  distinguishes its different weighting objectives and resets rewards before divergence.
- Checked the Baird DP-sweep interpretation and independently reproduced the stated growth: after 1,000 mean sweeps,
  w₇ ≈ 6.85003, w₈ ≈ 335.00121 and the lower-state prediction ≈ 676.85245. Its zero true value is representable;
  the selected right-hand panel supports the claimed deterministic expected-update failure.
- Exported a byte-identical temporary copy through Microsoft PowerPoint to a 48-page PDF. Inspected all pages in
  contact sheets and enlarged the equations, algorithms, geometry charts, Baird panel and diagnostic table. No
  clipped essential text, missing equation symbol or misleading figure crop was found. Temporary review material
  stays outside the repository; this does not replace Claude's generated views or the final render check.
- Inspected the PPTX animation definitions: every referenced shape exists, the geometry charts have their five/six
  click groups, and exercise answer reveals target the expected tables/answer blocks. This verifies definitions,
  **not live slideshow playback**; the instructor still checks click behavior while reviewing.
- Confirmed 48 unique stable slide IDs, no hidden slides, and note targets of 58.5/59.5 minutes for the two 5.1
  routes and 58 for 5.2 Alt A/full geometry. Other route timings remain as documented. The session-source index is
  current. The source PPTX's fingerprint remained unchanged after inspection.

**Minor presentation observation, already noted by Claude:** slide 46 (G13) has a dense 14-point table. It is readable
in the enlarged export, but classroom readability is weaker than the surrounding slides. If it is too small on the
teaching display, shorten the repeated setup wording or split the table across a continuation while retaining the
same six-minute activity. This is a presentation preference for the instructor's pass, not a new content decision
or a reason for another pre-review polishing round. The nearby points on slide 29 (G03-A) are accurately located;
the leader labels and preceding numeric table distinguish them, so their proximity is not a numerical error.

**Still open:** O1 (geometry depth) and O3 (R03/C01/C02's visual item) remain instructor choices. This check confirms
that the caveats and alternative constructions are rendered; it does not resolve those choices or accept the deck.

## Instructor editing round 1 — Claude content and error check (2026-11-10)

**Saved instructor version reviewed:** `ddb48789…` (saved 2026-11-10 14:12), compared with the first render
`8f359e7e…`. Backed up in `output/deck_backups/`. The text view is regenerated from this version.

**Instructor changes:**
- **5.1 example decided by edit:** the grid slides (14–16) are kept, with "Alt A" removed from their titles. The three
  landmark slides are moved to the end as hidden slides 46–48. The title of slide 46 says "The next 3 are
  alternatives to 14-16". Recorded as D10.
- **F02:** four questions added: Pacman state-space size, a humanoid robot, and whether boards 1–2 and boards 2–3
  are similar. Old P5's boards are now copied natively (groups), replacing the cropped image. Caption added:
  "Storage – Exploration – Generalization".
- **F03:** retitled "Learning with state descriptions (aka state features)". It now has the approximation
  equations, "Ideal Requirements" (with "A compact representation: |w| ≪ |S|"), and old P4's closing quote.
- **F04:** "Side Question: What are some potential models?"
- **F05:** VE is written as an expectation and as a sum, with μ_π(s). A trailing line "How to learn".
- **Smaller edits:**
  - F08: "(Bootstrapping)";
  - F09: "x(s): Features";
  - F15: "the state-action features".
- **Animations:** click animations on F01, F02 and F04–F10. Every animation target exists, and no slide has more than
  one timing block.
- **Unchanged:** no speaker notes were edited. Equations re-saved by PowerPoint now store the bold w as 𝐰 and the
  minus as −; this is not a content change.

**Findings (Claude, 2026-11-10).** Status open unless noted.

| ID | Type / slide | Issue and consequence | Proposed fix | Status |
| --- | --- | --- | --- | --- |
| R10 | **Error / notation** — F03 | "A compact representation: \|w\| ≪ \|S\|" compares a weight vector with the number of states. \|w\| also reads as a norm. The guide's dimension symbol is d, and the state set is 𝒮. | "A compact representation: $d\ll\|\mathcal{S}\|$ (number of weights ≪ number of states)". | resolved — applied (D11) |
| R11 | **Error** — F05 | $\mathbb{E}_\pi[(v^\pi(s)-\hat v(s,\mathbf w))^2]$ uses the value s inside the expectation, so it reads as the expectation of a constant. The sum form is correct. | $\mathbb{E}_\pi[(v^\pi(S)-\hat v(S,\mathbf w))^2]$ with $S\sim\mu$ said aloud, or keep only the sum. | resolved — applied (D11) |
| R12 | **Notation** — F05 | μ_π(s): the guide defines μ(s) as the on-policy state distribution, and marks the policy with a superscript (v^π). Subscripts are kept for time, sweep and parameter indices (guide, 2026-10-11). | μ(s) as in the guide, or approve μ^π(s) as a guide addition. | resolved — notation guide μ^π(s); F05 applied with the superscript (D11) |
| R13 | **Teaching risk** — F05 | "How to learn" sits alone below the question and reads like an unfinished line. | The notes now treat it as the lead-in to F06. Optionally reword it as "How do we learn **w** when $v^\pi$ is unknown?" | resolved — notes guide toward gradient descent; slide text unchanged (D11) |
| R14 | **Optional preference** — F04 | F03 now shows the same two approximation equations, so F04's display repeats them. | Drop F04's equation line, or keep it as a deliberate recap; the notes say to point to the diagram. | resolved — kept by instructor (D11) |
| R15 | **Timing** — F02–F04 | F02 now has four questions, F03 more content and F04 a side question, but the targets are still 3/3/2. A realistic estimate is 1–2 extra minutes, which would make 5.1 about 60 minutes. That is within the 63-minute delivery allowance; the planning estimate is unchanged. | Raise F02 to 4 (and F03 to 4 if the brainstorm stays), or keep the targets and treat the questions as quick. | resolved — F02 4, F03 3.5; 5.1 targets 60 (D11) |

**Notes updates (Claude, prepared 2026-11-10; applied only once the deck is closed in PowerPoint):**
- **F02:** answers for the four questions. The state-space size is given as arithmetic only: food alone gives 2^n
  configurations. The board comparisons and the meaning of "Storage – Exploration – Generalization" are added.
- **F03:** the new title, the brainstorm and reveal, a gloss for each requirement with pointers to later slides, and
  the quote's source.
- **F04:** the side-question answer (old P8's model list) and "equations repeat F03".
- **F05:** the expectation/sum reading, and "How to learn" as the F06 lead-in.
- **F08, F09:** a line on "(Bootstrapping)" and on "x(s): Features".
- **Grid and landmark slides:**
  - F12-A–F13-A are the taught route, and their timing tags are updated;
  - 46–48 are hidden alternatives, not counted;
  - the slide IDs F12-B, F12a-B and F13-B lost in the move are restored;
  - F14's and G02's references to "whichever example" now say the grid.
- **Equation-source lines** on F03 and F05 now match the edited slides.

**Not checked this round:** a fresh PowerPoint render. PowerPoint had the deck open and timed out, so a LibreOffice
preview was used. LibreOffice cannot play the new click animations; their definitions were checked instead.

**Notes updates applied (Claude, 2026-11-10)** after the deck was closed:
- **Deck:** `3cb8de52…`, the instructor's saved version `ddb48789…` plus the notes changes listed above and the
  restored IDs F12-B, F12a-B and F13-B (backup in `output/deck_backups/`). Slide content is unchanged.
- **Views:** the text view is regenerated.
- **Check:** a PowerPoint export opens and exports all 45 visible slides.

R10–R15 stay open for the instructor.

**Instructor replies on R10–R15 (2026-11-10), recorded as D11 and applied by Claude:**
- **F03:** "d ≪ |𝒮| (number of weights ≪ number of states)".
- **F05:** the expectation uses S. The bullet reads μ^π(s), with the notation guide updated (superscript policy mark;
  μ(s) when π is fixed).
- **Notes:** F05 says "How to learn" leads to gradient descent.
- **Timing:** F02 4 minutes, F03 3.5.

Deck `b99cacc8…`, after a backup. Equation fallbacks are refreshed (37 boxes), and F02–F05 were checked in a fresh
PowerPoint export of all 45 visible slides. The text view is regenerated.

## Instructor requests during editing round 2 (2026-11-12)

- **No hedging or disclaimers on slides.** The instructor found too much hedging on slides and important information
  missing from the notes. Examples: slide 26's caption that the geometry figure is not a TD update, and slide 28's
  "mechanism fragment, not yet a complete process". The instructor has edited both. This is now a shared rule in
  `AGENTS.md` (Shared lecture-content conventions), which binds both AIs: slide text states what is taught, and
  every caveat, condition and "this is not…" statement goes in the speaker notes. The instructor moves a warning
  onto a slide if needed. **Both AIs: do not add such statements to slides, and do not put back ones the instructor
  removed.**
- **Convergence comparison slides** (instructor: MC versus semi-gradient TD, for tabular, linear and nonlinear
  approximation, for prediction and control; guided by old P55–56; after the "possible failure" slide). Claude
  prepared G12a (prediction) and G12b (control) in `course/lectures/week05/function_approximation_convergence_claude.yaml`.
  - **Slide text:** results only, with ✓ / (✓) / ✗ and what each converges to. All conditions are in the notes.
  - **Dropped rows:** gradient TD and gradient Q-learning (out of scope); off-policy MC (needs Week 8's
    corrections). The "other state weighting" row covers 5.2's examples.
  - **Timing:** 2 minutes each. 5.2's timed route goes from 58 to 62, within the 63-minute delivery allowance.
    G11's bullets now overlap G12a, so the instructor may shorten G11.
  - **Insertion:** after G12 once the deck is closed in PowerPoint; it was open when the slides were prepared.
- **Projection and Bellman operations:** Claude's comparison of other courses was reported to the instructor in the
  session only, at the instructor's request. No file change.

**Applied (Claude, 2026-11-12), after the instructor closed the deck:**
- **Insertion:** G12a/G12b inserted after G12 in the instructor's round-2 save `36af4cc8…` (backup taken). Deck is now
  `8a6042b4…`, 50 slides. A fresh PowerPoint export of all 45 visible slides shows both tables laid out correctly.
- **Slide ID:** the ID G03-B, lost when the instructor moved and hid the slide, is restored.
- **Records:** decision file D12–D13. The projection/Bellman comparison is recorded under "Consider for next
  semester" in the deck decision file.
- **Not done:** Claude has not yet checked round 2's other edits; that waits until the instructor finishes the round.

## Instructor editing round 2 — Claude content and error check (2026-11-12)

**Saved instructor version reviewed:** `13e58d03…`, backed up in `output/deck_backups/`. Compared with `b99cacc8…`
(end of round 1) and `8a6042b4…` (after the G12a/G12b insertion). The text view is regenerated. Preview: LibreOffice
only; the deck was open in PowerPoint and the export timed out.

**Instructor changes:**
- **5.2 divergence decided by edit:**
  - "Alt A" removed from the titles of I02–I07;
  - the fragment slides (G05, G06, G08, G07) moved to the end as hidden slides 47–50. Slide 47's title says
    "28-32 (33)", i.e. they are alternatives to slides 28–32 (and 33). Their slide IDs were lost in the move.
  - Recorded as D14.
- **I07 ("Change one component, keep the task") is hidden.** G09 ("Two off-policy questions") now sits in the
  taught route after I06.
- **I06:** "Function approximation/Feature Based Representation"; the two data questions are replaced by G08's
  "Which part would you change to investigate the growth mechanism?", and a "Deadly Triad" label is added.
- **G10:** the cropped right-hand panel is replaced by the full book Figure 11.2, including the left
  "Semi-gradient Off-policy TD" panel.
  - New text: "R = 0, γ = 0.99. Target policy follows the solid lines. Behavior policy is random switching to any
    other state including self."
  - The component-subscript and lower-state lines are removed from the slide; the notes already have them.
- **G00 (5.2 divider) hidden.**
- **G01:** retitled "Convergence: …". The update is now in the general ∇v̂ form, and two questions were added
  ("Would this effect stability?") plus "(Converge but to the wrong values vs diverge)".
- **G02:** definitions of "Best fit for VE" and "TD fixed point" added.
- **G03-A:** caption shortened to "Exact backup-and-fit picture of a fixed point."
- **I02:** "Part of an MDP" replaces the fragment disclaimer.
- **I04:** γ and α are shown.
- **F18 and G15:** "Exit question/check" became "Question".
- **Unchanged:** no speaker notes were edited. Animations are valid: every target exists, and no slide has more than
  one timing block.

**Timing (taught route, visible slides):**
- 5.1 = 60 minutes.
- 5.2 = 55.5 minutes: I07's 8 minutes and G00's 0.5 are out, G09's 2 are in.
- Restoring I07 would give 63.5, above the 63-minute delivery allowance, unless something shrinks. G11 (2 minutes)
  overlaps G12a.

**Findings (Claude, 2026-11-12).** Status open.

| ID | Type / slide | Issue and consequence | Proposed fix | Status |
| --- | --- | --- | --- | --- |
| R16 | **Prerequisite (Week 4 D6)** — G10 | The left panel is sampled semi-gradient off-policy TD, which reweights each sample by an importance ratio (book eq. 11.2). Ratios come in Week 8. The notes still say this panel is excluded. | Either crop back to the right-hand DP-sweep panel, or keep both panels with a notes explanation that needs no ratio: "left: the same update sampled along behaviour trajectories, reweighted to match the target policy (the reweighting is Week 8); it diverges too, noisily". | resolved — slide kept; notes explain the left panel without ratios; next offering: IS earlier (D16, decision log 2026-11-15) |
| R17 | **Accepted worked activity** — I07 hidden | 5.2's accepted worked activity is "work through a small divergent update example; **vary one part of the deadly triad**" (`topic_decisions.yaml`). With I07 hidden, the variation exists only as I06's question. | (a) Restore I07 and shorten or hide G11, which overlaps G12a: 61.5 minutes. (b) Keep I07 hidden and answer I06's question live with I07's results, which go in I06's notes: on-policy weighting ×0.96, Monte Carlo target ×0.75. Option (b) changes the activity's form, so record it as a decision. | resolved — I07 restored (D15, 2026-11-14); 5.2 targets 63.5, G11 overlap left to the instructor |
| R18 | **Error (typo)** — G01 | "Would this effect stability?" (twice) should be "affect". | Fix both. | resolved — applied (D16) |
| R19 | **Formatting** — G02 | "Episodes start at (1,1) and every actual preterminal visit contributes." is underlined. It looks accidental; nothing else on the slide is underlined. | Remove the underline, unless it is intended. | resolved — applied (D16) |
| R20 | **Precision** — G02 | "Best fit for VE: The minimum VE that can be achieved…" defines a number, but the column lists predictions; the minimum VE is the bottom row. | "Best fit for VE: the predictions with the smallest VE the chosen features allow." | resolved — applied (D16) |
| R21 | **Optional (new no-hedging rule)** | Caveat sentences from Claude's first render are still on slides, which the instructor may want to move to the notes: F12a-A's "A separately supplied sample, not the next transition after termination"; G02's "…not sampled learning curves" and its second takeaway sentence; I05's "in this experiment"; G11's "with appropriate sampling and step sizes", "under its conditions" and "generally"; G13's "Constructed examples: reference values are known". | The instructor decides. No AI edits slide text for this. | resolved — F12a-A, G02, I05, G13 caveats moved to notes (D16) |

**Notes updates needed** (prepared, not applied; the deck is open and two depend on R16/R17):
- **G01:** answers to the new questions:
  - features that merge states give a stable but wrong compromise (5.1's grid);
  - moving targets plus the update distribution can make it diverge (today);
  - hence "converge to wrong values vs diverge".
  - The equation-source line also needs updating to the ∇ form.
- **G02:** the TD-fixed-point definition holds for on-policy linear TD under the usual step-size conditions.
- **Route tags:** I02–I07, G09 and G11–G15: drop the "Alt A/Alt B route" wording now that D14 settles the route.
  - G09: now in the route (2 minutes).
  - I06: no longer "includes G09"; add the answer to its new question (depends on R17).
  - G13 and G15: drop the "if Alt B was taught" sentences.
- **G10:** rewrite the panel sentence (depends on R16). The behaviour description is correct: dashed 6/7 to one of
  the six upper states, solid 1/7 to the lower state, so the next state is uniform over all seven.
- **G00:** hidden; 5.2 starts at G01.
- **Hidden fragment slides:** restore the IDs G05, G06, G08 and G07, and mark them as hidden alternatives.

**R17 resolved (2026-11-14).** The instructor said "Restore I07".
- **Deck:** I07 is unhidden, after a backup. The slide IDs G05, G06, G08 and G07 are restored on the hidden fragment
  slides (slide names only). Deck is now `eaae14d2…`.
- **Check:** a PowerPoint export of all 41 visible slides works.
- **Timing:** 5.2's visible targets are 63.5 minutes.
- **Still not applied:** the other prepared notes updates.

**G11 hidden (2026-11-14).** The instructor said "Hide G11"; G12a covers its statements.
- **Deck:** `0502a2bb…`, after a backup. A notes line records why G11 is hidden.
- **Timing:** 5.2's visible targets are 61.5 minutes.

**Round 2 resolved (Claude, 2026-11-15).** The instructor said "The fixes you list are good", and decided R16:
"keep the slide as is and add the suggested speaker note".
- **Applied:** R18–R21, the prepared notes updates and the G10 note, after a backup. Equation fallbacks are
  refreshed (35 boxes).
- **Check:** a PowerPoint export of all 40 visible slides works, and F12a-A, G01, G02, I05 and G13 were inspected.
- **Deck:** `c4918df9…`. Text view regenerated.
- **Next offering:** reconsider introducing importance-ratio corrections earlier (decision log, 2026-11-15;
  pointer in `topic_decisions.yaml` at `ratios`). The generated `analysis/time_budget.md`, `output/lecture_plan.md`
  and `output/lectures/session_sources.md` are regenerated for that note.

**O3 closed (instructor, 2026-11-15).** C01 and C02 were closed as covered; R03 lapsed with D14. O1 was closed by D17 (full 13-minute geometry).

## Final complete check (Claude) — 2026-11-15

**Deck checked:** `course/lectures/week05/function_approximation_claude.pptx`, SHA-256 `c4918df9…`, 50 slides (40
visible, 10 hidden). Backed up as `output/deck_backups/…c4918df9.final-check.pptx`. The text view is regenerated
from this version. The deck was open in PowerPoint during the check, so it was read only.

**What was checked:**
- **Content and notes:** all 50 slides and their notes were read: mathematics, numbers, notation (guide and D6),
  agreement between slide and notes, stale references, and the no-hedging rule on visible slides. Numbers agree
  with `scripts/check_function_approximation_claude.py`.
- **Fresh PowerPoint render of every slide**, including the hidden ones, rendered from a temporary all-visible copy:
  no layout, equation, picture or crop problem found.
  - Hidden status matches the decisions: G00, G11; the landmark alternatives (D10); G03-B (D13); G05/G06/G08/G07
    (D14).
- **Equations:** 35 equation boxes, all correctly structured. The fallbacks were refreshed after the last
  equation edit, and the deck has not been saved since.
- **Animations from the definitions:** 23 slides have click builds. Every target exists, and no slide has more than
  one timing block. Live playback is for the instructor to check in slideshow mode.
- **Timing (visible slides):** 5.1 = 60 minutes, 5.2 = 61.5 minutes, both within the 63-minute delivery allowance.
  The planning allocations (58 + 58) are unchanged.
- **Slide IDs:** all 50 are unique, with no unnamed slide.

**Findings (Claude, 2026-11-15).** Status open.

| ID | Type / slide | Issue | Proposed fix | Status |
| --- | --- | --- | --- | --- |
| R22 | **Notation clash** — I02 | The instructor's edit "R = 0" stands for the reward on a slide whose two states are L and **R** (v̂(R, w) = 2w). | "$R_{t+1}=0$" (as rendered first) or "all rewards 0". G10's "R = 0" has no state R, so it is optional to change there. | resolved — "All rewards 0" (D18) |
| R23 | **Timing** — G12 | "Possible failure is not inevitable failure" is visible with three bullets but has a 0-minute target. It was folded into G11, which is now hidden. | Give G12 1 minute, which makes 5.2 = 62.5 (within the allowance), or say it in passing with G12a. | resolved — G12 1 minute; 5.2 = 62.5 (D18) |
| R24 | **Maintenance (notes only)** | Stale notes after D14–D17 and the O3 closure: | Clean these notes; no slide change. | resolved — notes cleaned (D18) |
| | | • G00: still says "Visible session boundary…" although it is hidden; | | |
| | | • G02, G03-A, G04, I04 and I05: "short route" timing text, although D17 settled the full route; | | |
| | | • I02: "If G03-B was used…"; | | |
| | | • I03: "C01 remains for instructor review"; | | |
| | | • I05: "C02's first bullet … remains for instructor review"; | | |
| | | • G07 (hidden): "R03 remains…"; | | |
| | | • G10: "Either route", and a sources line that still says the figure is cropped to the right panel; | | |
| | | • G12b: the remark that the instructor may shorten G11. | | |
| R25 | **Note (hidden slides)** | Hidden alternatives G03-B, G05 and G07 still carry first-render caveat lines ("…not one sampled TD update", "Mechanism fragment…", "…not one unchanged-task experiment"). This does not matter while they are hidden. | If one of them is ever unhidden, move those lines into its notes (no-hedging rule). | resolved — no action while hidden (noted in D18/O7) |

**After the fixes:** store the final previews (`output/lectures/week05/function_approximation_claude_preview.{pdf,png}`,
visible slides) and the text view from the fixed deck. Workflow step 7 also calls for ChatGPT's full content and
notes review. Acceptance ("done", with the deck's SHA-256) is the instructor's decision.

**Final-check fixes applied (Claude, 2026-11-15)** after the instructor said "Yes, apply all":
- **Applied:** R22, R23 and R24, each after a backup. I02's new run had inherited the language tag `ar-AE`, which put
  the comma right-to-left ("0 ,γ"); it is now `en-US` and renders as "All rewards 0, γ = 0.9, …".
- **Other `ar-AE` runs:** 32 more runs from the instructor's PowerPoint edits carry the tag. They render correctly
  in the export and were left alone. They matter only next to punctuation, or for spell-checking.
- **Equations:** fallbacks refreshed (35 boxes).
- **Check:** fresh PowerPoint export of all 40 visible slides; slide targets 5.1 = 60, 5.2 = 62.5.
- **Final previews** stored from this deck (`…_preview.{pdf,png}`), and the text view is regenerated.
- **Deck:** `2e02cbd3…`.
- **Still pending for step 7/8:** ChatGPT's full content and notes review; the instructor's slideshow check of click
  order; acceptance.

## Final review by ChatGPT, 2026-11-15

Reviewed saved deck `2e02cbd3a7f5a95f3061b1f8fd859773024e36e3dfc1dc4c0f36f5eba8653748` against D10–D18 and the earlier decisions they retain. Slide numbers below are the PowerPoint numbers printed on the slides. Slides 38 and 39 are pages 36 and 37 of the visible-only PDF.

**Two corrections matter before acceptance.** Both fit inside the existing convergence tables and their two-minute targets. The proposed wording retains the comparison requested in D12. Assumptions and counterexamples belong in the speaker notes.

| ID | Type and slide | Finding and proposed correction | Status |
| --- | --- | --- | --- |
| R26 | Error · 38, G12a, nonlinear gradient MC | The check mark promises convergence to a local minimum of VE. The notes give decreasing step sizes and coverage, which are insufficient even for a deterministic return. For a single terminal transition paying 1, take v̂(s,w) = w³ and start at w = 0. Every gradient MC update is zero, although positive weights arbitrarily close to zero give lower VE = (1−w³)². This also conflicts with F07's speaker cue. Replace the checked cell with **“Stationary points of VE”** and omit the convergence tick for that cell. Explain in the notes what a zero gradient means and give the example. Sutton & Barto §9.3 uses the customary local-optimum shorthand. For a precise nonconvex SGD result under assumptions, see [Bottou, Curtis & Nocedal, §4.3](https://arxiv.org/abs/1606.04838). | Approved (D19), pending application by Claude |
| R27 | Error · 39, G12b, linear MC control and Sarsa | The legend says the learner “stays near a good solution but keeps oscillating.” Both quality and persistent oscillation are stronger than the evidence. With one state, two actions that terminate with +1 and −1, identical action features and the deck's uniform tie-breaking, both actions always get the same prediction. The greedy tie policy earns 0 on average while the optimal policy earns 1. Scaling both rewards scales the gap. Use **“(✓) can oscillate as the policy changes”** and explain the role of feature quality in the notes. Also correct the notes' explanation of tabular policy improvement. A greedy improvement can change actions in several states simultaneously. The theorem compares candidate actions using the current policy's exact action values. See Sutton & Barto §§4.2 and 10.1 and [Zhang et al., ICML 2023](https://proceedings.mlr.press/v202/zhang23al.html) for the scope of a bounded-region result for projected linear Sarsa. | Approved (D19), pending application by Claude |

**Smaller corrections for the same edit pass**

| ID | Type and slide | Finding and proposed correction | Status |
| --- | --- | --- | --- |
| R28 | Teaching precision · 25, G02 | “The point where the semi-gradient TD algorithm converges” describes the outcome in this grid, but makes a fixed point sound attracting by definition. I05 supplies a counterexample in this deck. Under w ← 1.02w, zero is fixed and nearby nonzero weights move away. Suggested definition for the column is **“Predictions at the weights where the expected TD update is zero.”** Keep the grid's convergence conditions in the existing notes. | Approved (D19), pending application by Claude |
| R29 | Presenter cue · 26, G03-A | The notes say “Five clicks.” The PPTX defines five chart builds and a sixth click revealing the final paragraph about the start-state coordinate. Preserve the instructor's animation and update the cue to **“Five chart builds, then click once for the start-state value.”** The notes also call the fit “near-horizontal.” The move from the true pair (0.11636, 0.83636) to the weighted fit (0.12623, 0.12623) is almost vertical on these axes. Say that the horizontal coordinate changes by only about 0.010 because the right-hand cell carries 72 times the weight. | Approved (D19), pending application by Claude |
| R30 | Placement · 9, F08 | The italic instructor terminology aside remains on the slide. D7 asks to retain it and the later November 12 rule places such asides in speaker notes. Move the sentence verbatim into the notes and keep the definition of semi-gradient on the slide. | Approved (D19), pending application by Claude |
| R31 | Notes precision · 3, F02 | The humanoid answer says a table “cannot even be indexed” for continuous states. An observed joint configuration can serve as a key. The practical problems are sparse repeat visits, independent entries and the impossibility of enumerating every configuration in a finite table. Suggested cue is **“We can store each configuration we visit. With continuous joint angles and velocities, exact repeats are rare, so most new configurations need a fresh estimate.”** | Approved (D19), pending application by Claude |

**Verification.** Checked slide content and notes across the 50-slide deck, including the hidden alternatives. The saved PPTX matches the fingerprint in the text view. All 40 PDF page titles match the visible slide sequence and the stored contact sheet shows the same route. The 10 hidden slides match the decisions. The visible PowerPoint export shows legible equations and complete figures, including both panels of Baird's example. The earlier 14-point diagnostic table is now slide 40 and fits on the slide. All internal package links and animation shape references resolve. The sixth-click finding comes from PowerPoint's timing definitions. Live playback remains the instructor's check.

Recomputed the grid occupancy and value errors (0.00623535 at the best fit and 0.00637684 at the TD fixed point), the two-state growth and intervention factors (1.02, 0.96, 0.75), and the diagnostic error sequence (250, 260.1, 270.60804). The visible targets sum to 60 and 62.5 minutes against the accepted 63-minute delivery allowance. The second meeting retains eight minutes for the intervention activity and six minutes for diagnosis. Findings above require wording or cue changes within the existing time. The instructor approved all six fixes on 2026-11-15 for Claude to apply. [Deck decision D19](../../decisions/lectures/function_approximation.md)
