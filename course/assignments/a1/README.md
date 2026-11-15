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
    python staff/check_wrong_variants.py   # tests fail on 24 wrong implementations
    python staff/build_starter.py          # regenerate starter/
    (cd solution && python run_experiments.py)

    python grading/grade.py <submission_dir>

Expected numbers in the cases come from independent computations in
`make_cases.py` (linear solves, direct sums, a transition-by-transition replay),
each compared with the reference solution at generation.

## Pilot results (reference solution, Python 3.11.6, Gymnasium 1.4.0, NumPy 1.26.4)

Numbers are from the build after the code review (2026-11-15), in which Q-learning
selects its next action after its update.

- With Q₀ = 0, zero step reward and lowest-index ties, the agent never reaches the
  goal on `ledge` in 200 episodes, at ε = 0 or ε = 0.1. The control comparison
  therefore starts from Q₀ = +1, and the initialization experiment (E3) comes first.
- E3: the +1 table at ε = 0 reaches the goal in 189 of 200 episodes (coverage 0.99
  after 500 transitions). A zero table with book-style rewards (−1 per transition,
  −100 pit) reaches it in 186 of 200 (coverage 1.0). E3 reports training outcomes,
  not a frozen greedy rollout: after 200 episodes at α = 0.1 the +1 table's greedy
  policy can still loop, although training reaches the goal in each of the last 20
  episodes.
- E4 (ε = 0.1, α = 0.1, 1000 episodes, 10 seeds): SARSA's greedy path is 11 moves
  in all seeds, Q-learning's 9.
- E5: ε = 0.1 × 0.9995^k brings SARSA to the 9-move path in all seeds; 0.9998 did not
  in the earlier pilot.
- `run_experiments.py` takes about 8 seconds.

## Suggestions awaiting the instructor's decision

These are Claude's suggestions as built. None is accepted.

**Grading shares** (`grading/points.json`, handout section 10):

| Component | Share | Basis |
| --- | --- | --- |
| Part 1 tests | 25 | 9 test functions; values and lookahead weigh most |
| Part 2 tests | 25 | 5 test functions; the three kernels weigh most |
| Part 3 tests | 35 | 10 test functions; probabilities and the Q-value trace weigh most (5 each) |
| Three short answers | 15 | 5 each, by hand, from `grading/answer_guide.md` |
| `results/` and LLM-use report | required | Presence only; no points |

A test function earns its points times the fraction of its graded cases that pass.

**Testing conditions:**

- Scored cases use the 4 × 3 grid only (12 states, 4 actions), for unit cases as well
  as full runs: the public cases plus hidden cases with other settings (slip 0, 0.1,
  0.4; γ 0.7 to 0.95; another step reward; other fixed inputs and other traces).
  Cases on the 2 × 2 grid carry no points. Each case file entry has a `graded` field
  set from its dimensions; the generator checks that it agrees with the `debug-` name,
  and `grade.py` reads the field.
- Tolerances are absolute, with no relative part: 1e-7 on converged value tables,
  1e-8 on Q-values and file runs, 1e-10 on single updates. Shapes must match. Action
  frequencies must be within 0.02 over 20,000 seeded draws.
- Exact counts are graded: value-iteration sweeps, policy-iteration improvement
  steps and evaluation sweeps. Each case's threshold is chosen with a 2 percent
  margin so the count does not sit at the stopping boundary.
- Converged policies are accepted if each action is optimal within 1e-6; exact
  lowest-index ties are graded only on fixed tables.
- The control loop is checked by two kinds of trace on a grid without slip. Scripted
  traces fix the actions and check targets, schedules and episode boundaries. Greedy
  traces use a selector that is greedy in the row it is given, so the run depends on
  the table: they check that actions come from the current state's row, and that
  Q-learning selects after its update.
- The goal-reaching check is a smoke test with no points and is not run in grading.
- Student changes to supplied files have no effect: grading copies the three student
  modules onto a clean starter. Each part runs separately with a 300-second limit; a
  part that cannot be imported is reported as not graded and does not affect the
  others. Cases without points are not executed in grading. Each required submission
  item is checked by name; missing ones are listed and flagged for follow-up, with no
  automated penalty.
- Scalar target cases use successors that can occur on the grid: the goal or the pit
  when the transition terminates, an ordinary cell otherwise.

**Other open items:** release and due dates; who runs the timed pilot (instructor
with the TAs); the clean-install check (after the code review).

## Not done

- No timed attempt from the starter by a student-level solver.
- Tested on one machine only (macOS, Python 3.11, NumPy 1.26); not on a clean install,
  Windows or NumPy 2.
- Points in `grading/points.json` and the shares in the handout are provisional.
- Release and due dates are not set.
