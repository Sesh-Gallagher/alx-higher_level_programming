#!/usr/bin/python3
""" A module thatDefines a class Rectangle 
that inherits from BaseGeometry. based on task 8-rectangle.py"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """empty class represents rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """creates a new rectangle"""

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
