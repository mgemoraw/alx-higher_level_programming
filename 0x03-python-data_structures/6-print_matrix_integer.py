#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            print("{}".format(matrix[row][col]), end=" ")

        print("{}".format(matrix[row][col]) + "$")

    for row in matrix:
        for col in row and matrix.index(row) < len(row):
            print("{}".format(matrix[row][col]), end=" ")
            
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
