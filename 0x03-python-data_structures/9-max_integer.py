#!/usr/bin/python3

def max_integer(my_list=[]):
    list_len = len(my_list)
    max = my_list[0]
    for i in range(list_len - 1):
        if max < my_list[i]:
            max = my_list[i]
    return max
