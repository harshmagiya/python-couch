"""Exercise solution.

You should only edit this file.
"""

from __future__ import annotations


def missing_in_bounds(
    ranges: list[tuple[int, int]],
    bounds: tuple[int, int],
) -> list[tuple[int, int]]:
    missing: list[tuple[int, int]] = []
    lo, hi = bounds
    cur = lo
    for s, e in ranges:
        if cur > hi:
            break
        # Range entirely before current cursor (can happen if range is left of bounds).
        if e < cur:
            continue
        # Since ranges are sorted by start, if this starts after hi, we're done.
        if s > hi:
            break
        if cur < s:
            missing.append((cur, min(hi, s - 1)))
        cur = max(cur, e + 1)
    if cur <= hi:
        missing.append((cur, hi))
    return missing
        

        
