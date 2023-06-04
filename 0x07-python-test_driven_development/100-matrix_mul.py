#!/usr/bin/python3


def matrix_mul(m_a, m_b):

    if not(isinstance(m_a, list)):
        raise TypeError("m_a must be a list")
    if not(isinstance(m_b, list)):
        raise TypeError("m_b must be a list")

    for row in m_a:
        if not(isinstance(row, list)):
            raise TypeError("m_a must be a list of lists")
    for row in m_a:
        if not(isinstance(row, list)):
            raise TypeError("m_a must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for val in row:
            if not (isinstance(val, int) or isintance(val, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for val in row:
            if not (isinstance(val, int) or isintance(val, float)):
                raise TypeError("m_b should contain only integers or floats")


    if (len(m_a) != len(m_b[0])) and (len(m_a[0]) != len(m_b)):
        raise ValueError("m_a and m_b can't be multiplied")

    for i in range(0, len(m_a)):
        row = [v for v in m_a[i]]
            
