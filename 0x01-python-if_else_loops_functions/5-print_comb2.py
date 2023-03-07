#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if ((j != 0) and (i != 9 and j != 9)):
            print("{0}{1}".format(i, j), end=", ")
print("{0}{1}".format(9, 9))
