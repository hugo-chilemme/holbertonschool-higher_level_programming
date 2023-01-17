#!/usr/bin/python3
for number in range(0, 100):
    zero_before = ""
    if number < 10:
        zero_before = "0"
    if number == 99:
        print("{}".format(number))
    else:
        print("{}{}, ".format(zero_before, number), end="")
