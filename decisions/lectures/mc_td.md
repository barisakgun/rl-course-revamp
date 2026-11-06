# Deck decisions: model-free prediction (sessions 3.1–3.2)

**Shared** deck decision file (`docs/lecture_workflow.md`). It holds outcomes only; discussion and findings will be in the shared review `analysis/lecture_suggestions/mc_td_review.md`.
- **Scope:** sessions 3.1 `mc_td` (Sampling, MC/TD and continuing objectives) and 3.2 `returns` (Bias, variance and n-step targets). Accepted teaching allocations, scope and mastery live in `decisions/topic_decisions.yaml`.
- **Status: DONE** (accepted by the instructor, 2026-10-27, D19). This is the deck's only current status record; other files point here.
  - Deck: `course/lectures/week03/mc_td_claude.pptx`, SHA-256 `b4ca75d4317a629ca7941888759a70ca926aae93d2c96baadde10e46f1ef72ba`, 50 slides. 3.1 = slides 1–20 (MT00–MT14 plus the recap). 3.2 live = slides 21–42 (MT15–MT23a, MTL1–MTL3, MTE1–MTE2, MT25). Optional, shown, no live time = slides 43–44 (instructor-added backup comparison and unified view, book Figure 8.11). Hidden appendix = slides 45–50 (MTX divider, MT24–MT24c, MTA1). Later substantive edits reopen the status.
  - Timing: slide targets 60 minutes for each session (D10, D18); planning allocations in `decisions/topic_decisions.yaml` stay 59 and 58.
  - Views: text view `output/lectures/week03/mc_td_claude.md`; previews `output/lectures/week03/mc_td_claude_preview.{png,pdf}` (hidden slides omitted), from this deck.
  - Inputs and history: first-render inputs, all frozen: 3.1 [`mc_td_content.md`](../../course/lectures/week03/mc_td_content.md) and `mc_td_claude.yaml`; 3.2 [`mc_td_returns_content.md`](../../course/lectures/week03/mc_td_returns_content.md) and `mc_td_returns_claude.yaml`; D18 revision: the shared review's renderer handoff and `mc_td_lambda_claude.yaml`. Rendering and edit-round notes: [shared review](../../analysis/lecture_suggestions/mc_td_review.md). Suggestions: [historical Claude 3.1](../../analysis/lecture_suggestions/mc_td_claude.md), [Claude 3.2](../../analysis/lecture_suggestions/mc_td_returns_claude.md), [ChatGPT](../../analysis/lecture_suggestions/mc_td_chatgpt.md).
  - O6 resolved by the November 2 midterm decision; see the Open table for its authoritative reference.

## Accepted (instructor, 2026-10-21)

Answers given before step 1, to the early choices Claude listed for 3.1.
- D1. **One deck `mc_td` for sessions 3.1 and 3.2**, as for Week 2 (`bellman`, C1). Files use `mc_td`, e.g. `course/lectures/week03/mc_td_claude.pptx`.
- D2. **Running example: the 2×2 grid** from the `bellman` deck (separate MDP, entry rewards, γ = 0.5 unless a choice says otherwise). In addition, **the book's example is kept as a standalone illustration (one or two slides)** to make the points it makes well. Which book example is meant is open (O1).
- D3. **3.1 drops the embedded psychology connection; the average-reward contrast stays** (instructor: average reward is important). The psychology/neuroscience connection keeps its 7.2 placement. Recorded in `decisions/topic_decisions.yaml` (`mc_td`) and the decision log; the 59-minute allocation is unchanged.

