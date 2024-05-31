#!/usr/bin/python3
"""
This module that computes Area and perimeter
"""


class Rectangle:
    """Represent a rectangle as a class"""

    number_of_instances = 0
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter method - get value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter- sets the value of width
        Args:
           value(int): the value to set the width
        """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter- gets value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter: sets the value of height
        Args:
            value(int): the value to set to width
        """
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns Area of rectangle"""
        area = self.height * self.width
        return area

    def perimeter(self):
        """Returns perimeter of rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        per = (self.width + self.height) * 2
        return per

    def __str__(self):
        """
        Return the printable representation of a rectangle.
        use # symbol to represent rectangle
        """
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        else:
            for height in range(self.height):
                for widht in range(self.width):
                    string += "#"
                if height != self.height - 1:
                    string += "\n"
            return string

    def __repr__(self):
        """Return the official string representation of Rectangle
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        the method that is called when an instance is
        garbage collected or deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
