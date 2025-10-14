"""
Decimal to Binary

A simple module for converting non-negative integers (base-10) into their
binary (base-2) string representations.
"""
def to_binary(decimal):
    """
    Convert a non-negative integer into its binary (base-2) string representation.

    Args:
        decimal (int): A non-negative integer to convert.

    Returns:
        str: A string representing the binary equivalent of the input integer.
             Contains only '0' and '1'.

    Example:
        >>> to_binary(5)
        '101'
        >>> to_binary(12)
        '1100'
        >>> to_binary(0)
        '0'
    """
    if decimal == 0:
        return "0"

    rests = []

    while decimal != 0:
        buffer = decimal % 2
        rests.append(buffer)
        decimal //= 2

    binary = "".join([str(num) for num in rests])[::-1]

    return binary

# Tests
print(to_binary(5))  # should return "101"
print(to_binary(12)) # should return "1100"
print(to_binary(50)) # should return "110010"
print(to_binary(99)) # should return "1100011"
