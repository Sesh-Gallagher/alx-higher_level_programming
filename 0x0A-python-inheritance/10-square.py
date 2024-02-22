#!/usr/bin/python3
"""Defines subclass square from rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defines a class square."""

    def __init__(self, size):
        """Creates a instance of a class square.

        Args:
            size (int): The size of the new square.
        """

        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
