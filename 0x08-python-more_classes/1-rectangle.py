#!/usr/bin/python3
"""Simple Rectangle class"""


class Rectangle:
    """defines a rectangle class"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        if not (isinstance(width, int)):
            raise TypeError("width must be an integer")
        if self.width < 0:
            raise ValueError("width must be >= 0")
        return self.__width

    @property
    def height(self):
        if not (isinstance(height, int)):
            raise TypeError("width must be an integer")
        if self.height < 0:
            raise ValueError("height must be >= 0")
        return self.__height

    @width.setter
    def width(self, value):
        self.__width = value
    
    @height.setter
    def height(self, value):
        self.__height = value
