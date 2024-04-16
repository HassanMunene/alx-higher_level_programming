#!/usr/bin/python3
"""
Inherit from list and then add a new
method that return the list sorted in
ascending order
"""


class MyList(list):
    """
    The subclass of list
    """
    def __init__(self):
        super().__init__(self)

    def print_sorted(self):
        """
        sort a list in ascending
        using a bubble sort
        """
        print(sorted(self))
