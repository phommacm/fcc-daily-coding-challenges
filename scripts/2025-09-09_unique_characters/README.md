# Unique Characters
[View Original Challenge](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-09)

## 📝 Challenge Description

Given a string, determine whether **all characters in the string are unique**.

1. The input will be a string containing **letters, digits, symbols, or whitespace**.
2. Uppercase and lowercase letters **must be treated as different characters** (`"A"` is not the same as `"a"`).
3. Return `True` if **every character appears only once**.
4. Return `False` if **any character is repeated**.

**Return Values:**

- `True` → if all characters in the string are unique  
- `False` → if any character appears more than once  

---

## 💡 Example

```python
all_unique("abc")         # returns True
all_unique("aA")          # returns True
all_unique("hello")       # returns False
all_unique("QwErTy123!@") # returns True
