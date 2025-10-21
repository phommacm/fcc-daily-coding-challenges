"""
Array difference utility

Provides a function to compute the symmetric difference between two lists of strings:
the values that appear in exactly one of the two input lists. The result is returned
as a sorted list of unique strings.
"""

from typing import List

def array_diff(arr1: List[str], arr2: List[str]) -> List[str]:
    """
    Return the sorted symmetric difference of two string lists.

    Args:
        arr1 (List[str]): First list of strings.
        arr2 (List[str]): Second list of strings.

    Returns:
        List[str]: Sorted list of strings that appear in exactly one of the two inputs.

    Example:
        >>> array_diff(["apple", "banana"], ["banana", "cherry"])
        ['apple', 'cherry']
    """
    diff = list(set(arr1) ^ set(arr2))
    diff.sort()

    return diff

# Tests
print(array_diff(["apple", "banana"], ["apple", "banana", "cherry"]))                                  # should return ["cherry"]
print(array_diff(["apple", "banana", "cherry"], ["apple", "banana"]))                                  # should return ["cherry"]
print(array_diff(["one", "two", "three", "four", "six"], ["one", "three", "eight"]))                   # should return ["eight", "four", "six", "two"]
print(array_diff(["two", "four", "five", "eight"], ["one", "two", "three", "four", "seven", "eight"])) # should return ["five", "one", "seven", "three"]
print(array_diff(["I", "like", "freeCodeCamp"], ["I", "like", "rocks"]))                               # should return ["freeCodeCamp", "rocks"]
