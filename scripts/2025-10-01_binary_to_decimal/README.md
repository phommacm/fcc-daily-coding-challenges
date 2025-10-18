# Binary to Decimal
[View Original Challenge](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-01)

## 📝 Challenge Description

Given a string representing a **binary number**, return its **decimal equivalent** as a number.

A **binary number** uses only the digits `0` and `1` to represent values.  
To convert binary to decimal, multiply each digit by a power of 2 and add them together.  
Start from the **rightmost digit** (which is multiplied by 2⁰), then move left (2¹, 2², and so on).  
Finally, sum all the results to get the decimal value.

**Return Values:**

- Return an integer representing the decimal equivalent of the given binary string.

---

## 💡 Example

```python
to_decimal("101")      # returns 5
to_decimal("1010")     # returns 10
to_decimal("10010")    # returns 18
to_decimal("1010101")  # returns 85
