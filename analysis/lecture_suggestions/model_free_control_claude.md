# Week 4 (`control_targets`, sessions 4.1–4.2): initial content suggestion (Claude)

**Claude's step-1 suggestion** (`docs/lecture_workflow.md`, pilot v2), 2026-10-27. Analysis only: nothing here is
accepted. It becomes historical after step 3. No deck decision file exists yet; the instructor's choices will go to
`decisions/lectures/<deck>.md` (deck name: E1 below).

**Scope of this file:**
- the full teaching sequences for 4.1 `control_targets` and 4.2 `control_practice`;
- the old-deck delta for the whole old deck `5 - Model Free Control.pptx` (it spans both sessions);
- early choices the instructor may want to settle before the cross-review (E1–E6).

All numbers are checked by `scripts/check_control_claude.py`.

## Early choices for the instructor

These are the "reasons to pause" items (`docs/lecture_workflow.md`). Each has a recommendation; drafting continues
with the recommendation unless the instructor says otherwise.

| # | Choice | Recommendation | Alternative |
| --- | --- | --- | --- |
| E1 | Deck split and name | One deck for 4.1 and 4.2, as for Weeks 2 and 3 (`bellman` C1, `mc_td` D1). Name: ChatGPT's independent suggestion is filed as `model_free_control` (file name only; I have not read it). I recommend that name, which matches the old deck's title; I used `control_targets` (the first session's id, as for `bellman` and `mc_td`) and will rename this file when the instructor chooses. | `control_targets`, or two decks. |
| E2 | Running examples | 4.1 keeps the **2×2 grid** (B03 model, γ = 0.5) for the lock-in example, the target exercise and the value comparison. Two book examples, each a standalone illustration: windy gridworld in 4.1 (why TD control, Example 6.5) and cliff walking in 4.2 (Example 6.6). The grid cannot show the Sarsa/Q-learning *policy* difference: both reach the same greedy actions there (C15), so the cliff is needed. | Silver's two-doors example (L5 p. 10) instead of the grid lock-in. |
| E3 | 4.2 project activity and admin minutes vs the proposal deadline (1 November, `project_decisions.md`) | Plan as accepted (planning convention: as if on schedule). If 4.2 is delivered after the deadline, the same 15 minutes refine the submitted baseline/metric toward the Week 7 formulation/design milestone, and the 5 admin minutes cover the next milestone and the A1 release instead of proposal expectations. | Move the activity earlier (it would need 4.1 time) or replace it. |
| E4 | ε-greedy improvement argument | The pacing note says "no repeated policy-improvement proof". State the result and give the one-line intuition ("a maximum is at least any weighted average", the only new step beyond B19). Put the book's derivation (eq. 5.2; old slide 16) on a hidden appendix slide. | Derive it live (about 4 extra minutes, from the allowance). |
| E5 | Notation for MC control | Use the constant-step update Q(S_t, A_t) ← Q(S_t, A_t) + α[G_t − Q(S_t, A_t)], so no pair count is needed. The guide has N(s) only; N(s, a) would need approval. | Add N(s, a) (book §5 uses Returns lists; CS234 L4 uses N(s, a)). |
| E6 | Expected Sarsa and Boltzmann exploration | Accepted as **extension, no scheduled time** (`optional_extensions`), although the provisional plan listed them as exposure. Speaker-note pointers only. | Hidden appendix slide for Expected Sarsa (old slide 33). |

## Accepted frame

From `decisions/topic_decisions.yaml` and `output/lectures/session_sources.md` §4.1–4.2.

**4.1 `control_targets`.** 58 teaching minutes (range 50–65), delivery allowance up to 63.
- Worked activity: MC control bridge (about 8 minutes), then a SARSA/Q-learning target comparison.
- Pacing note: no repeated policy-improvement proof; no importance-sampling derivation here.
- Groups:
  - `control` (core; derive / implement / analyze): contrast SARSA and Q-learning on a small exploratory-control
    example; implement a representative tabular control loop with target changes;
  - `mc_control_bridge` (exposure; explain): short MC-to-TD bridge, no implementation;
  - `planning` (GPI reused).

**4.2 `control_practice`.** 53 teaching minutes plus 5 administrative minutes (range 48–63).
- Worked activity: explore a cliff-style target difference; choose a project baseline and evaluation metric
  (15 minutes). I read the 15 minutes as the project part only (the cliff gets its own time below). If the 15 covers
  both, the cliff block shrinks.
- Groups:
  - `control`;
  - `evaluation` (core; analyze): baseline choice, training/evaluation separation, seeds, budgets;
  - `prediction`: the brief data-access taxonomy, revisited.

**Placed elsewhere (not in Week 4) by accepted decisions:**
- importance sampling: 8.2 `ratios`;
- maximization bias and Double Q-learning: 6.2 `dqn_diagnosis`;
- bandits, optimism, UCB, regret: 9.2;
- exploration bonuses: 11.2 `model_exploration`;
- Expected Sarsa, softmax/Boltzmann: extension;
- n-step Sarsa and Sarsa(λ): not in scope; backward traces are existence-only.

The provisional plan's Week 4 list (importance sampling, maximization bias, Double Q-learning) is superseded by these
placements. I do not propose moving any of them back.

**Assessment link.** A1 (release Week 4, prerequisites include `control_practice`) asks students to "implement one
shared epsilon-greedy tabular control loop with SARSA and Q-learning target choices; compare one deliberately chosen
exploratory-control case". The 4.1 algorithm boxes and the 4.2 cliff analysis are its direct preparation. The
Midterm 1 bridge is "work through an unfamiliar backup or diagnose a changed target"; the C14 exercise is of that
form.

## What students already have

From Week 2 (`bellman`):
- **The 2×2 grid** (B03), with exact always-right values (B08a, B21): 14/275, 46/55, 32/275.
- **One-action comparison** (B14): q^π((2,1), up) ≈ 0.80036 vs v^π((2,1)) ≈ 0.11636.
- **The improvement argument:**
  - greedy improvement from v^π needs ℛ and 𝒯 (B18);
  - the policy improvement theorem, proved live (B19, protected);
  - policy iteration, and the improved policy (up, right, up) with values 199/550 and 469/550 (B20–B21r).
- **Q-value iteration** (B24a), with the note "Q-learning uses sampled transitions for this kind of target". This is
  the bridge C12 cashes in.
- **GPI** (B27): "in a few weeks … using experience".
- **B28's questions**: which computations need the model, and which action-selection step can use a learned table.

From Week 3 (`mc_td`):
- the model/online/on-policy taxonomy table (MT03);
- the common update form V ← V + α[U_t − V] with target U_t (MT07);
- first-visit MC and TD(0) algorithm boxes (MT07a, MT09a);
- driving home (MT08); bootstrapping (MT12);
- n-step targets and λ (3.2);
- "Before reporting a winner" (MTE2);
- the MC/TD/n-step reference table, which ends "Next: control with sampled targets" (MT25).

## Is the old material substantial?

**Yes.** `5 - Model Free Control.pptx` (61 slides, 4 hidden) covers both sessions directly. The delta below starts
from it; I did not need to ask.

## Central idea and the motivation thread

Week 3 evaluated a **fixed** policy from experience. Week 4 closes the GPI loop from experience, and two new problems
appear:
1. **Improvement needs action values.** Greedy improvement from V needs the model (B18). From Q it is an argmax
   (B24a/B28). So we estimate Q.
2. **The data now depends on our own choices.** A greedy learner can stop trying an action whose estimate is wrong
   and never find out (C05). Exploration has a cost, and the two TD targets account for that cost differently. That
   difference is the thread from 4.1's exercise to 4.2's cliff and its evaluation question.

The one update form from Week 3 carries over unchanged:

  Q(S_t, A_t) ← Q(S_t, A_t) + α[U_t − Q(S_t, A_t)].

MC, Sarsa and Q-learning differ only in U_t. Each target is a sample of a Bellman equation students already know:

| Method | Target | Bellman equation it samples |
| --- | --- | --- |
| MC control | G_t | definition of q^π |
| Sarsa | R_{t+1} + γQ(S_{t+1}, A_{t+1}) | expectation equation for q^π |
| Q-learning | R_{t+1} + γ max_a Q(S_{t+1}, a) | optimality equation for q^\* (B24a) |

**Explicit motivation time** (`bellman` retrospective; memory "motivation first"). About 20 of 4.1's 57.5 minutes
(C02, C03, C05, C06, C09, C15 and the derivation half of C12) go to "why" before "how":
- C02: how would you learn to act without a model?
- C03: why Q;
- C05/C06: why explore;
- C09: why not wait for the episode;
- C12: where the Q-learning target comes from;
- C15: what each method learns.

4.2 is mostly analysis: why the two targets behave differently, and why "which is better" depends on the measure.

## Teaching sequence for 4.1 `control_targets` (slide level, unpolished)

Slide IDs are proposals. Minutes are planning targets. "Old N" means `5 - Model Free Control.pptx` slide N (PPTX
numbering; the PDF omits hidden slides 2, 3, 9 and 22).

| ID | Slide | Content and reason | Sources | Min |
| --- | --- | --- | --- | ---: |
| C00 | Title | Title Slide layout: course name; **Model-Free Control** / instructor / Fall 2026. | deck title format | 0.5 |
| C01 | So far | Week 2: GPI with a model (B27). Week 3: evaluate a fixed π from samples (MT25). Missing: improve the policy without the model. | B27, MT25, old 7 (roadmap idea) | 2 |
| C02 | Brainstorm: learning to act without a model | Students propose. Prompts: (1) the grid again, model hidden, but the agent now chooses actions; (2) what changes when your choices decide which data you see? Collect answers; return to them in C06 and C13. Replaces old 4–5's bullet lists with a question (instructor added brainstorm slides in Week 2, B00b). | old 4–5 (content in notes), B00b format | 3 |
| C03 | Why Q, not V | Greedy improvement from v^π needs ℛ(s, a) and 𝒯(s, a, s′) (B18 formula recalled). From Q, π′(s) = argmax_a Q(s, a): no model. Price: one estimate per state–action pair, so data is needed for every action. Check: "which B28 question did this answer?" | old 10 (converted to ℛ, 𝒯, superscripts), book §5.2 opening, Silver L5 pp. 7–8 | 3 |
| C04 | GPI with sampled returns | Book §5.3 GPI picture: evaluation = average returns after visits to (s, a); improvement = greedy in Q, per episode. The policy improvement theorem (B19) applies unchanged; no reproof. Constant-α MC update for Q (E5). | old 8 and 13 (diagram), book §5.3 printed 97–98 / PDF 119–120, Silver L5 p. 6 | 2 |
| C05 | Would greedy work? | **Grid lock-in.** Q table so far: Q((2,1), right) ≈ 0.12, the other actions at (2,1) still 0 (never tried). Greedy keeps choosing right. Up is never tried, although choosing up once is worth ≈ 0.80 under the same continuation (B14). Students answer: what would make the learner try up? Click: "exploration vs exploitation". Notes: the 0.12 is q^π((2,1), right) under always-right, 32/275; a noisy estimate can dip below 0 and escape, so lock-in *can* happen, not *must*. Zero initialization with negative living rewards makes untried actions look good: accidental optimism (Week 9). | old 13 ("would this work?"), B14 numbers, book §5.3 end | 3 |
| C06 | Exploration vs exploitation | Old 14 cartoon (CS188). Two ways to keep visiting all pairs: exploring starts (start anywhere, with any first action: possible in simulators, rarely on a robot), or keep choosing every action with some probability. The latter has two forms: **on-policy** (the policy that acts is the one improved) and **off-policy** (learn about greedy while acting exploratorily; later today). | old 14, book §5.3 ES box / §5.4 opening printed 100 / PDF 122 | 2 |
| C07 | ε-greedy | π(a ∣ s) = 1 − ε + ε/∣𝒜(s)∣ for the greedy action, ε/∣𝒜(s)∣ otherwise. Check: ε = 0.1, four actions → 0.925 and 0.025 each. ε-soft: every action ≥ ε/∣𝒜(s)∣. Tie-breaking rule stated. | old 15 (equation reused; m → ∣𝒜(s)∣), book §5.4 printed 100 / PDF 122 | 3 |
| C08 | On-policy MC control | Algorithm box (book p. 101, constant-α version). Result, stated (E4): an ε-greedy policy w.r.t. q^π is at least as good as any ε-soft π. So MC control approaches the best ε-soft policy, not π^\*. To approach π^\*, decay ε while still visiting every pair (GLIE; e.g. ε_k = 1/k). Hidden appendix: eq. 5.2 derivation (old 16). | old 16–18 (remark on "explores the whole space" qualified), book §5.4 printed 101–102 / PDF 123–124, Silver L5 pp. 12–16, CS234 L4 pp. 19–21 and 29–31 | 3 |
| C09 | Why not wait for the episode? | Windy gridworld (old 25 images). The book's point: MC control is hard to use here, because a policy that never reaches the goal gives an episode that never ends. TD learns *during* the episode that the policy is bad. Callback to driving home (MT08). Other TD advantages carried from MT25 (online, often lower variance). | old 19 and 25, book Example 6.5 printed 130 / PDF 152 | 3 |
| C10 | Sarsa: TD on action values | Week 3's TD(0) target with Q in place of V: U_t = R_{t+1} + γQ(S_{t+1}, A_{t+1}). It is a one-sample estimate of the Bellman expectation equation for q^π (B07). Name from the quintuple (S_t, A_t, R_{t+1}, S_{t+1}, A_{t+1}). Q(terminal, ·) = 0. The next action is chosen by the same ε-greedy policy *before* the update, so Sarsa is on-policy. | old 21 and 23 (R_t → R_{t+1}), book §6.4 eq. 6.7 printed 129 / PDF 151, Sutton slides 11-12-TD pp. 34–36 | 5 |
| C11 | Sarsa algorithm | Book box (p. 130), rebuilt as editable text. Order: take A, observe R and S′, choose A′, update, shift. Convergence (spoken): Sarsa reaches π^\* and q^\* with GLIE exploration and Robbins–Monro step sizes (MT07 footnote). With constant ε it settles near the best ε-greedy policy. | old 23–24, book p. 130 / PDF 152 | 2 |
| C12 | Q-learning: sampled Q-value iteration | Recall B24a: Q_{k+1}(s, a) ← ℛ(s, a) + γ Σ_{s′} 𝒯(s, a, s′) max_{a′} Q_k(s′, a′). Replace the expectation with the one transition observed: U_t = R_{t+1} + γ max_a Q(S_{t+1}, a). Act ε-greedily. Q approaches q^\* whatever the behaviour, provided every pair keeps being updated and step sizes decay suitably. Finite-time behaviour still depends on the behaviour policy. Book box (p. 131). | old 40–43 (claims qualified), B24a, book §6.5 eq. 6.8 printed 131 / PDF 153, Abbeel L2 pp. 5–10, CS234 L4 p. 37 | 5 |
| C13 | Behaviour and target policies | Behaviour b(a ∣ s) generates the data; the target policy π is the one whose values the target estimates. Sarsa: b = π (both ε-greedy). Q-learning: b ε-greedy, π greedy. Why the one-step Q-learning target needs no correction: Q(S_t, A_t) already conditions on the action taken, and the next action is evaluated by π (the max), not sampled from b. Off-policy prediction from sampled returns needs ratio corrections: Week 8. Update MT03's row with these two examples. | old 6 and 32 (μ → b; "target should be π^\*" removed), old 40 ("IS not required" reason clarified), MT03, book §§5.4, 6.5, Exercise 6.11 | 3 |
| C14 | Your turn: two targets, one transition | **Protected worked comparison.** Grid, γ = 0.5, α = 0.5, Q((1,1), up) = 0.20. Row for (1,2): up 0.45, right 0.85, down 0.25, left 0.36. Transition: (1,1), up, −0.04, (1,2); ε-greedy then samples A′ = down (exploratory). (a) Sarsa: U = −0.04 + 0.5(0.25) = 0.085, giving Q = 0.1425. (b) Q-learning: U = −0.04 + 0.5(0.85) = 0.385, giving Q = 0.2925. (c) Next transition: (1,2), right, +1, goal: both targets are 1. (d) When would the two targets agree on a nonterminal step? When A′ is greedy. About 2 minutes setup, 5 minutes student work, 3 minutes discussion: Sarsa's target charges the exploratory action to (1,1), Q-learning's does not. | constructed (row = q^\* rounded, `check_control_claude.py`), A1 task, MT1 exam bridge | 10 |
| C15 | Which values does each learn? | Constant ε = 0.1 on the grid. Sarsa settles near the best ε-greedy policy's values: (1,1) 0.332, (2,1) and (1,2) 0.811. Q-learning settles near q^\*: 0.362, 0.853, 0.853. **The same greedy actions** (up, up, right). So here the target choice changes the values, not the behaviour. Question for next time: when would the two choose different paths? | `check_control_claude.py`, book §§6.4–6.5 | 3 |
| C16 | DP and TD side by side | Native table in course notation: iterative policy evaluation ↔ TD(0); Q-policy iteration ↔ Sarsa; Q-value iteration ↔ Q-learning. Full expected backups need the model; sampled backups need only experience. | old 50–51 (Silver images replaced by a native table in course notation), Silver L5 pp. 41–42 | 3 |
| C17 | Recap and next | Three targets, one update form; ε-greedy; on- vs off-policy in one sentence each. Next: where exploration is costly (cliff), failure modes, project baseline. | old 20 (recap purpose) | 2 |

**Sum: 57.5 minutes** against the 58-minute allocation. MC bridge: C04 + C06 + C08 = 7 minutes, plus the MC half of
C05, about 8. Exploration and ε-greedy (control group): C05 + C07 = 6. TD control and the targets: C09–C16 = 34, of
which 10 are the protected exercise. Nothing uses the delivery allowance; the instructor may spend up to 5 more
minutes on motivation (e.g. E4's live derivation or a longer C02).

## Teaching sequence for 4.2 `control_practice`

| ID | Slide | Content and reason | Sources | Min |
| --- | --- | --- | --- | ---: |
| P00 | Section opener | No second title slide (as `bellman` B17). | — | 0.5 |
| P01 | Which target? | Retrieval: a fresh grid transition; pairs say which next action each method uses and why that makes one on-policy. | C10–C14 | 3 |
| P02 | Cliff walking: predict first | Book Example 6.6 picture (old 44, left image). −1 per step; −100 and back to start on entering the cliff; undiscounted; ε = 0.1. Vote before the reveal: which path does each method learn, and which earns more reward *while learning*? | old 44, book Example 6.6 printed 132 / PDF 154 | 3 |
| P03 | Why the edge is costly under ε-greedy | Each step along the edge falls with probability ε/∣𝒜∣ = 0.025. Expected return from the start under ε-greedy (exact, γ = 1): around the edge path −51.8 (greedy return −13); around the top path −22.3; best ε-greedy policy −20.7. Sarsa's sampled A′ is sometimes "down", so its targets include the falls. Q-learning's max never does. This is the worked target difference. | `check_control_claude.py`, book §6.5 | 5 |
| P04 | What the book's run shows | Old 44 right image (online reward per episode: Sarsa about −25, Q-learning about −50, consistent with −20.7 and −51.8 above). Q-learning's *greedy* policy is the optimal −13 path. Old 44's questions: (a) decaying ε? Both approach the optimal path. (b) Slips in the motion? Then the edge is risky even for a greedy agent: q^\* itself changes, and Q-learning also moves away. | old 44 (image and notes), book Example 6.6 | 3 |
| P05 | Which one "wins"? | It depends on the measure: return during training, the final greedy policy's return in separate evaluation episodes, or the number of falls during learning. Three short cases for pairs: a game simulator where only the final policy matters; a robot learning on the job near stairs; a policy trained in simulation and then deployed. Ties back to MTE2 ("Before reporting a winner") and training/evaluation separation (evaluation group). | MTE2, accepted `evaluation` scope | 6 |
| P06 | Tabular control failure modes | A table of symptom → likely cause → check: (1) an action is never tried: greedy, ε = 0 or ε decayed too fast; check visit counts per pair (C05). (2) Good greedy policy, poor training return: exploration cost (cliff); evaluate separately. (3) Never settles or keeps thrashing: constant ε or large α; use GLIE decay or step-size schedules (MT07). (4) Very slow learning: small α, long horizons, sparse reward. (5) High-return but unintended behaviour: reward specification (B26). (6) One run says X: seed variance; compare seeds and intervals (MTE1). One line on (7): values too high in noisy problems, maximization bias, Week 6. Smarter exploration: Weeks 9 and 11. | old 18, 43–44, 53 (pointer only); B26; MTE1–MTE2 | 8 |
| P07 | Your turn: diagnose | Three short cases (a visit-count table with zeros; a training-curve-only comparison; a constant-ε curve that never stops fluctuating). Pairs name the likely cause and the check. Course-generated or described in text; no new long experiment. | constructed | 4 |
| P08 | Learning from others' data | Revisit MT03. Q-learning's target does not depend on b, so data could come from demonstrations, older policies or logs. But only pairs present in the data are learned: untried actions keep their initial values, and the max can choose them. Forward pointers: the deadly triad (Week 5, off-policy + bootstrapping + approximation) and offline RL (Week 12). Prediction-group revisit of the data-access taxonomy. | MT03; accepted `prediction` and `offline_concepts` scopes | 3 |
| P09 | Project: question, baseline, metric | **Protected worked activity (15).** 3 minutes worked example: the cliff as a mini project, with question, baseline (Sarsa), compared method (Q-learning), metric (greedy evaluation return *and* training falls), budget (episodes, seeds). 8 minutes: teams fill a one-slide template for their own project (question; what the agent controls; one baseline, which may be simple, random or heuristic; one primary metric and when it is measured; budget). 4 minutes: two or three teams share. Framing depends on E3. | accepted `control_practice` worked activity, `project_decisions.md` proposal / formulation_design scope | 15 |
| P10 | Recap and next | Target choice changes what is learned and what is measured. Next week: tables do not scale, so we approximate (Week 5). | — | 2 |
| P11 | Administration (5 min, separate) | Proposal expectations, or the next milestone if after the deadline (E3); A1 release pointer. | accepted 5 admin minutes | (5) |

**Sum: 52.5 teaching minutes** against 53, plus 5 administrative minutes (57.5 of 58). The cliff analysis (P02–P05) is
17 minutes; failure modes and diagnosis 12; the project activity 15.

## Delta against `5 - Model Free Control.pptx`

Keep = reuse the slide (copy natively) with the listed fixes. Notation fixes throughout: R_t → R_{t+1}; μ → b; m →
∣𝒜(s)∣; Q^{π_t} and q_π → course superscripts; ε missing from some text runs (font glyph) to be retyped.

| Old slides | Decision | Where / why |
| --- | --- | --- |
| 1 | Replace | Course title format (C00). |
| 2–3 (hidden: TD(λ) recaps) | Cut | λ was introduced in 3.2; backward traces are existence-only (accepted). |
| 4–5 (Active RL; why model-free control) | Fix → C02 notes | Turned into the brainstorm. Old 4's "this is NOT offline planning" clashes with the course's online/offline meaning (MT03); rephrase as "acting in the world, not planning with a model". |
| 6, 32 (on/off-policy) | Move → C13 | After Sarsa and Q-learning, where it is concrete. Remove "target should mostly be π^\*" (MT03 notes: the target need not be optimal). |
| 7 (prediction vs control list) | Cut | C01 and MT25 cover the roadmap. |
| 8 (GPI recall) | Keep → C04 | Diagram continuity with B27. |
| 9 (hidden), 10 (can we use TD/MC?) | Keep 10 → C03 | Equation converted to ℛ, 𝒯. |
| 11–12 (policy improvement theorem) | Cut | Proved in 2.2 (B18–B19); "no repeated proof". One sentence in C04. |
| 13 (GPI with MC; would greedy work?) | Keep → C04/C05 | Question kept; the abstract answer is replaced by the grid lock-in. |
| 14 (exploration cartoon) | Keep → C06 | CS188 image, as in the old deck. |
| 15 (ε-greedy) | Keep → C07 | Equation reused. |
| 16 (ε-greedy improvement and proof image) | Statement → C08; proof → hidden appendix | E4. |
| 17–18 (MC control; remarks) | Keep → C08 | Qualify "guaranteed to explore the entire state-space and improve your policy at each step": improvement holds with exact evaluation, among ε-soft policies. |
| 19 (TD control idea) | Merge → C09 | — |
| 20 (where were we) | Cut | Recaps C01/C17. |
| 21 (three TD targets) | Keep → C10/C12 | Expected Sarsa line moves to notes (E6). |
| 22 (hidden), 23–24 (Sarsa, book box) | Keep → C10/C11 | Convergence remark completed: also needs GLIE exploration and infinite visits, not only decaying α. |
| 25 (windy gridworld) | Keep → C09 | Add the book's "MC cannot easily be used here" point. |
| 26–31 (n-step Sarsa, Sarsa(λ), comparison) | Cut | Already skipped in the old course; not in scope. One spoken line: n-step targets work for Q too. |
| 33 (Expected Sarsa) | Notes only | Extension (E6). |
| 34–39 (off-policy prediction, importance sampling) | Move → 8.2 `ratios` | Accepted placement. For Week 8, fix: old 37's ratio product runs to π(a_T ∣ s_T), but should end at T − 1; old 35/39 write state-probability ratios P^π(s_t)/P^μ(s_t) where trajectory or action ratios are meant. |
| 40–43 (Q-learning, off-policy control, box, properties) | Keep → C12/C13 | Qualify old 43's "in the limit, it doesn't matter how you select actions": that holds only if every pair keeps being visited; finite-time learning depends on the behaviour. |
| 44 (cliff walking) | Keep → P02–P04 | Notes answer (learns the optimal path but falls during exploration) is kept; P03 adds the numbers. |
| 45 (empty "Q-learning recap") | Cut | Tablet placeholder; C17/P01 replace it. |
| 46–48 (maximization bias, Double Q) | Move → 6.2 `dqn_diagnosis` | Accepted placement; one forward line in P06. |
| 49 (other off-policy methods) | Cut | Tree backup and Q(σ) are out of scope. |
| 50–51 (Silver DP/TD tables) | Rebuild → C16 | Native table in course notation. |
| 52 (afterstates) | Cut | Out of scope; could be an optional appendix if the instructor wants it. |
| 53–61 (exploration strategies, Boltzmann, exploration functions, optimism, regret) | Move | Optimism, UCB and regret → 9.2; exploration bonuses → 11.2; Boltzmann → extension. One pointer line in P06. |

Teaching purposes of removed material are kept elsewhere: the improvement argument in 2.2; λ in 3.2 and 8.1;
importance sampling in 8.2; maximization bias in 6.2; principled exploration in 9.2 and 11.2.

## Other sources used

- **Book** (main reference):
  - §5.3 (MC ES, GPI with Q) printed 97–100 / PDF 119–122;
  - §5.4 (ε-soft control, eq. 5.2) printed 100–103 / PDF 122–125;
  - §6.4 (Sarsa, Example 6.5) printed 129–131 / PDF 151–153;
  - §6.5 (Q-learning, Example 6.6, Exercises 6.11–6.12) printed 131–132 / PDF 153–154.
- **Silver L5:**
  - pp. 6–9: model-free policy iteration with Q;
  - pp. 10–16: two doors, ε-greedy improvement, GLIE;
  - pp. 35–40: Q-learning, cliff;
  - pp. 41–42: DP/TD relationship.
- **CS234 L4:**
  - pp. 17–21: exploration problem, ε-greedy improvement;
  - pp. 29–31: GLIE;
  - pp. 34–38: on/off-policy, Q-learning convergence conditions.
- **Abbeel L2** pp. 5–10: Q-learning as Q-value iteration with samples; the same bridge as B24a.
- **Sutton slides** 11-12-TD pp. 34–39: Sarsa and Q-learning.
- **Previous homework** Comp438Spring2025Hw1a pp. 3–8: MC control and Q-value iteration agents. Its starter code is
  the A1 reuse base (`assignment_decisions.md`).

## Notation needs

Everything uses the guide's existing symbols: Q(s, a), q^π, q^\*, b(a ∣ s), ε, α, U_t, δ_t, 𝒜(s), ℛ, 𝒯. Two items:
- N(s, a) is avoided by E5. It would need approval if the instructor prefers sample means.
- ∣𝒜(s)∣ for the number of actions is set-cardinality notation, not a new symbol.

No conflict found with the book or the reused old equations after the conversions listed above.

## Correctness notes (for the cross-review)

- **C05 lock-in.** 0.11636 = q^π((2,1), right) under always-right; up scores 0.80036 under the same continuation (B14).
  Lock-in is possible, not certain: one sampled target, a left slip to (1,1), is −0.04 + 0.5·Q((1,1), ·), which can be
  negative.
- **C14 snapshot.** The (1,2) row is q^\* rounded to 2 places (exact: 0.44773, 0.85273, 0.25136, 0.36182).
  Q((1,1), up) = 0.20 is an arbitrary in-progress value, not a learned one.
- **C15 values.** The best ε-greedy (ε = 0.1) policy's greedy actions are (up, up, right), the same as one optimal
  deterministic policy. (1,1) has an up/right tie under q^\*; break the tie toward up, as B21r did.
- **P03 cliff values.** Exact linear solves on the 4×12 cliff under the book's rules. The "best ε-greedy" value comes
  from value iteration on the environment with ε moved inside (book §5.4). The book's curves are single smoothed runs,
  so only approximate agreement with −20.7 and −51.8 should be claimed.
- **Sarsa and greedy action selection** (book Exercise 6.12): with greedy selection, Sarsa and Q-learning are almost
  the same but not identical. Sarsa chooses A′ before the update, so when S′ = S the two can differ. This is a speaker
  note for P01, not a slide.

## Open questions and limitations

- **E1–E6** above.
- **Old 44's image.** It is a raster of the book's Figure 6.4 region. I have not checked its resolution for reuse.
- **Calendar.** The schedule's lecture weekdays are unresolved (`schedule_decisions.yaml`), and 29 October is a
  holiday. The sessions' real dates relative to the 1 November proposal deadline are unknown to me, hence E3.
- **ChatGPT's suggestion** (`model_free_control_chatgpt.md`) exists, but I have not read it. The mutual cross-review
  is the next step, in one shared review file under the chosen deck name.
