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
        return self.__width

    @width.setter
    def width(self, value):
        if not(isinstance(self.width, int)):
            raise TypeError('width must be an integer')
        if self.width < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not(isinstance(self.heigt, int)):
            raise TypeError('height must be an integer')
        if self.height < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
