#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        rem = -number % 10
    if (number >= 0):
        rem = number % 10

    print("{0}".format(rem), end="")
    return rem
