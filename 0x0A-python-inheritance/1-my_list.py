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
        leng = len(self)
        for i in range(leng):
            for j in range(leng - 1):
                if self[j] > self[j + 1]:
                    temp = self[j]
                    self[j] = self[j+1]
                    self[j+1] = temp
        print(self)
