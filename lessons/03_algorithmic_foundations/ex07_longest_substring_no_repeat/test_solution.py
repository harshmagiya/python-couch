import pytest

from testutils import load_solution


solution = load_solution(__file__)


def test_canonical():
    assert solution.longest_substring_no_repeat("abcabcbb") == 3


def test_all_same():
    assert solution.longest_substring_no_repeat("bbbbb") == 1


def test_pwwkew():
    assert solution.longest_substring_no_repeat("pwwkew") == 3


def test_empty():
    assert solution.longest_substring_no_repeat("") == 0


def test_single_char():
    assert solution.longest_substring_no_repeat("z") == 1


def test_all_unique():
    assert solution.longest_substring_no_repeat("abcdef") == 6


def test_abba():
    assert solution.longest_substring_no_repeat("abba") == 2


def test_dvdf():
    assert solution.longest_substring_no_repeat("dvdf") == 3


def test_unicode_greek():
    assert solution.longest_substring_no_repeat("αβγ") == 3


def test_unicode_greek_with_repeat():
    assert solution.longest_substring_no_repeat("αβγαβγ") == 3


def test_emoji():
    assert solution.longest_substring_no_repeat("🎉🎊🎉") == 2


def test_two_chars_unique():
    assert solution.longest_substring_no_repeat("ab") == 2


def test_two_chars_same():
    assert solution.longest_substring_no_repeat("aa") == 1


def test_repeat_at_end():
    assert solution.longest_substring_no_repeat("abcdabce") == 5
