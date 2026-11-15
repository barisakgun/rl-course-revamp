# Deck decisions: function approximation (sessions 5.1–5.2)

**Shared** deck decision file (`docs/lecture_workflow.md`). It holds outcomes only. Discussion and findings are in the
[shared review](../../analysis/lecture_suggestions/function_approximation_review.md). The initial suggestions are
historical inputs:
- [Claude](../../analysis/lecture_suggestions/function_approximation_claude.md);
- [ChatGPT](../../analysis/lecture_suggestions/function_approximation_chatgpt.md).

**Scope:** sessions 5.1 `linear` (Linear approximation and semi-gradients) and 5.2 `instability` (Approximation
instability). Accepted teaching allocations, scope and mastery live in `decisions/topic_decisions.yaml`.

**Status: DONE** (accepted by the instructor, 2026-11-15, D20). This is the deck's only current status record; other files point here. A later substantive change reopens the status.
- **Deck:** `course/lectures/week05/function_approximation_claude.pptx`, SHA-256
  `72837e0a8984d400f2a3738d5aaa0c967416ecb94bbdfba61aa204fdf1c834b3`, 50 slides (40 visible). It is the instructor's round-2 save
  `13e58d03…` plus D15–D16, the final-check fixes R22–R24 (D18) and ChatGPT's final-review fixes R26–R31 (D19),
  with equation fallbacks current.
  - Hidden: G00 (5.2 divider), G11 (D15).
  - Hidden alternatives: F12-B, F12a-B, F13-B (D10); G03-B (D13); G05, G06, G08, G07 (D14).
- **Final previews:** `output/lectures/week05/function_approximation_claude_preview.{pdf,png}`, 40 visible
  slides, from this deck. The text view matches the same deck.
- **Sessions:**
  - **5.1** = slides 1–22 (F00–F18): 60 minutes.
  - **5.2** = slides 23–42 (G01 to G15 with I02–I07, G09, G12a, G12b; G11 hidden): visible targets sum to 62.5
    minutes, within the 63-minute delivery allowance (G12 1 minute, D18).
- **The PPTX is the teaching source.** Text view: `output/lectures/week05/function_approximation_claude.md`.
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

## Accepted (instructor, 2026-11-10, first editing round)

