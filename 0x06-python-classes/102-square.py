#!/usr/bin/python3
"""Define a class square module"""


class Square:
    """Represents square class"""

    def __init__(self, size=0):

        """
        initializes a new square instance

        Args:
            size (int): Size of the new square attribute
        """

        self.__size = size

    @property
    def size(self):

        """Get and/or set the size of the square.

        Return:
            int: The value of the size attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):

        """
        Get and/or set the size of a square object

        Args:
            size (int): The new value for the size attribute
        """

        if isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return the current area of a Square object"""
        return self.__size ** 2

    def __eq__(self, other):
        """Define the == comparison of a square"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison of a square"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Define the > comparison of a square"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= comparison of a square."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Define the < comparison of a square"""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a square"""
        return self.area() <= other.area()
