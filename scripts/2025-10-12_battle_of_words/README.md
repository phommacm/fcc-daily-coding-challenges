# Battle of Words
[View Original Challenge](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-12)

## 📝 Challenge Description

Given two sentences representing your team and an opposing team, where each word from your team battles the corresponding word from the opposing team, determine which team wins using the following rules:

1. The given sentences will always contain the same number of words.
2. Words are separated by a single space and will only contain letters.
3. The value of each word is the sum of its letters:
   - Letters `a` to `z` correspond to the values 1 through 26 (e.g., `a` = 1, `z` = 26).
   - A capital letter doubles the value of the letter (e.g., `A` = 2, `Z` = 52).
4. Words battle in order: the first word of your team battles the first word of the opposing team, and so on.
5. A word wins if its value is greater than the opposing word's value.
6. The team with more winning words is the winner.

**Return Values:**

- `"We win"` → if your team wins.
- `"We lose"` → if your team loses.
- `"Draw"` → if both teams have the same number of winning words.

---

## 💡 Example

```python
our_team = "hello world"
opponent = "hello word"

result = battle(our_team, opponent)
print(result)  # Output: "We win"
