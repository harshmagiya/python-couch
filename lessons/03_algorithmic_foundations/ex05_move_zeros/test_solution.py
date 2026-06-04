import pytest

from testutils import load_solution


solution = load_solution(__file__)


def test_canonical():
    xs = [0, 1, 0, 3, 12]
    out = solution.move_zeros(xs)
    assert out == [1, 3, 12, 0, 0]


def test_returns_same_list_object():
    xs = [0, 1, 0, 3, 12]
    assert solution.move_zeros(xs) is xs


def test_empty():
    xs: list[int] = []
    out = solution.move_zeros(xs)
    assert out is xs
    assert out == []


def test_no_zeros():
    xs = [1, 2, 3, 4]
    out = solution.move_zeros(xs)
    assert out is xs
    assert out == [1, 2, 3, 4]


def test_all_zeros():
    xs = [0, 0, 0]
    out = solution.move_zeros(xs)
    assert out is xs
    assert out == [0, 0, 0]


def test_single_zero():
    xs = [0]
    out = solution.move_zeros(xs)
    assert out is xs
    assert out == [0]


def test_single_nonzero():
    xs = [5]
    out = solution.move_zeros(xs)
    assert out is xs
    assert out == [5]


def test_zeros_at_start():
    xs = [0, 0, 1, 2]
    out = solution.move_zeros(xs)
    assert out == [1, 2, 0, 0]


def test_zeros_at_end():
    xs = [1, 2, 0, 0]
    out = solution.move_zeros(xs)
    assert out == [1, 2, 0, 0]


def test_stability_preserves_order():
    xs = [0, 5, 0, 3, 0, 2, 0, 1]
    out = solution.move_zeros(xs)
    assert out == [5, 3, 2, 1, 0, 0, 0, 0]


def test_mixed_with_negatives():
    xs = [0, -1, 0, -2, 3, 0]
    out = solution.move_zeros(xs)
    assert out == [-1, -2, 3, 0, 0, 0]


def test_interleaved_pair_swap_pattern_rejected():
    """Regression guard: 'swap zero to end' loses stability; the answer
    should keep relative order of non-zeros."""
    xs = [1, 0, 2, 0, 3]
    out = solution.move_zeros(xs)
    assert out == [1, 2, 3, 0, 0]
