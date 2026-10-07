# Notation guide

**Shared** by Claude and ChatGPT for all lecture, assignment and exam material. Status: draft started 2026-10-05; the instructor confirms changes and resolves the open items at the end. Updated 2026-10-06 (instructor-requested): O_t added; O9 conversions listed; O10–O11 recorded.

Base convention: Sutton & Barto, *Reinforcement Learning: An Introduction*, 2nd ed., "Summary of Notation". Later units add symbols the book does not use; they are listed separately so the base stays recognisable to students who read the book.

**Rule for content authors:** use only symbols defined here. If material needs a symbol that is missing, or a symbol here clashes with another meaning, the old decks, the book or a cited paper, **ask the instructor before inventing or reusing one**, and record the question under "Open items". Do not change this file without instructor approval.

**When to resolve items (instructor, 2026-10-06):** address notation questions when the current content needs them. Future-unit ambiguities do not block earlier material and need not be resolved in advance. Approved contextual reuse, such as action/advantage in O1, does not require repeated approval.

## General

| Symbol | Meaning |
| --- | --- |
| Capital letters (S_t, A_t, R_t, G_t) | Random variables |
| Lower-case letters (s, a, r) | Values of random variables; scalar functions |
| Bold lower-case (**w**, **θ**, **x**) | Vectors |
| 𝔼[·], 𝔼_π[·] | Expectation, with the distribution as a subscript when it matters (always the blackboard 𝔼) |
| Pr{X = x} | Probability |
| ≐ | Equality by definition |
| ← | Assignment, in algorithm boxes and update rules |
| argmax_a | Maximising argument (state the tie-breaking rule when it matters) |

## MDPs, returns and values (Weeks 1–4)

| Symbol | Meaning |
| --- | --- |
| 𝒮, 𝒮⁺ | Non-terminal states; all states including terminal |
| 𝒜(s) | Actions available in s |
| ℛ | Possible rewards |
| t, T | Time step; final time step of an episode |
| S_t, A_t, R_{t+1} | State, action, and the reward that follows them (reward index is t+1) |
| O_t | Observation at time t (book §17.3); distinct from the state S_t the agent keeps (added 2026-10-06) |
| p(s′, r ∣ s, a) | Four-argument dynamics |
| p(s′ ∣ s, a), r(s, a) | State-transition probabilities; expected reward |
| γ | Discount factor |
| G_t | Return following time t |
| G_{t:t+n}, G_t^λ | n-step return; λ-return |
| π, π(a ∣ s), π(s) | Policy; stochastic action probability; deterministic action |
| v_π(s), q_π(s, a) | State/action value under π |
| v_\*(s), q_\*(s, a), π_\* | Optimal values and policy |
| V(s), Q(s, a) | Tabular estimates (with subscript t when time matters) |
| B_π | Bellman operator (used sparingly; finite examples before operator notation) |
| δ_t | TD error |
| U_t | Update target |
| α, ε | Step size; exploration probability of ε-greedy |
| b(a ∣ s) | Behaviour policy (off-policy learning) |
| ρ_{t:h}, ρ_t | Importance-sampling ratio |
| r(π) | Average reward (5-minute continuing-task contrast only) |

## Bandits (Week 9)

| Symbol | Meaning |
| --- | --- |
| q_\*(a), Q_t(a) | True and estimated action value |
| N_t(a) | Number of times a was selected before t |
| c | UCB exploration coefficient |

## Function approximation and deep value methods (Weeks 5–6)

| Symbol | Meaning |
| --- | --- |
| **w**, d | Value-function weight vector; its dimension |
| v̂(s, **w**), q̂(s, a, **w**) | Approximate values |
| **x**(s), **x**_t | Feature vector |
| μ(s) | On-policy state distribution |
| **w**⁻ | Target-network weights (DQN) |
| 𝒟 | Replay buffer or fixed dataset |

## Policy methods (Weeks 7–9)

