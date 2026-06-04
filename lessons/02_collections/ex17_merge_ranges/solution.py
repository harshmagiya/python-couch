"""Exercise solution.

You should only edit this file.
"""

from __future__ import annotations


def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not ranges:
        return []
    merge = []
    sorted_ranges = sorted(ranges)
    start, end = sorted_ranges[0]
    for i,j in sorted_ranges[1:]:
        if i <=end+1:
            end = max(j,end)
        else:
            merge.append((start,end))
            start = i
            end = j
    merge.append((start,end))
    return merge
