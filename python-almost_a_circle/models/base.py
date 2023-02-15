#!/usr/bin/python3
"""Class Base"""


from json import dumps, loads
"""Import dumps to convert object to json and other side"""


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert object to json"""
        if type(list_dictionaries) is not list:
            return "[]"
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        arr = []
        if list_objs:
            for element in list_objs:
                arr.append(element.to_dictionary())
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string(arr))

    @staticmethod
    def from_json_string(json_string):
        if not json_string:
            return []
        try:
            return loads(json_string)
        except:
            return json_string

    @classmethod
    def create(cls, **dictionary):
        try:
            clone = cls(1)
        except:
            clone = cls(1, 1)
        clone.update(**dictionary)
        return clone

    @classmethod
    def load_from_file(cls):
        list_obj = []
        try:
            with open(cls.__name__+".json", "r") as f:
                data = cls.from_json_string(f.read())
                for element in data:
                    list_obj.append(cls.create(element))
            f.close()
        except:
            pass
        return list_obj
