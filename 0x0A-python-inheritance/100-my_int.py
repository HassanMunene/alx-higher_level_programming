#!/usr/bin/python3
"""
module contains class MyInt
"""


class MyInt(int):
    """
    represent a rebel integer that does the opposite
    """
    def __new__(cls, *args, **kwargs):
        """
        creates new instance of the class
        """
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """
        what was != is now ==
        """
        return int(self) != other

    def __ne__(self, other):
        """
        what was == is now !=
        """
        return int(self) == other
