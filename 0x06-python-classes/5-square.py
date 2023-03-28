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

    def my_print(self):
        if (self.__size == 0):
            print("#" * self.__size)
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()


"""
my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")

"""
