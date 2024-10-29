#!/usr/bin/env python3
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

    
class Circle(Shape):

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return 3.14 * self.__radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.__radius 


class Rectangle(Shape):

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
    
    def area(self):
        return self.__width * self.__height
    
    def perimeter(self):
        return 2 * (self.__width + self.__height)


def shape_info(obj):
    print("Area: ", obj.area())
    print("Perimeter: ", obj.perimeter())
    

if __name__ == '__main__':
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=7)
    
    shape_info(circle)
    shape_info(rectangle)
