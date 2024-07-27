#!/usr/bin/python3
"""
This module defines binary search
"""
def find_peak(list_of_integers):
    """
    The function to define the serach
    """
    def binary_search_peak(start, end):
        """
        binary function
        """
        if start == end:
            return list_of_integers[start]

        mid = (start + end) // 2

        # Check if mid element is a peak
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1])\
                and (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]

        # If the left neighbor is greater, then a peak must be on the left side
        if mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            return binary_search_peak(start, mid - 1)

        # If the right neighbor is greater, then a peak must be on the right side
        return binary_search_peak(mid + 1, end)

    if not list_of_integers:
        return None

    return binary_search_peak(0, len(list_of_integers) - 1)
