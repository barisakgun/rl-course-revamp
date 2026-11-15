# Assignment 1 — Planning and learning from sampled transitions

**Release:** to be announced. **Due:** two weeks after release. **Submission:** KUHub Learn.

This assignment is individual work. You may discuss ideas, but the code and the answers must be your own. LLM use is allowed under the syllabus rules and must be reported (section 8).

## 1. What you will do

You work on small gridworlds in three parts, and then run five supplied experiments.

1. **Planning with the model:** value iteration and policy iteration.
2. **Prediction from samples:** Monte Carlo and TD(0) on supplied episodes.
3. **Control from interaction:** one ε-greedy loop with SARSA and Q-learning targets.

You write 13 short functions in three files. Everything else is supplied: the environment, the tests, the experiment driver and the plots.

Plan to finish Parts 1 and 2 in the first week, and Part 3 with the short answers in the second.

## 2. Setup

You need Python 3.10 or later.

```bash
python -m pip install -r requirements.txt
```

```bash
pytest
```

All tests fail before you start. They pass one by one as you complete the functions.

If you prefer to work in a notebook, write and try your functions there, then copy them into the `.py` files before you run the tests. In Jupyter, *File → Save and Export Notebook As → Executable Script* produces a `.py` file you can copy from. Only the three `.py` modules are graded.

## 3. Files

| File | What it is | You edit it |
| --- | --- | --- |
| `dp.py` | Part 1 functions | Yes |
| `prediction.py` | Part 2 functions | Yes |
| `control.py` | Part 3 functions | Yes |
| `answers.md` | Three short answers | Yes |
| `llm_report.md` | LLM-use report | Yes |
| `run_experiments.py` | Runs the five experiments with your code | No |
| `rlhw/` | Environment, schedules, drivers, plots | No |
| `tests/` | Public tests with their expected numbers | No |
| `data/` | Episodes for Part 2 | No |

Grading uses clean copies of the supplied files, so changes you make to them have no effect.

## 4. The environment

`rlhw.make_env(name)` returns a Gymnasium environment.

- **States** are cell indices, counted row by row from the top-left cell: `state = row * n_cols + col`.
- **Actions:** 0 up, 1 right, 2 down, 3 left.
- **Movement:** with probability 1 − `slip` the agent moves as intended; with probability `slip`/2 each, it moves in one of the two perpendicular directions. A move into a wall or off the grid leaves the state unchanged.
- **Rewards:** entering the goal or a pit gives that cell's reward, as the total reward of the transition, and ends the episode. Every other transition gives the step reward.
- **Time limit:** a long episode is cut off with `truncated=True`. That is not a terminal state.

`env.reset()` returns `(state, info)`. `env.step(action)` returns `(next_state, reward, terminated, truncated, info)`.

The model is `env.unwrapped.P`: `P[s][a]` is a list of `(probability, next_state, reward, terminated)` tuples. **Only Part 1 may use the model.**

| Name | Grid | Settings | Used for |
| --- | --- | --- | --- |
| `tiny` | 2 × 2 lecture grid | goal +1, step −0.04, slip 0.2, γ = 0.5 | Debugging; not graded |
| `small` | 4 × 3 lecture grid | goal +1, pit −1, step −0.04, slip 0.2, γ = 0.5 | Graded tests |
| `ledge` | 8 × 4, pits along the bottom | goal +1, pit −1, step 0, no slip, γ = 0.95 | Experiments E3–E5 |

```
tiny        small        ledge
. G         . . . G      . . . . . . . .
S .         . # . P      . . . . . . . .
            S . . .      . . . . . . . .
                         S P P P P P P G
```

`S` start, `G` goal, `P` pit, `#` wall. In `tiny` the states are 0 (top-left), 1 (goal), 2 (start), 3 (bottom-right).

Two helpers print tables as grids: `env.unwrapped.format_values(V)` and `env.unwrapped.format_policy(policy)`.

**Ties.** Every greedy choice in this assignment uses `rlhw.argmax_lowest`, which returns the lowest index among the best actions.

## 5. Tasks

Each function has a docstring that states its inputs, outputs and conventions. Read it before you write the function.

### Part 1 — `dp.py`

The supplied `policy_evaluation(P, policy, gamma, theta)` evaluates a deterministic policy and returns `(V, n_sweeps)`.

| Function | What it does |
| --- | --- |
| `q_from_v(P, V, s, gamma)` | One-step lookahead: the action values of state `s` under the table `V` |
| `value_iteration(P, gamma, theta)` | Returns `(V, n_sweeps)` |
| `policy_improvement(P, V, gamma)` | The greedy policy for `V` |
| `policy_iteration(P, gamma, theta)` | Returns `(policy, V, n_improvements, n_evaluation_sweeps)` |

Conventions the tests rely on:

