#!/usr/bin/python3
"""Defines Rectangle class/module."""


class Rectangle:
    """Represents an empty class of a rectangle."""

    def __init__(self, width=0, height=0):
        """initializes the new rectangle."""

        self.width = width
        self.height = height

    @property
    def width(self):

        """Gets the width of the rectangle."""
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

        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):

        """Calculates the area of the rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):

        """Calculates the perimeter of the rectangle."""
        if self.__width == 0 or self.height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):

        """Calculates and present the rectangle in # characters."""
        if self.__width == 0 or self.__height == 0:
            return ""

        ret = []
        for i in range(self.__height):
            [ret.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                ret.append("\n")
        return ("".join(ret))

    def __repr__(self):
        """Calculates the string rep of the rectangle."""
        ret = "Rectangle(" + str(self.__width)
        ret += ", " + str(self.__height) + ")"
        return (ret)
