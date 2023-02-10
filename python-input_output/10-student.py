#!/usr/bin/python3
"""Student"""


class Student:

    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def to_json(self, attrs=None):
        keys = ["first_name", "last_name", "age"]
        json = {}
        for element in keys:
            if not attrs or element in attrs:
                json[element] = vars(self)["_Student__"+element]
        return json
