""""Tests the functions in dictionary.py."""
__author__ = "730482673"


from dictionary import invert
from dictionary import favorite_color
from dictionary import count


def test_invert_normal_nums() -> None:
    """Tests what happens when given normal values."""
    a: dict[str,str] = {"a" : "b", "b" : "c", "c" : "d"}
    assert invert(a) == {"b" : "a", "c" : "b", "d" : "c"}


def test_invert_no_values() -> None:
    """Tests what happens when given no values."""
    a: dict[str,str] = {}
    assert invert(a) == {}


def test_invert_same_nums() -> None:
    """Tests what happens when key and value are the same."""
    a: dict[str,str] = {"a" : "a"}
    assert invert(a) == {"a" : "a"}


def test_favorite_color_normal_nums() -> None:
    """Tests what happens when regular values are given."""
    colors: dict[str, str] = {"Thomas" : "Blue", "Emma" : "Yellow", "Madi" : "Blue"}
    assert favorite_color(colors) == "Blue"


def test_favorite_color_tied() -> None:
    """Tests what happens when given a tied value."""
    colors: dict[str, str] = {"Thomas" : "Blue", "Emma" : "Yellow", "Madi" : "Yellow", "Emily" : "Blue"}
    assert favorite_color(colors) == "Blue"


def test_favorite_color_one() -> None:
    """"Tests what happens when given an one person list."""
    colors: dict[str, str] = {"Lucas": "green"}
    assert favorite_color(colors) == "green"


def test_count_normal_nums() -> None:
    """Tests what happens when given normal values."""
    x: list[str] = ["Chocolate", "Vanilla", "Chocolate"]
    assert count(x) == {"Chocolate" : 2, "Vanilla" : 1}


def test_count_tied_count() -> None:
    """Tests what happens when given a value with the same count as another value."""
    x: list[str] = ["Chocolate", "Chocolate", "Vanilla", "Vanilla"]
    assert count(x) == {"Chocolate" : 2, "Vanilla" : 2}


def test_count_empty() -> None:
    """Tests what happens when given an empty list."""
    x: list[str] = []
    assert count(x) == {}