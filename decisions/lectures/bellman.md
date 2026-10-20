# Deck decisions: Bellman equations and dynamic programming (sessions 2.1–2.2)

**Shared** deck decision file (`docs/lecture_workflow.md`). It holds outcomes only; discussion and findings are in the [shared review](../../analysis/lecture_suggestions/bellman_review.md). The initial 2.1 AI suggestions ([Claude](../../analysis/lecture_suggestions/bellman_claude.md), [ChatGPT](../../analysis/lecture_suggestions/bellman_chatgpt.md)) are historical inputs; ChatGPT's dated 2.2 section is a new step-1 proposal.
- **Scope:** sessions 2.1 `bellman` and 2.2 `improvement`. Accepted teaching allocations, scope and mastery live in `decisions/topic_decisions.yaml`.
- **Status: DONE** (accepted by the instructor, 2026-10-20, C25). This is the deck's only current status record; other files point here.
  - Deck: `course/lectures/week02/bellman_claude.pptx`, SHA-256 `ec28bf43c37e2b7f37fa8e18e3f400414a0aaaeea91645923e847ea9561d20db`, 39 slides (2.1: B00–B16 with B00a, B00b, B05a, B05b; 2.2: B17–B28 with B21r, B24r, B24a, B25a; appendix BA1, visible, 0 minutes). Later substantive edits reopen the status.
  - Timing: slide targets 61 minutes for 2.1 (C15) and 59.5 for 2.2 (C24); planning estimates in `decisions/topic_decisions.yaml` stay 60 and 58.
  - Views: text view `output/lectures/week02/bellman_claude.md`; previews `output/lectures/week02/bellman_claude_preview.{png,pdf}` (39 pages), from this deck.
  - History: findings R01–R49 in the [shared review](../../analysis/lecture_suggestions/bellman_review.md); the first-render inputs (`bellman_content.md`, `bellman_claude.yaml`, `bellman_improvement_content.md`, `bellman_improvement_claude.yaml`, `bellman_additions_claude.yaml`) are frozen and must not be used to rebuild the deck.

## Accepted (instructor, 2026-10-09)

These are the instructor's answers to Claude's step-1 questions Q1–Q6.
- C1. **One deck `bellman` for sessions 2.1 and 2.2**, separate from the Week 1 decks. Files use `bellman`: `course/lectures/week02/bellman_claude.pptx`, among others.
- C2. **The running example moves to the grid.** This gives another pass on MDPs. The recycling robot is no longer the worked example for this deck. C7 resolves the grid choice.
- C3. **The Bellman optimality equation is presented in 2.1**, positioned towards the end. The initial fallback was to move it to 2.2 if timing was short; C9 now retains it in the longer first draft for the instructor to cut after reviewing the whole content.
- C4. **Matrix form: the instructor derives it live on the tablet.** Students are assumed familiar with matrix operations. The slides need no typed matrix notation. If matrix symbols are later typed on slides, the notation guide needs an entry first.
- C5. **The one-line convergence argument stays in the first draft.** Each sweep multiplies the largest error by at most γ. The instructor may remove it while editing.
- C6. **Notation: V_k(s) is the estimate after k sweeps** of a dynamic-programming method, stated once when introduced. Recorded in `course/notation_guide.md`.
- C7. **Grid selection (G1 resolved):** retain the 3×4 grid for the MDP introduction and use the simplified 2×2 grid for the calculations. The smaller map is a separate MDP sharing the movement rules, not an equivalent state reduction of the larger one.
- C8. **Rewards on entry (G2 resolved):** pay the terminal reward on entering the terminal cell, then zero continuation. In the 3×4 illustration this includes both +1 and −1 terminal outcomes; the 2×2 has the +1 goal only. The terminal payoff is the total entry reward, not an additional living reward. Other transitions retain the proposed −0.04 for the 2.1 example. Recalculate or clearly adapt old values/policy illustrations rather than carrying their old terminal-boundary convention into this deck.
- C9. **Longer 2.1 first draft authorized:** keep the optimality equations near the end of 2.1. The instructor will cut while reviewing the entire content if needed. Implement this with the already proposed approximately 60-minute consolidated sequence, rather than the compressed 58-minute alternative; synchronize the session planning estimate accordingly. This uses 0.5 minute beyond 59.5 usable and leaves 10 physical minutes. It is not a new numerical ceiling or a target to expand further. No earlier-session carryover. The 2.2 allocation stays 58 minutes and must not count the same optimality introduction twice.
- C10. **First-render content authorized:** consolidate the cross-reviewed 2.1 material in the shared `course/lectures/week02/bellman_content.md`, including the accepted tablet derivation, convergence argument and review corrections. No separate text-proposal review loop. Claude renders the first PPTX; the content becomes historical at first render under pilot v2. This does not authorize inventing the unprepared 2.2 portion or mark the combined deck done.

