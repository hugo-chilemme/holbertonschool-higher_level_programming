#!/usr/bin/python3
"""Square"""


class Square:
    """Init Square"""
    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise ValueError("size must be an integer")
        if value < 0:
            raise ValueError("size must be an integer")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            return print() #blank line
        
        for y in range (0, self.__size):
            for x in range (0, self.__size):
                print("#", end="")
            print() #blank line
