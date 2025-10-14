"""
24 to 12

This module contains the implementation and examples for converting
24-hour format time strings ("HHMM") into their 12-hour format equivalent
("H:MM AM" or "H:MM PM").

Example:
    >>> to_12("1455")
    '2:55 PM'
"""
def to_12(time_str: str) -> str:
    """
    Converts a 24-hour format time string to a 12-hour format string.

    Given a string in "HHMM" 24-hour format, this function returns the
    equivalent time in 12-hour format with "AM" or "PM" suffix.

    Rules:
        - Midnight ("0000") is "12:00 AM".
        - Noon ("1200") is "12:00 PM".
        - Hours 13-23 are converted to 1-11 PM.
        - Leading zeros in the hour are removed in the 12-hour output.

    Parameters:
        time_str (str): A 4-digit string representing time in 24-hour format.

    Returns:
        str: A string representing the time in 12-hour format.

    Example:
        >>> to_12("1124")
        '11:24 AM'
        >>> to_12("0900")
        '9:00 AM'
        >>> to_12("1455")
        '2:55 PM'
    """
    hour24 = int(time_str[:2])

    if hour24 < 12 or hour24 == 24:
        meridiem = "AM"
        if hour24 == 24 or hour24 == 0:
            hour24 = 12
    else:
        hour24 -= 12
        meridiem = "PM"

    time12 = f"{hour24}:{time_str[2:]} {meridiem}"

    return time12
