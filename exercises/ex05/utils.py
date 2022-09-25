"""Building list utilities functions."""

__author__ = "730482673"


def only_evens(odds_and_evens: list[int]) -> list[int]:
    """Returns even numbers given in a list."""
    i: int = 0
    even_squad: list[int] = []
    while i < len(odds_and_evens):
        if odds_and_evens[i] % 2 == 0:
            even_squad.append(odds_and_evens[i])
        i += 1
    return even_squad


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """Takes two lists and combines them."""
    third_list: list[int] = []
    i: int = 0
    while i < len(first_list):
        third_list.append(first_list[i])
        i += 1
    i = 0
    while i < len(second_list):
        third_list.append(second_list[i])
        i += 1
    return third_list


def sub(input_list: list[int], start_index: int, end_index: int) -> list[int]:
    """A subset of the given list between the specified start and end values."""
    new_list: list[int] = []
    if start_index < 0:
        start_index = 0
    elif end_index > len(input_list):
        end_index = len(input_list)
    elif len(input_list) == 0:
        return input_list
    while start_index < len(input_list) + 1 and start_index < end_index:
        new_list.append(input_list[start_index])
        start_index += 1
    return new_list