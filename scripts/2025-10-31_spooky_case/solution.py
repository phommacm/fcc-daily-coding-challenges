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

if __name__ == "__main__":
    assert spookify("hello_world") == "HeLlO~wOrLd"
    assert spookify("Spooky_Case") == "SpOoKy~CaSe"
    assert spookify("TRICK-or-TREAT") == "TrIcK~oR~tReAt"
    assert spookify("c_a-n_d-y_-b-o_w_l") == "C~a~N~d~Y~~b~O~w~L"
    assert spookify("thE_hAUntEd-hOUsE-Is-" \
    "fUll_Of_ghOsts") == "ThE~hAuNtEd~HoUsE~iS~fUlL~oF~gHoStS"
    print("All tests passed!")
