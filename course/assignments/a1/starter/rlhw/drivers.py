"""Supplied drivers, recorders and evaluation helpers (do not modify)."""
import gymnasium as gym
import numpy as np

from .utils import argmax_lowest


def policy_evaluation(P, policy, gamma, theta):
    """Iterative policy evaluation for a deterministic policy (supplied).

    Conventions: V starts at 0; sweeps are synchronous (every state is backed up
    from the previous sweep's table); stop when the largest change in a sweep is
    strictly below ``theta``; the final sweep is counted.

    Returns ``(V, n_sweeps)``.
    """
    n_states = len(P)
    V = np.zeros(n_states)
    sweeps = 0
    while True:
        V_new = np.zeros(n_states)
        for s in range(n_states):
            for prob, s2, reward, terminated in P[s][int(policy[s])]:
                V_new[s] += prob * (reward + (0.0 if terminated else gamma * V[s2]))
        sweeps += 1
        delta = np.max(np.abs(V_new - V))
        V = V_new
        if delta < theta:
            return V, sweeps


def rms_error(V, true_v, states):
    states = list(states)
    return float(np.sqrt(np.mean((np.asarray(V)[states] - np.asarray(true_v)[states]) ** 2)))


def run_prediction(episodes, method, kernel, alpha, gamma, n_states, true_v=None, states=None):
    """Apply a prediction kernel over episodes in order, from V = 0.

    ``method`` is ``"mc"`` (``kernel`` is ``mc_update``, called once per episode)
    or ``"td"`` (``kernel`` is ``td0_update``, called once per transition, in
    order). Returns ``(V, errors)``; ``errors[i]`` is the root-mean-square error
    against ``true_v`` over ``states`` after episode ``i`` (empty without ``true_v``).
    """
    V = np.zeros(n_states)
    errors = []
    for episode in episodes:
        if method == "mc":
            V = kernel(V, episode, alpha, gamma)
        elif method == "td":
            for t in episode:
                V = kernel(V, t.state, t.reward, t.next_state, t.terminated, alpha, gamma)
        else:
            raise ValueError(f"unknown method {method!r}")
        if true_v is not None:
            errors.append(rms_error(V, true_v, states))
    return V, errors


class VisitRecorder(gym.Wrapper):
    """Records which state-action pairs were tried, and when they were first tried.

    ``first_visit[s, a]`` is the index (0-based, over all episodes) of the first
    transition that took action ``a`` in state ``s``, or -1 if never tried.
    """

    def __init__(self, env):
        super().__init__(env)
        base = env.unwrapped
        self.first_visit = -np.ones((base.n_states, base.n_actions), dtype=int)
        self.counts = np.zeros((base.n_states, base.n_actions), dtype=int)
        self.total_transitions = 0
        self.pit_entries = 0
        self.goal_entries = 0
        self.episodes_started = 0
        self.first_goal_episode = None   # 1-based episode number, or None
        self._state = None

    def reset(self, **kwargs):
        obs, info = self.env.reset(**kwargs)
        self._state = obs
        self.episodes_started += 1
        return obs, info

    def step(self, action):
        s, a = self._state, int(action)
        if self.first_visit[s, a] < 0:
            self.first_visit[s, a] = self.total_transitions
        self.counts[s, a] += 1
        self.total_transitions += 1
        obs, reward, terminated, truncated, info = self.env.step(action)
        base = self.env.unwrapped
        if terminated and obs in base.pit_states:
            self.pit_entries += 1
        if terminated and obs in base.goal_states:
            self.goal_entries += 1
            if self.first_goal_episode is None:
                self.first_goal_episode = self.episodes_started
        self._state = obs
        return obs, reward, terminated, truncated, info

    def coverage(self, pairs, by_transition=None):
        """Fraction of ``pairs`` tried, optionally only within the first N transitions."""
        hit = 0
        for s, a in pairs:
            t = self.first_visit[s, a]
            if t >= 0 and (by_transition is None or t < by_transition):
                hit += 1
        return hit / len(pairs)


def reachable_pairs(env):
    """All (state, action) pairs with a non-terminal state reachable from the start."""
    base = env.unwrapped
    seen, frontier = {base.start_state}, [base.start_state]
    skip = set(base.terminal_states) | set(base.wall_states)
    while frontier:
        s = frontier.pop()
        for a in range(base.n_actions):
            for _, s2, _, _ in base.P[s][a]:
                if s2 not in seen and s2 not in skip:
                    seen.add(s2)
                    frontier.append(s2)
    return [(s, a) for s in sorted(seen) for a in range(base.n_actions)]


def greedy_rollout(env, Q, gamma, seed=0, max_steps=None):
    """Follow the greedy policy of ``Q`` (ties to the lowest index) for one episode.

    Returns a dict with the visited ``states``, the raw and discounted returns,
    and whether the goal was reached.
    """
    base = env.unwrapped
    s, _ = env.reset(seed=seed)
    states, raw, disc, discount = [int(s)], 0.0, 0.0, 1.0
    reached_goal = False
    for _ in range(max_steps or 10**6):
        s, r, terminated, truncated, _ = env.step(argmax_lowest(Q[s]))
        states.append(int(s))
        raw += r
        disc += discount * r
        discount *= gamma
        if terminated:
            reached_goal = s in base.goal_states
        if terminated or truncated:
            break
    return dict(states=states, moves=len(states) - 1, raw_return=raw,
                discounted_return=disc, reached_goal=bool(reached_goal))
