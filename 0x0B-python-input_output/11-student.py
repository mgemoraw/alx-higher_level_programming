#!/usr/bin/python3
"""Student class."""


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
            return {v: getattr(self, v) for v in attrs if hasattr(self, v)}    
        return self.__dict__
    
    def reload_from_json(self, json):
        """Replace all attributes of the student
        Args:
            json (dict): the keyvalue pair
        """
        for key, value in json.items():
            setattr(self, key, value)

