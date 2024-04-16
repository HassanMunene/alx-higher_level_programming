#!/usr/bin/python3
"""
contains a function that that employs
use of isinstance
"""


def is_kind_of_class(obj, a_class):
    """
    True if object is  instance/inherited from a_class, else false
    """
    return (isinstance(obj, a_class))
