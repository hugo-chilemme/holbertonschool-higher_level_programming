#!/usr/bin/python3
"""print_square"""


def text_indentation(text):
    """Function that prints a text with 2 new lines"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    new_line = False
    for k, v in enumerate(text):
        if k > 0:
            before = text[k - 1]
            if before in [".", "?", ":"]:
                print("\n")
                new_line = True
                if v == ' ':
                    continue
        if new_line and v == ' ':
            continue
        print(v, end="")
        new_line = False
