"""
Battle of Words Challenge Solution

This module contains the implementation and test cases for the
"Battle of Words" coding challenge from FreeCodeCamp.
"""

from typing import List

def scoring(sentence: str) -> List:
    """
    Calculates the word scores for a given sentence based on letter values.

    Each word's score is determined by summing the values of its letters:
    - Lowercase letters 'a' to 'z' are worth 1 to 26 points.
    - Uppercase letters 'A' to 'Z' double their value (2 to 52 points).

    The function returns a list of integer scores corresponding to each word
    in the sentence, in order.

    Parameters:
        sentence (str): A string consisting of one or more words.

    Returns:
        List[int]: A list of numerical scores, one for each word in the sentence.

    Example:
        >>> scoring("Hello world")
        [60, 72]
    """
    score = [sum((ord(char.lower()) - 96) * (2 if char.isupper() else 1)for char in word) for word in sentence.split()]

    return score

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
    our_score, opp_score, our_word_score, opp_word_score = 0, 0, scoring(our_team), scoring(opponent)

    for our_word_value, opp_word_value in zip(our_word_score, opp_word_score):
        if our_word_value > opp_word_value:
            our_score += 1
        elif our_word_value < opp_word_value:
            opp_score += 1

    if our_score > opp_score:
        return "We win"
    if our_score < opp_score:
        return "We lose"

    return "Draw"

# Tests
print(battle("hello world", "hello word")) # should return "We win"
print(battle("Hello world", "hello world")) # should return "We win"
print(battle("lorem ipsum", "kitty ipsum")) # should return "We lose"
print(battle("hello world", "world hello")) # should return "Draw"
print(battle("git checkout", "git switch")) # should return "We win"
print(battle("Cheeseburger with fries", "Cheeseburger with Fries")) # should return "We lose"
print(battle("We must never surrender", "Our team must win")) # should return "Draw"
