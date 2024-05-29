#!/usr/bin/python3
"""square class a child of rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square that inherits from the Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """retrieve the value of width"""
        return self.width

    @size.setter
    def size(self, value):
        """set the value of width and height"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """use setattr to update the class attributes"""
        attributes = ["id", "size", "x", "y"]
        for index, val in enumerate(args):
            if index > len(attributes):
                return
            self.__setattr__(attributes[index], val)
        if args:
            return
        for key, value in kwargs.items():
            self.__setattr__(key, value)

    def __str__(self):
        """
        string representation of the class
        """
        return "[Square] ({}) {}/{} - {}" \
            .format(self.id, self.x, self.y, self.width)
