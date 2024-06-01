#!/usr/bin/python3
"""
module that defines function that
adds attributes to objects
"""


def add_attribute(obj, att, value):
    """
    Add new attribute to object if possible.
    Args:
        obj: object to add an attribute to
        att: name of the attribute to add to object.
        value: value of attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
