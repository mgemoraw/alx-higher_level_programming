#!/usr/bin/python3

def print_square(size):

    if not (isinstance(size, int) or isinstance(size, float)):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")


    for r in range(size):
        for c in range(size):
            print("#", end="")
        print()

    