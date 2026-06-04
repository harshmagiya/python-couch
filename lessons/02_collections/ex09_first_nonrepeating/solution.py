"""Exercise solution.

You should only edit this file.
"""

from __future__ import annotations


def first_nonrepeating(items: list[str]) -> str | None:
    
    
    item_count = {}
    for item in items:
        if item in item_count:
            item_count[item] += 1
        else:
            item_count[item] = 1
    for key,value in item_count.items():
        if value == 1:
            return key
    return None