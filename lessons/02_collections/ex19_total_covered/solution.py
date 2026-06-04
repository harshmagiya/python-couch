"""Exercise solution.

You should only edit this file.
"""

from __future__ import annotations


def total_covered(ranges: list[tuple[int, int]]) -> int:
    sorted_range = sorted(ranges)
    count = 0
    if not ranges:
        return count
    integer, _ = sorted_range[0]
    for range in sorted_range:
        start ,end = range
        if integer< start:
            integer = start
        if integer <= end:
            count += end - integer + 1
            integer = end + 1
    return count
