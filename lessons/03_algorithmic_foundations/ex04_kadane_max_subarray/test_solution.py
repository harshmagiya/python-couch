import ast
import inspect
import textwrap

import pytest

from testutils import load_solution


solution = load_solution(__file__)


def _assert_no_nested_loop(func) -> None:
    """AST-only check. Disallow O(n^2) brute force inside the function."""
    src = textwrap.dedent(inspect.getsource(func))
    tree = ast.parse(src)
    for node in ast.walk(tree):
        if isinstance(node, ast.For):
            for child in ast.walk(node):
                if child is not node and isinstance(child, ast.For):
                    raise AssertionError(
                        "Do not use nested loops in this exercise; "
                        "Kadane's is a single-pass O(n) algorithm."
                    )


def _assert_no_dp_table(func) -> None:
    """AST-only check. Disallow a full DP array of length proportional to n."""
    src = textwrap.dedent(inspect.getsource(func))
    tree = ast.parse(src)
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for tgt in node.targets:
                if isinstance(tgt, ast.Name) and tgt.id in {"dp", "table", "memo"}:
                    if isinstance(node.value, (ast.List, ast.ListComp)):
                        raise AssertionError(
                            "Do not build a full DP table for this exercise; "
                            "keep a single scalar."
                        )


def test_empty_raises():
    with pytest.raises(ValueError):
        solution.max_subarray_sum([])


def test_single_element():
    assert solution.max_subarray_sum([5]) == 5
    assert solution.max_subarray_sum([-7]) == -7


def test_canonical_example():
    assert solution.max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_all_positive():
    assert solution.max_subarray_sum([1, 2, 3, 4, 5]) == 15


def test_all_negative_returns_largest():
    assert solution.max_subarray_sum([-3, -1, -2]) == -1
    assert solution.max_subarray_sum([-10, -5, -3]) == -3


def test_mixed_with_negatives():
    assert solution.max_subarray_sum([1, -3, 2, 1, -1]) == 3
    assert solution.max_subarray_sum([-1, 2, -1, 3, -2]) == 4


def test_single_positive_in_negatives():
    assert solution.max_subarray_sum([-5, -2, 3, -1, -4]) == 3


def test_zeros_mixed_in():
    assert solution.max_subarray_sum([0, -1, 0, 2, 0, -3, 0, 1]) == 2


def test_best_at_end():
    # The best subarray is at the end; the running `cur` will equal `best` at
    # the final position. Catches the "return cur instead of best" bug.
    assert solution.max_subarray_sum([-1, -2, 5, 1, 2]) == 8


def test_best_in_middle_not_at_end():
    # The best subarray is in the middle; `cur` at the final position is
    # strictly less than `best`. Catches the same bug in a different shape.
    assert solution.max_subarray_sum([1, 2, -5, 3, 4, -1, -1, -1]) == 6


def test_constraint_no_nested_loop():
    _assert_no_nested_loop(solution.max_subarray_sum)


def test_constraint_no_dp_table():
    _assert_no_dp_table(solution.max_subarray_sum)
