#Ted Pavlov 348705732

def keyShift(word, shift):
    shifted = []
    list(word)
    for i in word:
        i = ord(i)
        i += int(shift)
        
        i = chr(i)
        shifted.append(i)
    shifted = "".join(shifted)

    return shifted

#test cases:
print(keyShift("hello", 3))
print(keyShift("world", -1))
print(keyShift("python", 5))
print(keyShift("example", -2))
print(keyShift("cryptography", -15))

input = input()
input = input.split(", ")
print(keyShift(input[0], input[1]))
