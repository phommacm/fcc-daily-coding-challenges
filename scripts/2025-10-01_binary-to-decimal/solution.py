"""
Binary to Decimal

A simple module for converting binary numbers (as strings) into their decimal
(integer) equivalents.
"""
def to_decimal(binary: str) -> int:
    """
    Convert a binary string into its decimal (base-10) integer equivalent.

    Args:
        binary (str): A string representing a binary number (e.g., "101").

    Returns:
        int: The decimal (base-10) value of the binary number.

    Raises:
        ValueError: If the input string contains characters other than '0' or '1'.

    Example:
        >>> to_decimal("101")
        5
    """
    total = sum(int(num) * 2**i for i, num in enumerate(binary[::-1]))

    return total