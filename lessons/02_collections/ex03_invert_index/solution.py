"""Exercise solution.

You should only edit this file.
"""

from __future__ import annotations


def invert_index(pairs: list[tuple[str, str]]) -> dict[str, list[str]]:
    inverted_dict = {}
    for user,tag in pairs:
        if tag not in inverted_dict:
            inverted_dict[tag] = [user]
        else:
            inverted_dict[tag].append(user)

    asc_dict = {user:sorted(set(tag)) for user,tag in inverted_dict.items()}
    return asc_dict

