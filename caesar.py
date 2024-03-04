#Ted Pavlov 348705732

def keyShift(word, shift):
    looping = True
    shifted = []
    list(word)
    for i in word:
        i = ord(i)
        i += int(shift)

        while looping:
            if i >= ord("z") + 1:
                i -= 26
            elif i <= ord("Z"):
                i += 26
            else:
                looping = False
        looping = True

        i = chr(i)
        shifted.append(i)
    shifted = "".join(shifted)

    return shifted

#test cases:
print(keyShift("hello", 3))
print(keyShift("world", -1))
print(keyShift("python", 5))

input = input()
input = input.split(", ")
print(keyShift(input[0], input[1]))
