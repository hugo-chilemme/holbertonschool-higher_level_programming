#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if number < 0:
    last_digit = number % -10
print(f"Last digit of {number} is {last_digit} and ", end="")
if last_digit > 5:
    print("is greater than 5")
elif last_digit == 0:
    print("is 0")
elif last_digit < 6:
    print("is less than 6 and not 0")
