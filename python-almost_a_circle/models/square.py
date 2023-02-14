#!/usr/bin/python3
"""Class Square"""


from models.rectangle import Rectangle
"""Class Base"""


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width
        )

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """that assigns an argument to each attribute:"""
        keys = ["id", "size", "x", "y"]
        values = {}
        for k, v in enumerate(args):
            element = keys[k]
            values[element] = v
        if not args or len(args) == 0:
            for k, v in kwargs.items():
                values[k] = v
        for k, v in values.items():
            if k == "size":
                self.width = v
                self.height = v
            if k == "x":
                self.x = v
            if k == "y":
                self.y = v
            if k == "id":
                self.id = v

    def to_dictionary(self):
        """Create object data"""
        obj = {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
        return obj
