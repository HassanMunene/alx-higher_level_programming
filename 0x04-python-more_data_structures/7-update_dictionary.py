#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    dict_list = list(a_dictionary)
    for item in dict_list:
        if item != key:
            a_dictionary[key] = value
        elif item == key:
            a_dictionary[item] = value
    return a_dictionary
