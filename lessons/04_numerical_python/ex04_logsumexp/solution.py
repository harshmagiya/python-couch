"""Exercise solution.

You should only edit this file.
"""

from __future__ import annotations


def logsumexp(x: list[float]) -> float:
    """Return log(sum(exp(x_i))) computed in a numerically stable way.

    - For large positive x, the naive form log(sum(exp(x))) overflows;
      factor out the max first.
    - For empty x, raise ValueError.
    - Use numpy; no Python loops.
    """
    raise NotImplementedError
