"""Episode files (supplied; do not modify)."""
import json
from collections import namedtuple

Transition = namedtuple(
    "Transition", ["state", "action", "reward", "next_state", "terminated", "truncated"]
)


def save_episodes(path, episodes):
    rows = [[[int(t.state), int(t.action), float(t.reward), int(t.next_state),
              bool(t.terminated), bool(t.truncated)] for t in ep] for ep in episodes]
    with open(path, "w") as f:
        json.dump(rows, f)


def episodes_from_rows(rows):
    return [[Transition(int(s), int(a), float(r), int(s2), bool(term), bool(trunc))
             for s, a, r, s2, term, trunc in ep] for ep in rows]


def load_episodes(path):
    """Return a list of episodes; each episode is a list of ``Transition``."""
    with open(path) as f:
        return episodes_from_rows(json.load(f))


def save_dataset(path, layout, policy, episodes):
    rows = [[[int(t.state), int(t.action), float(t.reward), int(t.next_state),
              bool(t.terminated), bool(t.truncated)] for t in ep] for ep in episodes]
    with open(path, "w") as f:
        json.dump({"layout": layout, "policy": [int(a) for a in policy], "episodes": rows}, f)


def load_dataset(path):
    """Return ``(layout_name, policy, episodes)`` from a supplied episode file."""
    with open(path) as f:
        data = json.load(f)
    return data["layout"], data["policy"], episodes_from_rows(data["episodes"])
