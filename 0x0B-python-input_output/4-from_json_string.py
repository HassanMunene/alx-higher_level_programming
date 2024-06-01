#!/usr/bin/python3
"""
convert from a json string to
a python object
"""
import json


def from_json_string(my_str):
    """
    from json string to a python object
    """
    return json.loads(my_str)
