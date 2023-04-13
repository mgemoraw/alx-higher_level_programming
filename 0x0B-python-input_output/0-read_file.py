#!/usr/bin/python3
"""
file handling using python3
"""


def read_file(filename=""):
    """Prints the contents of a text file (UTF8) file format into the stdout"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
        #print()
