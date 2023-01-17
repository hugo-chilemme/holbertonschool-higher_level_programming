#!/usr/bin/python3
separator = ""
for number in range(0, 100):
    if number % 11 != 0:
        last_number = number%10
        first_number = int(number/10)
        reverse_number = last_number * 10 + first_number
        if reverse_number > number:
            if number < 10:
                print("{}0{}".format(separator, number), end="")
            else:
                print("{}{}".format(separator, number), end="")
            separator = ", "
print("\n", end="")
