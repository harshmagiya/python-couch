import pytest

from testutils import load_solution


solution = load_solution(__file__)


def test_k_zero_or_negative():
    assert solution.top_k_frequencies(["a", "a"], 0) == []
    assert solution.top_k_frequencies(["a", "a"], -1) == []


def test_empty_items():
    assert solution.top_k_frequencies([], 3) == []


def test_basic_top_k():
    items = ["a", "b", "a", "c", "b", "a"]
    assert solution.top_k_frequencies(items, 2) == [("a", 3), ("b", 2)]


def test_tie_breaker_lexicographic():
    items = ["b", "a", "b", "a"]
    assert solution.top_k_frequencies(items, 2) == [("a", 2), ("b", 2)]


def test_k_larger_than_distinct():
    items = ["x", "y", "x"]
    assert solution.top_k_frequencies(items, 10) == [("x", 2), ("y", 1)]


def test_constraint_no_collections_counter(monkeypatch):
    import collections

    def boom(*_args, **_kwargs):
        raise AssertionError("Do not use collections.Counter in this exercise")

    monkeypatch.setattr(collections, "Counter", boom)
    assert solution.top_k_frequencies(["a", "a", "b"], 1) == [("a", 2)]
