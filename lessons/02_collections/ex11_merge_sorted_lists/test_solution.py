import pytest

from testutils import load_solution


solution = load_solution(__file__)


def test_basic_merge():
    assert solution.merge_sorted([1, 3, 5], [2, 4]) == [1, 2, 3, 4, 5]


def test_preserves_duplicates():
    assert solution.merge_sorted([1, 1], [1]) == [1, 1, 1]


def test_empty_inputs():
    assert solution.merge_sorted([], []) == []
    assert solution.merge_sorted([1, 2], []) == [1, 2]
    assert solution.merge_sorted([], [3]) == [3]


def test_does_not_mutate_inputs():
    a = [1, 2]
    b = [1]
    out = solution.merge_sorted(a, b)
    assert a == [1, 2]
    assert b == [1]
    assert out == [1, 1, 2]
