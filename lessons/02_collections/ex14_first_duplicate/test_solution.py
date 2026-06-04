import pytest

from testutils import load_solution


solution = load_solution(__file__)


def test_empty_and_single():
    assert solution.first_duplicate([]) is None
    assert solution.first_duplicate(["a"]) is None


def test_no_duplicates():
    assert solution.first_duplicate(["x", "y", "z"]) is None


def test_picks_by_second_occurrence_position():
    assert solution.first_duplicate(["a", "b", "a", "b"]) == "a"


def test_duplicate_immediate():
    assert solution.first_duplicate(["a", "a", "b"]) == "a"


def test_allows_empty_strings():
    assert solution.first_duplicate(["", "x", ""]) == ""
