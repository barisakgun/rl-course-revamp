"""A small gridworld with the Gymnasium interface (supplied; do not modify).

States are cell indices, counted row by row from the top-left cell:
``state = row * n_cols + col``. Walls and terminal cells have indices too.

Actions: 0 = up, 1 = right, 2 = down, 3 = left.

The model is available as ``env.unwrapped.P``, in the convention of Gymnasium's
FrozenLake: ``P[s][a]`` is a list of ``(probability, next_state, reward,
terminated)`` tuples. Only Part 1 (planning) may use it.

Rules
-----
* With probability ``1 - slip`` the agent moves in the intended direction; with
  probability ``slip / 2`` each, it moves in one of the two perpendicular
  directions. A move into a wall or off the grid leaves the state unchanged.
* Entering a goal cell gives ``goal_reward`` and ends the episode. Entering a
  pit gives ``pit_reward`` and ends the episode. This is the total reward of
  that transition. Every other transition gives ``step_reward``.
* A time limit ends long episodes with ``truncated=True``. That is not a
  terminal state: the returned observation is an ordinary state.
"""
import gymnasium as gym
import numpy as np
from gymnasium import spaces

ACTION_NAMES = ["up", "right", "down", "left"]
_MOVES = [(-1, 0), (0, 1), (1, 0), (0, -1)]
_ARROWS = "^>v<"

LAYOUTS = {
    # The 2 x 2 lecture grid used for hand calculations (debugging only).
    "tiny": dict(
        map=[".G",
             "S."],
        step_reward=-0.04, goal_reward=1.0, pit_reward=-1.0, slip=0.2,
        gamma=0.5, max_episode_steps=100,
    ),
    # The 4 x 3 lecture grid (graded tests).
    "small": dict(
        map=["...G",
             ".#.P",
             "S..."],
        step_reward=-0.04, goal_reward=1.0, pit_reward=-1.0, slip=0.2,
        gamma=0.5, max_episode_steps=200,
    ),
    # Control experiments: pits between start and goal, no slip, no step reward.
    "ledge": dict(
        map=["........",
             "........",
             "........",
             "SPPPPPPG"],
        step_reward=0.0, goal_reward=1.0, pit_reward=-1.0, slip=0.0,
        gamma=0.95, max_episode_steps=100,
    ),
}


def resolve_layout(layout, overrides=None):
    """Return a full layout specification from a name or a dict."""
    spec = dict(LAYOUTS[layout]) if isinstance(layout, str) else dict(layout)
    for key, value in (overrides or {}).items():
        if value is not None:
            spec[key] = value
    return spec


