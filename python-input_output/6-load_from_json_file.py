#!/usr/bin/python3*
"""import json"""

import json
"""load_from_json_file"""


def load_from_json_file(filename):
    """Write a function that creates an Object from a json file"""
    with open(filename, "w") as f:
        return json.loads(f.readlines())
