#!/usr/bin/python3

def max_integer(my_list=[]):
    list_len = len(my_list)
    if list_len == 0:
        return
    max = my_list[0]
    for i in range(list_len):
        if max < my_list[i]:
            max = my_list[i]
        else:
            continue
    return max
