"""Schedules for the exploration rate and the step size (supplied; do not modify).

A schedule maps the schedule clock to a value. In this homework the clock is the
number of environment transitions taken so far, over all episodes, starting at 0.
"""


class Constant:
    """The same value at every step."""

    def __init__(self, value):
        self._value = float(value)

    def value(self, step):
        return self._value

    def __repr__(self):
        return f"Constant({self._value})"


class ExponentialDecay:
    """value(step) = max(floor, start * rate ** step)."""

    def __init__(self, start, rate, floor=0.0):
        self.start, self.rate, self.floor = float(start), float(rate), float(floor)

    def value(self, step):
        return max(self.floor, self.start * self.rate ** step)

    def __repr__(self):
        return f"ExponentialDecay(start={self.start}, rate={self.rate}, floor={self.floor})"
