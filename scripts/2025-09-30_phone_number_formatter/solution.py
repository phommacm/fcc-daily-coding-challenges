"""
Phone Number Formatter

This module provides a simple utility function to reformat a string of digits
into a standardized phone number structure. It is intended for basic input
consisting of exactly eleven digits and does not handle malformed or non-numeric
strings. This challenge focuses on string slicing and formatting.
"""

def format_number(number: str) -> str:
    """
    Format a 11-digit string into a phone number representation.

    The output is structured as: `"+D (DDD) DDD-DDDD"`, where:
    - The first digit represents the country code.
    - The next three digits form the area code.
    - The next three digits form the central office code.
    - The final four digits represent the line number.

    Args:
        number (str): A string containing exactly eleven digits
                      (e.g., "18005551234" or "21255598761").

    Returns:
        str: A formatted phone number string in the form `"+D (DDD) DDD-DDDD"`.

    Example:
        >>> format_number("18005551234")
        '+1 (800) 555-1234'
        >>> format_number("21255598761")
        '+2 (125) 559-8761'
    """
    return f"+{number[0]} ({number[1:4]}) {number[4:7]}-{number[7:]}"

if __name__ == "__main__":
    assert format_number("05552340182") == "+0 (555) 234-0182"
    assert format_number("15554354792") == "+1 (555) 435-4792"
    print("All tests passed!")
