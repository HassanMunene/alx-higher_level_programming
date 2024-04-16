#!/usr/bin/python3
"""
module to define a function
"""


def is_same_class(obj, a_class):
    """
    determine if indeed an obj is an
    instance of the specified class
    """
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
