import ast
import inspect
import textwrap

import pytest

from testutils import load_solution


solution = load_solution(__file__)


def _assert_no_nested_loops_over_pairs(func) -> None:
    """Reject an O(n^3) shape: nested loops over all subsequence pairs."""
    # The O(n^2) DP is allowed (it has nested loops but over a 1-D state).
    # The O(n^3) shape is "two outer loops for i,j plus a third inner loop
    # for the subsequence check". We don't try to distinguish; we just
    # reject any function whose body has *three or more* nested For loops.
    src = textwrap.dedent(inspect.getsource(func))
    tree = ast.parse(src)
    for outer in ast.walk(tree):
        if not isinstance(outer, ast.For):
            continue
        for middle in ast.walk(outer):
            if middle is outer or not isinstance(middle, ast.For):
                continue
            for inner in ast.walk(middle):
                if inner is middle or not isinstance(inner, ast.For):
                    continue
                raise AssertionError(
                    "Do not use triple-nested loops in this exercise; "
                    "the O(n^2) DP has only double-nested loops."
                )


def _assert_no_itertools_subsequence_enumeration(func) -> None:
    """Reject `itertools.combinations(...)` over the input to enumerate
    all subsequences."""
    src = textwrap.dedent(inspect.getsource(func))
    tree = ast.parse(src)
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr == "combinations":
                raise AssertionError(
                    "Do not enumerate all subsequences with itertools.combinations; "
                    "use the O(n^2) DP."
                )


def test_empty():
    assert solution.lis([]) == 0


def test_single():
    assert solution.lis([5]) == 1
    assert solution.lis([-1]) == 1


def test_strictly_increasing():
    assert solution.lis([1, 2, 3, 4, 5]) == 5


def test_strictly_decreasing():
    assert solution.lis([5, 4, 3, 2, 1]) == 1


def test_all_same():
    assert solution.lis([2, 2, 2]) == 1


def test_canonical_example():
    assert solution.lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4


def test_alternating():
    assert solution.lis([0, 1, 0, 3, 2, 3]) == 4


def test_with_negatives():
    assert solution.lis([-1, 0, 1, 2, -1, -1]) == 4


def test_lis_ends_in_middle_not_at_end():
    # For [3, 1, 2], the LIS is [1, 2], length 2, ending at index 2.
    # Returning dp[-1] would still be 2 here, but consider [3, 1, 2, 0]:
    # LIS is [1, 2], length 2, ending at index 2; dp[-1] = 1 (wrong).
    assert solution.lis([3, 1, 2, 0]) == 2


def test_returns_max_not_last():
    # If the implementation returns dp[-1] by mistake, this fails.
    # LIS of [1, 5, 2, 3, 4] is [1, 2, 3, 4], length 4, ending at index 4 (last).
    # LIS of [1, 3, 2] is [1, 2] or [1, 3], length 2, ending at index 1 or 2.
    # LIS of [4, 1, 2, 3] is [1, 2, 3], length 3, ending at index 3 (last).
    # The classic "max not last" test:
    assert solution.lis([2, 5, 3, 1, 4]) == 3
    assert solution.lis([4, 1, 2, 3, 0]) == 3


def test_constraint_no_triple_loops():
    _assert_no_nested_loops_over_pairs(solution.lis)


def test_constraint_no_combinations_enumeration():
    _assert_no_itertools_subsequence_enumeration(solution.lis)
