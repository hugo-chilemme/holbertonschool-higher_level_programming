#!/usr/bin/python3
"""append_write"""


def append_write(filename="", text=""):
    """that appends a string at the end of a text file (UTF8)"""
    length = 0
    with open(filename, "a") as myfile:
        length = myfile.write(text)
        myfile.close()
        return length
    return 0
