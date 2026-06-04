from testutils import load_solution


solution = load_solution(__file__)


def test_empty():
    assert solution.subtract_range([], (3, 5)) == []


def test_remove_disjoint():
    assert solution.subtract_range([(1, 2), (6, 7)], (3, 5)) == [(1, 2), (6, 7)]


def test_remove_exact_match():
    assert solution.subtract_range([(3, 5)], (3, 5)) == []


def test_remove_middle_split():
    assert solution.subtract_range([(1, 10)], (3, 4)) == [(1, 2), (5, 10)]


def test_remove_left_clip():
    assert solution.subtract_range([(1, 10)], (-5, 3)) == [(4, 10)]


def test_remove_right_clip():
    assert solution.subtract_range([(1, 10)], (8, 20)) == [(1, 7)]


def test_remove_point():
    assert solution.subtract_range([(1, 5)], (3, 3)) == [(1, 2), (4, 5)]


def test_remove_across_multiple_ranges():
    ranges = [(1, 2), (5, 7), (10, 12)]
    assert solution.subtract_range(ranges, (6, 10)) == [(1, 2), (5, 5), (11, 12)]


def test_negative_numbers():
    assert solution.subtract_range([(-10, -8), (-3, -1)], (-9, -2)) == [(-10, -10), (-1, -1)]
