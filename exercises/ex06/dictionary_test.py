"""A set of unit tests for dictionary program."""

__author__ = "tjschroeder23"

from exercises.ex06.dictionary import invert, count, favorite_color
import pytest


def test_invert_empty() -> None:
    assert invert({}) == {}


def test_invert_usecase() -> None:
    assert invert({"Tar Heels": "Number One", "Duke": "Last Place"}) == {"Number One": "Tar Heels", "Last Place": "Duke"}


def test_invert_duplicate_value() -> None:
    with pytest.raises(KeyError):
        invert({"Tar Heels": "Number One", "Duke": "Number One"})


def test_count_empty() -> None:
    assert count([]) == {}


def test_count_usecase() -> None:
    assert count(["unc", "duke", "unc", "nc state"]) == {"unc": 2, "duke": 1, "nc state": 1}


def test_count_usecase2() -> None:
    assert count(["unc", "unc", "unc"]) == {"unc": 3}


def test_favorite_color_empty() -> None:
    assert favorite_color(dict()) == ""


def test_favorite_color_usecase() -> None:
    assert favorite_color({"unc": "carolina blue", "duke": "blue", "nc state": "red"}) == "carolina blue"


def test_favorite_color_usecase2() -> None:
    assert favorite_color({"duke": "blue", "unc": "carolina blue", "kellyn": "carolina blue", "nc state": "red"}) == "carolina blue"
