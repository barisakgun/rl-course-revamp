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

### Explanation to keep: why policy-gradient code drops γ^t
- **Asked for by:** instructor, 2026-11-23 (recorded by Claude), so that it survives if the Week 7 slides are gone. Fall 2026 placement: `policy_gradients` D05b–D06 (`decisions/lectures/policy_gradients.md` D1, D8).
- **The exact estimator.** With J(**θ**) = 𝔼[Σ_t γ^t R_{t+1}] and G_t = Σ_{k≥t} γ^{k−t} R_{k+1}, ∇J = 𝔼[Σ_t γ^t G_t ∇log π(A_t ∣ S_t, **θ**)]. The outer γ^t appears because G_0 = (rewards before t) + γ^t G_t; the earlier rewards average out, since the score has mean zero given the history before A_t.
- **What most code does.** It uses Σ_t G_t ∇log π(A_t ∣ S_t, **θ**): the discount stays inside G_t and the outer factor is dropped.
- **Why this is acceptable in practice.** (1) The two discounts do different jobs: the inner one controls how strongly later rewards credit an action, the outer one how much a decision at time t counts toward the start-state objective. (2) With the outer factor, late decisions get almost no weight: 0.99^100 ≈ 0.37 and 0.99^500 ≈ 0.007. (3) Often the task's goal is undiscounted reward and γ < 1 is an algorithm choice that trades bias for variance; Schulman et al. set up the problem this way. It is a deliberate approximation whose performance can be evaluated.
- **What not to claim.** Dropping only the outer factor does not give the undiscounted gradient. The result need not be the gradient of any function, and Nota and Thomas give a counterexample that approaches a globally pessimal policy. Teach it as a common approximation, not as harmless.
- **Worked numbers (two-step fork).** Start: right → upper, left → lower, either pays 2. Upper: right 4, left 2, then the end. Lower: right 2, left 0, then the end. γ = ½; one preference θ for right (left 0), shared by all states; at θ = 0 both actions have probability ½ and scores ±½. Mean over the four episodes: **0.5** (discounted gradient, with γ^t), **0.75** (γ^t dropped), **1.0** (undiscounted gradient). On the single episode right–left the same three give 1, 0.5 and 1. Recompute: `scripts/check_policy_gradients_claude.py` §9 (means).
- **Sources:** Schulman et al., GAE (arXiv 1506.02438; §2 sets the undiscounted problem, §4 has the phrase "variance reduction parameter"; read 2026-11-23 through a fetch tool); Nota and Thomas, "Is the Policy Gradient a Gradient?" (arXiv 1906.07073 v3, 2026-10-16; abstract only); Sutton and Barto §13.3, box on p. 328 (has γ^t) and Exercise 13.2.
- **Open:** which form A3 and Midterm 2 use (not decided).
- **Status:** adopted in the Week 7 deck, Fall 2026; kept here for reuse.

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
