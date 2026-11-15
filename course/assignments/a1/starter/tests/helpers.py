"""Test helpers (supplied; do not modify)."""
import json
import os
from pathlib import Path

import numpy as np
import pytest

CASES_DIR = Path(__file__).resolve().parent / "cases"


def load_cases(part, section):
    """Cases of one section from every case file of a part (plus optional extra directory)."""
    dirs = [CASES_DIR]
    if os.environ.get("A1_EXTRA_CASES"):
        dirs.append(Path(os.environ["A1_EXTRA_CASES"]))
    params = []
    for d in dirs:
        for path in sorted(d.glob(f"{part}_*.json")):
            for case in json.loads(path.read_text()).get(section, []):
                params.append(pytest.param(case, id=case["id"]))
    return params


def make_case_env(spec):
    from rlhw import make_env
    return make_env(spec["layout"], max_episode_steps=spec.get("max_episode_steps"),
                    **spec.get("overrides", {}))


class ScriptedSelector:
    """A stand-in for ``select_action`` that plays a fixed script.

    It recognises the schedule clock ``k`` from the epsilon it is given, so it
    also checks that the loop passes ``epsilon_schedule.value(k)``. The first
    call for a clock value returns the scripted action. A repeated call for the
    same clock value returns a different action, unless that clock value starts
    an episode: a loop that selects SARSA's next action twice is caught that way.
    """

    def __init__(self, script, episode_starts, epsilon_schedule):
        self.script = list(script)
        self.starts = set(episode_starts)
        self.eps_values = [epsilon_schedule.value(k) for k in range(len(self.script))]
        self.calls = {}
        self.errors = []

    def __call__(self, q_row, epsilon, rng):
        matches = [k for k, v in enumerate(self.eps_values) if abs(v - epsilon) < 1e-12]
        if not matches:
            self.errors.append(
                f"select_fn received epsilon={epsilon!r}, which is not "
                "epsilon_schedule.value(k) for any clock value k reached in this test")
            return 0
        k = matches[0]
        self.calls[k] = self.calls.get(k, 0) + 1
        action = self.script[k]
        if self.calls[k] > 1 and k not in self.starts:
            return (action + 2) % 4
        return action


def close(actual, expected, atol=1e-8):
    return np.allclose(np.asarray(actual, dtype=float), np.asarray(expected, dtype=float), atol=atol)
