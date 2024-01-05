#!/usr/bin/python3
"""Defines a rectangle class."""


class Rectangle:
    """An empty class that represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes the new rectangle."""

        self.height = height
        self.width = width

    @property
    def width(self):

        """set the width of rectangle."""
        return self.__width

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):

        """get the height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
