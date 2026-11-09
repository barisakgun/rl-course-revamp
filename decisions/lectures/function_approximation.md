# Deck decisions: function approximation (sessions 5.1–5.2)

**Shared** deck decision file (`docs/lecture_workflow.md`). It holds outcomes only. Discussion and findings are in the
[shared review](../../analysis/lecture_suggestions/function_approximation_review.md). The initial suggestions are
historical inputs:
- [Claude](../../analysis/lecture_suggestions/function_approximation_claude.md);
- [ChatGPT](../../analysis/lecture_suggestions/function_approximation_chatgpt.md).

**Scope:** sessions 5.1 `linear` (Linear approximation and semi-gradients) and 5.2 `instability` (Approximation
instability). Accepted teaching allocations, scope and mastery live in `decisions/topic_decisions.yaml`.

**Status: first render handed off for instructor editing (workflow step 5 → 6), 2026-11-09.** This is the deck's only
current status record; other files point here. O1 and O3 below are open.
- **Deck:** `course/lectures/week05/function_approximation_claude.pptx`, SHA-256
  `8f359e7e20f753af406c9466cbb79bb90b202aeb82291271930f3388b37606aa`, 48 slides, none hidden. All alternates are
  visible and tagged Alt A / Alt B (D2, D3, D5, D8).
- **Sessions:**
  - **5.1** = slides 1–25 (F00–F18). The timed Alt A (grid) route targets 58.5 minutes; the Alt B (landmark) route
    targets 59.5 (D8).
  - **5.2** = slides 26–48 (G00–G15 with I02–I07). The timed route (full geometry, geometry Alt A, divergence Alt A)
    targets 58. Other routes' minutes are in each slide's notes, as in the content file's route table.
- **The PPTX is the teaching source.** Text view: `output/lectures/week05/function_approximation_claude.md`.
  No stored previews until the final check.
- **First-render inputs, all frozen:**
  - the shared [content](../../course/lectures/week05/function_approximation_content.md) (ChatGPT, step 4);
  - `function_approximation_claude.yaml` (5.1);
  - `function_approximation_instability_claude.yaml` (5.2, appended after F18).

  Render notes are in the [shared review](../../analysis/lecture_suggestions/function_approximation_review.md#first-render-claude--2026-11-09).

## Accepted (instructor, 2026-11-02, after the mutual cross-review)

The instructor answered the six items in the shared review's "Status after the mutual cross-review".

- **D1. One deck `function_approximation` for sessions 5.1 and 5.2**, with a visible session divider, as for Weeks 2–4.
  Files use `function_approximation`, e.g. `course/lectures/week05/function_approximation_claude.pptx`.

- **D2. 5.1 worked example: both alternatives go into the deck, marked as alternates.** The instructor chooses while
  going over the deck. Only one alternate counts toward the slide targets.
  - **Alternate A, the 2×2 grid:** always-right, features (1, steps to goal), two semi-gradient TD updates and the
    aliasing diagnosis (Claude F12–F13, 14 minutes).
  - **Alternate B, the landmark features** from old Midterm 1 (Spring 2025, Q4): two TD updates (ChatGPT F10,
    9 minutes) and its two-state diagnosis (ChatGPT F11, 6 minutes).
  - The alternate not chosen is removed, or hidden, when the instructor decides. The geometry picture in O1 depends on
    this choice.

- **D3. 5.2 worked divergence example: both alternatives go into the deck, marked as alternates.** The instructor
  chooses while going over the deck. Only one alternate counts toward the slide targets.
  - **Alternate A, ChatGPT's complete two-state construction** (I02–I07): the fragment as an opener, then the
    balanced-update calculation and one-component changes. Open fixes C01–C02 apply.
  - **Alternate B, Claude's two-state fragment** (G05–G08): three updates, the multiplier, the triad, three variants.
    Open fix R03 applies: label the variants as separate constructions.
  - Either alternate is followed by Baird's counterexample as a three-minute picture (Claude G10, DP-sweep panel; no
    importance ratio).

