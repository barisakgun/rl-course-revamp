# MDPs, returns and values: Claude's initial content suggestion (session 1.2)

**[Claude 2026-10-07]** Initial content suggestion for the second pilot round, written **without reading ChatGPT's 1.2 suggestion or the 1.2 review file**. The only ChatGPT input seen was the three open-item rows (P1–P3) in the shared decision file `decisions/lectures/mdp_values.md`. This is a recommendation, not an accepted decision.

**Accepted frame:**
- Session `mdp_values`: 58 minutes; worked activity "compute returns and define a policy/model/value on the running MDP".
- Group `formulation`: core; explain, analyze. Representation and partial observability remain conceptual; no Bellman equations (2.1).
- Deck decisions B1–B6.
- **Starting point:** the accepted 1.1 deck. 1.1 introduced the model (figure with 0.8/0.7), "Returns?" on two example trajectories, observation vs state, and no symbols. Per B6, 1.2 makes all of this formal and introduces the symbols. Timing follows the plan-as-if-on-schedule convention.

All numbers below were checked by solving the MDP: γ = 0.5; search +2 on success; failed low search −3 total; wait 0; recharge 0.

## Key choices (for the comparison)

| # | Choice | Claude's suggestion |
| --- | --- | --- |
| K1 | Order | **Straight to MDPs, no Markov-chain/MRP warm-up.** The robot already has actions; the book and Sutton's slides go straight to MDPs (Silver and the old caveman sequence go Markov process → MRP → MDP). One line, "an MDP plus a fixed policy is a Markov reward process", bridges to 2.1 policy evaluation. Saves about 8 minutes. |
| K2 | Model presentation | **The instructor's 1.1 figure** (copied natively from the accepted deck) plus **one table p(s′, r ∣ s, a)** with the numbers. Derive **one** expected reward: r(low, search) = 0.7·2 + 0.3·(−3) = **0.5**. |
| K3 | Returns | γ = 0.5 on the **same two 1.1 trajectories**, computed backwards with G_t = R_{t+1} + γG_{t+1}. Then a **tail bound**: the unseen future can change G_0 by at most 0.375. This answers 1.1's "Returns?" question. |
| K4 | Terminal version (P1) | **Terminal reward −3, the same as the rescue penalty**, so the only difference is termination. The point needs no computation: termination forfeits future rewards. 1.1's "−10" was a spoken example; −10 can be mentioned as a design choice. |
| K5 | Values | Define v_π and q_π as expected returns. **Show** (not derive) the exact values as a teaser for 2.1, and contrast them with the sampled returns. |
| K6 | Markov property | The old slide's sequence form, with no history symbol. Diagnose question: battery ageing. The history symbol (B5) stays optional: use it only if the instructor runs the "no gauge" aside, after approving O10's form. |

## Teaching sequence (56 of 58 min)

| Min | Segment | Content | Sources / reuse (old `2 - Markov Decision Processes.pptx`, PPTX numbers) |
| --- | --- | --- | --- |
| 5 | From story to symbols | Recap the robot with the 1.1 figure. The interaction loop with S_t, A_t, R_{t+1}, S_{t+1}, and why the reward index is t+1. A trajectory S_0, A_0, R_1, S_1, … as the 1.1 example sequences rewritten in symbols. | 1.1 deck figure slide (instructor's native figure). Old **3** (edit: S_t, R_{t+1}; observation in words). |
| 7 | Markov property | "The future depends on the past only through the present state (and action)." Written with explicit sequences of states and actions. Diagnose question Q1 (battery ageing). Optional aside, if time and O10 are settled: no gauge → the agent's state must come from the history. | Old **7** (equations: convert P → Pr; keep the S/A sequence form). Old **4/5** only for the optional aside. Old **8** (higher-order) as backup. |
| 9 | The MDP and its model | Definition: 𝒮, 𝒜(s), ℛ, p(s′, r ∣ s, a), γ. Robot table with the numbers; p(s′ ∣ s, a) and r(s, a) derived from it; worked example r(low, search) = 0.5. Note: 𝒜(high) has no recharge, which shows why 𝒜 depends on s. | Old **36** (convert T, R(·) to p, r) and **11** (convert T(s, a, s′) → p(s′ ∣ s, a), R(s, a) → r(s, a), and P(S_{t+1}, R_t ∣ …) → p(s′, r ∣ s, a)). New table slide. |
| 14 | Returns and discounting | Episodic vs continuing tasks. G_t for both. Discounting and why: the old slide's reasons, plus γ = 0.5 "not the norm" (B4). Worked activity Q2 (below). Recursion G_t = R_{t+1} + γG_{t+1}. Bound \|G\| ≤ 3/(1 − γ) = 6. | Old **21** (finite horizon, discounting, absorbing state), **22** (convert to G_t = R_{t+1} + γR_{t+2} + …), **23** (why discount), **24** (keep its worked-example structure; replace the caveman numbers with the robot's). |
| 6 | Terminal-state version | "Out of battery" replaces the rescue: a terminal state, absorbing with reward 0 afterwards (book §3.4 unified notation). Q3 (can we compare without discounting?) and Q4 (rescue vs termination). | Old **21** (absorbing state, B3 anchor). A redrawn figure with the terminal state, drawn natively; the instructor may draw it live instead. |
| 4 | Policies | Deterministic π(s) and stochastic π(a ∣ s), e.g. at low: recharge 0.9, search 0.1. The two 1.1 strategies as policies. Stochastic parameterisation waits for policy gradients (scope note). | Old **50** (convert to π(a ∣ s), π(s)). |
| 9 | Values | v_π(s) = 𝔼_π[G_t ∣ S_t = s], q_π(s, a) = 𝔼_π[G_t ∣ S_t = s, A_t = a]. A value is the average return over many days, so averaging sampled returns estimates it (preview of Monte Carlo in Week 3). Teaser table and Q5. Relation v_π(s) = Σ_a π(a ∣ s) q_π(s, a). Stop before the one-step recursion: that is 2.1. | Old **58** (value definitions: convert V_π → v_π, Q_π → q_π, r → R_{t+k+1}). Old **59** (keep only v = Σ π q; cut the q = r + γ Σ p v line, which belongs to 2.1). Old **25** (estimate by averaging many runs). |
| 2 | Recap and bridge | The worked activity is done: model, policy, return, value. Next: how to *compute* v_π (2.1, Bellman). | New. |

