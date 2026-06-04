import pytest

from testutils import load_solution


solution = load_solution(__file__)


def test_canonical():
    assert solution.max_sum_subarray_k([1, 4, 2, 10], 2) == 12


def test_k_equals_1():
    assert solution.max_sum_subarray_k([1, 4, 2, 10], 1) == 10


def test_k_equals_length():
    assert solution.max_sum_subarray_k([1, 4, 2, 10], 4) == 17


def test_single_element():
    assert solution.max_sum_subarray_k([5], 1) == 5


def test_k_zero():
    assert solution.max_sum_subarray_k([1, 2, 3], 0) == 0


def test_all_negative_k_equals_1():
    assert solution.max_sum_subarray_k([-1, -2, -3], 1) == -1


def test_all_negative_k_equals_length():
    assert solution.max_sum_subarray_k([-1, -2, -3], 3) == -6


def test_mixed_with_negatives():
    assert solution.max_sum_subarray_k([2, -1, 3, -2, 4], 2) == 4


def test_window_at_end_is_best():
    assert solution.max_sum_subarray_k([1, 2, 3, 100, 4, 5], 2) == 105


def test_window_at_start_is_best():
    assert solution.max_sum_subarray_k([100, 4, 5, 1, 2, 3], 2) == 104


def test_k_greater_than_length_raises():
    with pytest.raises(ValueError):
        solution.max_sum_subarray_k([1, 2, 3], 4)


def test_empty_with_positive_k_raises():
    with pytest.raises(ValueError):
        solution.max_sum_subarray_k([], 1)


def test_empty_with_zero_k_returns_zero():
    assert solution.max_sum_subarray_k([], 0) == 0


def test_all_zeros():
    assert solution.max_sum_subarray_k([0, 0, 0, 0], 2) == 0
