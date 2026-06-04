"""Exercise solution.

You should only edit this file.
"""

from __future__ import annotations


def best_per_category(records: list[tuple[str, str, int]]) -> dict[str, tuple[str, int]]:
    
    final_records = {}
    for category, item, score in records:
        if category in final_records:
            old_item, old_score = final_records[category]
            if old_score < score:
                final_records[category] = (item,score)
            elif old_score == score:
                new_item = sorted([item,old_item])[0]
                final_records[category] = (new_item,score)
        else:
            final_records[category] = (item,score)
    return final_records

