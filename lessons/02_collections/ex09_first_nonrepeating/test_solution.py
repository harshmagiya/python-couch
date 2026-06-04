import pytest

from testutils import load_solution


solution = load_solution(__file__)


def test_empty_returns_none():
    assert solution.first_nonrepeating([]) is None


def test_single_item():
    assert solution.first_nonrepeating(["a"]) == "a"


def test_finds_first_unique_by_position():
    items = ["a", "b", "a", "c", "b", "d"]
    assert solution.first_nonrepeating(items) == "c"


def test_none_when_no_unique_exists():
    assert solution.first_nonrepeating(["x", "x"]) is None
    assert solution.first_nonrepeating(["a", "b", "a", "b"]) is None


def test_case_sensitive():
    assert solution.first_nonrepeating(["a", "A", "a"]) == "A"


def test_allows_empty_strings():
    assert solution.first_nonrepeating(["", "x", "x"]) == ""


def test_constraint_no_collections_counter(monkeypatch):
    import collections

    def boom(*_args, **_kwargs):
        raise AssertionError("Do not use collections.Counter in this exercise")

    monkeypatch.setattr(collections, "Counter", boom)
    assert solution.first_nonrepeating(["a", "b", "a"]) == "b"
