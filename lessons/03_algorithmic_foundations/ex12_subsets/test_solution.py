import ast
import inspect
import textwrap

import pytest

from testutils import load_solution


solution = load_solution(__file__)


def _assert_no_itertools_combinations(func) -> None:
    """AST-only check. Ban imports of itertools.combinations and calls to it."""
    src = textwrap.dedent(inspect.getsource(func))
    tree = ast.parse(src)
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            if node.module and node.module.split(".")[0] == "itertools":
                for alias in node.names:
                    if alias.name == "combinations":
                        raise AssertionError("Do not import itertools.combinations in this exercise.")
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr == "combinations":
                raise AssertionError("Do not use itertools.combinations in this exercise.")


def test_empty():
    assert solution.subsets([]) == [[]]


def test_single():
    assert solution.subsets([1]) == [[], [1]]


def test_two():
    assert solution.subsets([1, 2]) == [[], [1], [2], [1, 2]]


def test_three_unsorted_input():
    assert solution.subsets([3, 1, 2]) == [
        [], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]
    ]


def test_three_with_negatives():
    assert solution.subsets([-1, 0, 1]) == [
        [], [-1], [0], [1], [-1, 0], [-1, 1], [0, 1], [-1, 0, 1]
    ]


def test_four_size_is_2_pow_n():
    out = solution.subsets([1, 2, 3, 4])
    assert len(out) == 2 ** 4


def test_four_count_by_length():
    out = solution.subsets([1, 2, 3, 4])
    counts = {}
    for s in out:
        counts[len(s)] = counts.get(len(s), 0) + 1
    assert counts == {0: 1, 1: 4, 2: 6, 3: 4, 4: 1}


def test_no_shared_internal_lists():
    """Mutating one subset must not affect the others."""
    out = solution.subsets([1, 2, 3])
    for s in out:
        s.append(999)
    fresh = solution.subsets([1, 2, 3])
    for s in fresh:
        assert 999 not in s


def test_constraint_no_itertools_combinations():
    _assert_no_itertools_combinations(solution.subsets)
