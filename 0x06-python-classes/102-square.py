#!/usr/bin/python3
"""
define an empty class called Square
"""


class Square:
    """
    class Square with size
    """
    def __init__(self, size=0):
        self.size = size

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
        if isinstance(value, int) is False:
            raise TypeError('size must be a number')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """
        calculate the area of a square
        """
        return self.__size * self.__size

    def __eq__(self, other):
        '''return true of our current instance is equal to other'''
        return self.size == other.size

    def __ne__(self, other):
        '''return true if current instance is != to other'''
        return self.size != other.size

    def __gt__(self, other):
        '''return true current instance is greater than other'''
        return self.size > other.size

    def __ge__(self, other):
        '''return true if current instance >= other'''
        return self.size >= other.size

    def __lt__(self, other):
        '''return true if c.ins < other'''
        return self.size < other.size

    def __le__(self, other):
        '''return true if c.ins <= other.size'''
        return self.size <= other.size
