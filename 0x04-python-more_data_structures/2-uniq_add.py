#!/usr/bin/python3


def uniq_add(my_list=[]):
    unique_set = set(my_list)
    unique_list = list(unique_set)
    sum = 0

    for i in range(len(unique_list)):
        sum += unique_list[i]
    return sum
