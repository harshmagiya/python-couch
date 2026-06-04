import pytest

from testutils import load_solution


solution = load_solution(__file__)


def test_empty_input():
    assert solution.invert_index([]) == {}


def test_basic_inversion():
    pairs = [("alice", "p1"), ("bob", "p1"), ("alice", "p2")]
    assert solution.invert_index(pairs) == {"p1": ["alice", "bob"], "p2": ["alice"]}


def test_deduplicates_users_within_tag():
    pairs = [("a", "x"), ("a", "x"), ("b", "x"), ("b", "x")]
    assert solution.invert_index(pairs) == {"x": ["a", "b"]}


def test_users_sorted_lexicographically():
    pairs = [("b", "x"), ("a", "x"), ("c", "x")]
    assert solution.invert_index(pairs) == {"x": ["a", "b", "c"]}


def test_allows_empty_strings():
    pairs = [("", "x"), ("a", ""), ("", "x")]
    assert solution.invert_index(pairs) == {"": ["a"], "x": [""]}


def test_constraint_no_defaultdict(monkeypatch):
    import collections

    def boom(*_args, **_kwargs):
        raise AssertionError("Do not use collections.defaultdict in this exercise")

    monkeypatch.setattr(collections, "defaultdict", boom)
    assert solution.invert_index([("a", "x"), ("b", "x")]) == {"x": ["a", "b"]}
