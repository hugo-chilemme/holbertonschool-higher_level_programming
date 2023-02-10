#!/usr/bin/python3
"""import"""

Rectangle = __import__('9-rectangle').Rectangle
"""Square"""


class Square(Rectangle):
    """Square"""
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)

    def area(self):
        return self.__size * self.__size