The 2 minutes of slack absorb the optional history aside, or Q-value questions.

### Worked activity and diagnose questions (with intended answers)

**Q1 (Markov).** A worn battery drains faster as it ages. Is {high, low} still a Markov state?
*Intended:* no. The transition probabilities then depend on battery age, which the state doesn't contain. Either add age to the state or accept an approximation. A state must contain whatever changes the future dynamics.

**Q2 (returns, the worked activity).** With γ = 0.5, compute G_0 for the two 1.1 trajectories, backwards.

| Trajectory | Rewards | G_3 | G_2 | G_1 | G_0 |
| --- | --- | ---: | ---: | ---: | ---: |
| Always search | 2, 2, −3, 2 | 2 | −2 | 1 | **2.5** |
| Search when high, recharge when low | 2, 2, 0, 2 | 2 | 1 | 2.5 | **3.25** |

How much can the unseen future change G_0? At most 3·0.5⁴/(1 − 0.5) = **0.375**, so with discounting the excerpt nearly fixes this sample's return. But it is still one sample.

**Q3 (episodic vs continuing).** In the terminal version, "always search" eventually ends, but "search when high, recharge when low" never does. Can we compare their returns with γ = 1?
*Intended:* no. The never-ending policy's undiscounted return grows without bound. Discounting (or, later, the average-reward view: a 5-minute contrast in 3.1) makes both finite. Making the terminal state absorbing does not bound a policy that never reaches it.

**Q4 (rescue vs termination, same −3).** Under "always search", is the value at low higher with rescue or with termination?
*Intended:* with rescue. Termination forfeits all future rewards, so it's worse even with the same immediate penalty. Teaser numbers: 1.60 with rescue, **0.77** with termination; computing them is 2.1.

**Q5 (sample vs expectation).** Teaser table, exact values computed in 2.1:

| v_π | high | low |
| --- | ---: | ---: |
| Always search (rescue) | 3.60 | 1.60 |
| Search when high, recharge when low | **3.64** | **1.82** |

Our sampled days gave 2.5 vs 3.25, a large gap. Why are the values at high nearly equal?
*Intended:* a value averages over all days. Our sample happened to fail the low search. The real difference shows at low, where recharging avoids the risk. (The second policy is also the optimal one under these numbers, Introduction A14a; this is a good hook for 2.2.)

## Main teaching difficulties

1. **Sampled return vs value** (G_t is random, v_π is its expectation): Q2 → Q5.
2. **Episodic vs continuing, and why the terminal state doesn't remove the need to discount:** Q3, Q4.
3. **Symbol load:** 1.2 introduces about ten symbols at once. Introduce each on the robot and reuse the 1.1 trajectories, so the symbols name things students have already seen.

## Changes and tradeoffs vs the old MDP deck

- **Cut:**
  - caveman Markov process → MRP sequence (14–20, 24–35 as content), replaced by the robot;
  - MRP Bellman and matrix solution (26–33): 2.1;
  - gridworld (37–48, 51–52, 65–66): 2.2;
  - optimal values and Bellman optimality (62–64): 2.2;
  - learning vs planning (12–13): covered in 1.1;
  - the recurrent state-update equation (10): partial observability stays conceptual;
  - stationary-preferences theorem (20): optional, low value here.
- **Reused with notation conversions:** 3, 7, 11, 21, 22, 23, 24 (structure), 25, 36, 50, 58, 59 (partly). These are native equations, per the equation-reuse convention.
- **New:** robot model table, terminal-state figure, trajectory/return table, teaser value table.
- **Time:** 56/58, within budget. The risk is the 14-minute returns block; if it runs long, compute only one trajectory's G_0 live and give the other.
- **No change to scope, mastery, minutes or assessment.** It prepares MT1 (returns and definitions) and A1 (supplied small MDP).

## Positions on the open items

- **P1:** −3 terminal reward (K4). It isolates the effect of termination; −10 conflates termination with a bigger penalty. Mention −10 as a reward-design variant.
- **P2 / history symbol:** no H_t needed for the core content (K6). If the optional "no gauge" aside is used with a symbol, settle O10 first. My earlier proposal stands: the book's form, with the remark that rewards are treated as part of the observation.
- **P3:** agree that the accepted wording should read **successful search +2; a failed low-charge search gives −3 in total** (no +2 on that transition). This matches the figure, the trace and the book; the instructor's "every search +2" meant success at high or low.

## Notation needed (all in the guide unless marked)

S_t, A_t, R_{t+1}, G_t, γ, T, 𝒮, 𝒮⁺, 𝒜(s), ℛ, p(s′, r ∣ s, a), p(s′ ∣ s, a), r(s, a), π(a ∣ s), π(s), v_π, q_π, 𝔼_π, Pr. Not needed: H_t (O10, optional aside only).

Old-slide conversions (guide O9, plus new ones found here):
- P(·) → Pr{·} or p(·);
- V_π, Q_π → v_π, q_π (capitals are estimates in the guide);
- lowercase r_{t+k} with old indexing → R_{t+k+1}.
