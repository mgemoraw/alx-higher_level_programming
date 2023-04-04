#!/usr/bin/python3
"""Matrix Division"""
def matrix_divided(matrix, div):
    """divide matrix
        Args:
            matrix (list) - input matrix
            div (int)- divider integer
            Return - returns matrix / div
    """

    divs = []
    rows = [len(row) for row in matrix]
    for i in range(1, len(matrix)):
        if (rows[i - 1] != rows[i]):
            raise TypeError("Each row of the matrix must have the same size")

    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        rows = []
        for col in row:
            if not(isinstance(col, int) or isinstance(col, float)):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
            else:
                rows.append(round(col/div, 2))
        divs.append(rows)
    
    return divs
