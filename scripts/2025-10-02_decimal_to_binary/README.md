# Decimal to Binary
[View Original Challenge](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-02)

## 📝 Challenge Description

Given a non-negative integer, return its binary representation as a string.

A binary number uses only the digits 0 and 1 to represent any number. To convert a decimal number to binary, repeatedly divide the number by 2 and record the remainder. Repeat until the number is zero. Read the remainders last recorded to first. For example, to convert 12 to binary:

12 ÷ 2 = 6 remainder 0  
6 ÷ 2 = 3 remainder 0  
3 ÷ 2 = 1 remainder 1  
1 ÷ 2 = 0 remainder 1  
12 in binary is 1100.

**Return Values:**

- A string representing the binary equivalent of the input integer.  
- The string should contain only the digits `'0'` and `'1'`.  

---

## 💡 Example

```python
print(to_binary(0))    # "0"
print(to_binary(1))    # "1"
print(to_binary(5))    # "101"
print(to_binary(12))   # "1100"
print(to_binary(255))  # "11111111"
