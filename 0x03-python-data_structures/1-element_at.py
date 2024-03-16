#!/usr/bin/python3

def element_at(my_list, idx):
    length = len(my_list)
    if idx > length:
        return None
    elif idx < 0:
        return None
    else:
        return my_list[idx]
