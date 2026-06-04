"""Exercise solution.

You should only edit this file.
"""

from __future__ import annotations


def top_k_frequencies(items: list[str], k: int) -> list[tuple[str, int]]:
    item_dict = {}
    for item in items:
        if item in item_dict:
            item_dict[item] += 1
        else:
            item_dict[item] = 1
    
    if k < 1 or not item_dict:
        return []

    dec_values = sorted(list(set(item_dict.values())), reverse = True)
    nested_dict = {}
    for value in dec_values:
        nested_dict[value] = sorted([key for key,val in item_dict.items() if val == value])

    item_list = []
    while len(item_list) < (min(k,len(item_dict))):
        for key,values in nested_dict.items():
            for val in values:
                item_list.append((val,key))
                
                if len(item_list) == min(k,len(item_dict)):
                    break
            else:
                continue
            break
        else:
            continue
        break
    return item_list