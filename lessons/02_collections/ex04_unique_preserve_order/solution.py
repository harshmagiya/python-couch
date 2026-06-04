"""Exercise solution.

You should only edit this file.
"""

from __future__ import annotations


def unique_preserve_order(items: list[str]) -> list[str]:
    unique_item = []
    for item in items:
        if item in unique_item:
            pass
        else:
            unique_item.append(item)
    return unique_item
