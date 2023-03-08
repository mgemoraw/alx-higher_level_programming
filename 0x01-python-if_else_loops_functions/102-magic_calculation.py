#!/usr/bin/python3
def magic_calculation(a, b, c):
    if (a < b):
        return c
    if(b > c):
        c = a + b
        return (a + b)
    else:
        return (a * b - c)

# import dis
# print(dis.dis(magic_calculation))
