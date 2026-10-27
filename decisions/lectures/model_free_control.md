# Deck decisions: model-free control (sessions 4.1–4.2)

**Shared** deck decision file (`docs/lecture_workflow.md`). It holds outcomes only. Discussion and findings are in the
[shared review](../../analysis/lecture_suggestions/model_free_control_review.md). The initial suggestions are now
historical inputs:
- [Claude](../../analysis/lecture_suggestions/model_free_control_claude.md), renamed from `control_targets_claude.md`
  after D1 with its content unchanged;
- [ChatGPT](../../analysis/lecture_suggestions/model_free_control_chatgpt.md).

**Scope:** sessions 4.1 `control_targets` (Exploratory control and target policies) and 4.2 `control_practice`
(Control failure modes and project formulation). Accepted teaching allocations, scope and mastery live in
`decisions/topic_decisions.yaml`.

**Status: step 3 done** (instructor choices recorded, 2026-10-27). Next is step 4, the first-render content
`course/lectures/week04/model_free_control_content.md`. This is the deck's only current status record; other files
point here.

## Accepted (instructor, 2026-10-27, after the mutual cross-review)

The instructor answered the five items in the shared review's "Status after this pass".

- **D1. One deck `model_free_control` for sessions 4.1 and 4.2**, as for Weeks 2 and 3 (`bellman` C1, `mc_td` D1).
  Files use `model_free_control`, e.g. `course/lectures/week04/model_free_control_claude.pptx`.

- **D2. Running examples: the AIs' joint recommendation.**
  - **4.1 uses the 2×2 grid** from the `bellman` deck (B03 model, γ = 0.5). It carries:
    - one Monte Carlo control cycle on the familiar episode;
    - the greedy lock-in question at (2,1), with B14's 0.116 versus 0.800;
    - the always-left policy, labelled ε = 0, showing that MC needs episodes to end (review R02, R19). It replaces the
      windy gridworld, which becomes optional;
    - the SARSA / Q-learning target exercise, with a new illustrative Q snapshot.
  - **4.2 uses book cliff walking** (Example 6.6) as a separate, explicitly introduced task.

- **D3. Project timing is outside this deck's planning** (instructor: "Ignore the project timing. I will handle it in
  another way."). The relation of 4.2 to the 1 November proposal deadline is not planned for (review R10, closed).
  - 4.2's accepted 15-minute project activity and its 5 administrative minutes stay as in the merged sequence.
  - The instructor notes that the A1 release might move to the following week and that the administrative minutes are
    enough to cover it. This is not recorded as a schedule or assignment change; `decisions/assignment_decisions.md` is
    unchanged.

- **D4. Show the two fixed-policy cliff route returns on the slide initially** (review R18). These are ε-greedy around
  the edge route ≈ −52 and around the top route ≈ −22, with the greedy edge route −13 for reference. Label them as
  fixed-policy expected returns. The full route policies, the reset convention and the best ε-soft value (−20.7) go in
  the notes. The instructor may remove the numbers while editing.

- **D5. The merged sequence is the basis for first-render content.** This is the review's "Consolidated sequence
  proposal" with every R01–R23 fix, as recorded in the response tables:
  - 4.1: 18 units, targets sum to 57.5 minutes;
  - 4.2: 11 teaching units summing to 53 minutes, plus 5 administrative minutes.

  The planning allocations in `decisions/topic_decisions.yaml` (58; 53 + 5) are unchanged, and the delivery allowance
  is not used. No scope, mastery, notation, assessment or reading change.

## Open

| # | Item | Where discussed |
| --- | --- | --- |
| — | None. R01–R23 are resolved between the AIs, and D1–D5 settle the instructor items. | [Shared review](../../analysis/lecture_suggestions/model_free_control_review.md) |

**Note for A1 preparation (not a deck decision):** use uniform random tie-breaking among maximizing actions in
ε-greedy selection, so that the starter code matches the lecture (review R03).
