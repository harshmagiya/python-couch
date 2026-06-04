import pytest

from testutils import load_solution


solution = load_solution(__file__)


def test_empty_list():
    assert solution.group_by_length([]) == {}


def test_basic_grouping_preserves_order():
    words = ["a", "to", "b", "cat", "do", "I"]
    assert solution.group_by_length(words) == {
        1: ["a", "b", "I"],
        2: ["to", "do"],
        3: ["cat"],
    }


def test_includes_empty_strings():
    assert solution.group_by_length(["", "x", ""]) == {0: ["", ""], 1: ["x"]}


def test_case_sensitive():
    assert solution.group_by_length(["a", "A"]) == {1: ["a", "A"]}
