#!/usr/bin/python3
"""square class a child of rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square that inherits from the Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        string representation of the class
        """
        return "[Square] ({}) {}/{} - {}" \
            .format(self.id, self.x, self.y, self.width)