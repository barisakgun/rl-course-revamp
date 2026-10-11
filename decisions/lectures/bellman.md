# Deck decisions: Bellman equations and dynamic programming (sessions 2.1–2.2)

**Shared** deck decision file (`docs/lecture_workflow.md`). It holds outcomes only; discussion and findings are in the [shared review](../../analysis/lecture_suggestions/bellman_review.md). The initial AI suggestions ([Claude](../../analysis/lecture_suggestions/bellman_claude.md), [ChatGPT](../../analysis/lecture_suggestions/bellman_chatgpt.md)) are historical inputs.
- **Scope:** sessions 2.1 `bellman` and 2.2 `improvement`. Accepted teaching allocations, scope and mastery live in `decisions/topic_decisions.yaml`.
- **Status: 2.1 portion ready for teaching after the final short check (2026-10-11); 2.2 not started.** Current saved deck `course/lectures/week02/bellman_claude.pptx`, SHA-256 `841adc8ef562a67b3be29862ac88a82686e2d2324a78ba67195906803c984988`: 22 slides (B00–B16 plus B00a, B00b, B05a, B05b), targets summing to 61 minutes against the 60-minute estimate (C9; not re-recorded). Review findings R01–R28 are resolved. The first-render content and YAML are frozen. Views: `output/lectures/week02/bellman_claude.md` and `bellman_claude_preview.{png,pdf}`. Session 2.2 continues in this deck (C1); the combined deck is not done or accepted. This is the deck's only current status record; other files point here.

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

## Open

| # | Item | Where discussed |
| --- | --- | --- |
| — | Initial content suggestions for session 2.2 | not started |

No substantive 2.1 choice remains open. G1/G2 and the longer sequence are resolved by C7–C10; the shared review tracks implementation and later rendering checks.
