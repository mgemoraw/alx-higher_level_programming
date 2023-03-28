#!/usr/bin/python3


""" Defining a Square class """


class Square:
    """
    Square Class
    """
    # size = None
    def __init__(self, size=0):
        """Initialize a Square Object

        Args:
            size (int): The size of the square
        """

        self.size = size

    @property
    def size(self):
        """
        gets the value of size
        :Return - returns the size
        """
        return (self.__size)

    @size.setter
    def size(self, value):

        """
        sets the value of size
        Args:
            :value - value of size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):

        """
        Public method area
            :Return - returns square of the size
        """

        return (self.__size ** 2)


"""
my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)
"""
