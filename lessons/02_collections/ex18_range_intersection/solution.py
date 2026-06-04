"""Exercise solution.

You should only edit this file.
"""

from __future__ import annotations


def intersect_ranges(
    a: list[tuple[int, int]],
    b: list[tuple[int, int]],
) -> list[tuple[int, int]]:
    intersection = []
    i = j = 0
    while i< len(a) and j<len(b):
        a_start , a_end = a[i]
        b_start , b_end = b[j]
        hi = min(a_end,b_end)
        lo = max(a_start,b_start)
        if lo <= hi:
            intersection.append((lo,hi))
        if a_end < b_end:
            i+=1
        else:
            j+=1
    
    return intersection