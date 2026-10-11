# Session 2.1 (`bellman`): initial content suggestion (Claude)

**Claude's step-1 suggestion** (`docs/lecture_workflow.md`, pilot v2), 2026-10-09. Analysis only: nothing here is accepted. This file becomes historical after step 3; deck status will live in `decisions/lectures/bellman.md` once that file exists.

**Accepted frame** (`decisions/topic_decisions.yaml`, `lecture_plan` → `bellman`; `output/lectures/session_sources.md` §2.1):
- 58 teaching minutes (range 55–70); 59.5 usable.
- Worked activity: derive one expectation backup and perform policy-evaluation sweeps.
- Pacing note: high density; finite examples before operator formalism.
- Instructor placements (B11): old MDP PPTX 42–48 (two-step transition prediction) and 59–61 (state/action-value relationships) go here, alongside the expectation backup. They are integrated with the worked backup, not added as another exercise block.
- Planning group: core; derive / implement / analyze. No full convergence-proof sequence. A1 implements VI (after 2.2), so 2.1 has no direct assignment dependency.

**What students already have from 1.2** (the accepted deck, `mdp_values_claude.pptx`):
- ℳ, 𝒯 and ℛ, including ℛ(low, search) = 0.5;
- G_t = R_{t+1} + γG_{t+1};
- v_π and q_π as expected returns;
- the always-wait values (0) and their q-values, with the verbal statement that a state's value averages its action values;
- the shown but **not derived** table: always-search 3.60 / 1.60; search-high/recharge-low 3.64 / 1.82;
- M17's closing question: "how do we compute these values if the task continues forever?";
- M14's estimation by averaging repeated returns, and M13's truncation (missing tail).

2.1 starts from that question.

## Central idea and why it is taught here

1.2 left two obstacles to computing a value:
- **Sampling:** averaging many runs is noisy.
- **Truncation:** a continuing return has an infinite tail.

With a known model, the Bellman expectation equation removes both. The expectation is computed from the model, and the infinite tail is replaced by the value of the next state. That holds because, under the Markov property, the future after one step "starts again" from S_{t+1}.

Iterative policy evaluation turns that equation into an update. Each sweep adds one more step of exact look-ahead. This step-by-step view is what 2.2 (VI), Week 3 (TD with samples) and Week 5 (where approximation breaks the contraction) reuse.

## Running example

**Recycling robot, accepted numbers, γ = 0.5** (B3/B4). The worked policy is **π₁ = search at high, recharge at low**, the 1.1/1.2 "second strategy". Its hand numbers are clean. All are checked by script.

| Quantity | high | low |
| --- | ---: | ---: |
| Bellman equations | v(h) = 2 + 0.5[0.8 v(h) + 0.2 v(l)] | v(l) = 0 + 0.5 v(h) |
| Exact solution | 40/11 ≈ 3.64 | 20/11 ≈ 1.82 |
| Sweep 1 (V₀ = 0) | 2 | 0 |
| Sweep 2 | 2.8 | 1.0 |
| Sweep 3 | 3.22 | 1.40 |
| Sweep 4 | 3.428 | 1.61 |
| Error at high, sweeps 0–4 (each about halves: γ = 0.5) | 3.64, 1.64, 0.84, 0.42, 0.21 | |

**Consistency checks that tie the session together:**
- **Forward prediction from high under π₁** (old 42–48, transferred to the robot):
  - Pr{S₁ = high} = 0.8, Pr{S₂ = high} = 0.8·0.8 + 0.2·1 = 0.84;
  - expected R₂ = 0.8·2 + 0.2·0 = 1.6, expected R₃ = 0.84·2 = 1.68.
  - The expected two-step discounted sum is 2 + 0.5·1.6 = **2.8 = V₂(high)**; the three-step sum is 2 + 0.8 + 0.25·1.68 = **3.22 = V₃(high)**.
  - So sweep k equals exact k-step look-ahead. That is the iterates' meaning: no sampling, a shrinking tail.
