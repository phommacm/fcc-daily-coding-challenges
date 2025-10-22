def reverse_sentence(sentence: str) -> str:
    sentence = " ".join([word for word in sentence.split()[::-1]])
    return sentence