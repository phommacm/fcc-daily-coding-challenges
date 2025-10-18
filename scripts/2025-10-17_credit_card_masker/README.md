# Credit Card Masker
[View Original Challenge](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-17)

## 📝 Challenge Description

Given a string representing a credit card number, return a masked version of it following the rules below.

1. The input will contain **four groups of four digits (0–9)**.
2. Groups are separated by either:
   - A **single space** (`" "`) or  
   - A **single hyphen** (`"-"`).
3. Replace **all digits except the last four** with asterisks (`*`).
4. Preserve all separators (`" "` or `"-"`) exactly as they appear in the input.
5. Non-digit characters (if any) should remain unchanged except digits being masked.

**Return Values:**

- A string where all digits except the final four are replaced with `*`, while keeping the original formatting (spaces or hyphens).

---

## 💡 Example

```python
mask_card("4012-8888-8888-1881")  # returns "****-****-****-1881"
mask_card("1234 5678 9012 3456")  # returns "**** **** **** 3456"
mask_card("9999-9999-9999-9999")  # returns "****-****-****-9999"