- **D10. 5.1 uses the grid example; the landmark slides stay as hidden alternatives** (instructor's saved edit: the
  grid slides lost their "Alt A" tags, and the landmark slides were moved to the end and hidden, titled "The next 3
  are alternatives to 14-16").
  - D2's choice is settled for teaching. F12-B/F12a-B/F13-B remain in the deck, hidden and not counted.
  - 5.1 targets stay 58.5 (D8).
  - Geometry (O1) and the 5.2 divergence alternates (D3) are not affected.

## Accepted (instructor, 2026-11-10, first editing round findings R10–R15)

- **D11. Round-1 fixes** (instructor replies to the shared review's R10–R15).
  - **R10 (F03):** "A compact representation: d ≪ |𝒮| (number of weights ≪ number of states)". Applied.
  - **R11 (F05):** the expectation uses the random state, 𝔼_π[(v^π(S) − v̂(S, **w**))²]. Applied.
  - **R12:** the on-policy state distribution depends on the policy, so the notation guide now defines μ^π(s), with
    μ(s) acceptable when π is fixed and clear from context. F05 is applied with μ^π(s); Claude used the guide's
    superscript policy mark in place of the slide's μ_π. Later slides keep μ(s) under the context rule.
  - **R13 (F05):** "How to learn" asks how to learn **w** and guides students toward gradient descent. The notes
    now say so; the slide text is unchanged.
  - **R14 (F04):** the repeated equations stay.
  - **R15:** add 1.5 minutes. F02 goes from 3 to 4 and F03 from 3 to 3.5, so 5.1's grid route targets 60 minutes.
    This is fine for delivery under the 63-minute allowance; the planning estimate is unchanged at 58.
  - No scope, mastery or assessment change.

## Accepted (instructor, 2026-11-12, editing round 2)

- **D12. Convergence comparison slides G12a (prediction) and G12b (control) after G12** (instructor request: MC
  versus semi-gradient TD, tabular / linear / nonlinear, prediction and control, guided by old P55–56).
  - **Rows:** gradient MC, semi-gradient TD on-policy and with another state weighting; MC control, semi-gradient
    Sarsa, Q-learning. Gradient-TD and off-policy MC rows are left out.
  - **Slide text** states the results only; conditions are in the notes.
  - **Timing:** 2 minutes each, so 5.2's timed route targets 62, within the 63-minute delivery allowance. The planning
    allocation is unchanged. G11 overlaps G12a and may be shortened by the instructor.
  - Renderer input: `course/lectures/week05/function_approximation_convergence_claude.yaml` (first draft, not
    maintained).
- **D13. Geometry uses the grid picture P1; P2 (G03-B) stays as a hidden alternative** (instructor's saved edit:
  G03-B moved to the end and hidden). This settles D5's picture choice for teaching. Geometry depth (O1, 13 versus 8
  minutes) is not affected. The instructor also hid the 5.2 section divider G00.
- **Shared rule (decision log, 2026-11-12):** no hedging or disclaimers on slides; caveats go in the speaker notes
  (`AGENTS.md`).

- **D14. 5.2 teaches the complete two-state construction (I02–I06); the fragment slides stay as hidden
  alternatives** (instructor's saved edit, 2026-11-12: "Alt A" removed from I02–I07, and G05/G06/G08/G07 moved to the
  end and hidden as alternatives to slides 28–32 (33)). This settles D3 for teaching; R03 (fragment variants) no
  longer affects the taught route. The instructor also hid I07; its relation to the accepted worked activity is open
  (review R17).

- **D15. I07 is restored** (instructor, 2026-11-14: "Restore I07"; review R17). This keeps 5.2's accepted worked
  activity, which includes "vary one part of the deadly triad". **G11 is hidden** (instructor, 2026-11-14: "Hide
  G11"), because G12a's table covers its statements. 5.2's visible slide targets are 61.5 minutes, within the
  delivery allowance; the planning allocation is unchanged. No scope, mastery or assessment change.

- **D16. Round-2 findings resolved** (instructor, 2026-11-15: "The fixes you list are good").
  - **R16 (G10):** the slide stays as the instructor edited it, with both panels of book Figure 11.2. The notes
    explain the left panel without ratios: "the same update sampled along behaviour trajectories, reweighted to match
    the target policy; the reweighting is Week 8; it diverges too, just noisily". Week 4 D6 is unchanged for Fall
    2026. For the next offering, see the decision log (2026-11-15) on introducing importance-ratio corrections earlier.
  - **R18:** G01 "affect" (twice).
  - **R19:** G02 underline removed.
  - **R20:** G02 "Best fit for VE: The predictions with the smallest VE the chosen features allow".
  - **R21:** Claude's leftover first-render caveats moved from F12a-A, G02, I05 and G13 into their notes (G11 is
    hidden and left as is).
  - **Notes:**
    - G01: answers to the new questions, and the equation line in the ∇ form;
    - G02: when the definitions hold;
    - I06: now leads into I07;
    - G09: in the taught route;
    - the I02–I07 and G03-A route tags;
    - G00 hidden;
    - G12, G13 and G15: hidden-route references removed;
    - the hidden alternatives labelled.
  - No scope, mastery or assessment change. 5.2 stays at 61.5 minutes.

- **D17. Geometry depth: the full 13-minute version** (instructor, 2026-11-15; closes O1). G02 (5 minutes of
  linear-TD limits), G03-A (6) and G04 (2) are taught as rendered, with all five G03-A builds. The 8-minute fallback
  is not used. Under the accepted counting, projection itself stays at about 8 minutes (G03-A + G04), as in
  `topic_decisions.yaml`. 5.2 stays at 61.5 minutes.

- **D18. Final-check fixes** (instructor, 2026-11-15: "Yes, apply all"; review R22–R24).
  - **R22 (I02):** "All rewards 0" replaces "R = 0", which clashed with the state R.
  - **R23 (G12):** 1 minute, so 5.2 = 62.5, within the delivery allowance; the planning allocation is unchanged.
  - **R24:** stale notes cleaned (route, short-geometry and review-status wording) on G00, G02, G03-A, G04, I02–I05,
    G07, G10 and G12b.
  - **Fixed while rendering:** I02's new text run carried the language tag `ar-AE`, inherited from the instructor's
    edit, which put the comma in right-to-left order. It is now `en-US`.
  - No scope, mastery or assessment change.

- **D19. Instructor approval of R26–R31 (2026-11-15).** The instructor approved all six fixes as written in the [final review](../../analysis/lecture_suggestions/function_approximation_review.md#final-review-by-chatgpt-2026-11-15) for Claude to apply to the Week 5 deck.

## Accepted (instructor, 2026-11-15, deck acceptance)

- **D20. Deck accepted as done** (instructor: "I accept the deck").
  - **Accepted deck:** SHA-256 `72837e0a8984d400f2a3738d5aaa0c967416ecb94bbdfba61aa204fdf1c834b3`, 50 slides (40 visible).
    - Hidden: G00 and G11.
    - Hidden alternatives: F12-B, F12a-B, F13-B, G03-B, G05, G06, G08, G07.
  - **Slide targets:** 5.1 = 60 minutes and 5.2 = 62.5 minutes, within the 63-minute delivery allowance. The planning
    allocations in `decisions/topic_decisions.yaml` stay 58 + 58.
  - **Checks before acceptance:**
    - Claude's final complete check, including a PowerPoint render of all 50 slides, with fixes R22–R24 (D18);
    - ChatGPT's final review, with fixes R26–R31 (D19), applied by Claude;
    - a fresh PowerPoint export of the 40 visible slides.
  - **Views:** final previews `output/lectures/week05/function_approximation_claude_preview.{pdf,png}` and the text
    view, all from this deck.
  - **Not exercised before acceptance:** ChatGPT's focused recheck of R26–R31 (the instructor accepted without
    waiting for it); live slideshow playback (instructor, in slideshow mode).

## Consider for next semester (instructor, 2026-11-12)

Not part of the Fall 2026 deck. Revisit when this deck is prepared for the next offering.

- **Course planning (decision log, 2026-11-15): introduce importance-ratio corrections earlier**, before this deck, so
  that off-policy convergence (G10's sampled panel, the convergence tables) can be discussed without a forward
  reference.
- **5.2: show the Bellman operator and the projection explicitly, with one or two backup-and-fit steps on the
  geometry picture.** The instructor noticed that the machinery (B^π, projection) is left out, together with any
  update steps on the geometry. Claude compared other courses (2026-11-12):
  - **Sutton & Barto §11.4, Figure 11.3:** B^π, the μ-weighted projection Π, the Bellman error, PBE, VE and the TD
    fixed point (PBE = 0). The arrows (backup, then project) are a "DP-like process", not sampled TD steps.
  - **Sutton's CMPUT 366/609 slides (26-offpolicy, pp. 13–24):** about 12 slides covering:
    - TD is not the gradient of any objective;
    - the A-split example;
    - the VE/BE/PBE/TDE objectives;
    - gradient TD.
  - **Silver L6:** no operator or projection; convergence tables plus one line that TD follows no gradient.
  - **CS285 L8, pp. 30–35:** about 5 slides.
    - B is a contraction in the max norm, and Π is the squared-error projection onto the representable set Ω.
    - Fitted value iteration is V ← ΠBV, and "ΠB is not a contraction of any kind". The picture shows BV leaving Ω
      and being projected back.
    - The same argument covers fitted Q-iteration and online Q-learning, and leads to "target networks / replay
      really help".
    - It uses an unweighted norm and full fits, not semi-gradient steps.
  - **CS234 L4, p. 60:** words only (a backup is a contraction; fitting can expand). B^π and contraction are defined
    in its DP lecture.
  - **CS224R and Abbeel:** none. CS224R presents the semi-gradient as stopping the gradient through the target.
  - **Old course P48–52:** objectives, |𝒮| = 3 / dim(w) = 2 geometry and gradient TD, marked "not for exams".
  - **No course draws sampled TD steps on the geometry;** where steps appear they are full backup-and-fit iterations.
- **What it would look like here** (computed 2026-11-12, not in any deck file):
  - **Grid picture P1, on-policy weighting:** from 0 the shared value goes 0.074 → 0.107 → 0.122 → … → 0.133 (the TD
    fixed point). Each backup leaves the diagonal, e.g. to (0.064, 0.792), before the fit.
  - **Two-state picture P2, with the divergence example's zero rewards:** with equal state weights, w goes 10 → 10.8
    → 11.66 (×1.08 per step); with the target policy's weights, 10 → 9 → 8.1 (×0.9). This would tie the geometry to
    the divergence example.
- **Prerequisite:** students already know B^π and the one-line contraction argument (`bellman` deck).
- **Costs:**
  - about 2–4 more minutes in 5.2;
  - Π on slides needs the notation guide's layout fallback, or a guide entry;
  - PBE and gradient TD would go beyond the `projection` group's exposure scope, which would need a scope decision.

## Open

| # | Item | Where discussed |
| --- | --- | --- |
| O1 | Closed by D17 (2026-11-15): full 13-minute geometry. | — |
| O2 | Closed by D6 (2026-11-02). | — |
| O3 | Closed (instructor, 2026-11-15): C01 is covered by I03's "Rule of this experiment" and its Week 8 notes pointer; C02 by G10's Baird growth panels. R03 lapsed with D14. | — |
| O4 | Closed by D9 (2026-11-08): Claude's order is the step-4 basis. | — |
| O5 | Closed by D11 (2026-11-10). | — |
| O6 | Closed by D15–D16 (2026-11-15). | — |
| O7 | Closed by D18 (2026-11-15). R25 (caveat lines on hidden alternatives) needs action only if one of them is unhidden. | — |
