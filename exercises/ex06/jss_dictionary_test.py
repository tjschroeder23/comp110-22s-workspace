"""A set of unit tests for jss_dictionary program."""

__author__ = "tjschroeder23"

from exercises.ex06.jss_dictionary import invert, count, favorite_color, alphabetizer, update_attendance
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
    assert favorite_color({"duke": "blue", "unc": "carolina blue", "jaidyn": "carolina blue", "nc state": "red"}) == "carolina blue"


def test_alphabetizer_usecase() -> None:
    assert alphabetizer(["cat", "apple", "boy", "angry", "bad", "car"]) == {'c': ['cat', 'car'], 'a': ['apple', 'angry'], 'b': ['boy', 'bad']}


def test_alphabetizer_usecase2() -> None:
    assert alphabetizer(["Python", "sugar", "Turtle", "party", "table"]) == {'p': ['Python', 'party'], 's': ['sugar'], 't': ['Turtle', 'table']}


def test_update_attendence_usecase() -> None:
    attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_attendance(attendance_log, "Tuesday", "Vrinda")
    update_attendance(attendance_log, "Wednesday", "Kaleb")
    assert attendance_log == {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda'], 'Wednesday': ['Kaleb']}
