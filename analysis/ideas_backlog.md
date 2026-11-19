# Ideas backlog (shared)

**Shared** by the instructor, Claude and ChatGPT. This file collects ideas for teaching materials and course tooling that are not planned for the current offering but may be adopted in later iterations of the course. Deferred *curriculum topics* are tracked separately in `analysis/future_topics.md`.

Nothing here is accepted or scheduled. Adopting an idea needs an instructor decision; for anything that adds student-facing material or workload, follow the usual decision and time/workload rules.

Conventions: one entry per idea, with who proposed it and when, the motivation, known risks and its status (`idea`, `under consideration`, `adopted <where>`, `dropped <why>`).

## Teaching materials

### Shareable code for the book's examples
- **Proposed:** instructor, 2026-10-05.
- **Motivation:** let students experiment with the textbook examples used in lectures.
- **Risk:** students may copy the code into their assignments.
- **Possible mitigations:** use environments or variants that differ from the assignments; release the code only after the related assignment is due.
- **Status:** idea.

### Algorithms as both verbose steps and pseudocode
- **Proposed:** instructor, 2026-11-17 (recorded by Claude, while editing the Week 6 deck).
- **Motivation:** decks currently present an algorithm either as numbered prose steps (e.g. Week 6 V08) or as code-style pseudocode (e.g. the old decks' Q-learning and DQN boxes). Instructor's idea: put both on slides, and go over only one of them in class; the other stays for study.
- **Needs:** probably an algorithmic-notation section (pseudocode conventions: assignment, loops, terminal handling, how code names map to course symbols such as q̂, **w**⁻ and 𝒟) next to `course/notation_guide.md`.
- **Risk:** two versions of each algorithm can drift apart when one is edited; extra slides add study material.
- **Status:** idea, for the next offering.

## Tooling

### LaTeX → native PowerPoint equation converter
- **Proposed:** instructor, 2026-10-05.
- **Motivation:** keep equations editable in PowerPoint when the existing PowerPoint equations are not enough (the current fallback is LaTeX-rendered images).
- **Status:** idea; a possible separate project. A minimal converter for the LaTeX subset used in decks exists as `scripts/omml_claude.py` (Claude, used for the 1.2 deck, 2026-10-07).

### Slim, git-tracked copies of large decks
- **Proposed:** instructor, 2026-10-09 (recorded by Claude).
- **Motivation:** decks are git-ignored (`*.pptx`), so accepted versions live only in Dropbox history and `output/deck_backups/`. A slim copy with large objects replaced (e.g. a video by a screenshot) or removed, plus a log of what each replaced object should be, could be committed to GitHub.
- **Risk:** the slim copy and the full deck can drift apart; the log must say how to restore the full deck.
- **Status:** idea; for after the main lecture workflow is settled. For this semester Dropbox and the backups are enough (instructor, 2026-10-09).
