"""Exercise solution.

You should only edit this file.
"""

from __future__ import annotations


def first_duplicate(items: list[str]) -> str | None:
    
    item_set = set()
    for i in items:
        if i in item_set:
            return i
        else:
            item_set.add(i)
    
    return None
