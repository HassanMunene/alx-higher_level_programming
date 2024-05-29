#!/usr/bin/python3
"""
class Rectangle that inherits from class Base
"""
from models.base import Base


class Rectangle(Base):
    """
    The rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        getter method for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter method for width
        """
        if isinstance(value, int) is False:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        """
        getter method for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter method for height
        """
        if isinstance(value, int) is False:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        """
        getter method for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter method for x
        """
        if isinstance(value, int) is False:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """
        getter method for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter method for y
        """
        if isinstance(value, int) is False:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        """
        calculate and return the area
        of a rectangle
        """
        ar = self.width * self.height
        return ar

    def display(self):
        """
        display a rectangle using # symbol
        """
        if self.width == 0 or self.height == 0:
            print("")
            return
        for y in range(self.y):
            print("")
        for i in range(self.height):
            for x in range(self.x):
                print(" ", end='')
            for j in range(self.width):
                print("#", end='')
            print()

    def update(self, *args):
        """
        update the specified attribute
        1st is id, 2nd is width, 3rd is height,
        4th is x and 5th is y
        """
        attributes = ['id', 'width', 'height', 'x', 'y']

        for index, val in enumerate(args):
            if index > len(attributes):
                return
            self.__setattr__(attributes[index], val)

    def __str__(self):
        """
        readable string representation of
        our Rectangle class
        """
        return "[Rectangle] ({}) {}/{} - {}/{}" \
            .format(self.id, self.x, self.y, self.width, self.height)
