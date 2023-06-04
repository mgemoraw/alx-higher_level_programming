#!/usr/bin/python3
"""This module adds two integers"""


def add_integer(a, b=98):
    if not(isinstance(a, float) or isinstance(a, int)):
        raise TypeError('a must be an integer')
    
    if not (isinstance(b, float) or isinstance(b, int)):
        raise TypeError('b must be an integer')

    a = int(a)
    b = int(b)
    return a + b
