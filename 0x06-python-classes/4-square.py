#!/usr/bin/python3

"""A Class square module based on 3-square.py"""


class Square():
    """intializes a square class.

    defines __init__ function."""

    def __init__(self, size=0):

        """initializes size of self."""
        self.size = size

    @property
    def size(self):
        """set size of square and return and return size of self."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = (value)
        """ defines area function """

    def area(self):
        """returns current area of the square."""

        return self.__size ** 2
