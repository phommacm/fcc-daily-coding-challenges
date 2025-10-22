"""
Reverse Sentence Utility

This module provides a function that reverses the order of words in a sentence.
Extra spaces in the input are ignored, and the returned string contains only
single spaces between words, with no leading or trailing spaces.
"""

def reverse_sentence(sentence: str) -> str:
    """
    Return a new string with the words in reverse order.

    Words in the input may be separated by one or more spaces. The output
    string will contain the words reversed, joined by a single space only.

    Args:
        sentence (str): A string containing one or more words.

    Returns:
        str: A string with the word order reversed and normalized spacing.

    Example:
        >>> reverse_sentence("world hello")
        'hello world'
    """
    sentence = " ".join([word for word in sentence.split()[::-1]])
    return sentence