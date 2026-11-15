"""Part 3 - Control from interaction: SARSA and Q-learning in one loop.

Complete the six functions marked TODO. Do not change their names or arguments.

``Q`` is an array of shape ``(n_states, n_actions)``. Part 3 must not use the
model ``env.unwrapped.P``; it learns from ``env.reset`` and ``env.step`` only.
"""
import numpy as np

from rlhw import argmax_lowest


def init_q(n_states, n_actions, value, terminal_states):
    """A Q-table filled with ``value``; the rows of terminal states are 0."""
    raise NotImplementedError("TODO: write this function")


def epsilon_greedy_probs(q_row, epsilon):
    """Action probabilities of the epsilon-greedy policy for one state.

    Every action gets ``epsilon / n_actions``; the greedy action (from
    ``argmax_lowest``) gets the remaining ``1 - epsilon`` on top.
    """
    raise NotImplementedError("TODO: write this function")


def select_action(q_row, epsilon, rng):
    """Sample an action from ``epsilon_greedy_probs`` with the generator ``rng``.

    ``rng`` is a ``numpy.random.Generator``; use it for all randomness.
    """
    raise NotImplementedError("TODO: write this function")


def sarsa_target(Q, r, s_next, a_next, terminated, gamma):
    """SARSA target: ``r + gamma * Q[s_next, a_next]``; ``r`` alone if terminated."""
    raise NotImplementedError("TODO: write this function")


def q_learning_target(Q, r, s_next, terminated, gamma):
    """Q-learning target: ``r + gamma * max_a Q[s_next, a]``; ``r`` alone if terminated."""
    raise NotImplementedError("TODO: write this function")


def train(env, method, gamma, epsilon_schedule, alpha_schedule, q_init, n_episodes, seed,
          select_fn=select_action):
    """Tabular control with SARSA (``method="sarsa"``) or Q-learning (``"q_learning"``).

    Requirements
    ------------
    * Work on a copy of ``q_init``.
    * Create one generator, ``rng = np.random.default_rng(seed)``. Reset the
      environment with ``env.reset(seed=seed)`` for the first episode and
      ``env.reset()`` afterwards.
    * Choose every action with ``select_fn(Q[state], epsilon, rng)`` and in no
      other way.
    * The schedule clock ``k`` counts environment transitions over all episodes,
      starting at 0. The action executed as transition ``k`` is selected with
      ``epsilon_schedule.value(k)``; the update for transition ``k`` uses
      ``alpha_schedule.value(k)``.
    * SARSA selects the next action once, uses it in the target, and then
      executes that same action as the next transition.
    * An episode ends when ``terminated`` or ``truncated`` is true. On
      termination the target is the reward alone. On truncation both methods
      still bootstrap from the final observation; SARSA selects a next action
      for its target (with ``epsilon_schedule.value(k + 1)``) even though that
      action is never executed.

    Returns ``(Q, episode_returns, episode_lengths)``: the learned table, the
    undiscounted sum of rewards of each episode, and the number of transitions
    of each episode.
    """
    raise NotImplementedError("TODO: write this function")
