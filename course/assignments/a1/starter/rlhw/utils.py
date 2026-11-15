"""Small shared helpers (supplied; do not modify)."""
import numpy as np


def argmax_lowest(values, tol=1e-9):
    """Index of the largest entry; ties go to the lowest index.

    Entries within ``tol`` of the maximum count as tied. Use this for every
    greedy choice in the homework (planning and control), so that floating-point
    noise cannot change which of two equally good actions is picked.
    """
    values = np.asarray(values, dtype=float)
    return int(np.flatnonzero(values >= values.max() - tol)[0])
