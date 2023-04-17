#!/usr/bin/python3
"""Square Module"""
from models.base import Base
from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set teh size of square"""
        self.width = value
        self.height = value

    def __str__(self):
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y, self.size)


    def update(self, *args, **kwargs):
        if args and len(args) != 0:
            b = 0
            for arg in args:
                if b == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif b == 1:
                    self.width = arg
                elif b == 2:
                    self.height = arg
                elif b == 3:
                    self.x = arg
                elif b == 4:
                    self.y = arg
                b += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v