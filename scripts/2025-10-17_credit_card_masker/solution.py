"""
Credit Card Masker

This module provides a utility function to mask credit card numbers, revealing
only the last four digits while preserving the original formatting (spaces or
hyphens).
"""
def mask(card: str) -> str:
    """
    Mask a credit card number, keeping only the last four digits visible.

    This function accepts a string representing a credit card number formatted
    as four groups of four digits separated by either spaces or hyphens. It replaces
    the first twelve digits with asterisks (`*`) while preserving the original
    separator style.

    Args:
        card (str): The credit card number string, e.g. "4012-8888-8888-1881"
                    or "1234 5678 9012 3456".

    Returns:
        str: The masked credit card string with only the last four digits visible.
             For example, "****-****-****-1881" or "**** **** **** 3456".

    Example:
        >>> mask("4012-8888-8888-1881")
        '****-****-****-1881'
        >>> mask("1234 5678 9012 3456")
        '**** **** **** 3456'
    """
    if "-" in card:
        masked = f"****-****-****-{card.split('-')[3]}"
    else:
        masked = f"**** **** **** {card.split()[3]}"

    return masked

# Tests
print(mask("4012-8888-8888-1881"))  # returns "****-****-****-1881"
print(mask("5105 1051 0510 5100"))  # returns "**** **** **** 5100"
print(mask("6011 1111 1111 1117"))  # returns "****-****-****-1117"
print(mask("2223-0000-4845-0010"))  # returns "****-****-****-0010"
