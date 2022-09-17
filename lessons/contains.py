"""Example implementing a list utility function."""

# Function name: contains
# We will have 2 parameters: needle (str), haystack (list[str])
# Return type bool

# Gameplan:
# 1. start with the first index
# 2. Loop through every index
#   2A Test if item at index = needle
#   2B True return true
# 3. Return False


def contains(needle: str, haystack: list[str]) -> bool:
    i: int = 0
    while i < len(haystack):
        if haystack[i] == needle:
            return True
        i += 1
    return False
