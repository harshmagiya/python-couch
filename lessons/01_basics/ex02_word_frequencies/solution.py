"""Exercise solution.

You should only edit this file.
"""

from __future__ import annotations
import re

def word_frequencies(text: str) -> dict[str, int]:

    punct = '.,;:!?\"\'()[]'
    clean_text = ''
    for char in text:
        if char not in punct:
            clean_text += char
        else:
            clean_text += " "

    words = clean_text.split()
    word_dict = {}
    if not words:
        return {}
    for word in words:
        if word.lower() in word_dict.keys():
            word_dict[word.lower()] += 1
        else:
            word_dict[word.lower()] = 1

    return word_dict


    raise NotImplementedError
