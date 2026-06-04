"""Exercise solution.

You should only edit this file.
"""

from __future__ import annotations


def parse_kv_lines(text: str) -> dict[str, str]:
    line_dict = {}
    lines = text.split('\n')
    for line in lines:
        clean_line = line.replace(' ', '')
        if not clean_line:
            continue
        if  clean_line[0] == '#':
            continue
        if '=' not in clean_line:
            raise ValueError
        key_value = clean_line.split('=',1)
        if not key_value[0]:
            raise ValueError
        line_dict[key_value[0]] = key_value[1]
    return line_dict