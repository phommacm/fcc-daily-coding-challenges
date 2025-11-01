"""
SpOoKy~CaSe

This module provides a function to convert variable-style strings into
"SpOoKy CaSe" — alternating uppercase and lowercase characters while
preserving separators in a spooky way.
"""

def spookify(boo: str) -> str:
    """
    Convert a variable name string into SpOoKy~CaSe.

    This function takes a string representing a variable name and transforms it
    into SpOoKy CaSe by alternating uppercase and lowercase letters, starting
    with uppercase. Underscores (`_`) and hyphens (`-`) are replaced with a
    tilde (`~`) and ignored when determining letter-case alternation.

    All other characters remain unchanged except alphabetic characters, which
    are lowercased first then altered according to the alternating pattern.

    Args:
        boo (str): Input string, e.g. "hello_world" or "Spooky-Case".

    Returns:
        str: The transformed SpOoKy~CaSe string.  
             Example: `"hello_world"` → `"HeLlO~wOrLd"`

    Example:
        >>> spookify("hello_world")
        'HeLlO~wOrLd'
        >>> spookify("Spooky-Case")
        'SpOoKy~cAsE'
    """
    count = 0
    boo = boo.lower()

    separator = ("-","_")

    for sep in separator:
        boo = boo.replace(sep,"~")

    result = []
    for char in boo:
        if char.isalpha():
            result.append(char.upper() if count % 2 == 0 else char)
            count += 1
        else:
            result.append(char)

    return "".join(result)