- A transition with `terminated=True` contributes its reward only.
- Value tables start at 0.
- Sweeps are synchronous: every state is backed up from the previous sweep's table.
- Stop after the first sweep whose largest change is strictly below `theta`. That sweep is counted.
- Policy iteration starts from action 0 in every state and stops when an improvement step changes nothing. That step is counted.

### Part 2 — `prediction.py`

An episode is a list of `Transition(state, action, reward, next_state, terminated, truncated)`. The supplied episodes are complete: each ends in a terminal state.

| Function | What it does |
| --- | --- |
| `returns(rewards, gamma)` | The return G_t of every step of an episode |
| `mc_update(V, episode, alpha, gamma)` | Constant-α, every-visit Monte Carlo update from one episode |
| `td0_update(V, s, r, s_next, terminated, alpha, gamma)` | One TD(0) update |

- **Monte Carlo:** compute all returns first, then update in chronological order: V(S_t) ← V(S_t) + α [G_t − V(S_t)]. A state visited twice is updated twice.
- **TD(0):** V(S_t) ← V(S_t) + α [R_{t+1} + γ V(S_{t+1}) − V(S_t)]. When the transition terminates, the target is R_{t+1} alone.

The supplied `rlhw.drivers.run_prediction` applies your kernels over the episode files.

### Part 3 — `control.py`

| Function | What it does |
| --- | --- |
| `init_q(n_states, n_actions, value, terminal_states)` | A Q-table filled with `value`; terminal rows are 0 |
| `epsilon_greedy_probs(q_row, epsilon)` | Action probabilities of the ε-greedy policy |
| `select_action(q_row, epsilon, rng)` | Samples an action from those probabilities |
| `sarsa_target(Q, r, s_next, a_next, terminated, gamma)` | R + γ Q(S′, A′) |
| `q_learning_target(Q, r, s_next, terminated, gamma)` | R + γ max_a Q(S′, a) |
| `train(env, method, gamma, epsilon_schedule, alpha_schedule, q_init, n_episodes, seed, select_fn)` | The shared control loop |

Requirements for `train` (also in its docstring):

- **Schedules.** ε and α come from schedule objects with a `value(k)` method. The clock `k` counts environment transitions over all episodes, starting at 0. The action executed as transition `k` is selected with `epsilon_schedule.value(k)`. The update for transition `k` uses `alpha_schedule.value(k)`.
- **Action selection.** Choose every action with `select_fn(Q[state], epsilon, rng)`. The tests pass their own `select_fn`.
- **SARSA.** Select the next action once, use it in the target, then execute that same action.
- **Termination.** The target is the reward alone.
- **Time limit.** Both methods still bootstrap from the final observation. SARSA selects a next action for its target, with `epsilon_schedule.value(k + 1)`, even though it is never executed.
- **Return value.** `(Q, episode_returns, episode_lengths)`, with undiscounted episode returns.

## 6. Debugging with the 2 × 2 grid

The `debug-` test cases use `tiny` and carry no points. Run them first:

```bash
pytest -k debug
```

Compare your tables with the numbers below. State order is 0, 1 (goal), 2 (start), 3.

**Value iteration** on `tiny` (γ = 0.5):

| After sweep | V(0) | V(1) | V(2) | V(3) |
| --- | --- | --- | --- | --- |
| 1 | 0.79200 | 0 | −0.04000 | 0.79200 |
| 2 | 0.82960 | 0 | 0.31440 | 0.82960 |
| 3 | 0.84920 | 0 | 0.34904 | 0.84920 |
| converged (16 sweeps, θ = 10⁻¹⁰) | 0.85273 | 0 | 0.36182 | 0.85273 |

The greedy policy is right in state 0 and up in states 2 and 3. In state 2, up and right tie at 0.36182, and the lowest index (up) wins.

**Policy iteration** on `tiny` (θ = 10⁻¹⁰): 3 improvement steps and 59 evaluation sweeps in total.

| Step | Policy evaluated (states 0, 2, 3) | Sweeps | V(0), V(2), V(3) | Improved policy |
| --- | --- | --- | --- | --- |
| 1 | up, up, up | 27 | 0.11636, 0.05091, 0.83636 | right, right, up |
| 2 | right, right, up | 16 | 0.85273, 0.36182, 0.85273 | right, up, up |
| 3 | right, up, up | 16 | 0.85273, 0.36182, 0.85273 | right, up, up (unchanged) |

**Prediction** on the episode 2 → 0 → 0 → goal, with rewards −0.04, −0.04, +1, γ = 0.5, α = 0.1, from V = 0:

- Returns: G_0 = 0.19, G_1 = 0.46, G_2 = 1.
- Monte Carlo: V(2) = 0.019. State 0 is updated twice: 0.046 after its first visit, then 0.046 + 0.1 (1 − 0.046) = 0.1414.
- TD(0), one transition at a time: V(2) = −0.004; then V(0) = −0.004; then V(0) = −0.004 + 0.1 (1 + 0.004) = 0.0964.

