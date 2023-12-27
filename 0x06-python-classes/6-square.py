#!/usr/bin/python3

"""A Class square module based on 3-square.py"""


class Square():
    """intializes a square class.

    defines __init__ function."""

    def __init__(self, size=0, position=(0, 0)):

        """initializes size of self."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """set size of square and return and return size of self."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = (value)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 posetive integers")
        self.__position = value

    def area(self):
        """returns current area of the square."""

        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for a in range(0, self.__position[1])]
        for a in range(0, self.__size):
            [print(" ", end="") for b in range(0, self.__position[0])]
            [print("#", end="") for b in range(0, self.__size)]
            print("")
