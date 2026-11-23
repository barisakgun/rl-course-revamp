# Deck decisions: policy gradients (sessions 7.1–7.2)

**Shared** deck decision file (`docs/lecture_workflow.md`). It holds outcomes only. Discussion and findings are in the
[shared review](../../analysis/lecture_suggestions/policy_gradients_review.md). The initial suggestions are historical
inputs:
- [Claude](../../analysis/lecture_suggestions/policy_gradients_claude.md);
- [ChatGPT](../../analysis/lecture_suggestions/policy_gradients_chatgpt.md).

**Scope:** sessions 7.1 `reinforce` (Policy-search history and REINFORCE) and 7.2 `baseline` (Sampled gradients,
baselines and critic motivation). Accepted teaching allocations, scope and mastery live in
`decisions/topic_decisions.yaml`.

**Status: first render done (2026-11-23); next is step 6, instructor edits and AI checks.** Deck
`course/lectures/week07/policy_gradients_claude.pptx`, SHA-256 `fea8b056def5…`, 34 slides: 7.1 = slides 1–21 (targets 63),
7.2 = slides 22–34 (targets 58; ADM carries the separate 5 administrative minutes). Text view:
`output/lectures/week07/policy_gradients_claude.md`. Frozen first-render inputs: the shared
[content](../../course/lectures/week07/policy_gradients_content.md), `policy_gradients_claude.yaml` (7.1) and
`policy_gradients_baseline_claude.yaml` (7.2). Equation fallback pictures refreshed and all slides
rendered in PowerPoint (shared review K48); slideshow playback not checked. This is the deck's only current status record; other files point here.

## Accepted (instructor, 2026-11-21, after the initial suggestions, before the cross-review)

The instructor answered Claude's early choices E6, E8, E12 and the paper-check note.

- **D1. Discounting.** The slides keep the discount: the estimator is taught in its exact discounted form,
  Σ_t γ^t G_t ∇log π(A_t ∣ S_t, **θ**). A slide note says that most code drops the γ^t factor, and slides explain why
  that is acceptable.

- **D2. The finite-difference formula goes on the slides** (answer to E8), so that students remember the methods when
  they revisit the slides. The 10-minute allocation and `recognize` mastery are unchanged. This changes the accepted
  `policy_history` scope ("No mathematics or algorithms") in `decisions/topic_decisions.yaml`; recorded in
  `decisions/decision_log.md`. The CEM steps were added by D9.

- **D3. Notation** (recorded in `course/notation_guide.md`):
  - **log**, not ln, for the logarithm (more general): ∇log π(a ∣ s, **θ**);
  - **τ** for an episode (trajectory), with a note that context separates it from the Polyak rate τ (Week 6);
  - **μ(s, **θ**), σ(s, **θ**)** for the Gaussian policy's mean and standard deviation, treated
    the same way as τ (context, with a note): this μ is not the state distribution μ^π(s);
  - approved as proposed: h(s, a, **θ**) action preference; ĝ for a policy-gradient estimate; α_**θ**, α_**w** for
    the two step sizes; A^π(s, a) = q^π(s, a) − v^π(s); ℛ(a) for a single-state problem's expected reward; the word
    "score" for ∇log π, with the book's "eligibility vector" named once.

- **D4. Unverified facts stay marked; remind the instructor after the first render.** Facts from papers that are not in
  the local sources (Kohl and Stone 2004; Szita and Lőrincz 2006; Salimans et al. 2017; Williams 1992, including the
  REINFORCE acronym; Sutton et al. 2000) keep their "verify" notes. **After rendering, Claude reminds the instructor to
  check them.**

## Accepted (instructor, 2026-11-23, answers to Q1, Q3–Q8 and Q10 of the shared review)

- **D5. Worked examples (Q1).** The book's short corridor motivates stochastic policies and replaces the old aliased
  gridworld (old 8–10). ChatGPT's two-step fork, with the corrected critic of R01, carries every calculation in both
  sessions. No corridor critic.
- **D6. Reasons to learn a policy (Q3).** 2 extra minutes in 7.1 for the list promised in Week 6.
- **D7. Book Fig. 13.2 (Q7)** is used in 7.2's four-minute evaluation slide.
- **D8. Presentation of dropping γ^t (Q4; details D1).** A common, deliberate approximation: late decisions keep full
  weight, and γ inside the return shortens the credit horizon; fork values 0.5 (discounted gradient), 0.75 (γ^t dropped)
  and 1.0 (undiscounted gradient). The formal limits go in the notes.
- **D9. CEM steps on the slide (Q5)**, beside the finite-difference formula. Changes the `policy_history` scope again;
  logged.
- **D10. Symbols (Q6).** ε**u**_k for finite differences on the slide; ∇_**θ** where **θ** and **w** both appear; scalar
  θ for the fork's single preference. In `course/notation_guide.md`.
- **D11. Cuts (Q8, in part).** Old 54–58 (time scales, traces) and 60–63 (compatible approximation) are cut with no
  appendix. Old 43 (puck world) is open.
- **D12. Agreed items (Q10).** Accepted segment order; a one-decision check before the path derivation; the policy
  gradient theorem stated without the book's proof, **with a pointer to where the proof is** (Sutton and Barto §13.2, box
  on printed p. 325 / PDF p. 347); one update per episode with **θ** fixed; old 49–52 move to 8.1; two short psychology
  lines.

## Accepted (instructor, 2026-11-23, second answer)

- **D13. Gaussian score (Q2).** 2 minutes in 7.1.
- **D14. Puck world (Q8; old 43) is kept and gets class time**: the variable goal, the multi-dimensional action, and the
  learning curve, which shows that a seemingly simple problem can need a lot of training (tied to high variance). Extends
  D11.
- **D15. One deck for 7.1–7.2 (Q9).** Merging 8.1 into it may be decided later. File name `policy_gradients`.

- **D16. Pendulum in 7.1, puck world in 7.2** (third answer, same day; choice C18 of the shared review).
  - 7.1 opens with the pendulum (old 41) as an MDP and reuses it for the Gaussian policy and its score.
  - 7.2 uses puck world (old 43), about 4 minutes, at the start of the variance segment.
  - Slide targets estimated at 63 (7.1) and 58 + 5 administrative (7.2); planning allocations (59 and 54 + 5) unchanged.

- **D17. Puck world's actions** (fourth answer, same day; C21): show the published controller (four discrete thrusts,
  softmax), then ask how to redesign it for a freely adjustable two-axis force.

- **D18. D03 wording; the γ^t explanation is kept outside the slides** (instructor, 2026-11-23, after the first render).
  D03 reads "Suppose the weight on this score is positive" (K47). The explanation of dropping γ^t is recorded in
  `analysis/ideas_backlog.md` for later offerings.

## Open

D4's reminder was given with the first render (2026-11-23); the instructor's checks are pending.

Outside the deck: the A3 and Midterm 2 convention for γ^t. The Baxter et al. source check is complete (shared review R07–R08).
