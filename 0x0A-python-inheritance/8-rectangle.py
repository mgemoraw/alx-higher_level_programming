#!/usr/bin/python3
"""Defines new class called Rectangled which
inherits from class BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class using parent class BaseGeometry."""

    def __init__(self, width, height):
        """Initializing new Rectangle object.
        Args:
            width (int): width of the new Rectangle.
            height (int): height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
