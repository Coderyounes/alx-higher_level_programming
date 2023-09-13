#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    pow_matrix = []
    for row in matrix:
        pow_row = []
        for i in row:
            pow_row.append(i ** 2)
        pow_matrix.append(pow_row)
    return pow_matrix
