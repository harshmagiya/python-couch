"""Exercise solution.

You should only edit this file.
"""

from __future__ import annotations


def confusion_counts(
    y_true: list[int],
    y_pred: list[int],
    *,
    positive: int = 1,
) -> tuple[int, int, int, int]:
    raise NotImplementedError


def precision_recall_f1(
    y_true: list[int],
    y_pred: list[int],
    *,
    positive: int = 1,
) -> tuple[float, float, float]:
    raise NotImplementedError
