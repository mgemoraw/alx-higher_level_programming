#!/usr/bin/python3
for i in range(10):
    for j in range(i, 10):
        if ((i != j) and (i != 8 and j != 9)):
            print("{0}{1}".format(i, j), end=", ")
print("{0}{1}".format(8, 9))