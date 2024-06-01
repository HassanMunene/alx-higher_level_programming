#!/usr/bin/python3
"""
get a python object by loading its
previously stored json string
"""
import json


def load_from_json_file(filename):
    """
    creats an object from json file
    """
    with open(filename) as file:
        return json.load(file)
