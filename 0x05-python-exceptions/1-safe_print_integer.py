#!/usr/bin/python3
def safe_print_integer(value):
    count = 0
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        return False


"""TEST Code
value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))
"""
