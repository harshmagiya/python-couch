import pytest

from testutils import load_solution


solution = load_solution(__file__)


def test_empty_string():
    assert solution.word_frequencies("") == {}


def test_whitespace_only():
    assert solution.word_frequencies("   \n\t  ") == {}


def test_basic_counting_and_casefold():
    assert solution.word_frequencies("Hi hi HI") == {"hi": 3}


def test_punctuation_is_ignored():
    text = "Python, python! PYTHON?"
    assert solution.word_frequencies(text) == {"python": 3}


def test_mixed_punctuation_set():
    text = "a.(a)[a] 'a' \"a\" (a)!"
    assert solution.word_frequencies(text) == {"a": 6}


def test_newlines_tabs_and_multiple_spaces():
    text = "\t a\nA  b  a\n"
    assert solution.word_frequencies(text) == {"a": 3, "b": 1}


def test_constraint_no_collections_counter(monkeypatch):
    import collections

    def boom(*_args, **_kwargs):
        raise AssertionError("Do not use collections.Counter in this exercise")

    monkeypatch.setattr(collections, "Counter", boom)
    assert solution.word_frequencies("x x") == {"x": 2}
