#!/usr/bin/python3
"""Object that returns list of functions"""


def lookup(obj):
    """Returns list of functions and attributes in obj"""
    return (dir(obj))
