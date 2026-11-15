# A1 — staff notes

Shared homework files (both AIs may edit; see `AGENTS.md`). Design record:
`analysis/assignment_suggestions/a1_claude.md` and `a1_review.md`; accepted choices:
`decisions/assignment_decisions.md`.

| Path | Content | Released |
| --- | --- | --- |
| `handout.md` | Assignment text | Yes |
| `starter/` | Generated from `solution/`; do not edit by hand | Yes |
| `solution/` | Reference solution; the single source for all supplied code, tests and data | No |
| `grading/` | Hidden cases, `grade.py`, provisional `points.json`, answer guide | No |
| `staff/` | Generators and checks | No |

`solution/`, `grading/` and `staff/` are excluded from git (`.gitignore`), like exam material; `staff/` contains solution code in its checks. They exist only in the working folder, so they are not backed up by git.

## Rebuild, in order

    python staff/make_data.py              # Part 2 episode files
    python staff/make_cases.py             # public test cases
    python staff/make_cases.py --hidden    # hidden test cases
    (cd solution && pytest)                # reference solution passes
    python staff/check_wrong_variants.py   # tests fail on 21 wrong implementations
    python staff/build_starter.py          # regenerate starter/
    (cd solution && python run_experiments.py)

    python grading/grade.py <submission_dir>

Expected numbers in the cases come from independent computations in
`make_cases.py` (linear solves, direct sums, a transition-by-transition replay),
each compared with the reference solution at generation.

## Pilot results (2026-11-14, reference solution, Python 3.11, Gymnasium 1.4.0)

- With Q₀ = 0, zero step reward and lowest-index ties, the agent never reaches the
  goal on `ledge` in 200 episodes, at ε = 0 or ε = 0.1. The control comparison
  therefore starts from Q₀ = +1, and the initialization experiment (E3) comes first.
- E4 (ε = 0.1, α = 0.1, 1000 episodes, 10 seeds): SARSA's greedy path is 11 moves
  in all seeds, Q-learning's 9. Same split at 300 episodes with α = 0.5.
- E5: ε = 0.1 × 0.9995^k brings SARSA to the 9-move path in all seeds; 0.9998 does not.
- E3 fourth run (2026-11-15): Q₀ = 0, ε = 0 with book-style rewards (−1 per transition, −100 pit)
  reaches the goal in 184 of 200 episodes with coverage 1.0. At γ = 1 the greedy policy
  is not yet settled after 200 episodes, so the run keeps the layout's γ = 0.95.
- `run_experiments.py` takes about 8 seconds.

## Suggestions awaiting the instructor's decision

These are Claude's suggestions as built. None is accepted.

**Grading shares** (`grading/points.json`, handout section 10):

| Component | Share | Basis |
| --- | --- | --- |
| Part 1 tests | 25 | 9 test functions; values and lookahead weigh most |
| Part 2 tests | 25 | 5 test functions; the three kernels weigh most |
| Part 3 tests | 35 | 9 test functions; the Q-value trace weighs most (7) |
| Three short answers | 15 | 5 each, by hand, from `grading/answer_guide.md` |
| `results/` and LLM-use report | required | Presence only; no points |

A test function earns its points times the fraction of its graded cases that pass.

**Testing conditions:**

- Scored cases use the 4 × 3 grid only: the public cases plus hidden cases with other
  settings (slip 0, 0.1, 0.4; γ 0.7 to 0.95; another step reward; other fixed inputs
  and another scripted trace). `debug-` cases on the 2 × 2 grid carry no points.
- Tolerances: 1e-7 on converged value tables, 1e-8 on Q-values and file runs, 1e-10
  on single updates; action frequencies within 0.02 over 20,000 seeded draws.
- Exact counts are graded: value-iteration sweeps, policy-iteration improvement
  steps and evaluation sweeps. Each case's threshold is chosen with a 2 percent
  margin so the count does not sit at the stopping boundary.
- Converged policies are accepted if each action is optimal within 1e-6; exact
  lowest-index ties are graded only on fixed tables.
- The goal-reaching check is a smoke test with no points.
- Student changes to supplied files have no effect: grading copies the three student
  modules onto a clean starter. Time limit 600 seconds per submission.

**Other open items:** release and due dates; who runs the timed pilot (instructor
with the TAs); the clean-install check (after the code review).

## Not done

- No timed attempt from the starter by a student-level solver.
- Tested on one machine only (macOS, Python 3.11, NumPy 1.26); not on a clean install,
  Windows or NumPy 2.
- Points in `grading/points.json` and the shares in the handout are provisional.
- Release and due dates are not set.
