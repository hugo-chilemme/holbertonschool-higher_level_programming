#!/usr/bin/python3
"""inherits_from"""


def inherits_from(obj, a_class):
    """Write a function that returns True"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
