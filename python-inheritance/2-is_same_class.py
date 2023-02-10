#!/usr/bin/python3
"""MyList"""

def is_same_class(obj, a_class):
    if isinstance(obj, int) and issubclass(a_class, int):
        return True
    return False