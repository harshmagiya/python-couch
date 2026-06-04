import ast
import inspect
import math
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


def _assert_subtracts_max(func) -> None:
    """Source-level check. The solution must subtract a max for stability."""
    src = textwrap.dedent(inspect.getsource(func))
    tree = ast.parse(src)
    has_sub = False
    has_max = False
    for node in ast.walk(tree):
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Sub):
            has_sub = True
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr == "max":
                has_max = True
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id == "max":
                has_max = True
    assert has_max, "Compute the max of x first (the stability trick depends on it)."
    assert has_sub, "Subtract the max from each x_i before exponentiating."


def test_canonical():
    out = solution.logsumexp([1.0, 2.0, 3.0])
    assert out == pytest.approx(math.log(math.exp(1) + math.exp(2) + math.exp(3)))


def test_all_zeros():
    out = solution.logsumexp([0.0, 0.0, 0.0])
    assert out == pytest.approx(math.log(3.0))


def test_single_element():
    out = solution.logsumexp([5.0])
    assert out == pytest.approx(5.0)


def test_all_equal():
    out = solution.logsumexp([2.0, 2.0, 2.0, 2.0])
    assert out == pytest.approx(2.0 + math.log(4.0))


def test_large_positive_no_overflow():
    # The unstable form would give inf; stable form gives a finite number.
    out = solution.logsumexp([1000.0, 1000.0, 1000.0])
    assert math.isfinite(out), f"expected finite, got {out}"
    assert out == pytest.approx(1000.0 + math.log(3.0))


def test_large_negative_no_underflow():
    out = solution.logsumexp([-1000.0, -1000.0, -1000.0])
    assert math.isfinite(out)
    assert out == pytest.approx(-1000.0 + math.log(3.0))


def test_mixed_extremes():
    out = solution.logsumexp([-1000.0, 0.0, 1000.0])
    assert math.isfinite(out)
    # The 1000 dominates; answer should be ~ 1000 + log(1 + e^-1000 + e^-2000) ~ 1000.
    assert out == pytest.approx(1000.0, abs=1e-9)


def test_very_large_input():
    out = solution.logsumexp([10000.0, 10001.0, 9999.0])
    assert math.isfinite(out)
    # m = 10001; arr - m = [-1, 0, -2]; exp = [0.3679, 1, 0.1353]; sum ~ 1.5032; log ~ 0.4076
    # answer = 10001 + 0.4076 ~ 10001.4076
    assert out == pytest.approx(10001.0 + math.log(math.exp(-1) + 1.0 + math.exp(-2)))


def test_empty_raises():
    with pytest.raises(ValueError):
        solution.logsumexp([])


def test_returns_python_float():
    out = solution.logsumexp([1.0, 2.0, 3.0])
    assert type(out) is float


def test_constraint_no_python_loops():
    _assert_no_python_loops(solution.logsumexp)


def test_constraint_subtracts_max():
    _assert_subtracts_max(solution.logsumexp)
