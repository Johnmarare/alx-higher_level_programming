#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix_cp = []
    for row in matrix:
        matrix_cp.append(list(map(lambda n: n * n, row)))

    return matrix_cp
