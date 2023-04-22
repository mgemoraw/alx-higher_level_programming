#!/usr/bin/python3
"""Defines Student class."""


class Student:
    """Student object."""

    def __init__(self, first_name, last_name, age):
        """class constructor for student class.

        Args:
            first_name (str): student first name.
            last_name (str): student last name.
            age (int): age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets a dictionary representation of the Student object
        If attrs is a list of strings, only attribute \
        names contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved
        Args
            attrs (list): (Optional) attributes to represent
        """
        if (type(attrs) == list and all(type(el) == str for el in attrs)):
            return {v: getattr(self, v) for v in attrs if hasattr(self, v)}   
        return self.__dict__
