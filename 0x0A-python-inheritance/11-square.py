#!/usr/bin/python3
"""
module defines a class square
that inherits from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represent a square class
    """

    def __init__(self, size):
        """
        Initialize a new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
