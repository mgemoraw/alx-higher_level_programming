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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size

    def area(self):

        """
        Public method area

            :Return - returns square of the size
        """

        return (self._Square__size ** 2)


"""
my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))
"""
