#!/usr/bin/python3
"""import"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Rectangle"""


class Rectangle(BaseGeometry):
    """Rectangle"""
    def __init__(self, width, height):
        BaseGeometry.integer_validator("width", width)
        BaseGeometry.integer_validator("height", height)
        self.__width = width
        self.__height = height
