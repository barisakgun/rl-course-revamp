# Session 2.2 (`improvement`): initial content suggestion (Claude)

**Claude's step-1 suggestion** for the 2.2 portion of the `bellman` deck (`docs/lecture_workflow.md`, pilot v2), 2026-10-11. Analysis only: nothing here is accepted. Deck status: `decisions/lectures/bellman.md`. The file is named after the session id because the deck's step-1 files (`bellman_{claude,chatgpt}.md`) cover 2.1. Suggested counterpart name: `bellman_improvement_chatgpt.md`.

**Accepted frame** (`decisions/topic_decisions.yaml` → `improvement`; `output/lectures/session_sources.md` §2.2):
- **Time:** 58 teaching minutes (range 55–70); 59.5 usable.
- **Worked activity:** reuse one grid/table to compare improvement, VI and PI.
- **Pacing note:**
  - Protect the improvement argument; asynchronous DP is optional.
  - Reward sensitivity (old MDP PPTX 52: a changing living reward changes the preferred behaviour) goes here, on the same grid/table. It replaces repeated example narration.
  - Formal optimality relationships stay as appropriate.
- **Planning group:** core; derive / implement / analyze. The improvement argument is derived; no full convergence-proof sequence.
- **A1 prerequisite:** A1 implements value iteration and compares against a supplied PI.

**Constraints from 2.1:**
- **Already covered at the end of 2.1** (C3/C9; B14–B16): v^\*, q^\*, both Bellman optimality equations and π^\*(s) = argmax_a q^\*(s, a). 2.2 recalls them in one slide and does not re-teach them. If the end of 2.1 slips into 2.2, that time comes out of 2.2's 58 minutes.
- **Example and notation:**
  - the 2×2 grid with always-right, entry rewards (C7/C8) and γ = 0.5;
  - superscript notation (C11) and Accent 5 equations (C12);
  - V_k for sweeps (C6).
- **Students already have:**
  - the exact values of always-right (14/275, 46/55, 32/275);
  - the B14 teaser, q^π((2,1), up) ≈ 0.80036 > v^π((2,1)) ≈ 0.11636, with "How to formalize this step?" left open;
  - B^π and the one-line contraction argument.

## Central idea

2.1 ended by noticing that one changed action looked better. 2.2 turns that observation into two algorithms.
- **Policy improvement:** act greedily with respect to q^π. The improvement theorem says the greedy policy is at least as good everywhere. If nothing changes, the Bellman optimality equation holds, so the policy is optimal.
- **Policy iteration:** alternates full evaluation and improvement. It must stop, because there are finitely many deterministic policies and each step improves.
- **Value iteration:** uses the optimality equation from 2.1 as an update. It is policy iteration with a single evaluation sweep between improvements.
- **Generalized policy iteration (GPI):** the common picture behind all three, reused in Week 4 control.
- **Reward sensitivity:** shows what "optimal" depends on. Change the living reward and the optimal behaviour changes, even though the algorithm is the same.

## Worked numbers (2×2 grid, γ = 0.5, entry rewards; exact checks by script)

**Policy iteration from always-right.**
- Improvement uses q^π for always-right:

  | State | up | down | left | right |
  | --- | ---: | ---: | ---: | ---: |
  | (1,1) | **0.30291** | −0.01127 | 0.02473 | 0.05091 |
  | (1,2) | 0.44036 | 0.12618 | 0.33891 | **0.83636** |
  | (2,1) | **0.80036** | 0.01491 | 0.09018 | 0.11636 |

- The new policy π′ is up at (1,1), right at (1,2) and up at (2,1).
- Evaluating π′ gives v^{π′} = (199/550, 469/550, 469/550) ≈ (0.36182, 0.85273, 0.85273). Every state improves over always-right (0.05091, 0.83636, 0.11636), which checks the theorem.
- Improving again changes nothing, except that at (1,1) **up and right tie exactly** (0.36182; the grid is symmetric). A tie-breaking rule that prefers the current action stops PI here. A rule that flips between tied actions makes the book's "policy-stable" test never fire: book §4.3, Exercise 4.4.
- So π′ is optimal, and v^\* = v^{π′}. PI needed one improvement and two evaluations.

**Value iteration from V₀ = 0.**

| Sweep | (1,1) | (1,2) | (2,1) |
| --- | ---: | ---: | ---: |
| V₁ | −0.04 | 0.792 | 0.792 |
| V₂ | 0.3144 | 0.8296 | 0.8296 |
| V₃ | 0.34904 | 0.8492 | 0.8492 |
| V₆ | 0.36173 | 0.85270 | 0.85270 |
| v^\* | 0.36182 | 0.85273 | 0.85273 |

