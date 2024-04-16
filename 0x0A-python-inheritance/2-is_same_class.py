#!/usr/bin/python3
"""
module to define a function
"""


def is_same_class(obj, a_class):
    """
    determine if indeed an obj is an
    instance of the specified class
    """
    return type(obj) is a_class
