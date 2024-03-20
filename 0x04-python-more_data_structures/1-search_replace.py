#!/usr/bin/python3

new_list = []


def search_replace(my_list, search, replace):
    """create a copy of the original list"""
    new_list = my_list[:]

    for idx, val in enumerate(new_list):
        if val == search:
            new_list[idx] = replace
    return new_list
