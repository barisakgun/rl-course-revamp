# Deck decisions: deep Q-learning (sessions 6.1–6.2)

**Shared** deck decision file (`docs/lecture_workflow.md`). It holds outcomes only. Discussion and findings are in the
[shared review](../../analysis/lecture_suggestions/deep_q_learning_review.md). The initial suggestions are historical
inputs:
- [Claude](../../analysis/lecture_suggestions/deep_q_learning_claude.md);
- [ChatGPT](../../analysis/lecture_suggestions/deep_q_learning_chatgpt.md).

**Scope:** sessions 6.1 `dqn_loop` (DQN as approximate Q-learning) and 6.2 `dqn_diagnosis` (Double estimators and
experimental diagnosis). Accepted teaching allocations, scope and mastery live in `decisions/topic_decisions.yaml`.

**Status: DONE** (accepted by the instructor, 2026-11-19, D18). A later substantive change reopens the status. This is the
deck's only current status record; other files point here.
- **Deck:** `course/lectures/week06/deep_q_learning_claude.pptx`, SHA-256 `1ec0df827bae…`, 46 slides, 39 visible (6.2 ends with the instructor's D13a; H01–H03 visible for the PDF, not taught) (three instructor-added 6.1 slides and the V11-B-home study slide outside the timing).
  - **6.1** = slides 1–24 (V00–V14, including the timed V00a; V03-B and V09–V11-A hidden): timed slides sum to 57
    minutes (D10, D13). Instructor-added slides 2, 3 and 14 have no time targets; V11-B-home is home study (0 minutes).
  - **6.2** = slides 25–43 (D00, D06-A and D07-A hidden; live route ends at D13a): timed route 58 minutes (D17).
    H01–H03 are slides 44–46, visible for the PDF and not taught (0 minutes).
- **Text view:** `output/lectures/week06/deep_q_learning_claude.md` (regenerated from `1ec0df827bae…`). Equation fallback pictures refreshed 2026-11-19 (36 boxes); preview
  `output/lectures/week06/deep_q_learning_claude_preview.png`; round-1 findings, fixes and latest cross-review are in the shared review (K05–K43).
- **First-render inputs, frozen:** the shared [content](../../course/lectures/week06/deep_q_learning_content.md);
  `deep_q_learning_claude.yaml` (6.1) and `deep_q_learning_diagnosis_claude.yaml` (6.2, appended after V14). Render
  notes are in the shared review. Round-1 inserts: `deep_q_learning_v11b_claude.yaml` (V11-B, V11-B-home) and
  `deep_q_learning_d05a_claude.yaml` (D05a); not maintained.

## Accepted (instructor, 2026-11-16, after the mutual cross-review)

The instructor answered the open-decision list at the end of the shared review.

- **D1. One deck `deep_q_learning` for sessions 6.1 and 6.2**, with a visible session divider, as in Weeks 2–5. Files
  use `deep_q_learning`, e.g. `course/lectures/week06/deep_q_learning_claude.pptx`.

- **D2. Worked example: both routes go into the deck, marked as alternates.** The instructor chooses while going over
  the deck. Only one alternate counts toward the slide targets.
  - **Alternate A, ChatGPT's two-row minibatch, reused in both sessions** (ChatGPT slides 7–9 and 11–15), with the
    additions of review finding C01: the trace declares that only the two output biases are trainable, and shows
    three reveals (the successor's online outputs move from (4, 2) to (4.1, 1.95); the label from online weights would
    move from 3 to 3.05; the target-network label stays at 4 until the copy). C06 (reward range) applies.
  - **Alternate B, Claude's corridor in 6.1** (Claude A12–A13), shortened as in review R02: both output tables and the
    left-head update are supplied; students compute the right-head update and transition 4's target before and after
    the copy; the goal is encoded as position 4 with its target outputs given (L 0.40, R 0.50). 6.2 then uses its own
    table (Claude B05–B07, as revised by R03–R04).
  - Each alternate covers the accepted 6.1 worked activity (replay, target construction, parameter update in one loop)
    and keeps the 6.2 blocks at 20 and 15 minutes.

- **D3. Target-network demonstration on the Week 5 example is added** (Claude A08–A09; review C02). The I02 fragment
  (v̂ = (w, 2w), reward 0, γ = 0.9, α = 0.1, w = 10) is replayed five times: with a label that moves, w goes
  10 → 10.8 → 11.664; with the label held at 18, w goes 10.8 → 11.52 → … → 13.28, and the copy then moves the label to
  23.9. Numbers: `scripts/check_deep_q_learning_claude.py` §2.

- **D4. Replay motivation: both versions go into the deck as alternates.** The instructor decides after seeing them.
  Only one counts toward the slide targets.
  - **Alternate A, pictures only** (ChatGPT slide 3: near-identical successive frames; revisiting a stored
    transition).
  - **Alternate B, the corrected mixing toy** (Claude A05 as fixed by review R01): one shared weight, four size-two
    updates from 0 with step size 0.5. Pairs AA, AA, BB, BB give 0.5, 0.75, −0.125, −0.5625; four AB pairs keep the
    weight at 0. Notes: the mixed pairs are deliberately balanced, and a uniform draw can be unbalanced.

- **D5. 6.2 opens with the Double DQN paper's Figure 3** (van Hasselt et al. 2016; review C03): value estimates
  ending above the measured discounted returns of the same agents. The instructor may change this choice while
  editing. The book's Example 6.7 figure stays inside the 20-minute block.

- **D6. Old slides 22 (tuning list) and 14 (Polyak averaging) become one 1-minute slide** (Claude A16). The lecture
  teaches the hard copy every C updates and the squared loss; Polyak averaging is one line on that slide.

- **D7. Methods not covered: one line in the speaker notes and a hidden appendix.**
  - Old slide 23's pointer (Rainbow and the other extensions) becomes one line in the notes of the closing slide.
  - A hidden appendix collects related methods the course does not cover, one short entry each with a paper link.
    Candidate list (links to be checked when the content file is written):
    - Neural fitted Q-iteration (Riedmiller 2005) and tree-based fitted Q-iteration (Ernst, Geurts and Wehenkel 2005,
      JMLR 6);
    - asynchronous one-step and n-step Q-learning (Mnih et al. 2016, arXiv 1602.01783), covering old slide 6;
    - prioritized experience replay (Schaul et al. 2016, arXiv 1511.05952), covering old slides 19–20;
    - dueling networks (Wang et al. 2016, arXiv 1511.06581), covering old slide 21;
    - multi-step targets in deep Q-learning (Hessel et al. 2018, as a component of Rainbow);
    - distributional DQN, C51 (Bellemare, Dabney and Munos 2017, arXiv 1707.06887);
    - noisy networks for exploration (Fortunato et al. 2018, arXiv 1706.10295);
    - Rainbow (Hessel et al. 2018, arXiv 1710.02298).
  - Appendix slides carry no minutes, no assessment and no required reading. They are not taught live.

- **D8. Ablation evidence: the published Atari replay × target-network table**, with Breakout and Seaquest worked live
  and the other games read (both proposals). If the slide attributes the numbers to Mnih et al. (2015), the cells and
  the reporting rule come from that paper's Extended Data Table 3, not from a course's rounded copy. ChatGPT takes the
  cells from the paper when writing the content file (the instructor reports more ChatGPT usage available). A
  course-generated small-task trace with per-seed curves is not made for Fall 2026.

- **D9. Notation, approved for now** (instructor may revise while editing). Recorded in `course/notation_guide.md`:
  - (s_j, a_j, r_j, s′_j) for a transition sampled from 𝒟, with j its position in the minibatch, and U_j its target;
  - L(**w**) for the minibatch TD loss;
  - C for the target-network copy period (hard copy every C updates);
  - Q₁, Q₂ for the two tables of tabular Double Q-learning (subscript = which table, stated on first use);
  - τ for the Polyak averaging rate, relying on context to separate it from the later IQL expectile (open item O5);
  - "minibatch", "done" (the terminal flag) and buffer capacity in words.

- **D10. Delivery allowance.** Slide targets may go up to 63 minutes in each session, with one alternate counted where
  D2 and D4 offer two. Planning allocations (55 + 55) are unchanged.

- **D11. Fact: Mnih et al. (2015) trained on 49 games** (instructor). Slides use the paper's denominator, not the
  book's "29 of the 46" (§16.5, printed p. 438).

- **D13. A 2-minute Week 5 recap slide V00a after the title** (instructor, 2026-11-16, review K01): G12b's control
  table with the nonlinear Q-learning ✗, and G14's three wishes, each labelled with the mechanism that answers it
  (network, replay, target copy). 6.1 slide targets become 57 minutes, within D10.

- **D14. Polyak averaging as a full alternative to the hard copy** (instructor edit in the saved deck, 2026-11-17;
  review K17). V07 shows both target updates with $\mathbf{w}^-\leftarrow\tau\mathbf{w}+(1-\tau)\mathbf{w}^-$, V08's step 5 and
  V12 name both, and an added pseudocode slide is titled "DQN Pseudocode with Polyak Averaging". This supersedes D6's
  "Polyak averaging is one line". Open consequence: which rule A2's target-network hook uses (A2 decision).

- **D15. V11-B revision and a study slide on per-transition updates** (instructor, 2026-11-17; review K19–K21).
  V11-B writes the left-head step in the same minibatch form as the right head ($\alpha=0.3$ divided by the 3 rows),
  states why the rise is surprising (row 2's own error would lower the prediction) and reveals the answer on the slide.
  A new slide V11-B-home after it is for study at home, outside the timing: one update per transition on rows 2 and 3
  only (the agent's last two transitions), $\alpha=0.1$ per update, weights after each update, the reversed order as a
  second question, and the comparison with the minibatch step. V11-B keeps its 6 minutes.

- **D16. 6.2 bias block reordered, summary slide, and a tables-to-networks slide** (instructor, 2026-11-17; review
  K22–K28). Worked example B in 6.2 as in 6.1 (D06-A, D07-A hidden); D00 hidden (instructor's choice; supersedes D1's
  visible divider for this deck). Order: D04 (Example 6.7, the puzzle), D03 (coin calculation, the cause), D01
  (Double DQN paper's Figure 3, the evidence with deep networks), D01a (the instructor's maximization-bias slide, as a
  summary, claims revised as agreed), D02, D05, new D05a "From two tables to two networks", D06-B, D07-B. Minutes:
  D01 4 → 3, D05 4 → 3, D06-B 4 → 3, D01a 2, D05a 2, D00 hidden (1 → 0); 6.2 stays 55. Supersedes D5's "6.2 opens
  with the Double DQN paper's Figure 3".

- **D17. 6.2 from D06-B on, instructor editing round 1** (instructor, 2026-11-18; review K31–K37).
  - D13a "Flexibility of Q-Learning" (instructor's slide) stays: a 3-minute overview of DQN extensions, exposure
    only, not in the exam. Supersedes D7's "one notes line and a hidden appendix" for the in-class part; logged in
    `decisions/decision_log.md` with the `topic_decisions.yaml` feasibility-note change. Corrections applied (K32);
    distributional RL is described as capturing the randomness of returns from the environment and the policy.
  - H01–H03 are visible so that they appear in the PDF; they are not taught (0 minutes).
  - D12 names each bug and its check, and gains a fifth row from D13's first exit question (3 → 4 minutes). D13
    keeps one question, continuous actions made explicit (3 → 2 minutes). Week 7 should state the other motivations
    for learning a policy directly (recorded in `analysis/phase7_brainstorming.md`).
  - D10's collapse example reworded with a link to Lipton et al. (arXiv 1611.01211).
  - 6.2 slide targets: 58 minutes (allocation 55, delivery allowance 63).

- **D18. Deck accepted as done** (instructor, 2026-11-19: "Accept the deck").
  - **Accepted deck:** SHA-256 `1ec0df827bae0d5c7c9ffb75291422d29bd7c1cd72a0b1586bd50a34da2d2b8b`, 46 slides (39
    visible). Includes the instructor's final V10-B edit (the unmasked goal row no longer assumes
    reward 1) with the question reworded to match its answer.
    - Hidden: D00.
    - Hidden alternatives: V03-B, V09-A, V10-A, V11-A, D06-A, D07-A.
    - Untimed: two recap slides and the DQN pseudocode slide (instructor-added), V11-B-home (home study), H01–H03
      (appendix, visible for the PDF, not taught).
  - **Slide targets:** 6.1 = 57 minutes and 6.2 = 58 minutes, within the 63-minute delivery allowance. The planning
    allocations (55 and 55) are unchanged; D17 records the 6.2 extensions slide.
  - **Open outside the deck:** which target-update rule (hard copy or Polyak averaging) A2's hook uses (D14; an A2
    decision).

- **D12. Next steps.** ChatGPT checks this record and writes the first-render content (step 4) if there are no glaring
  issues, carrying the resolved review findings (R01–R07, C01–C07) into it. Nothing in this record changes scope,
  mastery, assessment or allocations.
