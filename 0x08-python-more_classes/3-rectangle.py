#!/usr/bin/python3
'''contain class Rectangle'''


class Rectangle:
    '''the class'''

    def __init__(self, width=0, height=0):
        if isinstance(width, int) is False:
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = width

        if isinstance(height, int) is False:
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = height

    @property
    def width(self):
        '''return width of rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''set width for the priv attribute'''
        if isinstance(value, int) is False:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        '''return height of rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''set height for the priv attribute'''
        if isinstance(value, int) is False:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        '''return area of rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''return perimeter of the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        '''return a string rep of the rectangle in form of #'''
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repl__(self):
        '''return a developer friendly rep of the rec object'''
        return f"Rectangle(width={self.__width}, height={self.__height})"
