#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    key_list = []
    for key, val in a_dictionary.items():
        if val == value:
            key_list.append(key)

    if len(key_list) == 0:
        return a_dictionary
    for key in key_list:
        del a_dictionary[key]
    return a_dictionary
