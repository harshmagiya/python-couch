import ast
import inspect
import textwrap

import pytest

from testutils import load_solution


solution = load_solution(__file__)


def _assert_no_itertools_chain_from_iterable(func) -> None:
    """AST-only check. Ban calls to .from_iterable(...)."""
    src = textwrap.dedent(inspect.getsource(func))
    tree = ast.parse(src)
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr == "from_iterable":
                raise AssertionError("Do not use itertools.chain.from_iterable in this exercise.")


def test_empty():
    assert solution.flatten([]) == []


def test_already_flat():
    assert solution.flatten([1, 2, 3]) == [1, 2, 3]


def test_one_level_nested():
    assert solution.flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]


def test_two_levels():
    assert solution.flatten([[1, [2, 3]], [4, [5]]]) == [1, 2, 3, 4, 5]


def test_deeply_nested_chain():
    assert solution.flatten([1, [2, [3, [4, [5]]]]]) == [1, 2, 3, 4, 5]


def test_mixed_at_same_level():
    assert solution.flatten([1, [2, 3], 4, [5, [6, 7]], 8]) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_only_nested_lists():
    assert solution.flatten([[[1]], [[2]]]) == [1, 2]


def test_empty_inner_list():
    assert solution.flatten([1, [], 2]) == [1, 2]


def test_single_element_nested():
    assert solution.flatten([[42]]) == [42]


def test_negatives_and_zero():
    assert solution.flatten([-1, [0, [-2, [0]]], 3]) == [-1, 0, -2, 0, 3]


def test_constraint_no_itertools_chain_from_iterable():
    _assert_no_itertools_chain_from_iterable(solution.flatten)
