"""Part 2 tests. Run with:  pytest tests/test_part2_prediction.py"""
from pathlib import Path

import numpy as np
import pytest

import prediction
from helpers import close, load_cases
from rlhw.data import episodes_from_rows, load_dataset
from rlhw.drivers import run_prediction

DATA = Path(__file__).resolve().parent.parent / "data"


@pytest.mark.parametrize("case", load_cases("part2", "returns"))
def test_returns(case):
    G = prediction.returns(case["rewards"], case["gamma"])
    assert len(G) == len(case["rewards"]) and close(G, case["expected"], atol=1e-10), (
        f"expected {np.round(case['expected'], 6)}, got {np.round(G, 6)}")


@pytest.mark.parametrize("case", load_cases("part2", "mc"))
def test_mc_update(case):
    V = np.array(case["V0"], dtype=float)
    for episode in episodes_from_rows(case["episodes"]):
        V = prediction.mc_update(V, episode, case["alpha"], case["gamma"])
    assert V is not None, "mc_update must return V"
    assert close(V, case["expected"], atol=1e-10), (
        f"expected {np.round(case['expected'], 6)}, got {np.round(V, 6)}. A state visited "
        "twice gets two updates, in chronological order, each with its own return.")


@pytest.mark.parametrize("case", load_cases("part2", "td"))
def test_td0_update(case):
    V = prediction.td0_update(np.array(case["V0"], dtype=float), case["s"], case["r"],
                              case["s_next"], case["terminated"], case["alpha"], case["gamma"])
    assert V is not None, "td0_update must return V"
    assert close(V, case["expected"], atol=1e-10), (
        f"expected {np.round(case['expected'], 6)}, got {np.round(V, 6)}")


def _episodes(case):
    if case["dataset"]:
        return load_dataset(DATA / case["dataset"])[2]
    return episodes_from_rows(case["episodes"])


@pytest.mark.parametrize("case", load_cases("part2", "runs"))
def test_mc_over_episode_file(case):
    V, _ = run_prediction(_episodes(case), "mc", prediction.mc_update, case["alpha"],
                          case["gamma"], case["n_states"])
    assert close(V, case["expected_mc"], atol=1e-8), (
        f"expected {np.round(case['expected_mc'], 5)}, got {np.round(V, 5)}")


@pytest.mark.parametrize("case", load_cases("part2", "runs"))
def test_td0_over_episode_file(case):
    V, _ = run_prediction(_episodes(case), "td", prediction.td0_update, case["alpha"],
                          case["gamma"], case["n_states"])
    assert close(V, case["expected_td"], atol=1e-8), (
        f"expected {np.round(case['expected_td'], 5)}, got {np.round(V, 5)}")
