#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    n = len(sys.argv) - 1

    if (n == 0):
        print("{} {}".format(0, "arguments."))
    elif (n == 1):
        print("{} {}".format(n, "argument:"))
        print("{}: {}".format(n, sys.argv[n]))

    else:
        print("{} {}".format(n, "arguments:"))
        for x in range(1, n+1):
            print("{}: {}".format(x, sys.argv[x]))
