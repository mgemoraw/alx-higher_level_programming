#!/usr/bin/python3
"""Defines new class called Rectangled which inherits from class BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class using parent class BaseGeometry."""

    def __init__(self, width, height):
        """Initializing new Rectangle object.
        Args:
            width (int): width of the new Rectangle.
            height (int): height of the new Rectangle.
        """
        super().__init__.integer_validator("width", width)
        self.__width = width
        super.__init__().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
