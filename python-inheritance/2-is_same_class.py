#!/usr/bin/python3
"""is_same_class"""


def is_same_class(obj, a_class):
    """if the object is exactly an instance of the specified class"""
    if type(obj) is a_class:
        return True
    return False
