# 24 to 12
[View Original Challenge](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-13)

## 📝 Challenge Description

Given a string representing a time of day in the **24-hour format** (`"HHMM"`), return its equivalent time in the **12-hour format** as `"H:MM AM"` or `"H:MM PM"`.

The input will always be a four-digit string between `"0000"` and `"2359"`.

1. The input format is always `"HHMM"`, where:
   - `HH` is the hour (00–23)
   - `MM` is the minute (00–59)
2. Midnight (`"0000"`) corresponds to `"12:00 AM"`.
3. Noon (`"1200"`) corresponds to `"12:00 PM"`.
4. Hours after noon (13–23) should be converted to 1–11 PM.
5. Leading zeros in the hour should be removed in the 12-hour output.

**Return Values:**

- A string in the format `"H:MM AM"` or `"H:MM PM"` representing the time in 12-hour format.

---

## 💡 Example

```python
to_12("1124")  # returns "11:24 AM"
to_12("0900")  # returns "9:00 AM"
to_12("1455")  # returns "2:55 PM"
