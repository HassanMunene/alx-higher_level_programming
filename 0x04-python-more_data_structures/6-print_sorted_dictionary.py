#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    sorted_list = sorted(a_dictionary)

    for item in sorted_list:
        print(f"{item}: {a_dictionary[item]}")
