#!/usr/bin/python3
# print matrix
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in range(len(row) - 1):
            print("{:d}".format(row[col]), end=" ")
        # print("{:d}".format(row[len(row) - 1]))
        print(row[len(row) - 1 ], end="$\n")

def print_matrix_integer():
    pass
