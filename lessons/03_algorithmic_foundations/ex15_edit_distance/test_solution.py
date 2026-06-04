import ast
import inspect
import textwrap

import pytest

from testutils import load_solution


solution = load_solution(__file__)


def _assert_no_full_matrix(func) -> None:
    """Reject the full m*n DP matrix; the prompt requires the rolling form.

    A full matrix is a 2-D list assignment like `dp = [[0] * (n + 1) for _ in range(m + 1)]`.
    A 2-D list comprehension of length proportional to m is the unambiguous
    signal of a full-matrix solution.
    """
    src = textwrap.dedent(inspect.getsource(func))
    tree = ast.parse(src)
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        for tgt in node.targets:
            if isinstance(tgt, ast.Name) and tgt.id in {"dp", "table", "memo"}:
                if isinstance(node.value, ast.ListComp):
                    # `dp = [[0] * (n + 1) for _ in range(m + 1)]` is a
                    # list comprehension with a list elt and a range() iter.
                    elt = node.value.elt
                    is_full_matrix = (
                        isinstance(elt, ast.List)
                        and len(elt.elts) == 1
                        and isinstance(elt.elts[0], ast.Constant)
                    )
                    if is_full_matrix:
                        raise AssertionError(
                            "Do not build a full m*n DP matrix for this exercise; "
                            "use the two-row rolling form (O(min(m, n)) space)."
                        )


def test_both_empty():
    assert solution.edit_distance("", "") == 0


def test_equal_strings():
    assert solution.edit_distance("abc", "abc") == 0
    assert solution.edit_distance("a", "a") == 0
    assert solution.edit_distance("hello world", "hello world") == 0


def test_one_empty():
    assert solution.edit_distance("", "abc") == 3
    assert solution.edit_distance("abc", "") == 3
    assert solution.edit_distance("", "a") == 1
    assert solution.edit_distance("a", "") == 1


def test_single_substitution():
    assert solution.edit_distance("a", "b") == 1
    assert solution.edit_distance("cat", "bat") == 1


def test_canonical_kitten_sitting():
    assert solution.edit_distance("kitten", "sitting") == 3


def test_canonical_flaw_lawn():
    assert solution.edit_distance("flaw", "lawn") == 2


def test_canonical_intention_execution():
    assert solution.edit_distance("intention", "execution") == 5


def test_swap_costs_two():
    # ab -> ba: cannot swap, must delete+insert (or substitute twice).
    assert solution.edit_distance("ab", "ba") == 2


def test_insert_at_end():
    assert solution.edit_distance("abc", "abcd") == 1


def test_delete_at_start():
    assert solution.edit_distance("xabc", "abc") == 1


def test_symmetric():
    a, b = "abcdef", "azced"
    assert solution.edit_distance(a, b) == solution.edit_distance(b, a)


def test_with_unicode():
    # 3 chars, all different -> 3 substitutions
    assert solution.edit_distance("αβγ", "xyz") == 3
    # Same -> 0
    assert solution.edit_distance("αβγ", "αβγ") == 0


def test_large_strings_complete_quickly():
    """O(m*n) on 500x500 should complete in well under a second."""
    a = "a" * 500
    b = "b" * 500
    result = solution.edit_distance(a, b)
    assert result == 500  # 500 substitutions


def test_constraint_no_full_matrix():
    _assert_no_full_matrix(solution.edit_distance)
