#!/usr/bin/python3
"""Student"""


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        json = {}
        for k, v in enumerate(self.__dict__):
            if attrs is None or i in attrs:
                json[v] = self.__dict__[v]
        return json
