#!/usr/bin/python3
import sys

n = len(sys.argv)

if (n == 1):
    print("{} {}".format(0, "arguments."))
else:
    for x in range(1, n):
        print("{}: {}".format(x, sys.argv[x]))
