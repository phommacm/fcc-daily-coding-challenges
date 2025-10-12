"""
Battle of Words Challenge Solution

This module contains the implementation and test cases for the
"Battle of Words" coding challenge from FreeCodeCamp.
"""

def battle(our_team: str, opponent: str) -> str:
    """
    Determines the winner of a word-by-word battle between two teams.

    Each word's value is calculated as the sum of its letters:
    - Lowercase letters 'a' to 'z' are worth 1 to 26.
    - Uppercase letters 'A' to 'Z' double their value (2 to 52).

    Words battle in order: the first word of `our_team` battles
    the first word of `opponent`, the second battles the second, etc.
    The team with more winning words is the winner.

    Parameters:
        our_team (str): A string of words representing our team's sentence.
        opponent (str): A string of words representing the opposing team's sentence.

    Returns:
        str: "We win" if our team has more winning words,
             "We lose" if the opponent has more winning words,
             "Draw" if both teams have the same number of winning words.

    Example:
        >>> battle("hello world", "hello word")
        'We win'
    """
    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    our_score, opp_score, our_word_score, opp_word_score = 0, 0, [], []
    score, value = 0, 0

    for char in our_team:
        if char == " ":
            our_word_score.append(score)
            score = 0
        elif char in lower_alphabet:
            value = lower_alphabet.index(char)
        else:
            value = upper_alphabet.index(char) * 2

        score += value

    our_word_score.append(score)
    score = 0

    for char in opponent:
        if char == " ":
            opp_word_score.append(score)
            score = 0
        elif char in lower_alphabet:
            value = lower_alphabet.index(char)
        else:
            value = upper_alphabet.index(char) * 2

        score += value

    opp_word_score.append(score)
    score = 0

    for i in range(len(our_word_score)):
        if our_word_score[i] > opp_word_score[i]:
            our_score += 1
        elif our_word_score[i] < opp_word_score[i]:
            opp_score += 1

    if our_score > opp_score:
        return "We win"
    elif our_score < opp_score:
        return "We lose"
    else:
        return "Draw"

# Tests
print(battle("hello world", "hello word")) # should return "We win"
print(battle("Hello world", "hello world")) # should return "We win"
print(battle("lorem ipsum", "kitty ipsum")) # should return "We lose"
print(battle("hello world", "world hello")) # should return "Draw"
print(battle("git checkout", "git switch")) # should return "We win"
print(battle("Cheeseburger with fries", "Cheeseburger with Fries")) # should return "We lose"
print(battle("We must never surrender", "Our team must win")) # should return "Draw"
