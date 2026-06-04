"""Exercise solution.

You should only edit this file.
"""

from __future__ import annotations


def softmax_rows(x: list[list[float]]) -> list[list[float]]:
    """Apply stable softmax along the row axis.

    - For each row, subtract the row max, exp, divide by row sum.
    - Use numpy with keepdims=True broadcasting.
    - No scipy, no Python loops.
    - If x is empty, raise ValueError.
    """
    raise NotImplementedError
