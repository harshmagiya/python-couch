"""Exercise solution.

You should only edit this file.
"""

from __future__ import annotations


def reverse_dict_unique(d: dict[str, str]) -> dict[str, str]:
    
    reverse_d = {}
    for key,value in d.items():
        if value in reverse_d:
            raise ValueError(f"There are two key mapping to the same value:{value}")
        else:
            reverse_d[value] = key
    return reverse_d