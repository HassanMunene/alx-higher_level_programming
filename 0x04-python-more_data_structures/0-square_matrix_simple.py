#!/usr/bin/python3

matrix2 = []
def square_matrix_simple(matrix=[]):
    #create a deep copy of the original matrix
    for row in matrix:
        matrix2.append(row[:])

    #then iterate through each element of matrix2 and then square it
    for i, row in enumerate(matrix2):
        for j, val in enumerate(row):
            matrix2[i][j] = matrix[i][j] * matrix2[i][j]
    return matrix2
