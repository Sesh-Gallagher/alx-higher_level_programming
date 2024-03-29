#!/usr/bin/python3
"""Defines a rectangle class/module."""


class Rectangle:
    """Represents a rectangle class."""

    def __init__(self, width=0, height=0):
        """Initializes the new rectangle."""

        self.height = height
        self.width = width

    @property
    def width(self):

        """Sets the width of the rectangle."""
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

        """Gets the height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
