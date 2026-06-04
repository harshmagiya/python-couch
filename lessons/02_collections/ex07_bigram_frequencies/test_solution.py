import pytest

from testutils import load_solution


solution = load_solution(__file__)


def test_empty_or_single_word():
    assert solution.bigram_frequencies([]) == {}
    assert solution.bigram_frequencies(["a"]) == {}


def test_basic_bigrams():
    words = ["a", "b", "a"]
    assert solution.bigram_frequencies(words) == {("a", "b"): 1, ("b", "a"): 1}


def test_repeated_bigram():
    assert solution.bigram_frequencies(["x", "x", "x"]) == {("x", "x"): 2}


def test_case_sensitive():
    words = ["a", "A", "a"]
    assert solution.bigram_frequencies(words) == {("a", "A"): 1, ("A", "a"): 1}


def test_allows_empty_strings():
    words = ["", "x", ""]
    assert solution.bigram_frequencies(words) == {("", "x"): 1, ("x", ""): 1}


def test_constraint_no_collections_counter(monkeypatch):
    import collections

    def boom(*_args, **_kwargs):
        raise AssertionError("Do not use collections.Counter in this exercise")

    monkeypatch.setattr(collections, "Counter", boom)
    assert solution.bigram_frequencies(["a", "b", "a"]) == {("a", "b"): 1, ("b", "a"): 1}


def test_constraint_no_itertools_pairwise(monkeypatch):
    import itertools

    def boom(*_args, **_kwargs):
        raise AssertionError("Do not use itertools.pairwise in this exercise")

    monkeypatch.setattr(itertools, "pairwise", boom)
    assert solution.bigram_frequencies(["a", "b", "c"]) == {("a", "b"): 1, ("b", "c"): 1}
