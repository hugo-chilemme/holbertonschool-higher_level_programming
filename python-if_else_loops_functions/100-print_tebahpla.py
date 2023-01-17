#!/usr/bin/python3
for letter in reversed(range(97, 123)):
    if letter % 2 == 0:
        print("{}".format(chr(letter)), end="")
    else:
        print("{}".format(chr(letter - 32)), end="")
