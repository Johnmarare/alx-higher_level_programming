#!/usr/bin/python3
# division in a matrix
# 2-matrix_divided.py
"""Defines a matrix division function"""


def matrix_divided(matrix, div):
    """Divides a matrix

    Args:
        matrix (list, int/float): matrix to be divided, any size.
        div (int): the number to divide the matrix.
    Raises:
        TypeError: Matrix must be a list of int or float.
        TypeError: div must be a number.
        ZeroDivisionError: div cannot be zero.
    """

    errors = "matrix must be a matrix (list of lists) of integers/floats"
    error2 = "Each row of the matrix must have the same size"
    if type(matrix) is not list:
        raise TypeError(errors)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(errors)
        if len(row) != len(matrix[0]):
            raise TypeError(error2)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    newmatrix = []
    for (row) in matrix:
        new_row = [round(i / div, 2) for i in row]
        newmatrix.append(new_row)

    return (newmatrix)
