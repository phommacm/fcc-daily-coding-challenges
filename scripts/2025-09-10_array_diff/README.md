# Array Diff
[View Original Challenge](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-10)

## 📝 Challenge Description

Given two arrays of strings, return a new array that contains only the elements that **appear in one array but not the other**.

The result should **exclude any values that exist in both arrays**, keeping only the unique elements from each side.

1. The input will consist of **two arrays of strings**.
2. The returned array must include only the values that appear in **exactly one** of the two arrays.
3. The final result must be **sorted alphabetically** in ascending order.
4. You may assume that string comparisons are case-sensitive.

**Return Values:**

- A **new array of strings** containing only the unique values, sorted alphabetically.

---

## 💡 Example

```python
array_diff(["a", "b", "c"], ["b", "d"])         # returns ["a", "c", "d"]
array_diff(["apple", "pear"], ["pear", "kiwi"]) # returns ["apple", "kiwi"]
