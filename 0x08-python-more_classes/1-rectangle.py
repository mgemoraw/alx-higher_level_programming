#!/usr/bin/python3

"""Redefining rectangle class"""


class Rectangle:
    """Rectangle Class"""

    def __init__(self, width=0, height=0):
        """Initialize enw Rectangle:

        Args:
            width(int): The width of the rectangle
            height(int): The height of the rectnagle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectagle."""

        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

        self._width = value

    @property
    def height(self):
        """Get/set the height of the rectagle."""

        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

        self._height = value
