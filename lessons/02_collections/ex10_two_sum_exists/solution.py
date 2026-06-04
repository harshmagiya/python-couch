"""Exercise solution.

You should only edit this file.
"""

from __future__ import annotations


def two_sum_exists(nums: list[int], target: int) -> bool:

    seen_num = set()
    for item in nums:
        if target - item in seen_num:
            return True
        seen_num.add(item)
    return False
    