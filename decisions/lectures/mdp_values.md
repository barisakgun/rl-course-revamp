# Deck decisions: MDPs, returns and values (session 1.2)

**Shared** deck decision file (`docs/lecture_workflow.md`). It holds outcomes only; the discussion goes in `analysis/lecture_suggestions/mdp_values_*`.
- **Scope:** session 1.2 `mdp_values` (58 minutes; `decisions/topic_decisions.yaml`). It is the second round of the workflow pilot (decision log 2026-10-07).
- **Status:** step 0. Instructor decisions taken before the initial suggestions; the AI suggestions have not started.

## Accepted (instructor, 2026-10-07)

- B1. **Separate deck** for 1.2 (not added to the accepted Introduction deck).
- B2. **Slide reuse:** the instructor decides which old slides to keep after seeing the initial AI suggestions, and will mark in advance anything wanted for 1.2 (and future decks).
- B3. **Running example: the recycling robot with the 1.1 numbers** (Introduction deck decision A14).
  - At high, a search stays high with 0.8, otherwise low.
  - At low, a search stays low with 0.7, otherwise rescue to high.
  - Rewards: search +2, wait +1, recharge 0, rescue −3.

  1.2 also shows a **terminal-state version** ("out of battery" instead of rescue) for the episodic contrast. Old `2 - Markov Decision Processes.pptx` slide 21 ("Infinite Utilities") already mentions absorbing states.
- B4. **Discount γ = 0.5** for hand calculations, with a remark that this small value is not the norm in practice.
- B5. **History symbol stays available** (notation-guide open item O10 remains open). It may be used, for example, in a "what if there were no battery gauge?" discussion, and later for partial observability.
- B6. The model and returns, introduced informally in 1.1, are **covered again formally** in 1.2. 1.2 keeps its 58 minutes.

## Open

| # | Item | Notes |
| --- | --- | --- |
| P1 | Terminal-state reward (1.1 suggested −10 if drawn) and how the episodic and continuing versions are compared | For the initial suggestions. Returns of never-ending safe policies need discounting, or the absorbing-state view in book §3.4. |
| P2 | Notation for the formal definitions (S_t, A_t, R_{t+1}, G_t, γ, π, p(s′, r ∣ s, a), v_π, q_π; history per B5) | Notation guide; old-deck conversions are listed in its O9. |
