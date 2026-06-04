"""Exercise solution.

You should only edit this file.
"""

from __future__ import annotations


def number_summary(nums: list[float]) -> dict[str, float | int] | None:
    """Return basic summary stats for a list of numbers.

    Returns None for an empty list. Otherwise returns a dict with:
    - count (int)
    - min (float)
    - max (float)
    - mean (float)
    """
    if not nums:
        return None

    first = nums[0]
    min_num = first
    max_num = first
    total = 0.0
    count = 0

    for n in nums:
        if n > max_num:
            max_num = n
        if n < min_num:
            min_num = n
        total += float(n)
        count += 1

    return {
        "count": count,
        "min": float(min_num),
        "max": float(max_num),
        "mean": float(total / count),
    }
