#!/usr/bin/python3
"""
define an empty class called Square
"""


class Square:
    """
    class Square with size
    """
    def __init__(self, size=0):
        if isinstance(size, int) is not True:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """
        calculate the area of a square
        """
        return self.__size * self.__size
