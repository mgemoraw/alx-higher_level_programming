#!/usr/bin/python3
if __name__ == "__main__":
    """My personal calculator programe"""

    import sys
    from calculator_1 import add, sub, mul, div

    n = len(sys.argv) - 1

    ops = {'+':add, '-':sub, '*':mul, '/':div}

    if (n != 3):
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
    
    if (sys.argv[2] not in list(ops.keys())):
        print("Unknown operator. Available operrators: +, -, * and /")
        sys.exit(1)

    a, b = int(sys.argv[1]), int(sys.argv[3])
    
    print("{} {} {} = {}".format(a,sys.argv[2], b, ops[sys.argv[2]](a, b)))