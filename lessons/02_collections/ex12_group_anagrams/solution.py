"""Exercise solution.

You should only edit this file.
"""

from __future__ import annotations


def group_anagrams(words: list[str]) -> list[list[str]]:
    anagram_pairs = {}
    for word in words:
        sig = ''.join(sorted(word))
        if sig in anagram_pairs:
            anagram_pairs[sig].append(word)
        else:
            anagram_pairs[sig] = [word]

    return list(anagram_pairs.values())