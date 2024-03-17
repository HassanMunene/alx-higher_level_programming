#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    length = len(my_list)
    if idx < 0:
        a = my_list
        return a
    if idx >= length:
        a = my_list
        return a

    new_list = []
    for index, value in enumerate(my_list):
        new_list.append(value)
    new_list[idx] = element
    return new_list
