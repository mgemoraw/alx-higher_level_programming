#!/usr/bin/python3
"""This divides matrices"""


def matrix_divided(matrix, div):
    """Args
        : matrix (float) - must be a list of lists of integers or floats
        div (float): divider float or integer
    """
    for row in matrix:
        for item in row:
            if not (isinstance(item, int) or isinstance(item, float)):
                raise TypeError("matrix must be a matrix \
                (list of lists) of integers/floats")
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        row_mat = []
        for item in row:
            value = item/div
            row_mat.append(round(value, 2))
        new_matrix.append(row_mat)
    return new_matrix
