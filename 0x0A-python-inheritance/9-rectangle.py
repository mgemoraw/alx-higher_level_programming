#!/usr/bin/python3
"""Defines new class called Rectangled which
inherits from class BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class using parent class BaseGeometry."""

    def __init__(self, width, height):
        """Initializing new Rectangle object.
        Args:
            width (int): width of the new Rectangle.
            height (int): height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self._width = width
        super().integer_validator("height", height)
        self._height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self._width * self._height

    def __str__(self):
        """Returns the print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self._width) + "/" + str(self._height)
        return string
