#!/usr/bin/python3
"""
save an object to a file in form
of a json string
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file,
    using a JSON representation
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
