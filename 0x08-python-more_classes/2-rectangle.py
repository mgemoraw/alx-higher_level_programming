#!/usr/bin/python3
"""Simple Rectangle class"""


class Rectangle:
    """defines a rectangle class"""
    def __init__(self, width=0, height=0):
        """class costrctor for rectangle
        Args:
            width(int) - width of the rectangle
            height(int) - height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not (isinstance(width, int)):
            raise TypeError("width must be an integer")
        if self.width < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not (isinstance(height, int)):
            raise TypeError("height must be an integer")
        if self.height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
#!/usr/bin/python3
"""Simple Rectangle class"""


class Rectangle:
    """defines a rectangle class"""
    def __init__(self, width=0, height=0):
        """class costrctor for rectangle
        Args:
            width(int) - width of the rectangle
            height(int) - height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not (isinstance(width, int)):
            raise TypeError("width must be an integer")
        if self.width < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not (isinstance(height, int)):
            raise TypeError("height must be an integer")
        if self.height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.height == 0:
            return (0)
        return (self.__width * 2 + self.__height * 2)
