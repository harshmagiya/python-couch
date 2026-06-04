import pytest

from testutils import load_solution


solution = load_solution(__file__)


def test_empty():
    assert solution.group_anagrams([]) == []


def test_example_grouping_and_ordering():
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    assert solution.group_anagrams(words) == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]


def test_preserves_order_within_group():
    words = ["ab", "ba", "ab", "b a"]
    assert solution.group_anagrams(words) == [["ab", "ba", "ab"], ["b a"]]


def test_case_sensitive():
    assert solution.group_anagrams(["a", "A", "a"]) == [["a", "a"], ["A"]]


def test_allows_empty_string():
    assert solution.group_anagrams(["", "", "a"]) == [["", ""], ["a"]]


def test_constraint_no_defaultdict(monkeypatch):
    import collections

    def boom(*_args, **_kwargs):
        raise AssertionError("Do not use collections.defaultdict in this exercise")

    monkeypatch.setattr(collections, "defaultdict", boom)
    assert solution.group_anagrams(["ab", "ba"]) == [["ab", "ba"]]