**Control trace** `debug-tiny-trace-sarsa`: `tiny` without slip, time limit 3, γ = 0.5, ε schedule 0.9 × 0.95^k, α schedule 0.5 × 0.9^k, three episodes. The initial table is:

| State | up | right | down | left |
| --- | --- | --- | --- | --- |
| 0 | 0.45 | 0.27 | −0.37 | 0.33 |
| 1 (goal) | 0 | 0 | 0 | 0 |
| 2 | −0.16 | 0.12 | 0.23 | 0.36 |
| 3 | −0.16 | −0.07 | 0.09 | 0.48 |

The scripted actions give these SARSA updates:

| k | State | Action | Reward | Next state | Episode ends | α | Target | Q before | Q after |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 2 | left | −0.04 | 2 | | 0.5 | −0.12 | 0.36 | 0.12 |
| 1 | 2 | up | −0.04 | 0 | | 0.45 | 0.185 | −0.16 | −0.00475 |
| 2 | 0 | up | −0.04 | 0 | time limit | 0.405 | 0.185 | 0.45 | 0.34268 |
| 3 | 2 | up | −0.04 | 0 | | 0.3645 | 0.095 | −0.00475 | 0.03161 |
| 4 | 0 | right | +1 | 1 | terminated | 0.32805 | 1 | 0.27 | 0.50948 |
| 5 | 2 | right | −0.04 | 3 | | 0.29525 | −0.12 | 0.12 | 0.04914 |
| 6 | 3 | up | +1 | 1 | terminated | 0.26572 | 1 | −0.16 | 0.14824 |

Row 2 is cut by the time limit and still bootstraps: its target uses Q(0, up), the action selected for k = 3.

## 7. Experiments and short answers

When your tests pass, run:

```bash
python run_experiments.py
```

It takes well under a minute and writes `results/results.json` and the plots.

| ID | Question | What is run |
| --- | --- | --- |
| E1 | Do the two planners agree, and how much work does each do? | Value iteration and policy iteration on `small` |
| E2 | How do the MC and TD(0) errors evolve on the same data? | Both kernels on 300 supplied episodes, α = 0.05 and 0.2, γ = 0.9 |
| E3 | What does the initial table change? | Q-learning on `ledge` for 200 episodes, four runs: Q₀ = 0 with ε = 0; Q₀ = +1 with ε = 0; Q₀ = 0 with ε = 0.1; and Q₀ = 0 with ε = 0 under book-style rewards |
| E4 | Which path does each method learn at constant ε? | SARSA and Q-learning on `ledge`, Q₀ = +1, ε = 0.1, α = 0.1, 1000 episodes, 10 seeds |
| E5 | What does decaying ε change? | E4 again with ε = 0.1 × 0.9995^k |

**Optimistic initialization.** E3 uses an idea that has not been covered in class. Starting every action value above the largest return the task can give is called *optimistic initialization*. In `ledge` the largest return is +1, so a table started at +1 is optimistic and a table started at 0 is not. Watch what each table does to exploration. The idea returns later in the course under the name *optimism in the face of uncertainty*.

**Link to the book.** The cliff-walking example in the book (Example 6.6) and in the Week 4 lecture gives −1 on every step and −100 for the cliff, and learns from a table started at 0. The fourth E3 run puts rewards of that style on the `ledge` map: −1 on every transition, including the one that reaches the goal, and −100 for a pit. Compare it with the first run, which also starts at 0, and ask what "optimistic" means for each set of rewards. The `ledge` version differs from the book's in two more ways: a pit ends the episode, and γ = 0.95.

Answer the three questions in `answers.md`, in at most four sentences each. Each answer must refer to your own numbers and plots.

## 8. LLM-use report

Fill in `llm_report.md`. It is required.

- If you did not use an LLM, say so in one sentence. Do not invent interactions.
- If you did, say where, give a representative prompt and output excerpt, say what you accepted, rejected or changed, and give at least one concrete check. The template includes a filled example.

A submission whose solution was delegated to an LLM in one or a few prompts earns no credit.

## 9. Submission

Submit one archive containing:

- `dp.py`, `prediction.py`, `control.py`
- `answers.md` and `llm_report.md`
- the `results/` folder produced by `run_experiments.py`

Download your submission afterwards and check that it is complete.

## 10. Grading

| Component | Share | How |
| --- | --- | --- |
| Part 1 tests | 25 | Automated |
| Part 2 tests | 25 | Automated |
| Part 3 tests | 35 | Automated |
| Three short answers | 15 | By hand |
| `results/` and the LLM-use report | required | Checked for presence |

- Automated grading runs the public tests and further tests of the same kind on the 4 × 3 grid with other settings.
- No points depend on which method scores higher or on a particular learned path.
- The short answers are credited for reasoning from your own run.
