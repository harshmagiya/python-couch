import ast
import inspect
import textwrap

import pytest

from testutils import load_solution


solution = load_solution(__file__)


def _assert_no_bisect_import(func) -> None:
    src = textwrap.dedent(inspect.getsource(func))
    tree = ast.parse(src)
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.split(".")[0] == "bisect":
                    raise AssertionError("Do not import the bisect module in this exercise")
        elif isinstance(node, ast.ImportFrom):
            if node.module and node.module.split(".")[0] == "bisect":
                raise AssertionError("Do not import the bisect module in this exercise")


def test_empty():
    assert solution.first_and_last([], 5) == (-1, -1)


def test_single_present():
    assert solution.first_and_last([5], 5) == (0, 0)


def test_single_absent():
    assert solution.first_and_last([5], 3) == (-1, -1)


def test_target_not_present():
    assert solution.first_and_last([1, 3, 5, 7, 9], 4) == (-1, -1)


def test_target_present_once():
    assert solution.first_and_last([1, 3, 5, 7, 9], 7) == (3, 3)


def test_target_present_multiple_middle():
    assert solution.first_and_last([1, 2, 2, 2, 3, 4], 2) == (1, 3)


def test_target_at_start():
    assert solution.first_and_last([2, 2, 3, 4, 5], 2) == (0, 1)


def test_target_at_end():
    assert solution.first_and_last([1, 2, 3, 4, 4], 4) == (3, 4)


def test_target_fills_array():
    assert solution.first_and_last([5, 5, 5, 5], 5) == (0, 3)


def test_target_smaller_than_all():
    assert solution.first_and_last([5, 6, 7], 1) == (-1, -1)


def test_target_larger_than_all():
    assert solution.first_and_last([5, 6, 7], 100) == (-1, -1)


def test_negatives():
    arr = [-10, -5, -3, -3, 0, 2, 8, 10, 10]
    assert solution.first_and_last(arr, -3) == (2, 3)
    assert solution.first_and_last(arr, 10) == (7, 8)
    assert solution.first_and_last(arr, -100) == (-1, -1)
    assert solution.first_and_last(arr, 100) == (-1, -1)


def test_constraint_no_bisect_module():
    _assert_no_bisect_import(solution.first_and_last)
