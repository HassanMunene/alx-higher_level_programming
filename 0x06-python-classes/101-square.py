#!/usr/bin/python3
"""
define an empty class called Square
"""


class Square:
    """
    class Square with size
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        getter method to get a private attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter method to set the the priv
        """
        if isinstance(value, int) is not True:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        '''getter method for position'''
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or\
                not all(isinstance(val, int) for val in value) or\
                not all(val >= 0 for val in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """
        calculate the area of a square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        print rep of the square as #
        """
        if self.__size == 0:
            print()
            return

        for i in range(0, self.__position[1]):
            print("")

        for length in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            for width in range(self.__size):
                print('#', end='')
            print()

    def __str__(self):
        '''return string rep of the object'''
        if self.__size != 0:
            for i in range(0, self.__position[0]):
                print("", end="")
        for length in range(0, self.__size):
            for j in range(0, self.__position[0]):
                print(" ", end="")
            for width in range(0, self.__size):
                print("#", end="")
            if length != self.__size - 1:
                print("")
        return ("")
