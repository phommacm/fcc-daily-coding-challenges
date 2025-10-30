"""
Array Diff

This module provides a utility function to compute the symmetric difference between
two lists of strings: the values that appear in exactly one of the two input lists.
The result is returned as a sorted list of unique strings.
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

if __name__ == "__main__":
    assert array_diff(["apple", "banana"], ["apple", "banana", "cherry"]) == ["cherry"]
    assert array_diff(["apple", "banana", "cherry"], ["apple", "banana"]) == ["cherry"]
    assert array_diff(["one", "two", "three", "four", "six"],
                      ["one", "three", "eight"]) == ["eight", "four", "six", "two"]
    assert array_diff(
        ["two", "four", "five", "eight"],
        ["one", "two", "three", "four", "seven", "eight"]) == ["five", "one", "seven", "three"]
    assert array_diff(["I", "like", "freeCodeCamp"],
                      ["I", "like", "rocks"]) == ["freeCodeCamp", "rocks"]
    print("All tests passed!")
