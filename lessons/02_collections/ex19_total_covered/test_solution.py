from testutils import load_solution


solution = load_solution(__file__)


def test_empty():
    assert solution.total_covered([]) == 0


def test_single_value_range():
    assert solution.total_covered([(5, 5)]) == 1


def test_disjoint_ranges():
    assert solution.total_covered([(1, 3), (5, 6)]) == 5


def test_overlap_ranges():
    assert solution.total_covered([(1, 4), (3, 6)]) == 6


def test_touching_ranges():
    assert solution.total_covered([(1, 3), (4, 4), (5, 8)]) == 8


def test_unsorted_input():
    assert solution.total_covered([(10, 12), (1, 2), (3, 9)]) == 12


def test_negative_numbers():
    assert solution.total_covered([(-5, -3), (-4, -4), (0, 1)]) == 5
