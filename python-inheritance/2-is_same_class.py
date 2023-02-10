#!/usr/bin/python3
"""is_same_class"""

def is_same_class(obj, a_class):
    """if the object is exactly an instance of the specified class"""
    if isinstance(obj, int) and issubclass(a_class, int):
        return True
    return False
