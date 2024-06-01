#!/usr/bin/python3
"""
append a text string to a file
"""


def append_write(filename="", text=""):
    """
    appends a text to a string file
    """
    with open(filename, "a", encoding="utf-8") as file:
        num = file.write(text)
        return num
