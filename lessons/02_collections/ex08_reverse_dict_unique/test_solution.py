import pytest

from testutils import load_solution


solution = load_solution(__file__)


def test_empty():
    assert solution.reverse_dict_unique({}) == {}


def test_basic_reverse():
    d = {"a": "x", "b": "y"}
    assert solution.reverse_dict_unique(d) == {"x": "a", "y": "b"}


def test_does_not_mutate_input():
    d = {"a": "x"}
    out = solution.reverse_dict_unique(d)
    assert d == {"a": "x"}
    assert out == {"x": "a"}


def test_allows_empty_strings():
    d = {"": "x", "a": ""}
    assert solution.reverse_dict_unique(d) == {"x": "", "": "a"}


def test_duplicate_values_raise_value_error():
    with pytest.raises(ValueError):
        solution.reverse_dict_unique({"a": "x", "b": "x"})
