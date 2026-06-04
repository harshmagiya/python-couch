import ast
import inspect
import textwrap

import pytest

from testutils import load_solution


solution = load_solution(__file__)


def _assert_no_shortcuts(func) -> None:
    """AST-only check. Ban nums[::-1], reversed(...), and .reverse() calls."""
    src = textwrap.dedent(inspect.getsource(func))
    tree = ast.parse(src)
    for node in ast.walk(tree):
        if isinstance(node, ast.Subscript) and isinstance(node.slice, ast.Slice):
            raise AssertionError("Do not use slicing in this exercise.")
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id == "reversed":
                raise AssertionError("Do not use reversed(...) in this exercise.")
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr == "reverse":
                raise AssertionError("Do not use the .reverse() method in this exercise.")


def test_empty():
    xs: list[int] = []
    out = solution.reverse_list_in_place(xs)
    assert out is xs
    assert out == []


def test_single():
    xs = [1]
    out = solution.reverse_list_in_place(xs)
    assert out is xs
    assert out == [1]


def test_two():
    xs = [1, 2]
    out = solution.reverse_list_in_place(xs)
    assert out is xs
    assert out == [2, 1]


def test_three():
    xs = [1, 2, 3]
    out = solution.reverse_list_in_place(xs)
    assert out is xs
    assert out == [3, 2, 1]


def test_four_even():
    xs = [1, 2, 3, 4]
    out = solution.reverse_list_in_place(xs)
    assert out is xs
    assert out == [4, 3, 2, 1]


def test_five_odd():
    xs = [1, 2, 3, 4, 5]
    out = solution.reverse_list_in_place(xs)
    assert out is xs
    assert out == [5, 4, 3, 2, 1]


def test_all_same():
    xs = [7, 7, 7, 7]
    out = solution.reverse_list_in_place(xs)
    assert out is xs
    assert out == [7, 7, 7, 7]


def test_negatives():
    xs = [-3, -1, 0, 2, 5]
    out = solution.reverse_list_in_place(xs)
    assert out is xs
    assert out == [5, 2, 0, -1, -3]


def test_palindrome_unchanged():
    xs = [1, 2, 3, 2, 1]
    out = solution.reverse_list_in_place(xs)
    assert out is xs
    assert out == [1, 2, 3, 2, 1]


def test_returns_same_list_object():
    xs = [1, 2, 3]
    out = solution.reverse_list_in_place(xs)
    assert out is xs


def test_constraint_no_shortcuts():
    _assert_no_shortcuts(solution.reverse_list_in_place)
