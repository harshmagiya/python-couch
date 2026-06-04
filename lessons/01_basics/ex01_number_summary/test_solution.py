import math

import pytest

from testutils import load_solution


solution = load_solution(__file__)


def test_empty_returns_none():
    assert solution.number_summary([]) is None


def test_simple_ints():
    out = solution.number_summary([2, 4, 6])
    assert out is not None
    assert out == {"count": 3, "min": 2.0, "max": 6.0, "mean": 4.0}


def test_floats_and_negatives():
    out = solution.number_summary([1.5, -2.0, 0.5])
    assert out is not None
    assert out["count"] == 3
    assert math.isclose(out["min"], -2.0)
    assert math.isclose(out["max"], 1.5)
    assert math.isclose(out["mean"], 0.0)


def test_single_value():
    out = solution.number_summary([7])
    assert out is not None
    assert out == {"count": 1, "min": 7.0, "max": 7.0, "mean": 7.0}


def test_output_types():
    out = solution.number_summary([1, 2, 3])
    assert out is not None
    assert isinstance(out["count"], int)
    assert isinstance(out["min"], float)
    assert isinstance(out["max"], float)
    assert isinstance(out["mean"], float)


def test_constraint_single_pass_smoke(monkeypatch):
    """Discourage use of min/max/sum by making them fail in this module."""

    def boom(*_args, **_kwargs):
        raise AssertionError("Do not use built-in min/max/sum in this exercise")

    monkeypatch.setattr(solution, "min", boom, raising=False)
    monkeypatch.setattr(solution, "max", boom, raising=False)
    monkeypatch.setattr(solution, "sum", boom, raising=False)

    out = solution.number_summary([3, 1, 2])
    assert out == {"count": 3, "min": 1.0, "max": 3.0, "mean": 2.0}
