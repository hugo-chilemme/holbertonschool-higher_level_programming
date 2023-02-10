#!/usr/bin/python3
"""salut"""


def class_to_json(obj):
    """that returns the dictionary description with simple data structure"""
    json = {}
    if obj is None:
        return json
    if obj.name is not None:
        json["name"] = obj.name
    if obj.number is not None:
        json["number"] = obj.number
    return json
