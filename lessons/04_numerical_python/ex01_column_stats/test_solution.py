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
            # List comprehensions over axis iteration are still loops.
            raise AssertionError(
                "Do not use Python for/while loops (or comprehensions over rows/cols) "
                "in this exercise. Use numpy's vectorised reductions."
            )


def _assert_uses_numpy(func) -> None:
    """AST-only check. The solution module must `import numpy`."""
    import inspect as _inspect

    module = _inspect.getmodule(func)
    if module is None:
        raise AssertionError("Could not locate the solution module.")
    src = textwrap.dedent(_inspect.getsource(module))
    tree = ast.parse(src)
    has_numpy = False
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and (node.module or "").startswith("numpy"):
            has_numpy = True
            break
        if isinstance(node, ast.Import) and any(
            alias.name.split(".")[0] == "numpy" for alias in node.names
        ):
            has_numpy = True
            break
        if isinstance(node, ast.Attribute) and node.attr in {"asarray", "array", "mean", "std"}:
            # Heuristic: calling .mean / .std on something is numpy-ish.
            has_numpy = True
            break
    if not has_numpy:
        raise AssertionError("Use numpy for this exercise; the point is vectorisation.")


def test_canonical():
    arr = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
    means, stds = solution.column_stats(arr.tolist())
    assert list(means) == pytest.approx([3.0, 4.0])
    assert list(stds) == pytest.approx([arr[:, 0].std(ddof=0), arr[:, 1].std(ddof=0)])


def test_single_row():
    means, stds = solution.column_stats([[7.0, 8.0, 9.0]])
    assert list(means) == pytest.approx([7.0, 8.0, 9.0])
    assert list(stds) == pytest.approx([0.0, 0.0, 0.0])


def test_single_column():
    means, stds = solution.column_stats([[1.0], [2.0], [3.0], [4.0]])
    assert list(means) == pytest.approx([2.5])
    assert list(stds) == pytest.approx([np.std([1, 2, 3, 4], ddof=0)])


def test_all_equal_column():
    means, stds = solution.column_stats([[7.0, 7.0], [7.0, 7.0]])
    assert list(means) == pytest.approx([7.0, 7.0])
    assert list(stds) == pytest.approx([0.0, 0.0])


def test_returns_python_floats_not_numpy():
    means, stds = solution.column_stats([[1.0, 2.0], [3.0, 4.0]])
    # tolist() returns plain Python floats, not numpy scalars.
    for x in means:
        assert type(x) is float, f"expected float, got {type(x)}"
    for x in stds:
        assert type(x) is float, f"expected float, got {type(x)}"


def test_population_std_not_sample():
    # Population std of [1, 2, 3] is sqrt(2/3) ~ 1.1547.
    # Sample std of [1, 2, 3] is sqrt(1) = 1.0.
    means, stds = solution.column_stats([[1.0], [2.0], [3.0]])
    assert list(means) == pytest.approx([2.0])
    assert list(stds) == pytest.approx([np.sqrt(2.0 / 3.0)])
    # And NOT 1.0 (which would be sample std).
    assert abs(stds[0] - 1.0) > 1e-6


def test_empty_raises():
    with pytest.raises(ValueError):
        solution.column_stats([])


def test_negative_values():
    means, stds = solution.column_stats([[-1.0, 2.0], [1.0, -2.0]])
    assert list(means) == pytest.approx([0.0, 0.0])
    assert list(stds) == pytest.approx([np.sqrt(2.0), np.sqrt(8.0)])


def test_many_rows():
    rng = np.random.default_rng(0)
    arr = rng.standard_normal((50, 3))
    means, stds = solution.column_stats(arr.tolist())
    assert list(means) == pytest.approx(arr.mean(axis=0))
    assert list(stds) == pytest.approx(arr.std(axis=0, ddof=0))


def test_constraint_no_python_loops():
    _assert_no_python_loops(solution.column_stats)


def test_constraint_uses_numpy():
    _assert_uses_numpy(solution.column_stats)
