#!/usr/bin/python3
"""
contains a function that prints the
full names of an individual
"""
def say_my_name(first_name, last_name=""):
    """
    print the names
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print(f"My name is {first_name} {last_name}")
