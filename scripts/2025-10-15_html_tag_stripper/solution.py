"""
HTML Tag Stripper

This module provides a simple utility function to remove HTML tags from a string
and return the plain text content. It is intended for basic HTML strings and
should not be used for complex or malformed HTML. For production use or
full HTML parsing, prefer libraries such as BeautifulSoup.
"""

import re

def strip_tags(html: str) -> str:
    """
    Remove all HTML tags from a given HTML string.

    This function uses a simple regular expression to strip out any text enclosed
    in angle brackets (`<...>`). It is suitable for basic cases with valid HTML but
    may not handle complex structures or attributes containing '>' correctly.

    Args:
        html (str): A string containing HTML code.

    Returns:
        str: The plain text content with all HTML tags removed.

    Example:
        >>> strip_tags('<a href="#">Click here</a>')
        'Click here'
        >>> strip_tags('<div><p>Hello <b>World</b></p></div>')
        'Hello World'
    """
    return re.sub("<.*?>", "", html)

if __name__ == "__main__":
    assert strip_tags('<a href="#">Click here</a>') == "Click here"
    assert strip_tags('<div><p>Hello <b>World</b></p></div>') == "Hello World"
    assert strip_tags('<img alt="x"/>No image shown') == "No image shown"
    assert strip_tags('Plain text with no tags') == "Plain text with no tags"
    print("All tests passed!")
