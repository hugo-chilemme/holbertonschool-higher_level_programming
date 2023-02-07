#!/usr/bin/python3
"""append_write"""


def append_write(filename="", text=""):
    """that appends a string at the end of a text file (UTF8)"""
    try:
        with open(filename, "r") as r:
            r.write(text)
            length = len(r.read())
            r.close()
            return length
    except:
        f = open(filename, "w")
        f.write(text)
        f.close()
        return len(text)
