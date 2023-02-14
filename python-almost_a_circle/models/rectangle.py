#!/usr/bin/python3
"""Class rectangle"""


from models.base import Base
"""Class Base"""


class Rectangle(Base):
    """Class rectangle inherit from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def area(self):
        """Area: width * heigh"""
        return self.width * self.height

    def display(self):
        """print the visualization of the rectangle"""
        for y in range(0, self.y):
            print()
        for h in range(0, self.height):
            for x in range(0, self.x):
                print(" ", end="")
            for w in range(0, self.width):
                print('#', end="")
            print("")

    def update(self, *args):
        """that assigns an argument to each attribute:"""
        keys = ["id", "width", "height", "x", "y"]
        for k, v in enumerate(args):
            element = keys[k]
            if element:
                if element == 'id':
                    self.id = v
                if element == 'width':
                    self.width = v
                if element == 'height':
                    self.height = v
                if element == 'x':
                    self.x = v
                if element == 'y':
                    self.y = v

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
        )
