#!/usr/bin/python3

"""Redefining rectangle class"""

class Rectangle:
    """Rectangle Class"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        if not(isinstance(self.width, int)):
            raise TypeError('width must be an integer')
        if self.width < 0:
            raise ValueError('width must be >= 0')
        return self.width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        if not(isinstance(self.heigt, int)):
            raise TypeError('height must be an integer')
        if self.height < 0:
            raise ValueError('height must be >= 0')
        return self.height

    @height.setter
    def height(self, value):
        self._height = value
