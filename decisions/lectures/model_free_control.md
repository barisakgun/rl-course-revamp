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

**Status: DONE** (accepted by the instructor, 2026-11-02, D9). This is the deck's only current status record; other
files point here. A later substantive change reopens the status.
- **Deck:** `course/lectures/week04/model_free_control_claude.pptx`, SHA-256
  `af4fc62455721d19427252635d870ba29dcd6b049d91a582be6d15717eed78e6`, 36 slides (P11 hidden). It is the
  instructor's saved edits (`15d45f04…`, then `cb46e392…`) plus Claude's changes:
  - C14 text and notes;
  - C12a inserted;
  - equation fallbacks refreshed;
  - the instructor-added slide 3 named C01a, with a short note and a 2-minute target (D8);
  - review fixes R24 (C09 picture labels and caption) and R25 (C12a γ = 1);
  - C11's notes reminder about the on-/off-policy definitions (instructor request, 2026-11-02).
- **Sessions:**
  - 4.1 = slides 1–22 (C00–C17, with C01a, C12a, C13a and C15a). Targets are 61.5 minutes (D7, D8).
  - 4.2 = slides 23–36 (P00–P11). 53 teaching minutes; P11 is hidden and carries the 5 administrative minutes. For
    Fall 2026 delivery only, see the delivery note below.

  The PPTX is the teaching source.
- **Views:** text view `output/lectures/week04/model_free_control_claude.md` and previews
  `output/lectures/week04/model_free_control_claude_preview.{png,pdf}` (35 visible slides; hidden P11 omitted), all
  from this deck.
- **First-render inputs, all frozen:**
  - the shared [content](../../course/lectures/week04/model_free_control_content.md) (prepared by ChatGPT in step 4);
  - `model_free_control_claude.yaml` (4.1);
  - `model_free_control_practice_claude.yaml` (4.2, appended after C17).

  Render notes are in the [shared review](../../analysis/lecture_suggestions/model_free_control_review.md).
- **Review:** ChatGPT's targeted recheck on 2026-11-02 closes R24–R26 and confirms C11's notes reminder in this saved version. No outstanding finding from that pass. The instructor's editing round continues; the final complete check and acceptance are still pending.

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

## Accepted (instructor, 2026-11-02, during the first editing round)

- **D6. On-policy versus off-policy is taught through SARSA and Q-learning; importance sampling stays out of Week 4.**
  The instructor asked to "talk about on-policy and off-policy for week 4 in the context of SARSA and Q-Learning but
  leave the IS out for now".
  - **C14:** remove the "Why no importance ratio in this one-step Q-learning target?" question and its answer, and the
    notes' ratio remarks. Spend the 2 minutes on what on-policy (SARSA) and off-policy (Q-learning) mean in terms of
    behaviour and target.
  - **Notes elsewhere:** keep importance sampling out of the spoken material too.
  - **Scope:** this agrees with accepted scope. Importance sampling stays in 8.2 `ratios`, as in
    `decisions/topic_decisions.yaml`. No allocation, mastery or assessment change.
  - **Refinement (instructor, 2026-11-02):** importance sampling was never introduced, so removing it loses nothing.
    - The removed question, "Why no importance ratio in this one-step Q-learning target?", is asked in Week 8 (8.2
      `ratios`) instead. That forward note is in that session's `feasibility_note` in `decisions/topic_decisions.yaml`.
    - C14 gains a one-line disclaimer that off-policy corrections come later in the course.
  - **Applied by Claude** to the instructor-saved deck (2026-11-02, after a backup).

- **D7. Add the "comparison of SARSA variants" figure, linking to multi-step updates, without algorithm coverage**
  (instructor, 2026-11-02).
  - **New slide C12a,** after C12: old P31's picture, book Figure 7.4 plus the Sarsa(λ) panel of Example 12.1
    (one-step, 10-step and λ = 0.9). It links back to Week 3's n-step and λ-return targets, with Q in place of V.
  - **Scope:** no n-step SARSA or Sarsa(λ) algorithm, implementation or assessment. The λ panel's trace computation is
    an existence mention only (accepted `backward_trace_mention`).
  - **Timing:** C12a targets 2 minutes. C14 stays at 2. 4.1's slide targets become 59.5 minutes, within the delivery
    allowance up to 63 (fine for delivery; planning estimate unchanged at 58). The instructor-added slide 3 is not
    counted yet; see Open.

## Accepted (instructor, 2026-11-02, editing round)

- **D8. C01a "Why Model-Free Control?" gets 2 minutes and a short note** (closes O2). The instructor says the slide is
  self-explanatory, so the note stays brief, and exceeding the regular duration is fine.
  - 4.1's slide targets become 61.5 minutes, within the delivery allowance up to 63 (fine for delivery; planning
    estimate unchanged at 58; about 8.5 physical minutes of buffer remain).
  - No scope, mastery or assessment change.

## Accepted (instructor, 2026-11-02, deck acceptance)

- **D9. Deck accepted as done** (instructor: "if there are no open issues, close week 4").
  - Accepted deck: SHA-256 `af4fc62455721d19427252635d870ba29dcd6b049d91a582be6d15717eed78e6`, 36 slides, P11
    hidden.
  - Checks before acceptance:
    - ChatGPT's content and error check of the instructor-saved deck (R24–R26), and its recheck of the fixes, with no
      open finding;
    - Claude's fresh PowerPoint render of all 35 visible slides;
    - equation fallbacks refreshed after the last equation changes. The later edits were text, notes and labels
      only.
  - Slide targets: 4.1 61.5 minutes (D7, D8, within the delivery allowance); 4.2 53 teaching + 5 administrative
    minutes. The planning allocations in `decisions/topic_decisions.yaml` stay 58 and 53 + 5.
  - Not exercised: click order and live slideshow playback (instructor, in slideshow mode).

## Fall 2026 delivery note (instructor, 2026-11-02; this semester only, not a design change)

- There is no live class on 3 November (instructor unavailable, as already listed in `decisions/schedule_decisions.yaml`).
  The instructor records the lecture as a video and shares it with the class. A recording may run shorter than the
  slide targets.
- The P09/P09a project activity (baseline, metric and budget) is done by students at home this semester. The slide
  note "Note for Fall26: Do this at home by yourself" on P09a marks this.
- **The design is unchanged for future offerings.** The activity stays in class with its protected 15 minutes, and
  the deck keeps its structure and slide targets. Accepted scope, allocations, the `control_practice` worked activity
  and D1–D7 do not change. Do not re-time the deck for this semester's recording.

## Open

| # | Item | Where discussed |
| --- | --- | --- |
| — | R24–R26 resolved: C09/C12a corrections, C11 notes reminder and matching review-view fingerprint rechecked by ChatGPT, 2026-11-02. No new scope or timing choice. | [Shared review](../../analysis/lecture_suggestions/model_free_control_review.md#chatgpt-content-and-error-check--2026-11-02) |
| — | O1 resolved 2026-11-02: P09a's at-home note is a Fall 2026 delivery note only (see above). The design and the 15 protected minutes are unchanged. | Fall 2026 delivery note |
| — | O2 resolved by D8 (2026-11-02): C01a has 2 minutes and a short note. | D8 |
| — | R01–R23 are resolved between the AIs; D1–D7 settle the earlier instructor items. | [Shared review](../../analysis/lecture_suggestions/model_free_control_review.md) |

**Note for A1 preparation (not a deck decision):** use uniform random tie-breaking among maximizing actions in
ε-greedy selection, so that the starter code matches the lecture (review R03).
