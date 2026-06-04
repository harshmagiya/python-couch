from testutils import load_solution


solution = load_solution(__file__)


def test_empty():
    assert solution.compact_ranges([]) == []


def test_single_value():
    assert solution.compact_ranges([7]) == [(7, 7)]


def test_already_one_range():
    assert solution.compact_ranges([1, 2, 3, 4]) == [(1, 4)]


def test_multiple_ranges():
    assert solution.compact_ranges([1, 2, 3, 5, 6, 9]) == [(1, 3), (5, 6), (9, 9)]


def test_with_negative_numbers():
    assert solution.compact_ranges([-3, -2, -1, 1, 2]) == [(-3, -1), (1, 2)]


def test_all_gaps():
    assert solution.compact_ranges([1, 3, 5]) == [(1, 1), (3, 3), (5, 5)]


def test_starts_with_zero():
    assert solution.compact_ranges([0, 1, 2, 4]) == [(0, 2), (4, 4)]
