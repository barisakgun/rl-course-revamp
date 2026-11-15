"""Part 1 tests. Run with:  pytest tests/test_part1_planning.py

Cases whose name starts with ``debug-`` use the 2 x 2 grid and are not graded.
"""
import numpy as np
import pytest

import dp
from helpers import close, load_cases, make_case_env

CASES = load_cases("part1", "planning")


def model(case):
    return make_case_env(case["env"]).unwrapped.P


@pytest.mark.parametrize("case", CASES)
def test_q_from_v(case):
    P = model(case)
    V = np.array(case["fixed_V"])
    for s in case["nonterminal"]:
        q = dp.q_from_v(P, V, s, case["gamma"])
        assert close(q, case["q_fixed"][s]), (
            f"state {s}: expected {np.round(case['q_fixed'][s], 6)}, got {np.round(q, 6)}")


@pytest.mark.parametrize("case", CASES)
def test_value_iteration_values(case):
    V, _ = dp.value_iteration(model(case), case["gamma"], case["theta"])
    assert close(V, case["V_star"], atol=1e-7), (
        f"expected\n{np.round(case['V_star'], 5)}\ngot\n{np.round(V, 5)}")


@pytest.mark.parametrize("case", CASES)
def test_value_iteration_terminal_states_are_zero(case):
    V, _ = dp.value_iteration(model(case), case["gamma"], case["theta"])
    assert all(V[s] == 0.0 for s in case["terminal"]), "terminal and wall cells must keep value 0"


@pytest.mark.parametrize("case", CASES)
def test_value_iteration_sweep_count(case):
    _, sweeps = dp.value_iteration(model(case), case["gamma"], case["theta"])
    assert sweeps == case["vi_sweeps"], (
        f"expected {case['vi_sweeps']} sweeps, got {sweeps}. Check: V starts at 0, sweeps are "
        "synchronous, stop when the largest change is strictly below theta, count the final sweep.")


@pytest.mark.parametrize("case", CASES)
def test_value_iteration_greedy_policy(case):
    P = model(case)
    V, _ = dp.value_iteration(P, case["gamma"], case["theta"])
    policy = dp.policy_improvement(P, V, case["gamma"])
    for s in case["nonterminal"]:
        assert int(policy[s]) in case["admissible"][s], (
            f"state {s}: action {int(policy[s])} is not optimal; optimal: {case['admissible'][s]}")


@pytest.mark.parametrize("case", CASES)
def test_policy_improvement_on_fixed_table(case):
    P = model(case)
    policy = dp.policy_improvement(P, np.array(case["fixed_V"]), case["gamma"])
    for s in case["nonterminal"]:
        assert int(policy[s]) == case["improve_fixed"][s], f"state {s}"


@pytest.mark.parametrize("case", CASES)
def test_policy_improvement_breaks_ties_to_lowest_index(case):
    P = model(case)
    policy = dp.policy_improvement(P, np.zeros(len(P)), case["gamma"])
    for s in case["nonterminal"]:
        assert int(policy[s]) == case["improve_zero"][s], (
            f"state {s}: with V = 0 several actions tie; the lowest index must win")


@pytest.mark.parametrize("case", CASES)
def test_policy_iteration_result(case):
    policy, V, _, _ = dp.policy_iteration(model(case), case["gamma"], case["theta"])
    assert close(V, case["V_star"], atol=1e-7), "the returned V is not the optimal value table"
    for s in case["nonterminal"]:
        assert int(policy[s]) in case["admissible"][s], f"state {s}: action is not optimal"


@pytest.mark.parametrize("case", CASES)
def test_policy_iteration_counts(case):
    _, _, improvements, sweeps = dp.policy_iteration(model(case), case["gamma"], case["theta"])
    assert (improvements, sweeps) == (case["pi_improvements"], case["pi_eval_sweeps"]), (
        f"expected {case['pi_improvements']} improvement steps and {case['pi_eval_sweeps']} "
        f"evaluation sweeps, got {improvements} and {sweeps}. Check: start from action 0 "
        "everywhere, count the final improvement step, add up the sweeps of every evaluation.")
