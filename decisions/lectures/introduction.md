# Deck decisions: Introduction (and MDPs)

**Shared** deck decision file (`docs/lecture_workflow.md`). It holds outcomes only; the discussion is in `analysis/lecture_suggestions/introduction_*` and `intro_mdps_claude.md`.
- **Scope of this deck:** session 1.1 `formulate` (the pilot). Session 1.2 is a separate deck, settled by [MDP decisions B1](mdp_values.md).
- **Status: DONE (re-accepted 2026-10-07 after the wait-reward change, A14a; title slide restyled 2026-10-08, A21).**
  - Deck: `course/lectures/week01/introduction_claude.pptx`, SHA-256 `60b76c839f5b8dcbccc26aedd4ea2609b4af2f4adad98d8a9fa05f303247a7bb`. This identifies the accepted saved version; later substantive edits reopen the status.
  - Source: `course/lectures/week01/introduction_claude.yaml`, in sync; 4 slides are PowerPoint-only.
  - Previews: `output/lectures/week01/introduction_claude_preview.{png,pdf}`.
  - Text view: `output/lectures/week01/introduction_claude.md`.
- **Content:** the [shared proposal](../../course/lectures/week01/introduction_content.md) is frozen as the record of what was agreed before handoff; the PPTX is now the teaching authority. **Discussion:** [shared review](../../analysis/lecture_suggestions/introduction_review.md).

## Accepted (instructor)

**2026-10-06, first comments** (decision log entry "Instructor comments on the session 1.1 pilot"):
- A1. The 1.1 working example is the **recycling robot** (Sutton & Barto, Example 3.3). Gridworlds come later.
- A2. Interaction diagram: `sources/current_course/1 - Introduction.pptx`, **slide 42** (PPTX position, hidden slides counted).
- A3. The instructor reveals the robot progressively on an **empty slide**. No dedicated reveal slide or prescribed pair exercise.
- A4. The instructor generally agrees with both AIs' **cut suggestions**: broad prerequisite review, history, extended applications. This is not approval of every individual slide deletion.
- A5. **Learning vs planning:** a brief contrast, only if it fits the discussion naturally.

**2026-10-06, second comments (to Claude):**
- A6. **No symbols in 1.1.** S_t, A_t, R_{t+1} and O_t arrive in 1.2.
- A7. Include a **short** contrast of RL with other learning methods.
- A8. Include **learning from experience and exploration**, briefly.
  - Wording both AIs agree on: on a given trial the robot does not directly observe what the action it did not choose would have produced.
  - Exploration methods stay in Weeks 4 and 9.
- A9. Include **why RL matters**, with motivating examples:
  - earlier DeepMind work: **Go** and **plasma control for fusion**;
  - **one robotics** example;
  - **one LLM** example.

  Dated examples only; no state-of-the-art claims. Robotics and LLM selections are recorded in A11.
- A10. The CS224R **chatbot observation-vs-state** example is good; **keep it for 1.2**.

**2026-10-06, shared-proposal choices (to ChatGPT):**
- A11. Choose **legged locomotion / learning to walk** and **ChatGPT / learning from human feedback** for the remaining motivation examples. The shared draft uses ANYmal (2019) and the historical ChatGPT training account (2022). Resolves O1.
- A12. Include a **compact recycling-robot formulation reference in the appendix**. Preserve the empty live discussion canvas. Resolves O2; this accepts placement, not every proposed detail or the separate project checklist (O8).

