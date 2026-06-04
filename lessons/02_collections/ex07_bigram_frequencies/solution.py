"""Exercise solution.

You should only edit this file.
"""

from __future__ import annotations


def bigram_frequencies(words: list[str]) -> dict[tuple[str, str], int]:
    bigram = {}
    word_length = len(words)
    i = 0
    while i < word_length - 1 :
        if (words[i], words[i+1]) in bigram:
            bigram[(words[i], words[i+1])] += 1
        else:
            bigram[(words[i],words[i+1])] = 1

        i += 1
            
    return bigram

