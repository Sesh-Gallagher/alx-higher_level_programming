#!/usr/bin/python3
"""Defines class rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class rectangle presented using BaseGeometry."""

    def __init__(self, width, height):
        """Represent a new instance of a rectangle """

        self.__width = width
        self.__height = height
        self.integer_validator("height", height)
        self.integer_validator("width", width)
