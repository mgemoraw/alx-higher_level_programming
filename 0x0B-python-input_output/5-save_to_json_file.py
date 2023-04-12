#!/usr/bin/python3
"""
writes an object to text file using JSON
"""


def save_to_file(my_obj, filename):
    """
    Writes an object to text file using JSON
    """
    with open(filename, "w") as file:
        json.dumps(my_obj, file)
