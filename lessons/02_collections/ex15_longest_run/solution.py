"""Exercise solution.

You should only edit this file.
"""

from __future__ import annotations


def longest_run(items: list[str]) -> int:
    if not items:
        return 0
    run_length = 0
    longest_run_length = 0
    longest_run_item = items[0]

    for i in items:
        if i != longest_run_item:
            run_length = 1
            longest_run_item = i
        else:
            run_length += 1
        if run_length > longest_run_length:
            longest_run_length = run_length
    return longest_run_length
        

