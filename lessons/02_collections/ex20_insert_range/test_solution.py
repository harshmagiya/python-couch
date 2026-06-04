from testutils import load_solution


solution = load_solution(__file__)


def test_empty_ranges():
    assert solution.insert_range([], (4, 4)) == [(4, 4)]


def test_insert_before_all():
    assert solution.insert_range([(5, 6), (10, 12)], (1, 2)) == [(1, 2), (5, 6), (10, 12)]


def test_insert_after_all():
    assert solution.insert_range([(1, 2), (5, 6)], (10, 12)) == [(1, 2), (5, 6), (10, 12)]


def test_overlap_middle():
    assert solution.insert_range([(1, 2), (6, 7)], (2, 6)) == [(1, 7)]


def test_touching_bridges_gap():
    assert solution.insert_range([(1, 2), (6, 7)], (3, 5)) == [(1, 7)]


def test_contained_in_existing():
    assert solution.insert_range([(1, 10)], (3, 4)) == [(1, 10)]


def test_existing_contained_in_new():
    assert solution.insert_range([(3, 4), (8, 9)], (1, 10)) == [(1, 10)]


def test_negative_numbers_and_touching():
    assert solution.insert_range([(-10, -8), (-3, -1)], (-7, -4)) == [(-10, -1)]