**Instructor, 2026-10-11 (comments on the first edited version):**
- C11. **Superscript notation** for policy and optimality marks: v^π, q^π, v^\*, q^\*, π^\*, B^π (notation guide updated). Applied to this deck and to the accepted 1.2 deck ([MDP B17](mdp_values.md)); the instructor announces the switch in class.
- C12. **Equation colour:** native equations use the theme colour Accent 5 (#4472C4) in 1.2, 2.1 and later decks; earlier decks are not changed. The builder defaults to it.
- C13. **Matrix form (amends C4):** the instructor still derives the matrix form live, with notation only; computing the exact values is an optional home exercise. No typed matrix notation is required on slides.
- C14. **Bellman operator definition** added to B13 (slide 19), so the operator is described rather than only shown.
- C15. **2.1 portion settled for teaching** (instructor, 2026-10-11): the 61-minute slide targets are fine for delivery; the planning estimate in `decisions/topic_decisions.yaml` stays 60 (as with 1.2's targets against its estimate). Slide wording stays as it is (R24/R27 remain notes-only). Animations confirmed by the instructor. Final instructor edits: V₁ row as question marks on B10; π^\*(s) = argmax_a q^\*(s, a) added to B16 (notes updated).
- C16. **2.2 preparation instruction** (instructor, later 2026-10-11 request): start independent suggestions in this combined deck using the old course sources and latest saved PPTX for continuity. Preserve entry rewards, instructor edits, the improvement argument, grid VI/PI comparison and reward sensitivity; do not repeat 2.1's optimality introduction. Keep the 58-minute estimate. R24–R28 remain recorded for the next PPTX edit and are not to be silently marked resolved. Preserve the PPTX and frozen first-render inputs during this step. This changes the pending-review disposition, not the recorded implementation history or 2.1's readiness for teaching.

**Instructor, 2026-10-11 (answers to Claude's 2.2 questions):**
- C17. **Reward sensitivity uses γ = 0.9** on the 3×4 grid, with a sentence explaining the change from the deck's γ = 0.5 (later rewards count more, so the risk/delay trade-off shows). Entry rewards (C8) stay; the panels are recomputed.
- C18. **Improvement theorem: the book's repeated-expansion proof** (§4.2). ChatGPT's suggestion uses the same argument.
- C19. **Include a short Q-value-iteration bridge to Q-learning.** Notation Q_k(s, a), by analogy with V_k, added to the notation guide.
- C20. **Asynchronous DP: one line.**
- C21. **Initial 2.2 render-ready content authorized** (instructor, subsequent 2026-10-11 request): review Claude's latest suggestions, ask about outstanding issues, and otherwise create the initial content. Reciprocal review found no remaining consequential choice requiring instructor input. Consolidate C17–C20 and the agreed sequence, with the correctness qualifications in R37–R40; keep the 58-minute estimate (57.5-minute slide targets). Because the original 2.1 content is frozen, put the new portion in shared `course/lectures/week02/bellman_improvement_content.md`, solely for appending to this deck after B16; freeze it at that portion's first render. This authorizes content preparation, not overwriting existing slides, closing R24–R28 or accepting the rendered deck.

**Instructor, 2026-10-20 (edit round on 2.2):**
- C22. **Additions requested:** a hidden appendix slide BA1 with the deterministic-policy forms of the evaluation and improvement updates and their ℛ(s, a, s′) forms (0 minutes), and a slide B25a after B25 on when to choose policy iteration or value iteration (2 minutes). 2.2's targets now sum to 59.5 minutes against the 58-minute estimate (the 59.5 usable minutes); the estimate is not changed by this record.
- C23. **BA1 stays visible with a 0-minute target** (instructor, 2026-10-20). The instructor kept the deterministic-policy heading over the value-iteration forms and the closing line giving the policy-evaluation form.
- C24. **2.2 portion settled for teaching** (instructor, 2026-10-20): the 59.5-minute slide targets are fine for delivery; the planning estimate in `decisions/topic_decisions.yaml` stays 58 (as in C15). The notes-level fixes for R24–R28 are kept and the items are closed (ends the C16 checkpoint). All open issues are answered.
- C25. **Deck accepted as done** (instructor, 2026-10-20) after both AIs' final checks; the instructor confirmed the animations in slideshow mode.

## Open

None.
