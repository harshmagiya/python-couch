"""Exercise solution.

You should only edit this file.
"""

from __future__ import annotations


def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    merged_numbers = []
    i = 0
    j = 0
    while 1:
        if i == len(a):
            merged_numbers += b[j:]
            break
        if j == len(b):
            merged_numbers += a[i:]
            break
        if a[i] <= b[j]:
            merged_numbers.append(a[i])
            i += 1
        else:
            merged_numbers.append(b[j])
            j += 1
            
    return merged_numbers