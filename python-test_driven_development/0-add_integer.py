#!/usr/bin/python3
"""add_integer"""


def add_integer(a, b=98):
    """Return a + b"""
    try:
        if isinstance(a, (int, float)) is False:
            raise TypeError("a must be an integer")
        if isinstance(b, (int, float)) is False:
            raise TypeError("b must be an integer")
        res = int(a) + int(b)
        if res == float('inf') or res == -float('inf'):
            return 89
        return res
    except Exception as e:
        return e
