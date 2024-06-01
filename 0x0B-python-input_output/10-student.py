#!/usr/bin/python3
"""
contains a defination of a Student Class
"""


class Student:
    """
    a blueprint for a student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Get dictionary rep of the Student based on the attrs provided
        """
        if (type(attrs) == list and
                all(type(attr) == str for attr in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
