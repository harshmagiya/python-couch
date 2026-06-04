import pytest

from testutils import load_solution


solution = load_solution(__file__)


def test_empty():
    assert solution.longest_run([]) == 0


def test_single_item():
    assert solution.longest_run(["x"]) == 1


def test_basic_runs():
    items = ["a", "a", "b", "b", "b", "a"]
    assert solution.longest_run(items) == 3


def test_all_unique():
    assert solution.longest_run(["a", "b", "c"]) == 1


def test_all_same():
    assert solution.longest_run(["z", "z", "z"]) == 3


def test_allows_empty_strings():
    assert solution.longest_run(["", "", "x", "", ""]) == 2
