"""
Battle of Words Challenge Solution

This module contains the implementation and test cases for the
"Battle of Words" coding challenge from FreeCodeCamp.
"""

from typing import List

def scoring(sentence: str) -> List[int]:
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
    score = [
        sum((ord(char.lower()) - 96) * (2 if char.isupper() else 1)
            for char in word) for word in sentence.split()
    ]

    return score

def battle(our_team: str, opponent: str) -> str:
    """
    Determines the winner of a word-by-word battle between two teams.

    Each team's sentence is split into words, and each word’s score is
    calculated using the `scoring()` function:
      - Lowercase letters 'a' to 'z' are worth 1–26 points.
      - Uppercase letters 'A' to 'Z' are worth double (2–52 points).

    The battle proceeds word by word in order:
      - The first word of `our_team` battles the first word of `opponent`,
        the second battles the second, and so on.
      - The team with the higher word score wins that round.
      - The overall winner is the team with more winning words.

    If both teams win the same number of rounds, the result is a draw.

    Parameters:
        our_team (str): A string of words representing our team's sentence.
        opponent (str): A string of words representing the opposing team's sentence.

    Returns:
        str: 
            - "We win" if our team wins more word battles.
            - "We lose" if the opponent wins more word battles.
            - "Draw" if both teams win the same number of word battles.

    Example:
        >>> battle("hello world", "hello word")
        'We win'
        >>> battle("Hello world", "hello world")
        'We win'
        >>> battle("hello world", "world hello")
        'Draw'
    """
    our_score, opp_score, our_word_score, opp_word_score = 0, 0, scoring(
        our_team), scoring(opponent)

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

if __name__ == "__main__":
    assert battle("hello world", "hello word") == "We win"
    assert battle("Hello world", "hello world") == "We win"
    assert battle("lorem ipsum", "kitty ipsum") == "We lose"
    assert battle("hello world", "world hello") == "Draw"
    assert battle("git checkout", "git switch") == "We win"
    assert battle("Cheeseburger with fries", "Cheeseburger with Fries") == "We lose"
    assert battle("We must never surrender", "Our team must win") == "Draw"
    print("All tests passed!")
