#!/usr/bin/python3
"""
constainsa funtion that reads
a file
"""


def read_file(filename=""):
    """
    reads a text file
    """
    with open(filename, encoding="utf-8") as file:
        texts = file.read()
        print(texts, end="")
