#!/usr/bin/python3
"""Defines a class named square"""


class Square():
    """defines a square."""

    def __init__(self, size=0):
        """iniatializes a new square."""
        if type(size) is not int:
            """ raise and error """
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
