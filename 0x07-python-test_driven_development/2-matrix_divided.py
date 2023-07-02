#!/usr/bin/python3
#division in a matrix
#2-matrix_divided.py

def matrix_divided(matrix, div):
    errors = "matrix must be a matrix (list of lists) of integers/floats"
    error2 = "Each row of the matrix must have the same size"
    if type(matrix) is not list:
        raise TypeError (errors)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(errors)
        if len(row) != len(matrix[0]):
            raise TypeError (error2)
    if not isinstance(div, (int, float)):
        raise TypeError ("div must be a number")
    if div == 0:
        raise ZeroDivisionError ("division by zero")
    
    newmatrix = []
    for (row) in matrix:
        new_row = [round(i / div, 2) for i in row]
        newmatrix.append(new_row)


    return(newmatrix)
