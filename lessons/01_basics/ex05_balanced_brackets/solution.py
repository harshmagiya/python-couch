"""Exercise solution.

You should only edit this file.
"""

from __future__ import annotations


def is_balanced(s: str) -> bool:
    open_brac = ['(','[','{']
    close_brac = [']',')','}']
    brac_list = []
    brac_relation = {'[':']','(':')','{':'}'}
    for i in s:
        if i in open_brac:
            brac_list.append(i)
        elif i in close_brac and brac_list:
            if brac_relation[brac_list[-1]] == i:
                brac_list.pop(-1)
            else:
                print(1)
                return False
        elif i in close_brac and not brac_list:
            print(2)
            return False

    if  brac_list:
        print(3)
        return False
    else:
        return True
