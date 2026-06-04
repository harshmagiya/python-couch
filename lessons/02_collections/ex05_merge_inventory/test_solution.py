import pytest

from testutils import load_solution


solution = load_solution(__file__)


def test_does_not_mutate_start():
    start = {"a": 2}
    out = solution.merge_inventory(start, [("a", 1)])
    assert start == {"a": 2}
    assert out == {"a": 3}


def test_new_items_start_from_zero():
    assert solution.merge_inventory({}, [("x", 2)]) == {"x": 2}


def test_applies_multiple_changes_in_order():
    start = {"a": 2, "b": 1}
    changes = [("a", 3), ("b", -2), ("a", -1), ("c", 5)]
    assert solution.merge_inventory(start, changes) == {"a": 4, "b": -1, "c": 5}


def test_omits_zero_final_counts():
    assert solution.merge_inventory({"a": 2}, [("a", -2)]) == {}
    assert solution.merge_inventory({"a": 2, "b": 1}, [("b", -1)]) == {"a": 2}


def test_negative_counts_allowed():
    assert solution.merge_inventory({}, [("a", -3)]) == {"a": -3}


def test_constraint_no_collections_counter(monkeypatch):
    import collections

    def boom(*_args, **_kwargs):
        raise AssertionError("Do not use collections.Counter in this exercise")

    monkeypatch.setattr(collections, "Counter", boom)
    assert solution.merge_inventory({"a": 1}, [("a", 1)]) == {"a": 2}
