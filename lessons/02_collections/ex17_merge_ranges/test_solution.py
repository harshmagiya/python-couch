from testutils import load_solution


solution = load_solution(__file__)


def test_empty():
    assert solution.merge_ranges([]) == []


def test_single_range():
    assert solution.merge_ranges([(3, 5)]) == [(3, 5)]


def test_already_disjoint_sorted():
    assert solution.merge_ranges([(1, 2), (5, 7)]) == [(1, 2), (5, 7)]


def test_overlap_merges():
    assert solution.merge_ranges([(1, 4), (3, 6)]) == [(1, 6)]


def test_touching_merges():
    assert solution.merge_ranges([(1, 3), (4, 4), (5, 8)]) == [(1, 8)]


def test_unsorted_input():
    assert solution.merge_ranges([(5, 7), (1, 3), (2, 6)]) == [(1, 7)]


def test_negative_numbers():
    assert solution.merge_ranges([(-5, -3), (-2, 1), (-4, -4)]) == [(-5, 1)]


def test_contained_ranges():
    assert solution.merge_ranges([(1, 10), (3, 4), (5, 6)]) == [(1, 10)]
