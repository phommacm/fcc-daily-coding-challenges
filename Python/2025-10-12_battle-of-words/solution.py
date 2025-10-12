def battle(our_team: str, opponent: str) -> str:
    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    our_score, opp_score, our_word_score, opp_word_score = 0, 0, list(), list()
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
