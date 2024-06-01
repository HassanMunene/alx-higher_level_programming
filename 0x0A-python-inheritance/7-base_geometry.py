#!/usr/bin/python3
"""
declare a class called BaseGeometry
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
