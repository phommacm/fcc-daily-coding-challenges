# Phone Number Formatter
[View Original Challenge](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-30)

## 📝 Challenge Description

Given a string of digits, return the string formatted as a phone number using the pattern:

`"+D (DDD) DDD-DDDD"`

1. The input will contain **ten digits**, where:
   - The **first digit** represents the country code.
   - The **next three digits** represent the area code.
   - The **next three digits** represent the central office code.
   - The **last four digits** represent the line number.
2. The output format must follow the exact structure:
   - A leading `+`
   - Then one digit (country code)
   - A space
   - The area code wrapped in parentheses
   - A space
   - Three digits
   - A hyphen
   - Four final digits
3. Non-digit characters (if any) are outside the scope of this challenge and may be ignored or rejected, as the input is assumed to be clean and valid.

**Return Values:**

- A string formatted in the structure: `"+D (DDD) DDD-DDDD"`.

---

## 💡 Example

```python
format_number("18005551234") # returns "+1 (800) 555-1234"
format_number("21255598761") # returns "+2 (125) 559-8761"
