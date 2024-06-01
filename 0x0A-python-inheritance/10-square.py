#!/usr/bin/python3
"""
module to define class square
that inherits from Rectangle class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    will represent a square
    """
    def __init__(self, size):
        """
        Intialize a new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
