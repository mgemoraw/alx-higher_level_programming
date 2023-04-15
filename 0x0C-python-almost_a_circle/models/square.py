#!/usr/bin/python3
"""Square Module"""
from models.base import Base
from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size[0], size[1],x, y, id)

    @property
    def size(self):
        """Gets the size of the Square."""
        return self.size[0]

    @size.setter
    def size(self, value):
        """Set teh size of square"""
        self.size[0] = value
        self.size[1] = value

    def __str__(self):
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y, self.size)
