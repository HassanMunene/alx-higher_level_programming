#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for array in matrix:
        for idx, value in enumerate(array):
            print("{:d}".format(value), end='')
            if idx < len(array)-1:
                print(" ", end="")
        print()
