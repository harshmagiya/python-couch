from testutils import load_solution


solution = load_solution(__file__)


def test_empty_ranges():
    assert solution.missing_in_bounds([], (5, 7)) == [(5, 7)]


def test_full_coverage():
    assert solution.missing_in_bounds([(1, 10)], (3, 5)) == []


def test_gaps_inside_bounds():
    assert solution.missing_in_bounds([(2, 3), (6, 7)], (1, 8)) == [(1, 1), (4, 5), (8, 8)]


def test_touching_coverage_removes_gap():
    assert solution.missing_in_bounds([(2, 3), (4, 6)], (1, 6)) == [(1, 1)]


def test_ranges_outside_bounds_are_clipped():
    assert solution.missing_in_bounds([(-10, 2), (8, 20)], (1, 10)) == [(3, 7)]


def test_range_strictly_before_bounds():
    assert solution.missing_in_bounds([(-10, -5)], (1, 3)) == [(1, 3)]


def test_range_strictly_after_bounds():
    assert solution.missing_in_bounds([(10, 12)], (1, 3)) == [(1, 3)]


def test_negative_bounds():
    assert solution.missing_in_bounds([(-5, -3)], (-6, -2)) == [(-6, -6), (-2, -2)]
