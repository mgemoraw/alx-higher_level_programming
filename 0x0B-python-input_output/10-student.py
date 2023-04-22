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
        """Gets a dictionary representation of the Student object"""
        if (type(attrs) == list and all(type(element) == str for element in attrs )):
            return {val: getattr(self, val), for val in attrs if hasattr(self, var)}    
        return self.__dict__
