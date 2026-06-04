"""Exercise solution.

You should only edit this file.
"""

from __future__ import annotations


def compact_ranges(nums: list[int]) -> list[tuple[int, int]]:
    
    ranges = []
    if not nums:
        return ranges
    start = end = nums[0]
    for i in nums[1:]:
        if i == end + 1:
            end = i
        else:
            ranges.append((start, end))
            start = i
            end = i
    ranges.append((start, end))
    return ranges