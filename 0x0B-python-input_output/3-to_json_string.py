#!/usr/bin/python3
"""
convert a python object to json string
"""
import json


def to_json_string(my_obj):
    """
    returns json representation of an object
    """
    return json.dumps(my_obj)
