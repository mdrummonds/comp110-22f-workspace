"""Writing dictionary functions and tests."""

__author__ = "730482673"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and the values."""
    reverse: dict[str, str] = {}
    for key in a:
        reverse[a[key]] = key
    if len(reverse) != len(a):
        raise KeyError("encountered two of the same key.")
    return reverse


def favorite_color(colors: dict[str,str]) -> str:
    """Reports the value with the greatest frequency in a list."""
    color_list: list[str] = []
    empty: dict[str,int] = {}
    nums_list: list[int] = []
    for rainbow in colors:
        color_list.insert(rainbow)
    empty = count(color_list)
    for num in empty:
        nums_list.append(empty[num])
    max_number: int = max(nums_list)
    reverse: dict[int, str] = {}
    for key in empty:
        reverse[empty[key]] = key
    return colors[reverse[max_number]]
        

def count(x: list[str]) -> dict[str, int]:
    """Given a list, reports a dictionary with the key as the value and the value as the number of times that value appeared in the list."""
    empty: dict[str,int] = {}
    for key in x:
        if key in empty:
            empty[key] += 1
        else:
            empty[key] = 1
    return empty