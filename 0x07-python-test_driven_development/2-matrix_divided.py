#!/usr/bin/python3
"""
divide the elements in a matrix
"""
def matrix_divided(matrix, div):

    for i in range(len(matrix)):
        for j in matrix[i]:
            if type(j) is not int and type(j) is not float:
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
            else:
                print(j)

matrix_divided([[1,2,3], [4,5,6]], 2)
