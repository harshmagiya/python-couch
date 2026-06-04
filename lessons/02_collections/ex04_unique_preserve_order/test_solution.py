import ast
import inspect
import textwrap

import pytest

from testutils import load_solution


solution = load_solution(__file__)


def _assert_no_dict_fromkeys(func) -> None:
    src = textwrap.dedent(inspect.getsource(func))
    tree = ast.parse(src)

    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr == "fromkeys":
                raise AssertionError("Do not use dict.fromkeys in this exercise")


def test_empty():
    assert solution.unique_preserve_order([]) == []


def test_no_duplicates():
    assert solution.unique_preserve_order(["a", "b", "c"]) == ["a", "b", "c"]


def test_preserves_first_occurrence_order():
    items = ["a", "b", "a", "c", "b", "d", "c"]
    assert solution.unique_preserve_order(items) == ["a", "b", "c", "d"]


def test_case_sensitive():
    assert solution.unique_preserve_order(["a", "A", "a"]) == ["a", "A"]


def test_allows_empty_strings():
    assert solution.unique_preserve_order(["", "", "x", ""]) == ["", "x"]


def test_constraint_no_dict_fromkeys(monkeypatch):
    _assert_no_dict_fromkeys(solution.unique_preserve_order)
    assert solution.unique_preserve_order(["a", "b", "a"]) == ["a", "b"]
