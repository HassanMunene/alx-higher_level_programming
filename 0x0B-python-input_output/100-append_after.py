#!/usr/bin/python3
"""
define an append function
"""


def append_after(filename="", search_string="", new_string=""):
    """
    appends new_string after  line that is containing
    search_string in filename
    """
    with open(filename, 'r', encoding='utf-8') as file:
        line_list = []
        while True:
            line = file.readline()
            if line == "":
                break
            line_list.append(line)
            if search_string in line:
                line_list.append(new_string)
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(line_list)
