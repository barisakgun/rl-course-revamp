"""Part 2 - Prediction from sampled episodes: Monte Carlo and TD(0).

Complete the three functions marked TODO. Do not change their names or arguments.

An episode is a list of ``Transition(state, action, reward, next_state,
terminated, truncated)``; ``reward`` is the reward that follows the action.
The supplied ``rlhw.drivers.run_prediction`` calls your kernels over the data.
"""
import numpy as np


def returns(rewards, gamma):
    """Discounted returns of one complete episode.

    ``rewards[t]`` is the reward after step ``t``. Returns an array ``G`` of the
    same length with ``G[t] = rewards[t] + gamma * rewards[t+1] + ...``.
    """
    raise NotImplementedError("TODO: write this function")


def mc_update(V, episode, alpha, gamma):
    """Constant-step-size, every-visit Monte Carlo update from one complete episode.

    First compute the return ``G[t]`` of every step. Then, in chronological
    order (t = 0, 1, ...), apply ``V[S_t] <- V[S_t] + alpha * (G[t] - V[S_t])``.
    A state visited several times is updated once per visit.

    Updates ``V`` in place and returns it.
    """
    raise NotImplementedError("TODO: write this function")


def td0_update(V, s, r, s_next, terminated, alpha, gamma):
    """One TD(0) update for the transition ``(s, r, s_next)``.

    The target is ``r + gamma * V[s_next]``; when ``terminated`` is true it is
    ``r`` alone. A transition that was only cut off by the time limit
    (truncated, not terminated) still bootstraps from ``V[s_next]``.

    Updates ``V`` in place and returns it.
    """
    raise NotImplementedError("TODO: write this function")
