#!/usr/bin/python3
"""append_write"""


def append_write(filename="", text=""):
    """that appends a string at the end of a text file (UTF8)"""
    f = open(filename, "r")
    f.write(text)
    f.close()
    with open(filename) as f:
        return len(f.read())
