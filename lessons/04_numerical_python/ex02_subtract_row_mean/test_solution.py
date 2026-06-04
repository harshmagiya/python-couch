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
                "Use numpy broadcasting."
            )


def _assert_no_tile_or_repeat(func) -> None:
    """AST-only check. Disallow `np.tile` / `np.repeat` / `np.broadcast_to`."""
    src = textwrap.dedent(inspect.getsource(func))
    tree = ast.parse(src)
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr in {"tile", "repeat", "broadcast_to"}:
                raise AssertionError(
                    "Do not use np.tile / np.repeat / np.broadcast_to in this exercise; "
                    "the point is broadcasting with keepdims=True."
                )


def test_canonical():
    out = solution.subtract_row_mean([[1.0, 2.0, 3.0], [4.0, 4.0, 4.0]])
    assert out == pytest.approx([[-1.0, 0.0, 1.0], [0.0, 0.0, 0.0]])


def test_single_row():
    out = solution.subtract_row_mean([[5.0, 5.0]])
    assert out == pytest.approx([[0.0, 0.0]])


def test_single_column():
    out = solution.subtract_row_mean([[1.0], [2.0], [3.0]])
    assert out == pytest.approx([[0.0], [0.0], [0.0]])


def test_each_row_sums_to_zero():
    rng = np.random.default_rng(0)
    arr = rng.standard_normal((7, 5))
    out = np.asarray(solution.subtract_row_mean(arr.tolist()))
    row_sums = out.sum(axis=1)
    assert row_sums == pytest.approx(np.zeros(7), abs=1e-9)


def test_returns_python_floats_not_numpy():
    out = solution.subtract_row_mean([[1.0, 2.0, 3.0], [4.0, 4.0, 4.0]])
    assert type(out) is list
    assert type(out[0]) is list
    for x in out[0] + out[1]:
        assert type(x) is float


def test_does_not_mutate_input():
    original = [[1.0, 2.0, 3.0], [4.0, 4.0, 4.0]]
    snapshot = [row[:] for row in original]
    _ = solution.subtract_row_mean(original)
    assert original == snapshot


def test_empty_raises():
    with pytest.raises(ValueError):
        solution.subtract_row_mean([])


def test_irregular_shape():
    # Tall thin matrix: many rows, few columns.
    arr = np.array([[1.0, 2.0]] * 4 + [[5.0, -1.0]] * 4)  # 8 rows, 2 cols
    out = np.asarray(solution.subtract_row_mean(arr.tolist()))
    assert out.shape == (8, 2)
    # First 4 rows: all [1, 2] -> centred to [0, 0].
    assert out[:4] == pytest.approx(np.zeros((4, 2)))
    # Last 4 rows: [5, -1] -> mean 2 -> centred to [3, -3].
    assert out[4:] == pytest.approx(np.array([[3.0, -3.0]] * 4))


def test_uses_keepdims_shape_dance():
    """Inspect the source to ensure `keepdims=True` is used."""
    src = textwrap.dedent(inspect.getsource(solution.subtract_row_mean))
    assert "keepdims" in src, (
        "Did you forget `keepdims=True` on the .mean() call? "
        "Without it, row means are shape (n_rows,) and do not broadcast over (n_rows, n_cols)."
    )


def test_constraint_no_python_loops():
    _assert_no_python_loops(solution.subtract_row_mean)


def test_constraint_no_tile_or_repeat():
    _assert_no_tile_or_repeat(solution.subtract_row_mean)
