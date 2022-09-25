"""Tests for utils functions only_evens, concat, and sub."""
__author__ = "730482673"


from utils import only_evens
from utils import sub
from utils import concat


def test_only_evens_empty() -> None:
    """Tests what happens with an empty list."""
    odds_and_evens: list[int] = []
    assert only_evens(odds_and_evens) == []


def test_only_evens_random_nums() -> None:
    """Tests with regular numbers."""
    odds_and_evens: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(odds_and_evens) == [2, 4, 6]


def test_only_evens_negative_nums() -> None:
    """Tests with negative numbers."""
    odds_and_evens: list[int] = [-4, -2, 0, 2, 4]
    assert only_evens(odds_and_evens) == [-4, -2, 0, 2, 4]


def test_concat_empty() -> None:
    """Tests when given two empty lists."""
    first_list: list[int] = []
    second_list: list[int] = []
    assert concat(first_list, second_list) == []


def test_concat_randoms_nums() -> None:
    """Tests when given two regular lists."""
    first_list: list[int] = [1, 2, 3]
    second_list: list[int] = [1, 2, 3]
    assert concat(first_list,second_list) == [1, 2, 3, 1, 2, 3]


def test_concat_negative_nums() -> None:
    """Tests when given two lists with negative numbers."""
    first_list: list[int] = [-1, -2 , -3]
    second_list: list[int] = [-3, -2, -1]
    assert concat(first_list, second_list) == [-1, -2, -3, -3, -2, -1]


def test_sub_negative_start() -> None:
    """Tests when given a negative start index."""
    input_list: list[int] = [1, 2, 3, 4]
    start_index: int = -1
    end_index: int = 4
    assert sub(input_list, start_index, end_index) == [1, 2, 3, 4]


def test_sub_random_nums() -> None:
    """Tests when given regular numbers."""
    input_list: list[int] = [2, 7, 42, 6]
    start_index: int = 1
    end_index: int = 4
    assert sub(input_list, start_index, end_index) == [7, 42, 6]


def test_sub_rand_int() -> None:
    """Tests when given a list with negative numbers."""
    input_list: list[int] = [-1, 2, 6, 7]
    start_index: int = 0
    end_index: int = 3
    assert sub(input_list, start_index, end_index) == [-1, 2, 6]