#!/usr/bin/python3
"""write_file"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8)"""
    f = open(filename, "a")
    f.write(text)
    f.close()
    with open(filename) as f:
        return len(f.read())
