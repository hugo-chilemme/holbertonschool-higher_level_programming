#!/usr/bin/python3
"""write_file"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8)"""
    with open(filename) as f:
        f.write(text)
        length = len(f.read())
        f.close()
        return length

