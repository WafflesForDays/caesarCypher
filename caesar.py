#Ted Pavlov 348705732

"""Shifts every letter in string by a specfied value

args: String: word to encrypt, Int/String: value to shift by (default 1)

return: String: encryted word
"""
def keyShift(word, shift = 1):
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
