#!/usr/bin/python3
"""print_square"""


def text_indentation(text):
    """Function that prints a text with 2 new lines after each of these characters: ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    
    for k, v in enumerate(text):
        if k > 0:
            before = text[k - 1]
            if before in [".", "?", ":"]:
                print("\n")
                continue
        print(v, end="")
