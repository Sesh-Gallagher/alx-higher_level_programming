#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry.
based on task 8-rectangle.py"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a class rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """creates a new Rectangle.

        Args:
            width (int):  width of the Rectangle.
            height (int): height of the Rectangle.
        """

        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def area(self):
        """calculates the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns str representation of the rectangle.

        Returns:
            str: a str representation of Rectangle.
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
