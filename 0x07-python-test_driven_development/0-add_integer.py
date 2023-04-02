#!/usr/bin/python3
"""0-add_integer Module
    This method adds two integers and returns their sum
"""
def add_integer(a, b=98):
    """add_integer
        Args:
            :@a - first input number
            :@b - second input number
            :Return - returns sum of a and b
    """
    if not(isinstance(a, int) or isinstance(a, float)):
        raise TypeError('a must be an integer')

    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError('b must be an integer')

    a = int(a)
    b = int(b)

    return (a + b)