**2026-10-07, deck edits and handoff (instructor):**
- A13. **Structure as handed off (16 slides).** Title; brainstorm (AI and intelligence); decision making; robot video (instructor's own); Atari video (DeepMind, pre-Google); why-RL examples; RL vs other learning methods; agent and environment; robot discussion (with prompts instead of an empty canvas; amends A3); reward and return; learning from experience; observation and state (merged into one slide); formulating a decision problem; robot formulation with figure; summary table; why RL is different.
- A14. **Robot model (book's rescue model with numbers).**
  - At high, a search stays high with 0.8, otherwise low.
  - At low, a search stays low with 0.7, otherwise the battery runs out and the robot is rescued and recharged to high.
  - Rewards: **every search +2** (the book's reasoning), **wait 0** (changed from +1 on 2026-10-07, see below), recharge 0, rescue −3.
  - The figure is drawn natively in PowerPoint by the instructor, with no symbols. Resolves O3; satisfies A6. The notation-guide item O11 is handled by using numbers on slides (the guide itself is unchanged).
- A14a. **Wait reward 0** (instructor, 2026-10-07; amends A14). With wait +1 and γ = 0.5, waiting at low becomes optimal (low: wait 2.0 vs recharge 1.83 vs search 1.75), which undermines the example. The book's +1 (someone brings a can) is ignored. With wait 0, the optimal policy is search when high, recharge when low (high: search 3.64 vs wait 1.82; low: recharge 1.82, search 1.68, wait 0.91), the deck's second example strategy. The instructor edits the PPTX; this re-opens the deck's done status until the edited version is pulled back and its fingerprint recorded.
- A15. **Other versions of the model:** if time allows, draw them on the figure: a "rescued" state with a probability-1 transition to high, and an "out of battery" terminal state (e.g. −10) instead of the rescue. If not, state them verbally. Conditional on timing.
- A16. **No reward-table slide.** The robot formulation slide shows two example transition sequences (always search; search when high and recharge when low) and asks "Returns?" and "Which strategy is better?". The intended answer is in its notes. Resolves O4 in this form.
- A17. **Summary table is a live 0.5-minute slide** (replaces the appendix of A12). Rows: Decisions, State, Model, Reward, Objective, Horizon (continuing).
- A18. **"Why is RL different?"** says "Can work with only a critic (reward) and no teacher (label)". Resolves O7. The observation/state question (O5) and the vacuum backup in the summary notes (O6) are kept as handed off.
- A20. **"Why is RL different?", first bullet** (instructor, 2026-10-07): "Learns from **evaluative** feedback (rewards: how good was what I did?), not only **instructive** feedback (labels: what should I have done?)", with the sub-bullet "and can also use a teacher when available, e.g. human game records (AlphaGo) or human comparisons (ChatGPT)". This uses the book's evaluative/instructive distinction (Ch. 2) and avoids "critic", which means a learned value function in actor-critic methods (Weeks 7–8). Replaces the A18 wording.
- A19. **Time:** the slides total **42.5 minutes** (robot formulation 9). This is now the session's accepted teaching time in `decisions/topic_decisions.yaml` (2026-10-07; was 38), with a recorded 3-minute overrun of the 39.5 usable minutes. The Week 1 spill-over is managed in delivery and not carried into later planning.
- A21. **Title slide format** (instructor, 2026-10-08; style edit). Slide 1 uses the template's Title Slide layout: "COMP438/538 Reinforcement Learning", then centred 36 pt lines with the deck topic in bold ("Introduction"), "Barış Akgün" and "Fall 2026"; no image or tagline. Later decks use the same format (builder kind `course_title`). The slide keeps a **0.5-minute** target with notes written for this deck, so the slides total **42 minutes** within the unchanged 42.5-minute allocation (A19). Slide 15 (summary table) was restyled with its text unchanged.

## Open

Unless marked otherwise, these are both AIs' recommendations and are not yet accepted. Where they are discussed:
- `introduction_review.md` (current shared review);
- `introduction_review_chatgpt.md` (including its addenda);
- `introduction_round2_claude.md`.

| # | Item | Current recommendation |
| --- | --- | --- |
| ~~O3~~ | RESOLVED by A14. Illustrative rewards: successful search 2, wait 1, rescue −3 (the −3 is the book's) | Both AIs agree: keep them, labelled as illustrative. No transition probabilities in 1.1. |
| ~~O4~~ | RESOLVED by A16. Reward-vs-return check | Both AIs agree: label the sampled table "first four steps: cumulative reward so far". Ask whether one day settles which behaviour is better; it does not. A low-battery search gives +2 or −3 on that transition. The real immediate-vs-later tradeoff is high-charge search (2) vs wait (1). |
| ~~O5~~ | RESOLVED: kept as handed off (A18). Observation vs state | Both AIs agree: verbal question only: "you just collected two cans: is the battery high or low; what earlier events would help?" Choice between search and wait only. No claim that a particular summary of the history is sufficient. |
| ~~O6~~ | RESOLVED: backup in the summary notes (A18). Vacuum reward-design question | Both AIs agree: backup only. |
| ~~O7~~ | RESOLVED by A18. Intro slide 51 ("Why is RL different?") | Both AIs agree: edit so it does not state "no teacher/labels" as universal. Reward evaluates an outcome without saying which action was correct. Overlaps A7. |
| ~~O8~~ | RESOLVED (instructor, 2026-10-07): not in the deck; it goes in the project-proposal instructions, possibly with a short proposal presentation. Formulation checklist (for the Week 4 project proposal) | Claude's proposal; remains open. A12 accepts the robot reference appendix, not this separate checklist. Shared draft keeps checklist prompts in speaker notes only. |
| ~~O9~~ | MOVED to `decisions/lectures/mdp_values.md` (1.2 is a separate deck, B1). 1.2 (if in this deck): return objective for the continuing robot plus a brief episodic contrast; the terminal-state variant (A15) if it is drawn in 1.1; notation item O10 (history) in the guide | Deferred to 1.2. 1.2 should reuse the A14 numbers. |
