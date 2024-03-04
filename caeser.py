#Ted Pavlov 348705732

def keyShift(word, shift=3):
    list(word)
    for i in word:
        i = ord(i)
        i += shift
        i = chr(i)
        

    return word


print(keyShift("test", 3))
