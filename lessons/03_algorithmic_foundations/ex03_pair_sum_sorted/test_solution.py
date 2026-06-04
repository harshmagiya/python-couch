import ast
import inspect
import textwrap

import pytest

from testutils import load_solution


solution = load_solution(__file__)


def _assert_no_dict_or_set_complement_lookup(func) -> None:
    """Detect the 'seen = set()' / 'target - x in seen' hash pattern.

    This exercise must use the two-pointer technique on the sorted input,
    not the O(n) hash-based 'two-sum' pattern.
    """
    src = textwrap.dedent(inspect.getsource(func))
    tree = ast.parse(src)
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for tgt in node.targets:
                if isinstance(tgt, ast.Name) and tgt.id in {"seen", "lookup", "complements"}:
                    if isinstance(node.value, ast.Call):
                        func_name = ast.unparse(node.value.func) if hasattr(ast, "unparse") else ""
                        if "set" in func_name or "dict" in func_name:
                            raise AssertionError(
                                "Do not use a dict/set 'complement' lookup in this exercise; "
                                "use the two-pointer technique on the sorted input."
                            )


def test_empty():
    assert solution.pair_sum_sorted([], 0) is None


def test_single_element():
    assert solution.pair_sum_sorted([5], 5) is None


def test_basic_true():
    i, j = solution.pair_sum_sorted([2, 7, 11, 15], 9)
    assert i < j
    assert [2, 7, 11, 15][i] + [2, 7, 11, 15][j] == 9


def test_basic_false():
    assert solution.pair_sum_sorted([1, 2, 3], 7) is None


def test_two_elements_true():
    i, j = solution.pair_sum_sorted([3, 3], 6)
    assert (i, j) == (0, 1)


def test_two_elements_false():
    assert solution.pair_sum_sorted([1, 2], 100) is None


def test_pinned_indices():
    i, j = solution.pair_sum_sorted([1, 2, 3, 4, 6], 10)
    assert (i, j) == (3, 4)


def test_pinned_indices_alt():
    i, j = solution.pair_sum_sorted([1, 2, 3, 4, 6], 7)
    assert i < j
    arr = [1, 2, 3, 4, 6]
    assert arr[i] + arr[j] == 7


def test_negatives_zero_target():
    i, j = solution.pair_sum_sorted([-3, -1, 1, 3], 0)
    arr = [-3, -1, 1, 3]
    assert (i, j) == (0, 3)
    assert arr[i] + arr[j] == 0


def test_zeros():
    i, j = solution.pair_sum_sorted([0, 0], 0)
    assert (i, j) == (0, 1)


def test_all_same():
    arr = [5, 5, 5, 5, 5]
    i, j = solution.pair_sum_sorted(arr, 10)
    assert (i, j) == (0, 4)


def test_first_and_last():
    i, j = solution.pair_sum_sorted([1, 5], 6)
    assert (i, j) == (0, 1)


def test_constraint_no_set_lookup():
    _assert_no_dict_or_set_complement_lookup(solution.pair_sum_sorted)
