"""Exercise solution.

You should only edit this file.
"""

from __future__ import annotations


def merge_inventory(start: dict[str, int], changes: list[tuple[str, int]]) -> dict[str, int]:
    
    final = start.copy()
    for item, delta in changes:
        if item in final:
            if final[item] + delta != 0:
                final[item] = final[item] + delta
            else:
                final.pop(item)
        else:
            final[item] = delta
        
    return final