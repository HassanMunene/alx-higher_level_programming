#!/usr/bin/python3
import json
"""
contain the base class
"""


class Base:
    """
    the class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        return the json representation of dictionaries
        """
        json_rep = json.dumps(list_dictionaries)
        return json_rep
