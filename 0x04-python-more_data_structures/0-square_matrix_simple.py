#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    pow_matrix = []
    for row in matrix:
        for i in row:
            pow_matrix.append(i ** 2)
    return pow_matrix
