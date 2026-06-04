"""Exercise solution.

You should only edit this file.
"""

from __future__ import annotations


def insert_range(
    ranges: list[tuple[int, int]],
    new_range: tuple[int, int],
) -> list[tuple[int, int]]:
    new_ranges = []
    new_s, new_e = new_range
    i = 0
    while i < len(ranges):
        s , e = ranges[i]
        if new_s > e + 1:
            new_ranges.append((s,e))
        
        elif max(new_s,s) <= min(new_e,e) + 1:
            new_s = min(new_s,s)
            new_e = max(new_e,e)
        elif new_e < s + 1:
            new_ranges.append((new_s,new_e))
            new_ranges += ranges[i:]
            return new_ranges
        i += 1
    new_ranges.append((new_s,new_e))
    return new_ranges 
