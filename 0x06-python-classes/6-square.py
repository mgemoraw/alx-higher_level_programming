#!/usr/bin/python3

""" Defining a Square class """


class Square:
    """
    Square Class
    """
    # size = None
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square Object

        Args:
            size (int): The size of the square
        """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(num, int) for num in value) or not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):

        """
        Public method area
            :Return - returns square of the size
        """

        return (self.__size ** 2)

    def my_print(self):
        if (self.__size == 0):
            print("")
        else:
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                for j in range(self.__size):
                    print("#", end="")
                print()


""" Test code
my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")

"""
