# Deck decisions: model-free prediction (sessions 3.1–3.2)

**Shared** deck decision file (`docs/lecture_workflow.md`). It holds outcomes only; discussion and findings will be in the shared review `analysis/lecture_suggestions/mc_td_review.md`.
- **Scope:** sessions 3.1 `mc_td` (Sampling, MC/TD and continuing objectives) and 3.2 `returns` (Bias, variance and n-step targets). Accepted teaching allocations, scope and mastery live in `decisions/topic_decisions.yaml`.
- **Status: session 3.1 accepted for teaching (instructor, 2026-10-22, D11); session 3.2 not started.** Accepted 3.1 deck: `course/lectures/week03/mc_td_claude.pptx`, SHA-256 `b1d2c2dec74ada2066b8a6134340c22e6a49688dbaf4b7dd0e505504c08b3be1`, 20 slides (MT00–MT14 plus the recap), slide targets 60 minutes (D10). Text view and previews in `output/lectures/week03/` come from this deck. The deck is not done: 3.2 is still to be added, and the combined deck needs its own acceptance (workflow step 8); acceptance of 3.1 is not inherited by later changes. Findings: [shared review](../../analysis/lecture_suggestions/mc_td_review.md) (R01–R27, all resolved or closed). The shared input [`mc_td_content.md`](../../course/lectures/week03/mc_td_content.md) and Claude's renderer YAML `course/lectures/week03/mc_td_claude.yaml` stay frozen. Suggestions: [Claude](../../analysis/lecture_suggestions/mc_td_claude.md), [ChatGPT](../../analysis/lecture_suggestions/mc_td_chatgpt.md). This is the deck's only current status record; other files point here.

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

## Open

| # | Item | Where discussed |
| --- | --- | --- |
| — | O1 resolved by D6, O2 by D7, O3 by D10 (2026-10-22). Deferred to 3.2: keeping the 19-state n-step plot (review R08/R13). | [Shared review](../../analysis/lecture_suggestions/mc_td_review.md) |
