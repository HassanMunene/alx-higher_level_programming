#!/usr/bin/python3


def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    total_weight = 0
    total_val = 0
    for i in my_list:
        score, weight = i
        total_weight += weight
        total_val += score * weight
    weighted_avg = total_val / total_weight
    return weighted_avg
