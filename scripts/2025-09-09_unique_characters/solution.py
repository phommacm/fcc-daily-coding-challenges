"""
Unique Characters

This module provides a simple utility function to check whether all characters
in a given string are unique. Uppercase and lowercase letters are treated as
distinct symbols, meaning 'A' and 'a' are considered different characters.
This challenge demonstrates basic string handling and set operations in Python.
"""

def all_unique(s: str) -> bool:
    """
    Determine whether all characters in a string are unique.

    This function returns True if every character in the input string appears
    only once. It treats uppercase and lowercase letters as different
    characters, so 'A' and 'a' do not count as duplicates of each other.

    Args:
        s (str): The input string to evaluate.

    Returns:
        bool: True if all characters in the string are unique, otherwise False.

    Example:
        >>> all_unique("abc")
        True
        >>> all_unique("hello")
        False
    """
    return len(s) == len(set(s))

if __name__ == "__main__":
    assert all_unique("abc")
    assert all_unique("aA")
    assert all_unique("QwErTy123!@")
    assert all_unique("~!@#$%^&*()_+")
    assert all_unique("hello")
    assert all_unique("freeCodeCamp")
    assert all_unique("!@#*$%^&*()aA")
    print("All tests passed!")
