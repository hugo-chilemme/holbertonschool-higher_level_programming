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
            if attrs is None or element in attrs:
                json[element] = vars(self)["_Student__"+element]
        return json

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value
        
    @property
    def age(self):
        return self.__last_name

    @age.setter
    def age(self, value):
        self.__age = value

    def reload_from_json(self, json):
        if "first_name" in json:
            self.first_name = json["first_name"]
        if "last_name" in json:
            self.last_name = json["last_name"]
        if "age" in json:
            self.age = json["age"]
