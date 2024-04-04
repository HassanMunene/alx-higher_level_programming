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

    @property
    def size(self):
        """
        getter method to get a private attribute
        """
        size = self.__size
        return size

    @size.setter
    def size(self, value):
        """
        setter method to set the the priv
        """
        if isinstance(value, int) is not True:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        calculate the area of a square
        """
        return self.__size * self.__size