**Instructor, 2026-10-21 (after Claude's step-1 suggestion):**
- D4. **Notation N(s)** for the Monte Carlo visit count (intuitive and widespread), added to `course/notation_guide.md`. The relation to the bandit N_t(a) is revisited when Week 9 needs it.
- D5. **The average-reward contrast uses a continuing example, not the 2×2 grid** (the grid is episodic; padding its terminal with zero rewards gives average reward zero). The recycling robot or another continuing example; which one is O2.

**Instructor, 2026-10-22 (choices I1–I3 after the mutual cross-review):**
- D6. **Book examples (resolves O1): split A.** Example 6.1 (driving home) in 3.1, as the motivation block before the TD rule, with the MC/TD arrow panels after it. Examples 6.2 (random walk) and 6.4 ("you are the predictor") in 3.2. Average reward keeps its accepted 5 minutes; 3.1 does not use the delivery allowance. 3.2's fit for 6.2 and 6.4 (batch setup before 6.4; random-walk setup counted outside the ten protected evaluation minutes) is to be shown in 3.2's step 1 (review R12, R13, R17).
- D7. **Average-reward example (resolves O2): ChatGPT's continuing service example.** At a ready state, steady service pays 0.8 and stays ready; a large job pays 0 and enters a busy state, whose completion pays 2 and returns to ready. The two policies' average rewards are 0.8 and 1 per step; their γ = 0.5 discounted returns from ready are 1.6 and 4/3, so the ranking flips. Show only the long-run time-average definition: the alternating policy is periodic, so the pointwise limit of 𝔼[R_t] does not exist (review R05). No differential values or §10.4 teaser live (R11).
- D8. **Basis for 3.1 content: the consolidated 15-unit sequence** in the shared review, with targets summing to 58 minutes (MC/TD segment 53 against the accepted 54; average reward 5), and with the R01–R17 dispositions and qualifications. The shared trajectory is (1,1) → (1,1) → (1,2) → goal under always-right (R01, R16). The instructor expects to add material during editing; the minute under the 59-minute allocation is buffer, not a target. The planning estimate in `decisions/topic_decisions.yaml` stays 59.
- D9. **First-render content authorized** (instructor, subsequent request, 2026-10-22): check Claude's responses and the recorded choices, raise any remaining consequential question, otherwise create the render-ready content. No unresolved 3.1 choice remained; the shared content implements D6–D8 and the review qualifications. This authorizes content preparation for 3.1, not preparation of the unstarted 3.2 portion or acceptance of a rendered deck. The 19-state example stays deferred to 3.2.

**Instructor, 2026-10-22 (after the first editing pass):**
- D10. **3.1 delivery target is 60 minutes, as saved (resolves O3).** The added two-minute recap stays and no minute is recovered elsewhere. This uses one minute of the delivery allowance up to 63 (decision log 2026-10-21), so D6's "3.1 does not use the delivery allowance" no longer holds. The planning allocation in `decisions/topic_decisions.yaml` stays 59; the nine-minute exercise and five-minute average-reward block are unchanged.

- D11. **Session 3.1 accepted for teaching** (instructor, 2026-10-22), after ChatGPT's last pass found no remaining issue. Accepted portion: slides 1–20 of SHA-256 `b1d2c2dec74ada2066b8a6134340c22e6a49688dbaf4b7dd0e505504c08b3be1`. A later substantive change to these slides reopens 3.1.

**Instructor, 2026-10-22 (3.2 choices Q1–Q3 after the mutual cross-review):**
- D12. **The 19-state α–n plot stays in 3.2 for now** (resolves R08/R13; Q1), at about 6 minutes (review R32). The instructor may change this later.
- D13. **One course-generated learning-curve figure in the evaluation block** (Q2), under ChatGPT's conditions (review R33–R35): it replaces part of the block's explanation within the protected ten minutes and serves the claims activity; one declared protocol for every plotted number; the band labelled as a pointwise 95% interval for the mean error; single runs chosen in advance; seeds, MC convention and interval method in the notes.
- D14. **Keep a single "when to prefer MC or TD" slide** as a reference students can remember and return to (instructor request). Sequence finalized by the AIs under D15 (2026-10-22, closes O4): place it at the end as C10, comparing MC, n-step and TD, for 3 minutes; C02 moves from 6 to 5 minutes to fund the extra minute.
- D16. **The generated figure gets its own time** (instructor, 2026-10-22; amends D13's "replaces part of the block" condition). The evaluation block becomes 12 minutes: about 2 for reading the figure (interval for the mean versus single runs; overlap at two episodes), and the ten protected minutes for the claims and the other checks unchanged. 3.2's slide targets become 60 minutes, using 2 minutes of the delivery allowance for worked reasoning, not new topics; the planning allocation in `decisions/topic_decisions.yaml` stays 58 (as D10 for 3.1). D13's other conditions stand.
- D15. **The consolidated sequence becomes the basis for 3.2's render-ready content once the AIs finalize it** (Q3): ChatGPT's response to R36–R37 and D14's placement first (O4).


**Instructor, 2026-10-22 (after sequence finalization):**
- D17. **Prepare the render-ready 3.2 addition while preserving accepted 3.1 and its frozen inputs.** ChatGPT prepared shared [`mc_td_returns_content.md`](../../course/lectures/week03/mc_td_returns_content.md): 21 new slides, targeting 60 minutes under D16, with the approved course-generated evaluation figure and reproducible data. This is a separate addition specification for the existing combined deck, following the Bellman 2.2 precedent; freeze it at the addition's first render. The figure assets are explicitly shared for rendering. Claude appends the new slides without rebuilding or modifying accepted 3.1. No scope, planning allocation, notation, assessment or workload change; this is content authorization, not acceptance of rendered 3.2 slides.


**Instructor, 2026-10-27 (after ChatGPT's review and appendix clarification):**
- D18. **Accept the revised 3.2 sequence for the next Claude edit/render** (resolves O5 and Q4/Q6/Q7). Authority: the instructor asks to update the relevant documents for rendering after confirming which comparison slides move to appendices. The checked current deck is still `d73b654747cbe83f39e94278a2a1d1a6c7a947d22f769d6380094f03305bfffe`; the review used its matching generated text and source evidence, not the frozen first-render inputs or stale preview.
  - Keep MT15–MT23 unchanged (41 minutes); keep MT23a's 19-state n-step plot live at 3 minutes, with its discussion continuing into the new mixture motivation.
  - Add **three forward-λ introduction slides, 7 minutes (2 + 3 + 2)**: mixing motivation, finite-episode weights/endpoints, and the fixed-snapshot grid result 0.03625. Correctness safeguards R38–R39 apply. Backward view is an existence mention only; no derivation or implementation is added here.
  - Replace MT24–MT24c's twelve live minutes with **two shorter evaluation slides, 6 minutes (4 + 2)**. Preserve the generated figure, a scoped comparison/vote, and a short question on tuning versus final evaluation and interaction/compute budgets. Move the four existing MT24–MT24c slides unchanged to an optional appendix. The additional λ-versus-n-step performance plot (book Figure 12.3, proposed L4) belongs in that appendix too; it has no live allocation or required-reading status.
  - Keep MT25's **MC/TD/n-step reference table live** for 3 minutes. Add one short λ-mixture line and update the Week 8 pointer; do not add another table column. Targets remain **60 minutes**: 41 + 3 + 7 + 6 + 3. This supersedes D6/D13/D16's ten protected evaluation minutes and D12's approximately six-minute n-step experiment block (now five, with continued motivation in the λ block). The nine-minute n-step exercise and Examples 6.2/6.4 remain intact. The 58-minute planning allocation and 3.1 acceptance are unchanged.
  - **Week 8 keeps its current 18-minute mixture segment and 59-minute session allocation.** Earlier exposure supports retrieval and the advantage/GAE connection; no ten-minute saving or replacement topic is assumed. The early placement is explicitly mapped in `topic_decisions.yaml` without importing the whole policy-method group into 3.2.
  - **Assessment:** A1 and existing assessment requirements remain unchanged. This approval prepares teaching content; it does not impose a new Midterm 1 λ requirement. Q5 remains O6 below and does not block rendering. No new video or required reading.
  - Edit the saved PPTX directly after backing it up; preserve accepted 3.1 and all instructor edits. Both sessions' first-render content/YAML inputs remain frozen. The shared review's “Accepted revision: renderer handoff” specifies the additions and safeguards. Acceptance of these edits is not acceptance of the eventual rendered deck.

**Instructor, 2026-10-27 (deck acceptance):**
- D19. **Deck accepted as done** (instructor, 2026-10-27): sessions 3.1 and 3.2, SHA-256 `b4ca75d4317a629ca7941888759a70ca926aae93d2c96baadde10e46f1ef72ba`, 50 slides, after the instructor edit round with Claude's notes check (shared review, "Instructor edit round after D18"). It includes the instructor's optional slides 43–44 (no live time) and supersedes D11's 3.1-only acceptance; 3.1's only change since D11 is one MT12 notes sentence. ChatGPT did not check this last edit round before acceptance. O6 stays open and does not block the deck.

## Next-offering note (instructor, 2026-11-03)

- State the convergence behaviour of MC/TD prediction: coverage, step-size conditions and constant-α fluctuation.
  This is groundwork for Week 4's control convergence conditions and the Week 5 deadly triad. The authoritative note
  is on the `mc_td` session in `decisions/topic_decisions.yaml`. The Fall 2026 deck stays done (D19); this is not a
  change to it.

## Open

| # | Item | Where discussed |
| --- | --- | --- |
| — | O6 resolved (instructor, 2026-11-02): one short written or true/false question at the 3.2 introductory forward-λ scope. No derivation or trace requirement. | `decisions/grading_decisions.md`, `midterm_1.return_mixtures`; November 2 decision log |
| — | O5 and Q4/Q6/Q7 resolved by D18, 2026-10-27. | Shared review, accepted revision handoff |
| — | O4 resolved under D15 (2026-10-22): both AIs agree on the sequence and D14 placement; targets sum to 60 minutes under D16. No open choice before 3.2 content preparation. | Shared review, ChatGPT response check and sequence finalization |
| — | O1 resolved by D6, O2 by D7, O3 by D10 (2026-10-22); R08/R13 resolved by D12. | [Shared review](../../analysis/lecture_suggestions/mc_td_review.md) |
