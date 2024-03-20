#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new_dict = dict(a_dictionary)

    for key, value in new_dict.items():
        value = value * 2
        new_dict[key] = value
    return new_dict
