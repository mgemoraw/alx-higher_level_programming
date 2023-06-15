#!/usr/bin/python3
"""Defines a Square class which is subclass of Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class of a square."""

    def __init__(self, size):
        """Initializing new square object.
        Args:
            size (int): size of the new square.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self._size = size
