# Midterm 1 exam decisions

Shared (instructor, Claude, ChatGPT). Git-ignored until the exam was held; committed afterwards at the instructor's request (2026-11-06, forced add, so the ignore rule stays in place for later exams). Workflow: `docs/exam_workflow.md`.

- **Status: FINAL (instructor, 2026-11-05, step 7), source SHA-256 `c8bf949d539ce6a84061fc69b54a176280cbd20424419daee5fad22fd6c324bd`.** X9, the instructor's text
  edits and X10 (Q1d, Q1e, Q3e and the Q3 intro) are applied and accepted. Any later change, including a correction
  announced during the exam, is recorded here. X6 (Q2 partial credit) stays open for grading; it does not change the
  exam text.
  Question numbers below follow the X9 order. Step 5 (ChatGPT, question-only, 2026-11-03) found no blocking
  question-side inconsistency; Claude compared it with the key and all answers agree; P02 (now Q4c) and P03 (now Q2d)
  were then added to the key at the instructor's request. ChatGPT traced the X9 figure on the X9 render and found it
  reproduces the old model. On November 5 ChatGPT rechecked the four X10 items and the updated Q1d rubric in the
  rendered exam and key. All match the accepted decisions (see the shared review). This is the
  exam's only status record.
  - Source: `course/exams/midterm_1/midterm_1_claude.tex`, SHA-256 `c8bf949d539ce6a84061fc69b54a176280cbd20424419daee5fad22fd6c324bd`
    (Q1d rubric, 2026-11-05; previous `3bca0363…` X10, `a746cf1b…` instructor text edits, `78669748…` X9, `c58fca68…` key revision P02/P03,
    `33cd4b9f…` first render), built from the Spring 2025 MT2 template (exam.cls). Shortened chain: rendered directly
    from X7–X8 and the review (no separate content file).
  - Question-only PDF checked in step 5: SHA-256 `1f6f49fe3f3c719efd7d974a1e4ea9db3226455c59d97499aeb1e096ad6b5422`
    (pre-X9 order). Current exam PDF: `db594b7353f8944527d6c2a305793a10be9d60fc0cbb9a498ca0144ca9b9d4eb`.
  - PDFs: `output/exams/midterm_1/midterm_1_claude.pdf` (exam, 14 pages) and `midterm_1_claude_solutions.pdf`
    (answers and rubric in blue, 14 pages). From the first render on, the `.tex` is the exam source.
- Date, duration (100 minutes, separate slot), materials (closed book, supplied equation sheet), coverage (sessions
  1.1–3.2) and the λ-return question: `decisions/grading_decisions.md` (`midterm_1`).
- Suggestions: `analysis/exam_suggestions/midterm_1_{claude,chatgpt}.md`. Review: `analysis/exam_suggestions/midterm_1_review.md`.

## Accepted

- X1 (instructor, 2026-11-02; Claude S1): the equation sheet includes the finite λ-return formula.
- X2 (instructor, 2026-11-02; Claude S5): COMP 438 and 538 take the same exam.
- X7 (instructor, 2026-11-02): Claude's selection recommendation in the shared review is accepted ("all the
  suggestions look reasonable"), with X8's change. The cross-review corrections are accepted: R01–R06 for Claude's
  parts, C02 (remove the two give-away instructions), C03 (i)–(ii) on the equation sheet and C05 (mastery labels).
  No Week 1 rebalancing. The exam (points; minutes are unpiloted estimates):

  | Question | Source | Parts and points | Minutes |
  | --- | --- | --- | ---: |
  | Q1 Formulation (tutoring) | Claude Q1, R01–R03 wording | a 4, b 6, c 6, d 4, e 2 = **22** | 15 |
  | Q2 Evaluation and improvement (A/B MDP) | ChatGPT Q2, synchronous sweeps | a 6, b 4, c 8, d 8, e 6 = **32** | 24 |
  | Q3 Learning from episodes | ChatGPT Q3a–b (C02) + Claude Q3e | a 7, b 7, c 6 = **20** | 15 |
  | Q4 n-step targets and λ | ChatGPT Q4 | a 4, b 6, c 1, d 3 = **14** | 10 |
  | Q5 Short answers | ChatGPT Q5a, ChatGPT Q5b, Claude T/F 3 (true form), 4, 5 | 2 + 4 + 6 = **12** | 9 |
  | **Total** | | **100** | **73** |

  Equation sheet: ChatGPT's ℳ-based sheet with C03 (i)–(ii); no n-step formula (Q4a constructs it).
- X8 (instructor, 2026-11-02): 3.2 evaluation uses ChatGPT's Q5b (4 points) in place of Claude's T/F item 8. To keep
  100 points, Q2b (IPE sweeps) goes from 6 to 4 points. Numbers only; the wording does not change.
- X9 (instructor, 2026-11-03, step 6): (i) the short-answer question (X7's Q5) moves to the front as a warm-up, so
  the order is Q1 short answers 12, Q2 tutoring 22, Q3 A/B MDP 32, Q4 episodes 20, Q5 n-step and λ 14; X7's table
  keeps its original numbering. (ii) The A/B MDP model is drawn as a figure in the style of previous exams (states as
  circles, a random action through a black dot, probability and reward on each arrow) instead of the transition
  table; the transitions are unchanged. Layout consequence: Q3b starts on its own page to keep answer space for Q3a;
  exam 14 pages. Points, wording of all parts and answers unchanged.
- X10 (instructor, accepted 2026-11-05, step 6): Q1d, Q1e, Q3e and the Q3 intro as recorded
  in the shared review (I01–I03 and ChatGPT's wording). Q1d is now True and Q1e is now about Monte Carlo on a continuing
  task; Q3e keeps the improvement argument and the PI/VI difference. Points, equation sheet and pagination unchanged.
  Q1d rubric (instructor, 2026-11-05): naming the policy improvement theorem without the strict-gain reason earns 0.5
  of the reason point.
- X3 and X4 resolved by X7 (the A/B MDP replaces the espresso MDP and includes IPE sweeps). X5 resolved by X8.

## Open

- X6 (Claude S6): partial credit for alternative answers on the tutoring question (Q1 in X7; Q2 since X9). The instructor will decide after seeing a few student answers (2026-11-05), so this is settled at grading and does not hold up the final record of the exam text.

Pointers: suggestions `analysis/exam_suggestions/midterm_1_{claude,chatgpt}.md`; findings and the selection
recommendation in `analysis/exam_suggestions/midterm_1_review.md`.

ChatGPT checked X7–X8 on 2026-11-02: no new instructor decision before consolidation. The shared review's
“ChatGPT check of accepted X7–X8” records the implementation checks for the hybrid selection (D01–D04), including
the added every-visit A estimate in Q3a and Q2b's revised rubric. These clarify the accepted selection; they do not
change its points, timing targets or status.
