#!/usr/bin/python3
"""Simple Rectangle class"""


class Rectangle:
    """defines a rectangle class
    Attributes:
        number_of_instances (int) - represents number of instances
        print_symbol (any) - the symbology used for string representation
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """class costrctor for rectangle
        Args:
            width(int) - width of the rectangle
            height(int) - height of the rectangle
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not (isinstance(value, int)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.height == 0:
            return (0)
        return (self.__width * 2 + self.__height * 2)

    def __str__(self):
        """Returns the string representation of Rectangle instance"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        hash_rect = []
        for h in range(self.__height):
            for w in range(self.__width):
                hash_rect.append(str(self.print_symbol))
            if (h != self.__height - 1):
                hash_rect.append("\n")
        return ("".join(hash_rect))

    def __repr__(self):
        """Returns the string representation of rectangle instance"""
        rect = "Rectangle(" + str(self.__width) + ", "
        rect += str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """prints message for deletion of every instance"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not (isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not (isinstance(rect_2, Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new rectangle instance with both sides same
        Args:
            size (int) - width of the square
        """
        return (cls(size, size))
