#!/usr/bin/python3
"""Class Base"""


from json import dumps
"""Import dumps to convert object to json"""


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """Convert object to json"""
        if type(list_dictionaries) is not list:
            return "[]"
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        return dumps(list_dictionaries)

Base.to_json_string = staticmethod(Base.to_json_string)
