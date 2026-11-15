"""Part 1 - Planning with the model: value iteration and policy iteration.

Complete the four functions marked TODO. Do not change their names or arguments.

The model ``P`` is ``env.unwrapped.P``: ``P[s][a]`` is a list of
``(probability, next_state, reward, terminated)`` tuples. ``len(P)`` is the number
of states and ``len(P[s])`` the number of actions.

Conventions (the tests rely on them)
------------------------------------
* A transition with ``terminated=True`` contributes its reward only: there is no
  value after termination. Terminal and wall cells have value 0.
* Value tables start at 0.
* Sweeps are synchronous: every state is backed up from the table of the previous
  sweep, not from values already changed in the current sweep.
* Stop after the first sweep whose largest change is strictly below ``theta``;
  that final sweep is counted.
* Greedy choices use ``argmax_lowest`` (ties go to the lowest action index).
"""
import numpy as np

from rlhw import argmax_lowest
from rlhw.drivers import policy_evaluation


def q_from_v(P, V, s, gamma):
    """One-step lookahead: the action values of state ``s`` under the table ``V``.

    Returns an array with one entry per action:
    sum over outcomes of probability * (reward + gamma * V[next_state]),
    without the ``gamma * V[next_state]`` term when the outcome terminates.
    """
    raise NotImplementedError("TODO: write this function")


def value_iteration(P, gamma, theta):
    """Value iteration.

    Returns ``(V, n_sweeps)``: the final value table (array of length
    ``len(P)``) and the number of sweeps performed.
    """
    raise NotImplementedError("TODO: write this function")


def policy_improvement(P, V, gamma):
    """The greedy policy for the table ``V``.

    Returns an integer array with one action per state (ties to the lowest index).
    """
    raise NotImplementedError("TODO: write this function")


def policy_iteration(P, gamma, theta):
    """Policy iteration, using the supplied ``policy_evaluation``.

    Start from the policy that takes action 0 in every state. Repeat: evaluate
    the current policy with ``policy_evaluation(P, policy, gamma, theta)``, then
    improve it. Stop when an improvement step leaves the policy unchanged.

    Returns ``(policy, V, n_improvements, n_evaluation_sweeps)``:
    the final policy, its value table, the number of improvement steps
    (including the last one, which changes nothing), and the total number of
    evaluation sweeps over all evaluations.
    """
    raise NotImplementedError("TODO: write this function")
