#!/usr/bin/python3
""" Base Class"""


class Base:
    """ Base Classs"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Base class constructor
        Args:
            id (int): The identity of the new Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
