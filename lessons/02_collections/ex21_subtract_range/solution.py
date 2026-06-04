"""Exercise solution.

You should only edit this file.
"""

from __future__ import annotations


def subtract_range(
    ranges: list[tuple[int, int]],
    remove: tuple[int, int],
) -> list[tuple[int, int]]:
    r_start, r_end = remove
    new_ranges = []
    for s, e in ranges:
        if e < r_start or r_end < s:
            new_ranges.append((s,e))
        elif s >= r_start and e <= r_end:
           continue
        else:
            if s < r_start:
                new_ranges.append((s,r_start-1))
            if e > r_end:
                new_ranges.append((r_end+1,e))
    return new_ranges
