#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        element = my_list[idx]
        my_list.remove(element)
    return my_list

delete_at()
