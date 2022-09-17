"""list, utility functions."""
__author__ = "730482673"


"""Evaluates whether a given number is in a given list."""
def all(list: list[int], number: int) -> bool:
    i: int = 0
    while  i + 1 < len(list):
        if number == list[i]:
            i += 1
        else:
            return False
    return True
    

"""Returns the maximum number in a list of numbers."""
def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    nums: int = 0
    max_number: int = input[nums]
    while nums + 1 <= len(input):
        if input[nums] > max_number:
            max_number = input[nums]
        nums += 1
    return max_number


"""Evaluates whether two lists are completely equal to each other."""
def is_equal(first_values: list[int], second_values: list[int]) -> bool:
    i: int = 0
    if len(first_values) != len(second_values):
        return False
    while i + 1 <= len(first_values):
        if first_values[i] == second_values[i]:
            i += 1
        else:
            return False
    return True



            

        



   
    
