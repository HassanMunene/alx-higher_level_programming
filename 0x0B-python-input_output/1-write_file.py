#!/usr/bin/python3
"""
write a text to a file and return
the number of characters written
"""


def write_file(filename="", text=""):
    """
    writes a text to a file
    """
    with open(filename, "w", encoding="utf-8") as file:
        num = file.write(text)
        return num