class GridWorldEnv(gym.Env):
    metadata = {"render_modes": ["ansi"], "render_fps": 4}

    def __init__(self, layout="small", render_mode=None, **overrides):
        spec = resolve_layout(layout, overrides)
        self.layout_spec = spec
        self.grid = [list(row) for row in spec["map"]]
        self.n_rows, self.n_cols = len(self.grid), len(self.grid[0])
        assert all(len(row) == self.n_cols for row in self.grid), "ragged map"
        self.step_reward = float(spec["step_reward"])
        self.goal_reward = float(spec["goal_reward"])
        self.pit_reward = float(spec["pit_reward"])
        self.slip = float(spec["slip"])
        self.gamma = float(spec["gamma"])
        self.render_mode = render_mode

        self.n_states = self.n_rows * self.n_cols
        self.n_actions = 4
        self.observation_space = spaces.Discrete(self.n_states)
        self.action_space = spaces.Discrete(self.n_actions)

        cells = {ch: [] for ch in "SGP#"}
        for r in range(self.n_rows):
            for c in range(self.n_cols):
                ch = self.grid[r][c]
                assert ch in "SGP#.", f"unknown map character {ch!r}"
                if ch in cells:
                    cells[ch].append(r * self.n_cols + c)
        assert len(cells["S"]) == 1, "the map needs exactly one start cell S"
        self.start_state = cells["S"][0]
        self.goal_states = sorted(cells["G"])
        self.pit_states = sorted(cells["P"])
        self.wall_states = sorted(cells["#"])
        self.terminal_states = sorted(cells["G"] + cells["P"])
        self.P = self._build_model()
        self._state = None

    # ----- model -----------------------------------------------------------
    def _move(self, state, direction):
        r, c = divmod(state, self.n_cols)
        nr, nc = r + _MOVES[direction][0], c + _MOVES[direction][1]
        if not (0 <= nr < self.n_rows and 0 <= nc < self.n_cols) or self.grid[nr][nc] == "#":
            return state
        return nr * self.n_cols + nc

    def _build_model(self):
        absorbing = set(self.terminal_states) | set(self.wall_states)
        P = {}
        for s in range(self.n_states):
            P[s] = {}
            for a in range(self.n_actions):
                if s in absorbing:
                    P[s][a] = [(1.0, s, 0.0, True)]
                    continue
                outcomes = {}
                for direction, prob in ((a, 1.0 - self.slip),
                                        ((a - 1) % 4, self.slip / 2),
                                        ((a + 1) % 4, self.slip / 2)):
                    if prob <= 0.0:
                        continue
                    s2 = self._move(s, direction)
                    if s2 in self.goal_states:
                        key = (s2, self.goal_reward, True)
                    elif s2 in self.pit_states:
                        key = (s2, self.pit_reward, True)
                    else:
                        key = (s2, self.step_reward, False)
                    outcomes[key] = outcomes.get(key, 0.0) + prob
                P[s][a] = [(prob, s2, reward, term)
                           for (s2, reward, term), prob in sorted(outcomes.items())]
        return P

    # ----- Gymnasium API ---------------------------------------------------
    def reset(self, *, seed=None, options=None):
        super().reset(seed=seed)
        self._state = self.start_state
        return self._state, {}

    def step(self, action):
        outcomes = self.P[self._state][int(action)]
        i = 0 if len(outcomes) == 1 else int(
            self.np_random.choice(len(outcomes), p=[o[0] for o in outcomes]))
        prob, s2, reward, terminated = outcomes[i]
        self._state = s2
        return s2, reward, terminated, False, {"prob": prob}

    def render(self):
        return self.format_values(None)

    # ----- helpers for printing and debugging -------------------------------
    def cell_label(self, state):
        """Lecture coordinates (column from the left, row from the bottom), 1-based."""
        r, c = divmod(state, self.n_cols)
        return (c + 1, self.n_rows - r)

    def nonterminal_states(self):
        skip = set(self.terminal_states) | set(self.wall_states)
        return [s for s in range(self.n_states) if s not in skip]

    def format_values(self, V, fmt="{:7.3f}"):
        """Text picture of the grid; with ``V`` given, of a state-value table."""
        lines = []
        for r in range(self.n_rows):
            cells = []
            for c in range(self.n_cols):
                s, ch = r * self.n_cols + c, self.grid[r][c]
                if ch == "#":
                    cells.append("   #   ")
                elif ch in "GP" or V is None:
                    cells.append(f"   {ch}   ")
                else:
                    cells.append(fmt.format(V[s]))
            lines.append(" ".join(cells))
        return "\n".join(lines)

    def format_policy(self, policy):
        """Text picture of a deterministic policy (one action index per state)."""
        lines = []
        for r in range(self.n_rows):
            row = ""
            for c in range(self.n_cols):
                s, ch = r * self.n_cols + c, self.grid[r][c]
                row += ch if ch in "#GP" else _ARROWS[int(policy[s])]
            lines.append(row)
        return "\n".join(lines)


gym.register(id="rlhw/GridWorld-v0", entry_point="rlhw.gridworld:GridWorldEnv")


def make_env(layout="small", max_episode_steps=None, **overrides):
    """Create a gridworld with its time limit.

    ``layout`` is a name from ``LAYOUTS`` or a layout dict. Keyword overrides
    (``slip``, ``gamma``, ``step_reward``, ...) replace the layout's settings.
    """
    spec = resolve_layout(layout, overrides)
    steps = max_episode_steps or spec.get("max_episode_steps", 100)
    return gym.make("rlhw/GridWorld-v0", layout=layout, max_episode_steps=steps, **overrides)
