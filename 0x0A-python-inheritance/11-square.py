#!/usr/bin/python3
"""Defines subclass square rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defines a class square."""

    def __init__(self, size):
        """Creates new square.

        Args:
            size (int): size of a new square.
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns a string representation of the square.

        Returns:
            str: string represented as asquare.
        """

        return ("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        """Calculates the area of a class square.

        Returns:
            int: area of the new square.
        """

        return self.__size ** 2
