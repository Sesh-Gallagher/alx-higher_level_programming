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
