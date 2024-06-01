#!/usr/bin/python3
"""
Contain a class Rectangle that inherits
from BaseGeometry
"""


class BaseGeometry:
    """
    BaseGometry class here
    """
    def area(self):
        """
        raise an exception when called
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        will be used to validate a value
        """
        if isinstance(value, int) is False:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """
    representation of Rectangle
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