- Contrast with policy evaluation: V₁((2,1)) is 0.792 here, against 0.064 for always-right. The max picks "up".
- The greedy policy with respect to V₁ is already optimal while the values keep converging: the policy converges before the values (old DP 11/25).

**Reward sensitivity (3×4 grid, entry rewards ±1, recomputed; old values not reused, C8).**

Optimal policies by value iteration:

| Living reward | γ | Optimal behaviour (summary) |
| --- | --- | --- |
| −2 | 0.9 | Rushes to finish at any cost: from (3,2) right and from (4,1) up, both **straight into the −1 pit** |
| −0.4 | 0.9 | Takes the short route past the pit and accepts the slip risk |
| 0 | 0.9 | Takes the long safe detour; at (2,1) it moves left, away from the goal |
| +0.2 | 0.9 | Never finishes: next to the goal, (3,3) moves left, **away from the +1** (any action is fine in many cells) |

With γ = 0.5, the policies for living rewards of −0.04 and above are almost identical, because the near future dominates. That makes it a weak demonstration (see Q1).

## Teaching sequence (slide level, unpolished)

IDs use **I** (improvement), added after B16 in the same deck. Old references are PPTX positions: `MDP` is the old MDP deck and `DP` the old DP deck.

| ID | Slide | Content and purpose | Sources | Target |
| --- | --- | --- | --- | ---: |
| I00 | Section divider: Session 2.2 | Recap of 2.1 in one slide. Keep B16's two optimality equations visible, plus B14's question "How to formalize this step?". Today: from evaluating to improving, then two algorithms. | 2.1 B14/B16; old DP 2 | 1.5 |
| I01 | Policy improvement step | Greedy with respect to q^π: π′(s) = argmax_a q^π(s, a) = argmax_a [ℛ(s, a) + γ Σ 𝒯(s, a, s′) v^π(s′)]. Extracting from v^π needs the model; extracting from q^π does not (link to B16's note). | old DP 30, MDP 62; book §4.2 | 3 |
| I02 | Worked: improve always-right (**protected**) | Students compute q^π((1,1), up) = 0.30291 and compare it with right (0.05091). (2,1) is already known from B14. Result: π′ = (up, right, up). Show the q table. | 2.1 values; script check | 5 |
| I03 | Policy improvement theorem | Statement: if q^π(s, π′(s)) ≥ v^π(s) for all s, then v^{π′}(s) ≥ v^π(s) for all s. **Derive** by repeated expansion (book §4.2, eq. 4.7): v^π(s) ≤ q^π(s, π′(s)) = 𝔼_{π′}[R_{t+1} + γ v^π(S_{t+1}) ∣ S_t = s] ≤ … ≤ v^{π′}(s). Check: v^{π′} = (0.362, 0.853, 0.853) ≥ (0.051, 0.836, 0.116). | old DP 36 (statement); book §4.2; CS234 L2 PDF 22–27; Silver L3 PDF 16–17 | 7 |
| I04 | When improvement stops | If π′ = π (no strict gain anywhere), v^π satisfies B16's optimality equation, so π is optimal. Ties: keep the current action, or stop when the values stop changing (Exercise 4.4). On our grid, up and right tie at (1,1). | book §4.2 end, §4.3 Ex. 4.4; Silver L3 PDF 17 | 2.5 |
| I05 | Policy iteration | Evaluate (2.1: linear solve or sweeps) → improve → repeat until stable. It terminates in finitely many iterations: finitely many deterministic policies, each improving. On the grid: one improvement and two evaluations. | old DP 26, 31; book §4.3 box; Silver L3 PDF 13 | 4 |
| I06 | Value iteration | Turn B16's v^\* equation into an update: V_{k+1}(s) ← max_a [ℛ(s, a) + γ Σ 𝒯(s, a, s′) V_k(s′)]. It is PI with a single evaluation sweep. Convergence: B^\* is also a γ-contraction, because a max of averages can't increase the largest discrepancy (one line, extending 2.1's B13). Stop on a small largest change, then extract the greedy policy. | old DP 9–12, 21–22; book §4.4 box; Silver L3 PDF 20–25 | 5 |
| I07 | Worked: VI sweeps (**protected**) | Students compute V₁ = (−0.04, 0.792, 0.792); show V₂, V₃ and V₆ against v^\*. Contrast V₁((2,1)) = 0.792 with 0.064 from the evaluation in 2.1: the max picks up. The greedy policy is optimal after one sweep while the values still converge. | old DP 13–16 (adapted to entry rewards); A1 | 7 |
| I08 | PI vs VI on the same grid | Same answer by different routes. PI: few iterations, each with a full evaluation. VI: cheap sweeps (|𝒮|²|𝒜| each), more of them. The policy settles before the values. Choice: VI for A1; PI is supplied for comparison. | old DP 25, 37, 39; book §4.4 end | 3 |
| I09 | Generalized policy iteration | Evaluation and improvement as two interacting processes (the book's GPI diagram). PI, VI and modified PI (k sweeps) are points on one spectrum. Week 4 control reuses this. | old DP 35; book §4.6 figures | 3 |
| I10 | What is optimal depends on the reward | The 3×4 grid, γ = 0.9, four living rewards (table above). Native policy-arrow grids, recomputed under entry rewards. Ask why the agent walks into the pit at −2 and avoids the goal at +0.2. | old MDP 51–52 (purpose; pictures not reused); C8 | 5 |
| I11 | Beyond full sweeps (exposure) | Asynchronous / in-place DP updates states in any order and converges if every state keeps being updated (one line). Full-width backups need ℳ and every successor; sample backups, (s, a, r, s′), come in Week 3. | old DP 41–45; book §4.5, §4.7; Silver L3 PDF 27–33 | 2.5 |
| I12 | Summary: DP for known MDPs | Table: problem (prediction / control) → Bellman equation (expectation / optimality) → algorithm (iterative policy evaluation / PI, VI). Next: when the model is unknown. | old DP 38–39; Silver L3 PDF 26 | 2 |

**Targets sum to 50.5 minutes**, against 58 teaching and 59.5 usable. The 7.5 minutes of reserve deliberately absorbs any spill-over from the end of 2.1 (B14–B16, 7 minutes) without double-counting it (C9). It also covers student-calculation overruns, as in 2.1. If no spill-over happens, the candidates are:
- Q-value iteration (+1.5, Q3);
- a second improvement theorem proof with operators (+3, Q2);
- the 3×4 V^\*/Q^\* display (+2, MDP 65–66, recomputed).

| Segment | Slides | Minutes |
| --- | --- | ---: |
| Recap and improvement step | I00–I02 | 9.5 |
| Improvement theorem and stopping | I03–I04 | 9.5 |
| Policy iteration | I05 | 4 |
| Value iteration and worked sweeps | I06–I07 | 12 |
| Comparison and GPI | I08–I09 | 6 |
| Reward sensitivity | I10 | 5 |
| Exposure and summary | I11–I12 | 4.5 |
| **Total** | | **50.5** |

## Introductory motivation per new concept

| Concept | Problem it addresses | Meaning first | Connection | Check |
| --- | --- | --- | --- | --- |
| Greedy improvement | B14's question: how to use a better first action systematically | Pick the best first action, then follow the old policy | q^π from 2.1 | q^π((1,1), up) |
| Improvement theorem | Does switching everywhere at once still help? | Each better first step compounds | Return recursion, v/q relations | v^{π′} ≥ v^π on the grid |
| Stopping and optimality | When are we done? | No action beats the policy's own choice | B16 optimality equation | Tie at (1,1) |
| PI | A systematic loop that ends at an optimal policy | Evaluate, improve, repeat | 2.1 evaluation | Iterations on the grid |
| VI | PI's full evaluation is expensive | One sweep, then improve, folded into a max | B16 equation; B13 contraction | V₁((2,1)) = 0.792 vs 0.064 |
| GPI | One picture for every method | Two processes pulling toward consistency | PI, VI; Week 4 control | Where VI and PI sit |
| Reward sensitivity | "Optimal" for which reward? | Same algorithm, different objective | MDP formulation (B03a) | Why the pit at −2? |

## Delta against the old decks

| Old slides | Decision | Reason / placement |
| --- | --- | --- |
| DP 8 (recall optimality equations) | **Cut**; recall in I00 | Taught in 2.1 (B15–B16); C9 forbids repeating it. |
| DP 9–10 (nonlinear, iterate; three update variants) | **Compress** → I06 | One ℛ/𝒯 form plus a note on the full ℳ form; convert R/P. |
| DP 11–12 (VI algorithm, O(S²A), convergence, policy before values; pseudocode image) | **Keep, fix** → I06/I08 | Use the book's §4.4 box in course notation; the policy-before-values point goes to I07/I08. |
| DP 13–16 (VI exercise on the 2×2 grid with R(s) and terminal value 1) | **Adapt** → I07 | Same grid, entry rewards and V₀ = 0 (C8); the old numbers are not reused. |
| DP 17–19 (policy extraction on 3×4 with R&N values; home exercise) | **Cut** | Old terminal-value convention (C8). Extraction is shown on the 2×2 grid (I01/I07). |
| DP 20 (B^π) | **Done in 2.1** | |
| DP 21–22 (B^\*, monotone, contraction) | **Compress** → I06 | One line: the max preserves the contraction. Monotonicity only if Q2 picks the operator proof. |
| DP 23–24 (what DP is) | **Done in 2.1** (B02); one spoken line on optimal substructure in I06 | |
| DP 25 (problems with VI) | **Keep** → I08 | |
| DP 26, 30–31 (policy-based methods, improvement, PI summary) | **Keep, fix** → I01/I05 | "Just do policy extraction" becomes greedy with respect to q^π. |
| DP 27–29 (prediction) | **Done in 2.1** | |
| DP 32 (Turing Award) | **Optional aside** | Not in the targets. |
| DP 33, 38–39 (recaps, summaries) | **Merge** → I12 | |
| DP 34 (brainstorm Q-value iteration) | **Q3** | Bridge to Q-learning. |
| DP 35 (GPI) | **Keep** → I09 | Book figures. |
| DP 36 (improvement theorem; "see the book for the proof") | **Expand** → I03 | Scope requires deriving the argument. |
| DP 37 (comparison) | **Keep** → I08 | |
| DP 40 (caveman home exercises) | **Replace** | Grid exercises are optional and not required (A1 covers VI). |
| DP 41–42 (async DP) | **Compress** → I11 | Optional per plan; one line. |
| DP 43–45 (full-width vs sample backups, foreshadowing) | **Compress** → I11/I12 | Bridge to Week 3. |
| MDP 51–52 (optimal policies under living rewards) | **Recompute** → I10 | Pictures use the old convention; draw native arrows from VI under entry rewards. |
| MDP 62 (Q induces policy) | **Done in 2.1** (B16) | |
| MDP 65–66 (V/Q demo snapshots) | **Optional** | Recompute if used. |
| MDP 67 (solving MDPs) | **Merge** → I00 | |

**Reference courses (evidence):**
- **Book §4.2–4.7:** improvement theorem (eq. 4.7–4.8), PI box with its tie issue (Exercise 4.4), VI box, async DP, GPI, efficiency.
- **Silver L3 PDF 12–33:** improvement proof, modified PI, VI and its shortest-path illustration, summary table, async and sample backups.
- **CS234 L2 PDF 15–44:** monotonic improvement proof and finite PI termination.
- **Abbeel l1 PDF 22–57:** VI on a grid, PI guarantees.
- **Sutton 7-8-DP PDF 8–27:** improvement, PI, VI, GPI, async.

Adopted from them:
- CS234's emphasis on monotone improvement and finite termination (I03–I05);
- Silver's prediction/control summary table (I12);
- the book's GPI figures (I09).

Not adopted: full contraction proofs, Jack's car rental (another full example) and the gambler's problem.

## Questions for the instructor

- **Q1. Discount for the reward-sensitivity comparison (I10).** With γ = 0.5 the four policies barely differ. *Recommend* γ = 0.9, with one sentence on why: a larger γ lets long-term trade-offs show, which is itself a sensitivity point. Alternatives: γ = 1 for negative living rewards only, which comes closest to the classic Russell–Norvig pictures; or keep 0.5 and accept a weak demonstration.
- **Q2. Improvement theorem proof (I03).** *Recommend* the book's repeated-expansion proof. It needs only 2.1's v/q relations; about 7 minutes including the check. Alternative: the operator proof (B^{π′} v^π ≥ v^π, plus monotonicity of B^{π′}). It is shorter if 2.1's operator landed well, but needs monotonicity as a new idea.
- **Q3. Q-value iteration (old DP 34).** It is B16's q^\* equation used as an update, and it foreshadows Q-learning in Week 4. A one-minute mention needs **Q_k(s, a)**, which is not in the notation guide; by analogy with V_k (C6) I propose Q_k. Include it as reserve time, or skip?
- **Q4. Asynchronous DP (I11):** one line as proposed, or skip entirely? The plan marks it optional.

## Not included

- No new required homework or reading.
- Not taught: the contraction-mapping theorem, the number of PI iterations, linear-programming solutions, finite-horizon DP and prioritized sweeping (Week 10 Dyna).
