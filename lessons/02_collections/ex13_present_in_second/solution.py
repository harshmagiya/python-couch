"""Exercise solution.

You should only edit this file.
"""

from __future__ import annotations


def present_in_second(first: list[str], second: list[str]) -> list[str]:
    
    repeat_item = []
    repeat_set = set()
    second_list = set(second)
    for i in first:
        if i in second_list and i not in repeat_set:
            repeat_item.append(i)
            repeat_set.add(i)

    return repeat_item
