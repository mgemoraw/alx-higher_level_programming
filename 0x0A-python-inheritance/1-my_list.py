#!/usr/bin/python3
"""Inherited from List class"""


class MyList(list):
    """MyList class"""
    def __init__(self):
        """class constructor"""
        super().__init__()

    def print_sorted(self):
        """Function prints sorted list"""
        print(sorted(self))
