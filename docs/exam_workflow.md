# Midterm exam guideline and workflow

**Shared** by the instructor, Claude and ChatGPT. **Adopted with corrections by the instructor, 2026-11-02**
(initial draft by Claude; adoption corrections by ChatGPT). This is the accepted workflow; individual question
choices and explicitly open format items still require instructor decisions. Exam weights, windows and coverage records live in `decisions/grading_decisions.md`; this file
does not restate them.

`AGENTS.md` / `CLAUDE.md` (file ownership, notation, evidence discipline), `docs/repository_contract.md` and the review
conventions in `docs/lecture_workflow.md` still apply. This file fixes what an exam may test, the order of steps and
where each artifact lives.

## Coverage

- **Accepted (instructor, 2026-11-02):** the coverage of each midterm is decided by the instructor right before that
  midterm, from the material actually taught by then. The session lists in `decisions/grading_decisions.md` are
  planning windows until that decision; the decision is recorded there and in `decisions/decision_log.md`. A
  coverage or format decision applies to the current semester only unless the instructor says otherwise; future
  offerings start again from the planning windows.
- Each midterm covers a different set of topics (syllabus); there is no final exam. A later midterm may use earlier
  material as working knowledge (e.g. a Bellman target inside a DQN question) but does not re-test it for its own
  sake.
- **Examinable:** material taught live in the covered sessions, within the accepted scope and mastery in
  `decisions/topic_decisions.yaml` and the deck as delivered.
- **Not examinable:** hidden or appendix slides; optional slides with no live time; readings (`decisions/reading_decisions.md`);
  extension topics; anything only in an unreleased, undue or ungraded assignment. An exam never assumes submission,
  solution access or graded feedback for any assignment (accepted 2026-09-28).
- **Exposure topics** are examinable only at their recorded mastery (`recognize` / `explain`), in short parts with
  small weight. A topic whose scope says its exam inclusion is not established needs an explicit coverage decision.

## Design rules

- **Assess intended mastery.** `derive` / `analyze` topics get derivations, hand calculations, comparisons and
  diagnoses; `explain` topics get short reasoning answers. An exam cannot establish `implement` mastery. It may ask
  students to complete or correct an update rule or pseudocode, never to recall assignment code.
- **Weight follows the course:** Core material carries most of the points; the split roughly follows the live time of
  the covered sessions, adjusted for importance. State the planned point split per session in the decisions file.
- **Question mix**, as in the previous exams: one formulation/modelling question; hand computations on small MDPs or
  trajectories; short conceptual questions (why, compare, what changes if, diagnose a changed target or result).
- **Reasoning over arithmetic.** Small state spaces and friendly numbers. Make parts independent where possible, or
  supply intermediate values, so one arithmetic slip does not cascade.
- **Unfamiliar but in scope.** Use the lecture's methods on a new example or a changed setting. Earlier exams in
  `sources/current_course/exams/` are a starting point (keep / adapt / cut), but questions reused from them change
  their numbers or structure, since old exams and solutions may circulate among students.
- **Notation** only from `course/notation_guide.md`; questions adapted from old exams are converted.
- **Length.** 100 points. Each part gets an estimated student time; the total stays at or below about 75% of the
  exam duration. Points roughly follow time and importance.
- **Gradeable by at most one TA:** every part has a worked solution and a partial-credit rubric. Prefer answers that
  can be checked quickly (tables, short justifications) over long open essays.
- **Equation sheet.** Midterm 1 is closed book with no aids and comes with a supplied equation sheet as in previous exams
  (accepted 2026-11-02); other midterms' allowed materials remain to be decided in the grading record. On a supplied sheet, equations are listed without names, semantics or context; they use
  notation-guide symbols and stay within the covered material. The sheet is drafted with the questions (step 1),
  reviewed with them and rendered as the exam's last page. Questions test understanding the sheet does not give away:
  choosing and applying the right equation, interpreting it, deriving from it.
- COMP 438 and 538 take the same exam unless the instructor decides otherwise.