- **q-values from v_{π₁}:**
  - high: search 3.64, wait 1.82;
  - low: recharge 1.82, search 1.68, wait 0.91.

  These are the Introduction A14a numbers. The q-relation explains why recharge is now worth 1.82 when it was worth 0 under always-wait (1.2 M16's question).
- **Closing teaser:** always-search has v = (3.6, 1.6). At low, recharge-then-always-search gives 0 + 0.5·3.6 = 1.8 > 1.6. A one-step look-ahead with a policy's own values suggests a better action: the 2.2 improvement step. It is not proved here.

## Teaching sequence (slide level, unpolished)

Slide IDs use **E** (evaluation) to avoid colliding with 1.2's M IDs and with deck-decision IDs. "Old MDP" / "old DP" refer to PPTX positions, hidden slides counted, in `sources/current_course/2 - Markov Decision Processes.pptx` and `3 - Dynamic Programming.pptx`.

| ID | Slide | Content and teaching purpose | Sources | Target |
| --- | --- | --- | --- | ---: |
| E00 | Title | Course title format (Introduction A21): **Bellman Equations and Policy Evaluation**. | memory/A21 | 0.5 |
| E01 | The question 1.2 left open | Show the 1.2 table and its question: how do we compute these values if the task never ends? Two obstacles from 1.2: sampling (M14) and the tail (M13). Today: with a known model, compute values exactly. **Prediction** (evaluate a given π: today) vs **control** (find a good π: next lecture). Why evaluate? To compare and improve policies, and almost every later algorithm estimates these quantities. | old DP 2–3 (definitions, reworded); 1.2 M13/M14/M17 | 2.5 |
| E02 | Looking ahead with the model | Under π₁ from high: where is the robot after 1 and 2 steps? Students compute Pr{S₂ = high} = 0.84 from Pr{S_{t+1} = s′} = Σ_s Pr{S_t = s} 𝒯(s, π(s), s′). Draw the small two-level tree. The expected discounted sum over two steps is 2.8. **Purpose:** this is the instructor-placed transition prediction. Its limit motivates the recursion: the tree grows with the horizon, but every branch reaches high or low again, so the same sub-problems repeat. | old MDP 42–48 (formula and tree idea; gridworld replaced by the robot, see Q2); book §3.1 | 4 |
| E03 | The future starts again | From 1.2's G_t = R_{t+1} + γG_{t+1}: v_π(s) = 𝔼_π[R_{t+1} + γG_{t+1} ∣ S_t = s] = 𝔼_π[R_{t+1} + γ v_π(S_{t+1}) ∣ S_t = s]. **Name where the Markov property is used:** given S_{t+1} = s′, what follows depends only on s′ and π, so its expected return is v_π(s′). The infinite tail becomes one number per next state. | old MDP 26 (its derivation equation, converted to v_π, R_{t+1}); book §3.5 eq. 3.14; Silver L2 PDF 19–20, 30 | 4 |
| E04 | How v and q relate | v_π(s) = Σ_a π(a ∣ s) q_π(s, a): 1.2 M16 said this in words. q_π(s, a) = ℛ(s, a) + γ Σ_{s′} 𝒯(s, a, s′) v_π(s′): immediate expected reward plus the discounted expected value of where we land. **Check:** q_{π₁}(low, recharge) = 0 + 0.5·3.64 = 1.82. Why was it 0 under always-wait? The continuation policy differs (answers M16). Spoken warning from old 59: we now write values s, a, s′ instead of random variables. | old MDP 59 (converted); book §3.5, Exercises 3.12–3.13 | 5 |
| E05 | Bellman expectation equation | Substitute one relation into the other: v_π(s) = Σ_a π(a ∣ s)[ℛ(s, a) + γ Σ_{s′} 𝒯(s, a, s′) v_π(s′)], with the full-model form Σ_{s′,r} ℳ(s, a, r, s′)[r + γ v_π(s′)] (book eq. 3.14, converted). Give the deterministic-policy case, and the q form q_π(s, a) = ℛ(s, a) + γ Σ_{s′} 𝒯(s, a, s′) Σ_{a′} π(a′ ∣ s′) q_π(s′, a′). Old 61's sequence derivation becomes a corrected **hidden backup**. | old MDP 60 (fixed), 61 (fixed, backup); book §3.5; Silver L2 PDF 30–35 | 4.5 |
| E06 | Backup diagrams | The book-style v_π and q_π diagrams: open circles are states, dots are actions. Ask: which branchings are the policy's choices and which are the model's outcomes? This revisits 1.2 M18's "which uncertainty is the policy's?". "Backup": value information flows back from successors. **Not** the expectimax search-tree framing, which B11 deferred to MCTS. | old DP 7 (diagram; fix its stochastic-diagram vs deterministic-equation mismatch); book §3.5 backup diagrams | 2 |
| E07 | Worked: the robot's equations (**protected**) | Give v(high) for π₁. **Students write v(low)** = 0 + 0.5 v(high), then solve by substitution: 40/11 and 20/11, the 1.2 numbers now derived. Notes: always-search (3.6, 1.6) is left as a home check. This is the "derive one expectation backup" activity. | 1.2 M17 values; accepted robot model | 7 |
| E08 | n states: n linear equations | For a fixed policy, the Bellman equations are |𝒮| linear equations in |𝒮| unknowns (fixing π gives a Markov reward process, as said once in 1.2). A direct solve is fine for small problems, but its cost grows roughly cubically and it needs the full model. **Why iterate instead:** cheaper sweeps that can stop early; no closed form once a max appears (2.2); the same update pattern later works from samples (Week 3). The matrix form is spoken or kept as a backup (see Q4). | old DP 5, old MDP 31–33 (verbal content only); CS234 L1 PDF 57–59 | 3 |
| E09 | Iterative policy evaluation | Turn the equation into an update: V_{k+1}(s) ← Σ_a π(a ∣ s)[ℛ(s, a) + γ Σ_{s′} 𝒯(s, a, s′) V_k(s′)] for all s (a synchronous sweep), starting from V₀ = 0. Stop when the largest change is small. In-place updating and the book's θ test go in the notes. This is a dynamic-programming method: a known model, with stored successor values reused. One line, without old DP 23–24's full DP definition. | old DP 6, 27 (fixed); book §4.1 eq. 4.5 and box; Silver L3 PDF 7–8; Sutton DP PDF 3, 6 | 4 |
| E10 | Worked: sweeps on the robot (**protected**) | A table for k = 0, 1, 2, … **Students fill k = 1, 2** (2, 0; 2.8, 1.0); show k = 3, 4 and the limit 3.64 / 1.82. **Interpretation:** V₂(high) = 2.8 is E02's two-step look-ahead. From V₀ = 0, sweep k is the exact expected k-step discounted sum. The model removes sampling noise (M14), and the remaining tail shrinks by γ per sweep (M13). | book §4.1; CS234 L2 PDF 12–13 (one backup at γ = 0.5) | 7 |
| E11 | Why sweeps converge | Subtract the Bellman equation from the update: V_{k+1}(s) − v_π(s) = γ Σ_a π(a ∣ s) Σ_{s′} 𝒯(s, a, s′)[V_k(s′) − v_π(s′)]. The weights are probabilities, so the largest error over states shrinks by at least a factor γ per sweep. Robot check: 3.64 → 1.82 → 0.84 → 0.42 → 0.21 (largest errors). This is a one-line argument, not a proof sequence (see Q5). | old DP 22 (contraction claim, made concrete); Silver L3 PDF 35–40; CS234 L2 PDF 33–44 | 3.5 |
| E12 | The Bellman operator | One sweep applies B_π: (B_π V)(s) = Σ_a π(a ∣ s)[ℛ(s, a) + γ Σ_{s′} 𝒯(s, a, s′) V(s′)]. v_π is its fixed point (B_π v_π = v_π), and E11 says B_π is a γ-contraction (name only). **Why name it:** 2.2 adds a max (the optimality operator), and Week 5 shows how approximation can break this property. | old DP 20, 22 (fixed); notation guide B_π ("used sparingly; finite examples first") | 2.5 |
| E13 | What evaluation buys us, and next | q_{π₁} for every action at both states (table above). **Question:** using always-search's own values (3.6, 1.6), which first action looks best at low? Recharge: 0 + 0.5·3.6 = 1.8 > 1.6. A one-step look-ahead suggests a better policy, which 2.2 develops (improvement, optimality, VI/PI). Everything today needed the model ℳ; Week 3 replaces the expectation with samples. | old DP 43 (full-width backups need the model; one spoken line); Introduction A14a | 3.5 |
| — | Hidden backups (0 min) | (a) Old MDP 61's sequence derivation, corrected. (b) The matrix form and direct solve, if Q4 keeps it off the live slides. (c) Old DP 28–29 or the book's Figure 4.1 gridworld sweeps, as a picture of values spreading over many states (see Q2). | | 0 |

**Targets sum to 53 minutes**, against 58 teaching and 59.5 usable. The 5-minute reserve is intentional: 1.1 and 1.2 grew by 3–4.5 minutes during instructor iteration, and E07/E10 are student-calculation slides that tend to overrun. If the instructor prefers to use it, the candidates are:
- Q3's optimality preview (+4);
- the gridworld visual (+2).

### Timing by segment

| Segment | Slides | Minutes |
| --- | --- | ---: |
| Opening and motivation | E00–E02 | 7 |
| Deriving the equations | E03–E06 | 15.5 |
| Worked backup and direct solution | E07–E08 | 10 |
| Iterative evaluation and sweeps | E09–E10 | 11 |
| Convergence and operator | E11–E12 | 6 |
| Closing bridge | E13 | 3.5 |
| **Total** | | **53** |

## Introductory motivation: checklist per new concept

| Concept | Problem it addresses | Meaning before formalism | Connection | Understanding check |
| --- | --- | --- | --- | --- |
| Transition prediction | Where will a policy take us? | Probabilities pushed forward through 𝒯 | 1.2 model table | Pr{S₂ = high} |
| Bellman expectation equation | Infinite tail and sampling noise (M13/M14) | Value = expected immediate reward + discounted value of the next state | G_t recursion (M10) | Write v(low) |
| v–q relations | Why recharge's value depends on what follows (M16) | Average over actions; one model step | 1.2 q table | q(low, recharge) = 1.82 |
| Backup diagram | Seeing policy vs model branching | Information flows back from successors | M18 question | Which branches are the policy's? |
| Direct solve | Exact values for small MDPs | Linear equations | E07 | 40/11 |
| Iterative evaluation | Large |𝒮|, no closed form with a max | k-step look-ahead | E02 forward sums | Fill k = 1, 2 |
| Contraction / B_π | Does iteration converge, and how fast? | The error shrinks by γ per sweep | E10 numbers | Halving errors |

## Delta against the old decks

Old material for 2.1 is substantial: old MDP 26–33 and 53–64, old DP 1–7 and 20–22. The instructor had already placed old MDP 42–48 and 59–61 here (B11). I treated it as substantial without asking.

| Old slides | Decision | Reason / where its purpose goes |
| --- | --- | --- |
| DP 1 (title) | **Replace** | A21 title format. |
| DP 2 (so far) | **Replace** with E01 | It recaps by listing; E01 recaps 1.2's open question, which motivates the session. |
| DP 3 (prediction vs control) | **Keep** (in E01, reworded) | It frames today vs 2.2. |
| DP 4, MDP 59–60 (prediction equations, v/q relations) | **Keep and fix** → E04/E05 | Convert R, P → ℛ, 𝒯; a ∈ 𝒜(s). MDP 60's q equation is deterministic-only; add the stochastic form. |
| MDP 61 (sequence derivation) | **Fix, hidden backup** | It uses λ for γ, lower-case random variables, and a wrong last line (P(s′, r ∣ s, a) beside ℛ(s, a)). E03 carries the idea live. |
| MDP 26 (MRP value derivation) | **Reuse equation, as v_π** → E03 | It is the cleanest "G_{t+1} → v(S_{t+1})" step, and its index is already R_{t+1}. **Cut** duplicates 29–30, which use the old R_t index. |
| MDP 31–33 (MRP Bellman, matrix form, Silver copies) | **Cut / verbal** → E08 | No separate MRP sequence (consistent with 1.2's exclusion). "Fixing π gives an MRP" was said in 1.2. Matrix symbols: see Q4. |
| MDP 34–35 (caveman MDP) | **Cut** | Replaced by the robot (1.2 decision). |
| MDP 41 (Markov for MDPs) | **Cut** | 1.2 M04 covers it. E03 points to where it is used. |
| MDP 42–48 (two-step North in the gridworld) | **Move to the robot** → E02 | Same reasoning, and it feeds E10's 2.8. Old formula without time indices fixed. The gridworld version is the alternative in Q2. |
| MDP 50–53 (why values, policies, optimal policies, living reward) | **Cut here** | Policies are in 1.2. MDP 52 (living reward) is placed in 2.2 (B11). |
| MDP 54 (MDP search trees, q-state) | **Cut here** | Search-tree framing deferred to MCTS (B11). E06 uses the backup diagram only. |
| MDP 55–58 (horizon, utilities, values) | **Cut** | 1.2 M11–M14 cover them. |
| MDP 62–64 (Q induces a policy; v\*, q\*; optimality equations) | **Move to 2.2** (Q3) | Improvement/VI material. E13 only teases the look-ahead. |
| MDP 65–67 (gridworld V/Q demo; solving MDPs) | **Move to 2.2** | They show optimal values. |
| DP 5–6 (linear solve; iterative synchronous sweeps) | **Keep and fix** → E08/E09 | DP 6 labels the matrix iteration "closed form"; it is the iteration in matrix form. Typo "becomes and MRP". |
| DP 7, 27 (backups; prediction slide) | **Keep diagram, fix** → E06/E09 | Diagram is stochastic, equation deterministic; t and k indices are mixed. |
| DP 8–19 (optimality, VI, VI exercise, policy extraction) | **2.2** | |
| DP 20 (Bellman policy operator) | **Keep, fixed** → E12 | Convert symbols; its vector form only if Q4 says so. |
| DP 21 (optimality operator) | **2.2** | |
| DP 22 (monotone, contraction) | **Make concrete** → E11–E12 | One-line error argument on the robot; monotonicity not needed in 2.1. |
| DP 23–24 (what DP is) | **Compress** to one spoken line in E09 | The DP naming is optional depth. If wanted, place the full slide in 2.2, where VI and PI make "reuse sub-solutions" vivid. |
| DP 28–29 (policy evaluation cartoons) | **Hidden backup** or 2.2 | They show values for a deterministic policy but carry no numbers. The book's Figure 4.1 shows propagation better (Q2). |
| DP 30–42 (improvement, PI, GPI, async) | **2.2** | |
| DP 43–45 (full-width vs sample backups; foreshadowing) | **One spoken line** in E13; full slide in 2.2 or 3.1 | The sampling bridge belongs at the end of Week 2. |

**Reference courses (evidence, not authority):**
- Book §3.5 (eq. 3.14, backup diagrams) and §4.1 (eq. 4.5, in-place sweep, Example 4.1). This is the base.
- Silver L2 PDF 19–23, 30–36 and L3 PDF 7–11. MRP-first derivation, backup diagrams, the gridworld sweeps; contraction is taught at the end of L3.
- CS234 L1 PDF 56–59 and L2 PDF 11–13. "MDP + π = MRP", analytic vs iterative cost, and a one-backup exercise at γ = 0.5 that resembles E10.
- Abbeel l1 PDF 54–57: evaluation as fixed-policy value iteration.
- Sutton slides 7-8-DP PDF 2–6: sweeps, one-array version.

What I took from them:
- the cost argument for iteration (CS234), in E08;
- "evaluation needs the model; samples later" (Silver L3 PDF 32–33), in E13;
- the contraction concept (Silver, CS234), stated concretely in E11 rather than as a proof.

Not adopted:
- an MRP-first derivation (Silver, CS234). Actions are already familiar, and 1.2 excluded a separate MRP sequence.
- the full contraction-mapping proof (scope).

## Old-slide fixes to carry if reused

- R, P, T → ℛ, 𝒯 (notation guide O9/O12); R_t → R_{t+1}; λ → γ (MDP 61).
- MDP 42 formula → Pr{S_{t+1} = s′} = Σ_s Pr{S_t = s} 𝒯(s, a, s′), or with π(s) for a policy.
- DP 7: the stochastic-branch diagram needs Σ_a π(a ∣ s), or a deterministic diagram; use one index (k) for sweeps.
- DP 6: "Closed form" for the matrix iteration is wrong; the closed form is the linear solve.

## Questions for the instructor

- **Q1. Session and deck.** I took the next session to be **2.1 `bellman`**, as a **separate deck** `bellman` (`course/lectures/week02/`). That follows the 1.1/1.2 precedent (B1); the general deck split is still open (brainstorming Q2). Alternative: one DP deck for 2.1–2.2, as in the old deck. *Recommend separate.*
- **Q2. Running example for the transition prediction** (cross-session choice):
  - (a) **Robot** (as above). It continues 1.2 and feeds E10's 2.8; the gridworld first appears in 2.2, which needs it anyway for the living-reward comparison.
  - (b) **The old gridworld exercise** (MDP 37–38, 42–48). It introduces 2.2's grid early (+3–4 min here, saving setup in 2.2) but splits 2.1 across two examples.

  *Recommend (a)*, optionally with one gridworld sweep picture as a hidden backup.
- **Q3. Where the Bellman optimality equation goes.** *Recommend 2.2* (with v\*, q\*, MDP 62–64), next to improvement and VI. 2.1 ends on E13's look-ahead question. Alternative: a 4-minute v\*/q\* and optimality-equation preview at the end of 2.1, which relieves the dense 2.2 and uses most of the reserve.
- **Q4. Matrix form.** Displaying the vector form needs symbols the notation guide does not have (old **P**^π, **R**^π; Silver P^π, R^π). *Recommend* the verbal "|𝒮| equations, |𝒮| unknowns" plus the robot's 2×2 substitution, with the matrix form as a hidden backup. If it should be live, the guide needs an entry (e.g. **v**_π, **r**_π, 𝐓_π); that is an instructor notation decision.
- **Q5. Convergence depth.** E11's one-line error-shrink argument is effectively the γ-contraction argument for B_π. I read the scope's "no full convergence-proof sequence" as excluding the contraction-mapping theorem and VI/PI proofs, not this line. Please confirm, or reduce E11 to the observed halving only (−1.5 min).
- **Q6. Notation for sweep iterates** (guide gap). The book writes the iterates as v_k; the old deck as V_k. The guide has V(s) for tabular estimates "with subscript t when time matters", but no sweep index. *Recommend* V_k(s), with k the sweep number, stated once. If accepted, add it to the guide (instructor approval needed).

## Not included, deliberately

- Asynchronous DP (optional in 2.2), prioritized sweeping, and real-time DP.
- Old DP 32 (Turing Award). It is fine as an aside, but it belongs in neither the 2.1 sequence nor the reserve.
- Advantage functions (Weeks 7–8).
- No new homework, reading or video. The always-search check in E07 is an optional self-check.
