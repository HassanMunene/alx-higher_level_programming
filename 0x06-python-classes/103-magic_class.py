#!/usr/bin/python3
'''define a class named MagicClass'''
import math


class MagicClass:
    '''class with circle methods'''
    def __init__(self, radius=0):
        self.__radius = 0

        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        '''return area of circle'''
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        '''return circumference of circle'''
        return 2 * math.pi * self.__radius
