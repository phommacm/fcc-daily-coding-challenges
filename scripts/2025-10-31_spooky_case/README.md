# SpOoKy~CaSe
[View Original Challenge](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-31)

## 📝 Challenge Description

Given a string representing a variable name, convert it into **SpOoKy CaSe** using the rules below:

1. The input may contain **letters**, underscores (`_`), and hyphens (`-`).
2. Replace all underscores (`_`) and hyphens (`-`) with a tilde (`~`).
3. Capitalize the **first letter** and **every other alphabetic character after that**.
4. **Ignore tildes** when counting alternating positions.
5. All other alphabetic characters should remain lowercase.

**Return Values:**

- A string where `_` and `-` are replaced by `~`, and letters alternate uppercase/lowercase (starting uppercase), counting only letters.

---

## 💡 Example

```python
spookify("hello_world") # returns "HeLlO~wOrLd"
spookify("Spooky-Case") # returns "SpOoKy~cAsE"
