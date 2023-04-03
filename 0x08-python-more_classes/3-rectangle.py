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

    def area(self):
        return self._width * self._height

    def perimeter(self):
        if self._width == 0 or self._height == 0:
            return (0)

        return (self._width * 2 + self._height * 2)
 
    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
