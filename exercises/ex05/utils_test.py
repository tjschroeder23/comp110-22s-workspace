"""A set of unit tests for utils program."""

__author__ = "tjschroeder23"

from exercises.ex05.utils import only_evens, sub, concat


def test_evens_only_empty() -> None:
    assert only_evens([]) == []


def test_evens_only_all_odds() -> None:
    assert only_evens([1, 3, 5, -1]) == []


def test_evens_only_both_odd_even() -> None:
    assert only_evens([1, 3, 5, -1, 0, 2, 4, -2]) == [0, 2, 4, -2]


def test_only_evens_empty() -> None:
    assert only_evens([]) == []


def test_only_evens_all_odds() -> None:
    assert only_evens([1, 3, 5, -1]) == []


def test_only_evens_both_odd_even() -> None:
    assert only_evens([1, 3, 5, -1, 0, 2, 4, -2]) == [0, 2, 4, -2]


def test_concat_two_lists() -> None:
    assert concat([1, 2, 3], [4, 6, 8]) == [1, 2, 3, 4, 6, 8]


def test_concat_empty() -> None:
    assert concat([], []) == []


def test_concat_empty_full() -> None:
    assert concat([], [-1, 2, -6, 8]) == [-1, 2, -6, 8]


def test_sub_empty() -> None:
    assert sub([], 0, 1) == []


def test_sub_regular() -> None:
    assert sub([1, 2, 3, 4, 5], 1, 4) == [2, 3, 4]


def test_sub_rt_index() -> None:
    assert sub([1, 2, 3, 4, 5], 1, 7) == [2, 3, 4, 5]


def test_sub_lft_index() -> None:
    assert sub([1, 2, 3, 4, 5], -1, 4) == [1, 2, 3, 4]
