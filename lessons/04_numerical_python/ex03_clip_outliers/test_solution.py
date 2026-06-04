import ast
import inspect
import textwrap

import numpy as np
import pytest

from testutils import load_solution


solution = load_solution(__file__)


def _assert_no_python_loops(func) -> None:
    """AST-only check. The implementation must be vectorised."""
    src = textwrap.dedent(inspect.getsource(func))
    tree = ast.parse(src)
    for node in ast.walk(tree):
        if isinstance(node, (ast.For, ast.While, ast.ListComp, ast.SetComp, ast.GeneratorExp)):
            raise AssertionError(
                "Do not use Python for/while loops (or comprehensions) in this exercise. "
                "Use numpy's vectorised operations."
            )


def _assert_uses_boolean_masking(func) -> None:
    """AST-only check. The solution must use np.where (boolean masking)."""
    src = textwrap.dedent(inspect.getsource(func))
    tree = ast.parse(src)
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr == "where":
                return
    raise AssertionError(
        "Use np.where (boolean masking) in this exercise; the point is the "
        "three-valued np.where cascade, not element-by-element logic."
    )


def test_canonical():
    out = solution.clip_outliers([1, 2, 3, 100, 5, 6])
    # 95th percentile of [1,2,3,100,5,6] is somewhere around 60+.
    assert out[3] < 100.0
    # The interior values are unchanged.
    assert out[0] == 1
    assert out[1] == 2
    assert out[2] == 3
    assert out[4] == 5
    assert out[5] == 6


def test_symmetric_extremes_clipped_both_sides():
    x = [-100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 100]
    out = solution.clip_outliers(x, low_pct=5, high_pct=95)
    # The -100 should be clipped upward.
    assert out[0] > -100
    # The 100 should be clipped downward.
    assert out[-1] < 100
    # Interior values unchanged.
    for i in range(1, len(x) - 1):
        assert out[i] == x[i]


def test_no_change_when_no_outliers():
    x = list(range(1, 11))
    out = solution.clip_outliers(x, low_pct=5, high_pct=95)
    # With 5/95 default percentiles on a 10-element range [1..10],
    # 5th percentile ~ 1.45, 95th ~ 9.55. No value is strictly outside.
    assert out == x


def test_returns_python_floats_not_numpy():
    out = solution.clip_outliers([1, 2, 3, 100, 5, 6])
    assert type(out) is list
    for x in out:
        assert type(x) is float


def test_empty_raises():
    with pytest.raises(ValueError):
        solution.clip_outliers([])


def test_low_greater_than_high_raises():
    with pytest.raises(ValueError):
        solution.clip_outliers([1, 2, 3], low_pct=80, high_pct=20)


def test_all_equal_unchanged():
    out = solution.clip_outliers([5.0, 5.0, 5.0, 5.0])
    assert out == [5.0, 5.0, 5.0, 5.0]


def test_single_element_unchanged():
    out = solution.clip_outliers([7.0])
    assert out == [7.0]


def test_pct_zero_and_hundred():
    out = solution.clip_outliers([1, 2, 3, 100, 5, 6], low_pct=0, high_pct=100)
    # 0th percentile is the min (1); 100th is the max (100). No clip.
    assert out == [1, 2, 3, 100, 5, 6]


def test_strict_boundaries_not_clipped_at_equal():
    # If a value equals the boundary, do not clip it.
    x = [5, 5, 5, 5, 5]
    out = solution.clip_outliers(x, low_pct=0, high_pct=100)
    assert out == [5, 5, 5, 5, 5]


def test_constraint_no_python_loops():
    _assert_no_python_loops(solution.clip_outliers)


def test_constraint_uses_boolean_masking():
    _assert_uses_boolean_masking(solution.clip_outliers)
