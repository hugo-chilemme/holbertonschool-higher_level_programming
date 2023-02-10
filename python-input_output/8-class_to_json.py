#!/usr/bin/python3*
"""class_to_json"""


def class_to_json(obj):
    """that returns the dictionary description with simple data structure"""
    return {
        "name": obj.name,
        "number": obj.number
    }
