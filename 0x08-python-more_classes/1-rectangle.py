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
