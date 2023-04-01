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
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
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

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
