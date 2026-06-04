from testutils import load_solution


solution = load_solution(__file__)


def test_both_empty():
    assert solution.intersect_ranges([], []) == []


def test_one_empty():
    assert solution.intersect_ranges([(1, 2)], []) == []


def test_single_overlap():
    assert solution.intersect_ranges([(1, 5)], [(2, 3)]) == [(2, 3)]


def test_single_touch_point():
    assert solution.intersect_ranges([(1, 3)], [(3, 5)]) == [(3, 3)]


def test_multiple_ranges():
    a = [(1, 2), (5, 7), (10, 15)]
    b = [(3, 4), (6, 10), (14, 20)]
    assert solution.intersect_ranges(a, b) == [(6, 7), (10, 10), (14, 15)]


def test_negative_numbers():
    a = [(-10, -5), (-2, 2)]
    b = [(-7, -6), (-3, -1), (3, 4)]
    assert solution.intersect_ranges(a, b) == [(-7, -6), (-2, -1)]


def test_contained_range():
    assert solution.intersect_ranges([(1, 10)], [(3, 4), (6, 7)]) == [(3, 4), (6, 7)]


def test_b_contains_a():
    assert solution.intersect_ranges([(3, 4)], [(1, 10)]) == [(3, 4)]
