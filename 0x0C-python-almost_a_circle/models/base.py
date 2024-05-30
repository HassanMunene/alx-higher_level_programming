#!/usr/bin/python3
"""
This is the base class from where everything
will be inherited from
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        return the json representation of dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        json_rep = json.dumps(list_dictionaries)
        return json_rep

    @classmethod
    def save_to_file(cls, list_objs):
        """
        write json string representation to a file
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))
