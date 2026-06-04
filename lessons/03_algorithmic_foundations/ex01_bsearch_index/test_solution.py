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


def test_empty_returns_minus_one():
    assert solution.bsearch_index([], 5) == -1


def test_single_present():
    assert solution.bsearch_index([5], 5) == 0


def test_single_absent():
    assert solution.bsearch_index([5], 3) == -1


def test_target_at_start():
    assert solution.bsearch_index([1, 3, 5, 7, 9], 1) == 0


def test_target_at_end():
    assert solution.bsearch_index([1, 3, 5, 7, 9], 9) == 4


def test_target_in_middle():
    assert solution.bsearch_index([1, 3, 5, 7, 9], 7) == 3


def test_target_not_present():
    assert solution.bsearch_index([1, 3, 5, 7, 9], 4) == -1


def test_target_smaller_than_all():
    assert solution.bsearch_index([5, 6, 7], 1) == -1


def test_target_larger_than_all():
    assert solution.bsearch_index([5, 6, 7], 100) == -1


def test_negatives():
    arr = [-10, -5, -3, 0, 2, 8, 10]
    assert solution.bsearch_index(arr, -3) == 2
    assert solution.bsearch_index(arr, -100) == -1
    assert solution.bsearch_index(arr, 10) == 6


def test_duplicates_any_valid_index():
    result = solution.bsearch_index([1, 1, 1, 1], 1)
    assert result in (0, 1, 2, 3)


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([1, 2, 3, 4, 5], 1, 0),
        ([1, 2, 3, 4, 5], 3, 2),
        ([1, 2, 3, 4, 5], 5, 4),
        ([1, 2, 3, 4, 5], 0, -1),
        ([1, 2, 3, 4, 5], 6, -1),
        ([10, 20, 30, 40, 50, 60, 70], 30, 2),
        ([10, 20, 30, 40, 50, 60, 70], 25, -1),
    ],
)
def test_position_parametrized(arr, target, expected):
    assert solution.bsearch_index(arr, target) == expected


def test_constraint_no_bisect_module():
    _assert_no_bisect_import(solution.bsearch_index)
