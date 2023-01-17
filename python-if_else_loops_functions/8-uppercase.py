#!/usr/bin/python3
def uppercase(c):
    for letter in c:
        return_ascii = ord(letter)
        if ord(letter) >= 97 and ord(letter) <= 122:
            return_ascii -= 32
        print(chr(return_ascii), end="")
    print("\n", end="")
