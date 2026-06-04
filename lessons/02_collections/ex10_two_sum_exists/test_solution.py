import pytest

from testutils import load_solution


solution = load_solution(__file__)


def test_empty_or_single():
    assert solution.two_sum_exists([], 0) is False
    assert solution.two_sum_exists([1], 1) is False


def test_basic_true():
    assert solution.two_sum_exists([2, 7, 11, 15], 9) is True


def test_basic_false():
    assert solution.two_sum_exists([1, 2, 3], 7) is False


def test_duplicates_can_form_pair():
    assert solution.two_sum_exists([3, 3], 6) is True


def test_negative_numbers():
    assert solution.two_sum_exists([-1, 2, 4], 3) is True
    assert solution.two_sum_exists([-1, -2, -3], -5) is True


def test_does_not_sort_input():
    nums = [3, 1, 2]
    _ = solution.two_sum_exists(nums, 3)
    assert nums == [3, 1, 2]
