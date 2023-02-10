#!/usr/bin/python3
"""salut"""


def class_to_json(obj):
    """that returns the dictionary description with simple data structure"""
    json = {}
    if obj is None:
        return json
    try:
        json["name"] = obj.name
    except:
        pass
    try:
        json["number"] = obj.number
    except:
        pass
    return json
