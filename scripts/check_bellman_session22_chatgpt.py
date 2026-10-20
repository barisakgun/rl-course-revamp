#!/usr/bin/env python3
"""Reproduce proposed Bellman session 2.2 examples without editing any artifact.

Run: python3 scripts/check_bellman_session22_chatgpt.py

Uses only the standard library and exact fractions. Calculation grid: gamma 1/2;
accepted reward-sensitivity comparison: gamma 9/10 (Bellman decision C17).
80/10/10 motion, blocked moves stay put, terminal rewards paid on entry
instead of a living reward, and zero terminal continuation. Output is
verification of teaching examples, not a source of curriculum decisions.
"""

from fractions import Fraction as F
from itertools import product

A = ("up", "right", "down", "left")
D = ((0, 1), (1, 0), (0, -1), (-1, 0))


def model(w, h, term, wall=(), living=F(-1, 25)):
    states = [
        (x, y)
        for x in range(1, w + 1)
        for y in range(1, h + 1)
        if (x, y) not in wall and (x, y) not in term
    ]
    m = {}
    for s in states:
        for a in range(4):
            rows = []
            for direction, p in [
                (a, F(4, 5)),
                ((a - 1) % 4, F(1, 10)),
                ((a + 1) % 4, F(1, 10)),
            ]:
                dx, dy = D[direction]
                sp = (s[0] + dx, s[1] + dy)
                if not (1 <= sp[0] <= w and 1 <= sp[1] <= h) or sp in wall:
                    sp = s
                rows.append((p, sp, term.get(sp, living)))
            assert sum(p for p, _, _ in rows) == 1
            m[s, a] = rows
    return states, m


def q(m, v, s, a, gamma=F(1, 2)):
    return sum(p * (r + gamma * v.get(sp, 0)) for p, sp, r in m[s, a])


def solve(states, m, pi, gamma=F(1, 2)):
    n = len(states)
    mat = [
        [
            F(i == j) - gamma * sum(p for p, sp, r in m[s, pi[s]] if sp == t)
            for j, t in enumerate(states)
        ]
        + [sum(p * r for p, sp, r in m[s, pi[s]])]
        for i, s in enumerate(states)
    ]
    for i in range(n):
        pivot = mat[i][i]
        assert pivot
        mat[i] = [x / pivot for x in mat[i]]
        for j in range(n):
            if i != j:
                coef = mat[j][i]
                mat[j] = [x - coef * y for x, y in zip(mat[j], mat[i])]
    return dict(zip(states, [row[-1] for row in mat]))


def greedy(states, m, v, pi, gamma=F(1, 2)):
    out = {}
    for s in states:
        vals = [q(m, v, s, a, gamma) for a in range(4)]
        mx = max(vals)
        out[s] = pi[s] if vals[pi[s]] == mx else vals.index(mx)
    return out


def display(v):
    return {str(s): round(float(x), 8) for s, x in v.items()}


if __name__ == "__main__":
    states, m = model(2, 2, {(2, 2): F(1)})
    pi = {s: 1 for s in states}
    v = solve(states, m, pi)
    print("STATES", states, "OLD", display(v))
    print(
        "Q OLD",
        {
            str(s): {A[a]: round(float(q(m, v, s, a)), 8) for a in range(4)}
            for s in states
        },
    )
    for i in range(4):
        new = greedy(states, m, v, pi)
        print("PI", i, [A[new[s]] for s in states])
        nv = solve(states, m, new)
        print("EVAL", display(nv), {str(s): str(x) for s, x in nv.items()})
        assert all(nv[s] >= v[s] for s in states)
        if new == pi:
            break
        pi, v = new, nv
    for candidate in product(range(4), repeat=3):
        cv = solve(states, m, dict(zip(states, candidate)))
        assert all(v[s] >= cv[s] for s in states)
    vi = {s: F(0) for s in states}
    for k in range(1, 4):
        vi = {s: max(q(m, vi, s, a) for a in range(4)) for s in states}
        print("VI", k, display(vi))
    gamma = F(9, 10)
    for living in [F(-2), F(-2, 5), F(-1, 25), F(0), F(1, 5)]:
        st, mo = model(
            4, 3, {(4, 3): F(1), (4, 2): F(-1)}, wall={(2, 2)}, living=living
        )
        pol = {s: 1 for s in st}
        for i in range(100):
            val = solve(st, mo, pol, gamma)
            npol = greedy(st, mo, val, pol, gamma)
            if npol == pol:
                break
            pol = npol
        else:
            raise AssertionError("No convergence")
        assert all(val[s] == max(q(mo, val, s, a, gamma) for a in range(4)) for s in st)
        print(
            "LIVING",
            str(living),
            "PI ROUNDS",
            i,
            "at(3,2)",
            A[pol[3, 2]],
            "at(1,1)",
            A[pol[1, 1]],
            "at(3,3)",
            A[pol[3, 3]],
        )
        for y in [3, 2, 1]:
            print(
                " ".join(
                    (
                        "X"
                        if (x, y) == (2, 2)
                        else (
                            "+"
                            if (x, y) == (4, 3)
                            else (
                                "-"
                                if (x, y) == (4, 2)
                                else "/".join(
                                    A[a]
                                    for a in range(4)
                                    if q(mo, val, (x, y), a, gamma) == val[x, y]
                                )
                            )
                        )
                    )
                    for x in [1, 2, 3, 4]
                )
            )
    print("All checks passed")
