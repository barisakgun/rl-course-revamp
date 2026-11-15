"""Part 3 tests. Run with:  pytest tests/test_part3_control.py

The trace tests run your ``train`` on a grid without slip, with a scripted
action selector in place of ``select_action``. Each one is a short, fully
determined run: the handout lists the ``debug-tiny`` trace step by step.
"""
import numpy as np
import pytest

import control
from helpers import ScriptedSelector, close, load_cases, make_case_env
from rlhw import ExponentialDecay


@pytest.mark.parametrize("case", load_cases("part3", "init_q"))
def test_init_q(case):
    Q = control.init_q(case["n_states"], case["n_actions"], case["value"], case["terminal_states"])
    assert np.shape(Q) == (case["n_states"], case["n_actions"])
    assert close(Q, case["expected"]), "terminal rows must be 0, every other entry the given value"


@pytest.mark.parametrize("case", load_cases("part3", "probs"))
def test_epsilon_greedy_probs(case):
    probs = control.epsilon_greedy_probs(np.array(case["q_row"]), case["epsilon"])
    assert close(probs, case["expected"]), (
        f"q_row={case['q_row']}, epsilon={case['epsilon']}: expected {case['expected']}, "
        f"got {np.round(probs, 6)}")


@pytest.mark.parametrize("case", load_cases("part3", "sample"))
def test_select_action_follows_the_probabilities(case):
    rng = np.random.default_rng(case["seed"])
    q_row = np.array(case["q_row"])
    draws = [control.select_action(q_row, case["epsilon"], rng) for _ in range(case["n_draws"])]
    assert all(int(a) == a and 0 <= a < len(q_row) for a in draws), "actions must be valid indices"
    freq = np.bincount(np.array(draws, dtype=int), minlength=len(q_row)) / case["n_draws"]
    assert np.max(np.abs(freq - np.array(case["expected"]))) <= case["tol"] + 1e-12, (
        f"action frequencies {np.round(freq, 3)} do not match the epsilon-greedy "
        f"probabilities {case['expected']}")


def test_select_action_uses_the_given_generator():
    q_row = np.array([0.0, 1.0, 0.5, 0.2])
    a = [control.select_action(q_row, 1.0, np.random.default_rng(3)) for _ in range(2)]
    b = [control.select_action(q_row, 1.0, np.random.default_rng(s)) for s in range(40)]
    assert a[0] == a[1], "the same generator state must give the same action"
    assert len(set(b)) > 1, "different generator states must be able to give different actions"


@pytest.mark.parametrize("case", load_cases("part3", "targets"))
def test_sarsa_target(case):
    target = control.sarsa_target(np.array(case["Q"]), case["r"], case["s_next"], case["a_next"],
                                  case["terminated"], case["gamma"])
    assert close(target, case["expected_sarsa"], atol=1e-10), (
        f"expected {case['expected_sarsa']:.6f}, got {float(target):.6f}")


@pytest.mark.parametrize("case", load_cases("part3", "targets"))
def test_q_learning_target(case):
    target = control.q_learning_target(np.array(case["Q"]), case["r"], case["s_next"],
                                       case["terminated"], case["gamma"])
    assert close(target, case["expected_q_learning"], atol=1e-10), (
        f"expected {case['expected_q_learning']:.6f}, got {float(target):.6f}")


def _run_trace(case):
    env = make_case_env(case["env"])
    eps = ExponentialDecay(**case["epsilon"])
    selector = ScriptedSelector(case["script"], case["episode_starts"], eps)
    q_init = np.array(case["q_init"])
    q_init_copy = q_init.copy()
    Q, returns, lengths = control.train(
        env, case["method"], case["gamma"], eps, ExponentialDecay(**case["alpha"]),
        q_init, case["n_episodes"], 0, select_fn=selector)
    return Q, returns, lengths, selector, np.array_equal(q_init, q_init_copy)


@pytest.mark.parametrize("case", load_cases("part3", "traces"))
def test_trace_epsilon_schedule(case):
    _, _, _, selector, _ = _run_trace(case)
    assert not selector.errors, selector.errors[0]
    executed = set(range(len(case["script"]) - 1))
    missing = sorted(executed - set(selector.calls))
    assert not missing, f"no action was selected with epsilon_schedule.value(k) for k = {missing}"


@pytest.mark.parametrize("case", load_cases("part3", "traces"))
def test_trace_episode_boundaries(case):
    _, returns, lengths, _, _ = _run_trace(case)
    exp = case["expected"]
    assert list(lengths) == exp["lengths"], f"episode lengths: expected {exp['lengths']}, got {list(lengths)}"
    assert close(returns, exp["returns"]), f"episode returns: expected {exp['returns']}, got {list(returns)}"


@pytest.mark.parametrize("case", load_cases("part3", "traces"))
def test_trace_q_values(case):
    Q, _, _, _, untouched = _run_trace(case)
    assert untouched, "train must work on a copy of q_init"
    expected = np.array(case["expected"]["Q"])
    diff = np.argwhere(~np.isclose(np.asarray(Q, dtype=float), expected, atol=1e-8))
    assert len(diff) == 0, (
        f"{len(diff)} Q entries differ; first at (state, action) = {tuple(int(i) for i in diff[0])}: "
        f"expected {expected[tuple(diff[0])]:.6f}, got {np.asarray(Q)[tuple(diff[0])]:.6f}. "
        "Check, in this order: the target at termination (reward only) and at the time limit "
        "(still bootstraps); SARSA uses, in its target, the same next action it then executes; "
        "the step size is alpha_schedule.value(k) for transition k.")


def test_smoke_training_reaches_the_goal():
    """Not graded: after training on the 4 x 3 grid the greedy policy should reach the goal."""
    from rlhw import Constant, make_env
    from rlhw.drivers import greedy_rollout
    env = make_env("small")
    base = env.unwrapped
    q0 = control.init_q(base.n_states, base.n_actions, 0.0, base.terminal_states)
    Q, _, _ = control.train(env, "q_learning", 0.9, Constant(0.2), Constant(0.2), q0, 2000, 0)
    reached = sum(greedy_rollout(make_env("small"), Q, 0.9, seed=s)["reached_goal"] for s in range(20))
    assert reached >= 14, f"the greedy policy reached the goal in only {reached} of 20 runs"
