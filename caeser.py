#Ted Pavlov 348705732

def keyShift(word, shift=3):
    list(word)
    for _ in word:
        word += shift
    ''.join(word)

    return word


keyShift("test")