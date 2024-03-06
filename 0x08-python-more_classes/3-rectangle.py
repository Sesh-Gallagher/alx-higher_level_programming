#!/usr/bin/python3
"""Defines a Rectangle class/module."""


class Rectangle:
    """An empty class that represents a rectangle."""

    def __init__(self, width=0, height=0):

        """Initializes the new Rectangle. """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets width of the Rectangle."""
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
        """Gets height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates the area of the rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """calculates the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """represents the triangle in # characters"""
        if self.__width == 0 or self.__height == 0:
            return ('')

        ret = ''
        for i in range(self.__height):
            for j in range(self.__width):
                ret += '#'
            ret += '\n'
        return ret[:-1]
