#!/usr/bin/python3
import json
"""
This is the base class from where everything
will be inherited from
"""


class Base:
    """
    the class Base itself with
    its initialization
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
        if list_dictionaries is None:
            return "[]"
        json_rep = json.dumps(list_dictionaries)
        return json_rep
