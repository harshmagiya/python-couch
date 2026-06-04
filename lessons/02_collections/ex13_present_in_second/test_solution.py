import pytest

from testutils import load_solution


solution = load_solution(__file__)


def test_empty_inputs():
    assert solution.present_in_second([], []) == []
    assert solution.present_in_second(["a"], []) == []
    assert solution.present_in_second([], ["a"]) == []


def test_basic_filter_and_order():
    first = ["a", "b", "a", "c", "b", "d"]
    second = ["b", "c", "x"]
    assert solution.present_in_second(first, second) == ["b", "c"]


def test_deduplicates_output():
    assert solution.present_in_second(["x", "x", "x"], ["x"]) == ["x"]


def test_case_sensitive():
    assert solution.present_in_second(["a", "A", "a"], ["A"]) == ["A"]


def test_allows_empty_strings():
    assert solution.present_in_second(["", "x", ""], [""]) == [""]
