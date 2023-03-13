#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lena, lenb = len(tuple_a), len(tuple_b)
    if lena == 0:
        tuple_a = (0, 0)
    if lena == 1:
        tuple_a = (tuple_a[0], 0)
    
    if lenb == 0:
        tuple_b = (0, 0)
    if lenb == 1:
        tuple_b = (tuple_b[0], 0)

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])  