## Files per exam

`<exam>` is `midterm_1`, `midterm_2` or `midterm_3`.

| Artifact | Path | Owner | Maintained? |
| --- | --- | --- | --- |
| Initial suggestions | `analysis/exam_suggestions/<exam>_{claude,chatgpt}.md` | each AI | Historical after step 3 |
| Review and responses | `analysis/exam_suggestions/<exam>_review.md` | shared | Yes, as in the lecture workflow |
| **Exam decisions** | `decisions/exams/<exam>.md` | shared | **Yes: point split, equation sheet, accepted questions, the exam's only status** |
| Render-ready content | `course/exams/<exam>/<exam>_content.md` | shared | No: frozen at the first render |
| Exam source | `course/exams/<exam>/<exam>_claude.tex` (exam.cls, previous exams' template) | Claude renders; instructor edits | The source from the first render on |
| PDFs | `output/exams/<exam>/<exam>_claude{,_solutions}.pdf` | generated from the source | Regenerated per saved source |

Date, duration, setting, allowed materials and coverage are not secret and live in `decisions/grading_decisions.md`.
One LaTeX source produces both PDFs (`\printanswers` on or off). **Confidentiality (accepted, 2026-11-02):** the paths
above are git-ignored until the exam has been held, as the old exam bank already is; Dropbox history keeps versions.
The instructor decides whether to commit them afterwards.

## Steps

0. **Coverage and format (instructor).** Coverage, date, duration, setting (in class or a separate slot), allowed
   material and the 438/538 decision, recorded in `decisions/grading_decisions.md` before step 1.
1. **Initial suggestions (both AIs, independently).** For each covered session: what is examinable at what mastery
   (from `decisions/topic_decisions.yaml`, the accepted deck and `output/lectures/session_sources.md`); a keep / adapt /
   cut delta against the relevant previous midterms; a draft exam of complete questions with points, estimated
   student times, answers and the mastery each part assesses; a draft equation sheet. Unpolished wording is fine; correct answers are not
   optional.
   Use shared accepted delivery decisions and the current deck, not frozen first-render content as a substitute
   for the delivered deck. Observe AI file ownership; disclose any source-verification limitation.
2. **One mutual cross-review** in the shared review file. Check: correctness of every answer (solve the other AI's
   questions independently before reading its solutions); coverage and weight against the accepted scope; untaught
   prerequisites; ambiguity and multiple valid answers; length; notation. Resolve straightforward corrections; present
   only consequential choices to the instructor.
3. **Instructor choices**, recorded once in `decisions/exams/<exam>.md` (question selection, point split, open items).
4. **Render-ready content and first render.** One AI consolidates the chosen questions, points, solutions and rubric
   into the content file; Claude renders the LaTeX and both PDFs. When time is short (as for midterm 1), Claude may
   render directly from the decisions file and the chosen suggestions, and the content file is skipped.
5. **Blind check (the AI that did not render).** Solve the question-only PDF without the solutions, then compare.
   Report disagreements, ambiguities and the solve-time estimate in the review. Correctness only; no polishing.
   This is a fresh solve without that render's answers, not a claim that the reviewer has never seen the questions
   during cross-review. Student-time estimates remain unpiloted unless an actual student pilot was performed.
6. **Instructor review and edits**, iterated as needed. Claude regenerates the PDFs from each saved source and
   rechecks what an edit affects (point totals, cross-references, solutions).
7. **Final.** On the instructor's acceptance, the decisions file records "final" with the source's SHA-256 and the
   decision log gets one line. Later changes, including corrections announced during the exam, are recorded there.

## Open items

- E1: setting, duration and allowed materials of midterms 2 and 3 (midterm 1 decided 2026-11-02, in
  `decisions/grading_decisions.md`).
- E2: whether 538 students get a different or additional question in midterms 2 and 3 (midterm 1: the same exam,
  instructor 2026-11-02).
- E3 resolved: guideline adopted with corrections (instructor, 2026-11-02).
