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


def _assert_uses_keepdims(func) -> None:
    """Source-level check. The solution uses keepdims=True for broadcasting."""
    src = textwrap.dedent(inspect.getsource(func))
    assert "keepdims" in src, (
        "Did you forget `keepdims=True` on the .max() or .sum() call? "
        "Without it, the (n_rows,) shape does not broadcast with (n_rows, n_cols)."
    )


def _assert_no_scipy(func) -> None:
    """The prompt bans scipy.special.softmax."""
    import inspect as _inspect

    module = _inspect.getmodule(func)
    if module is None:
        return
    src = textwrap.dedent(_inspect.getsource(module))
    tree = ast.parse(src)
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and (node.module or "").startswith("scipy"):
            raise AssertionError("Do not import scipy in this exercise; implement the softmax yourself.")
        if isinstance(node, ast.Import) and any(
            alias.name.split(".")[0] == "scipy" for alias in node.names
        ):
            raise AssertionError("Do not import scipy in this exercise; implement the softmax yourself.")


def test_canonical_single_row():
    out = solution.softmax_rows([[1.0, 2.0, 3.0]])
    expected = np.exp([-2, -1, 0]) / np.exp([-2, -1, 0]).sum()
    assert out[0] == pytest.approx(expected.tolist())


def test_two_rows_uniform_second():
    out = solution.softmax_rows([[1.0, 2.0, 3.0], [4.0, 4.0, 4.0]])
    assert out[0] == pytest.approx(np.exp([-2, -1, 0]) / np.exp([-2, -1, 0]).sum())
    assert out[1] == pytest.approx([1.0 / 3, 1.0 / 3, 1.0 / 3])


def test_each_row_sums_to_one():
    rng = np.random.default_rng(0)
    arr = rng.standard_normal((5, 7))
    out = np.asarray(solution.softmax_rows(arr.tolist()))
    assert out.sum(axis=1) == pytest.approx(np.ones(5), abs=1e-9)


def test_large_positive_does_not_overflow():
    # The unstable form would give inf/nan; stable form gives uniform.
    out = solution.softmax_rows([[1000.0, 1000.0, 1000.0]])
    assert all(np.isfinite(v) for v in out[0])
    assert out[0] == pytest.approx([1.0 / 3, 1.0 / 3, 1.0 / 3])


def test_large_negative_does_not_underflow():
    out = solution.softmax_rows([[-1000.0, -1000.0, -1000.0]])
    assert all(np.isfinite(v) for v in out[0])
    assert out[0] == pytest.approx([1.0 / 3, 1.0 / 3, 1.0 / 3])


def test_mixed_extremes():
    out = solution.softmax_rows([[-1000.0, 0.0, 1000.0]])
    # 1000 dominates; answer is ~ [0, 0, 1] within float.
    assert out[0][2] == pytest.approx(1.0, abs=1e-9)
    assert out[0][0] == pytest.approx(0.0, abs=1e-9)


def test_non_square_matrix():
    # 4 rows, 7 columns: forces the keepdims=True shape dance.
    arr = np.array(
        [
            [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0],
            [7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [-1.0, -2.0, -3.0, -4.0, -5.0, -6.0, -7.0],
        ]
    )
    out = np.asarray(solution.softmax_rows(arr.tolist()))
    assert out.shape == (4, 7)
    assert out.sum(axis=1) == pytest.approx(np.ones(4), abs=1e-9)


def test_returns_python_floats_not_numpy():
    out = solution.softmax_rows([[1.0, 2.0, 3.0]])
    assert type(out) is list
    assert type(out[0]) is list
    for x in out[0]:
        assert type(x) is float


def test_empty_raises():
    with pytest.raises(ValueError):
        solution.softmax_rows([])


def test_all_nonneg_in_range():
    rng = np.random.default_rng(0)
    arr = rng.standard_normal((3, 4)) * 5
    out = np.asarray(solution.softmax_rows(arr.tolist()))
    assert (out >= 0).all()
    assert (out <= 1).all()


def test_constraint_no_python_loops():
    _assert_no_python_loops(solution.softmax_rows)


def test_constraint_uses_keepdims():
    _assert_uses_keepdims(solution.softmax_rows)


def test_constraint_no_scipy():
    _assert_no_scipy(solution.softmax_rows)
