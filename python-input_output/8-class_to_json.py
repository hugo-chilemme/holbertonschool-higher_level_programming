#!/usr/bin/python3
"""salut"""


def class_to_json(obj):
    """that returns the dictionary description with simple data structure"""
    json = {}
    if obj is None:
        return json
    if obj.name:
        json["name"] = obj.name
    if obj.number:
        json["number"] = obj.number
    return json
