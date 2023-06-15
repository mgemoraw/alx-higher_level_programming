#!/usr/bin/python3
"""Function for class to JSON object file"""


def class_to_json(obj):
    """Returns the dictionary represntation of a simple data structure."""
    return obj.__dict__
