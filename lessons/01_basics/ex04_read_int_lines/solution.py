"""Exercise solution.

You should only edit this file.
"""

from __future__ import annotations

from pathlib import Path


def read_int_lines(path: Path) -> list[int]:
    int_list = []
    with path.open('r') as file:
        text_file = file.read()
    
    lines = text_file.split('\n')
    for line in lines:
        clean_line = line.strip()
        if not clean_line:
            continue
        if clean_line[0] == '#':
            continue
        print(clean_line)
        try:
            int_list.append(int(clean_line))
        except:
            raise ValueError(f'Line {lines.index(line)+1} is not an integer')
    return int_list