- **D4. Optional material is kept** (instructor: "Mountain car is an essential problem setting").
  - **5.1:** Mountain Car with linear Sarsa and tile coding (Claude F16, old slides 33–34). Problem setting and
    figures only. No further algorithm, implementation or assessment requirement.
  - **5.2:** a slide of scoped convergence statements (review C06, worded as in R02), not a blanket table.
  - **Scope:** no change to accepted scope, mastery or allocations. Timing is in the review's
    [time check](../../analysis/lecture_suggestions/function_approximation_review.md#time-check-for-the-alternates-claude-2026-11-02).

## Accepted (instructor, 2026-11-02, replies on geometry pictures and notation)

- **D5. Geometry pictures: P1 and P2 both go into the deck as alternates; P3 is left out for now.** The instructor will
  pick from the alternatives, so the final picture depends on that selection. Details are in the
  [review's geometry options](../../analysis/lecture_suggestions/function_approximation_review.md#item-4-geometry-options-and-pictures).
  - **P1, grid slice:** the (v(2,1), v(1,2)) plane with the diagonal as the representable set. It goes with D2 A (grid).
  - **P2, two-state line:** the (v(L), v(R)) plane with the line (w, 2w), plus the +1 reward variant used only for
    the picture. It goes with D3 A (complete construction) or D2 B (landmark).
  - **P3, the generic 3D plane** (old slides 49–50, book Figure 11.3): not in the deck now. The instructor leans toward
    a later appendix for interested students. ChatGPT's warning (review R01) applies to any later use:
    - the figure's arrows show an exact DP-like backup-then-project process (book §11.4, printed pp. 268–269 / PDF
      290–291), not the sampled semi-gradient TD step students compute;
    - its labels (Bellman error, projected Bellman error, VE) go beyond the accepted exposure scope of `projection`.

    An appendix version would need that caveat on the slide and no assessment use.
  - **No scope change.** The geometry stays at exposure depth with no projected-Bellman derivation.

- **D6. Notation: Claude's symbol proposals S1–S11 are accepted, with a layout fallback** (instructor: "if there is
  a layout error, we can use repeated symbols if they can be easily differentiated from context").
  - **Added to `course/notation_guide.md`** (Weeks 5–6):
    - ∇v̂(s, **w**) and ∇q̂(s, a, **w**), the gradient with respect to **w**;
    - VE(**w**), not J(**w**);
    - **x**(s, a).
  - **Avoided on slides:** Π (write "best fit"); the book's A and b; d as a feature name; μ for weightings other than
    on-policy (named in words).
  - **Words for clashing quantities:** Mountain Car "position" and "velocity"; coordinates as "column" and "row";
    landmark features x₁(s) … x₄(s).
  - **Weights:** a plain scalar w in the one-weight examples; Baird's components w₁ … w₈ labelled "subscript =
    component".
  - **Layout fallback:** a repeated symbol, such as x for position or Π for the projection, may replace the word form
    when the word form causes a layout problem, provided the context makes the meanings easy to tell apart. The slide
    states the local meaning.
  - The old-deck conversions (f → **x**, V̂^π → v̂, R_t → R_{t+1} and others) apply when slides are reused. This closes
    O2.

## Accepted (instructor, 2026-11-02, AI corrections)

- **D7. The AIs' agreed corrections are accepted for consolidation, with one change and three items kept open.**
  Details are in the [shared review](../../analysis/lecture_suggestions/function_approximation_review.md).
  - **Accepted:**
    - **R01:** the projection picture explains the representable set, the best fit and the TD fixed point, not a
      single sampled TD step. The failure sentence is "the tabular guarantee does not automatically survive fitting
      with a different state weighting".
    - **R02:** "any two of the triad are safe" is limited to linear approximation; convergence statements are scoped
      per method; "not, in general, a true gradient method".
    - **R04:** the every-visit weighting is stated once; grid results are labelled "computed best fit and TD fixed
      point"; fluctuation with a constant step size is mentioned.
    - **R05:** "some value functions cannot be represented; whether this policy's can depends on the policy".
    - **R08:** diagnosis panels state their construction and show value error next to the weights.
    - **R09:** notation is covered by D6.
    - **C03:** about 6 minutes for the three-way diagnosis.
    - **C02, second bullet:** only the γ = 0.9 multiplier is shown live, with no threshold.
    - **ChatGPT's continuity notes:** Week 4 left the importance-ratio question open; the reasons for cutting P6, P59
      and P60.
  - **Changed: R07.** Old slide 15's disclaimer stays (instructor: "I might keep calling them gradients"): semi-gradient
    methods may be called gradient methods in class. Old slide 13's "equivalent to full gradient update" sentence is
    still omitted.
  - **Kept open for the instructor's review:**
    - R03: the fragment variants in alternate B;
    - C01: the data rule in alternate A, which in any case shows no ratio on the slide, per Week 4 D6;
    - C02, first bullet: a visual of many updates or Baird's panel after the hand calculation.
  - **Closed by D5 and D6:** C04, C05 and C06.
  - **No change** to scope, mastery, allocations or assessment.

## Accepted (instructor, 2026-11-08, remaining early choices)

- **D8. Remaining early choices from the step-1 suggestions.** The instructor answered Claude's list of choices not yet
  decided (shared review, after D7).
  1. **Out-of-scope old slides are removed from this deck; the relevant ones are kept for later.**
     - **Removed:** average reward with approximation (old 37–40); gradient TD (old 48, 51–55); least squares, LSTD
       and LSPI (old 62–74, with hidden 63 and 66).
     - **Kept for later:**
       - old 57–58 (incremental versus batch) for the Week 6 deck's replay discussion (`dqn_loop`);
       - old 62–74 (least squares/LSTD) as source material if the optional `least_squares_td` mention is used in the
         offline unit.

       Both are pointers only; the Week 6 and offline decks decide their own content.
  2. **Control with approximation stays in 5.1** (Claude F15: q̂, the semi-gradient Sarsa and Q-learning targets, the
     semi-gradient Sarsa box). D4's Mountain Car slide (F16) builds on it, and 6.1 assumes it.
  3. **5.1's slide targets may use the delivery allowance:** 58.5 minutes with D2 alternate A, 59.5 with alternate B.
     This is fine for delivery under the 63-minute allowance; the planning estimate stays 58.
  4. **D2 alternate A (grid) keeps its second worked update** (transition B), which shows the two aliased cells pulling
     the shared weights in opposite directions.
  5. *(Not decided: the basis for the step-4 content. See O4.)*
  6. **Alternates are tagged "Alt A" and "Alt B"** in each alternate slide's title and notes. Only one alternate per
     choice counts toward the slide targets. The other is hidden or removed when the instructor chooses.
  - **Q-Pacman (old 30):** removed. The instructor would keep it only without a worked numerical example, and both D2
    alternates provide one.
  - **A2 exam bridge:** the stale Midterm 1 sentences are removed from `decisions/assignment_decisions.md`.
    Midterm 1 no longer covers Week 5 (decision log, 2026-11-02).
  - **No change** to scope, mastery, allocations or assessment.

## Accepted (instructor, 2026-11-08, step-4 basis)

- **D9. Claude's order is the basis for the step-4 content** (closes O4; instructor: "Claude's order"). Details are in
  [the review's O4 section](../../analysis/lecture_suggestions/function_approximation_review.md#o4-what-the-basis-for-step-4-content-means-claude-2026-11-08).
  - **5.1:** Claude's F00–F18. D2's alternates sit at F12–F13: Alt A is the grid; Alt B is ChatGPT's F10–F11. Two of
    ChatGPT's points are merged in without time cost: "linear in **w**; the features may be nonlinear" (into F09) and
    one-hot versus overlapping sharing (into F11).
  - **5.2:** Claude's frame, following the 5.2 rows of the review's time check. D3's alternates: Alt A is ChatGPT's
    I02–I07, compressed as in the time check; Alt B is Claude's G05–G08. Then come the Baird picture, the scoped
    convergence statements (D4) and the 6-minute diagnosis. "What convergence means" appears once, in 5.2's
    geometry block (O1).
  - **Applies throughout:** D5's pictures, D6's notation, D7's corrections and D8's tags and removals. Step 4 should
    also use the Week 4 changes accepted on 2026-11-05, listed in the review's O4 section: Expected SARSA as
    exposure, the 4.2 tabular convergence slide, and P08 as a callback.

## Open

| # | Item | Where discussed |
| --- | --- | --- |
| O1 | **Geometry depth** (instructor item 4). The instructor leans toward the 13-minute version (5 minutes of linear-TD limits plus 8 of projection, as in `topic_decisions.yaml`). It reverts to 8 minutes in total if time runs short. The pictures are settled by D5. | [Review: geometry options](../../analysis/lecture_suggestions/function_approximation_review.md#item-4-geometry-options-and-pictures) |
| O2 | Closed by D6 (2026-11-02). | — |
| O3 | **R03, C01 and C02 (first bullet)**: left for the instructor's review of the D3 alternates. The other AI corrections are accepted (D7). | [Shared review](../../analysis/lecture_suggestions/function_approximation_review.md#instructor-replies-on-o3--2026-11-02) |
| O4 | Closed by D9 (2026-11-08): Claude's order is the step-4 basis. | — |
