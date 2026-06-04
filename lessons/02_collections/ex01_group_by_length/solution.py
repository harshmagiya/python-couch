"""Exercise solution.

You should only edit this file.
"""

from __future__ import annotations


def group_by_length(words: list[str]) -> dict[int, list[str]]:
    word_dict = {}
    for word in words:
        if len(word) not in word_dict.keys():
            word_dict[len(word)] = [word]
        else:
            word_dict[len(word)].append(word)

    return word_dict
