#!/usr/bin/python3
"""print_square"""


def print_square(size):
    """Function that prints a square with the character #."""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for y in range(0, size):
        for x in range(0, size): 
            print("#", end="")
        print()