| Symbol | Meaning |
| --- | --- |
| **θ** | Policy parameters |
| π(a ∣ s, **θ**), π_**θ** | Parameterised policy |
| J(**θ**) | Performance objective |
| b(s) | Baseline (see open item O2) |
| A_t (advantage context) | Time-indexed advantage; distinguish from the action A_t by the locally stated context (O1 resolved) |
| Â_t | Advantage estimate; distinguish an estimate from the underlying quantity when needed |
| λ | λ-return and GAE mixing parameter |
| ρ_t(**θ**) | PPO probability ratio π_**θ** / π_**θ**_old (not r_t, which would clash with reward) |
| ε | PPO clipping range (see open item O4) |

## Offline, model-based and LLM units (Weeks 10–13)

| Symbol | Meaning |
| --- | --- |
| 𝒟 | Fixed dataset |
| p̂(s′ ∣ s, a) | Learned dynamics model |
| H | Planning horizon (MPC) |
| π_ref | Reference policy (LLM KL regularisation) |
| x, y | Prompt; generated response (LLM unit only) |

## Open items: overlaps and ambiguities for the instructor

| # | Clash | Proposal |
| --- | --- | --- |
| O1 | Advantage and action both use A | RESOLVED by instructor, 2026-10-06: contextual distinction is sufficient; A_t is permitted. No alternative letter or restriction to the defining slide is required. State the local meaning when introduced; settle any further function/estimator notation when that material needs it. |
| O2 | b is both the behaviour policy b(a ∣ s) and the baseline b(s) (the book uses both) | Keep both, as the book does; distinguish by arguments. Alternative: π_β for the behaviour policy in the offline unit (as CS285 does) |
| O3 | α is the step size and the SAC entropy temperature | Keep α as step size; temperature symbol to be chosen |
| O4 | ε is ε-greedy and the PPO clip range | Keep both (separate units, context is clear) or use ε_clip |
| O5 | τ is the soft target-update rate and the IQL expectile | Choose one; e.g. τ for the expectile, Polyak rate written explicitly |
| O6 | β is the KL coefficient (LLM unit), the IQL/AWR inverse temperature and the book's average-reward step size | Choose per unit and state it on first use |
| O7 | r is the reward value, r(s, a), the average reward r(π) and the LLM reward model r_φ(x, y) | Keep r(s, a); write the reward model as r_φ(x, y); avoid r(π) beyond the 5-minute mention |
| O8 | Network parameters: the book uses **w** for values, many deep-RL papers use θ for Q-networks and φ/ψ for critics | Follow the book: **w** for value/critic weights, **θ** for the policy |
| O9 | The old decks may use other symbols | Note the differences when slides are reused, and convert or ask. Known conversions (Weeks 1–2 decks, checked 2026-10-06): reward R_t → R_{t+1} (MDP deck slide 3; Intro slide 54); G_t = r_t + γr_{t+1} + … → G_t = R_{t+1} + γR_{t+2} + … (MDP deck slides 22, 24); T(s, a, s′) → p(s′ ∣ s, a) and R(s, a) → r(s, a) (MDP deck slides 11, 36); history H_t (MDP deck slide 4) → see O10; recurrent-state weights W_s, W_o (MDP deck slide 10) clash with **w** and are not planned for reuse |
| O10 | History H_t is not defined here. The book (§17.3) writes H_t = A_0, O_1, …, A_{t−1}, O_t, treating rewards as part of the observation; MDP deck slide 4 writes H_t = O_1, A_1, R_1, …, O_t. H is also the MPC planning horizon (Weeks 10–13) | Needed only if 1.2 reuses MDP deck slides 4/7 with symbols; otherwise say "history" in words. If a symbol is adopted, use the book form and state that rewards are part of the observation; the subscript keeps H_t (history) apart from H (horizon) |
| O11 | The book's recycling robot (Example 3.3) uses α and β as transition probabilities (clashing with the step size α and with O6) and a three-argument expected reward r(s, a, s′), which is not defined here | Applies only if the robot is chosen as the running example. Write numeric probabilities on slides; present the dynamics as p(s′, r ∣ s, a) rows rather than r(s, a, s′); mention the book's symbols only when pointing to Example 3.3 |
