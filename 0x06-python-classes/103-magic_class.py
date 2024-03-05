#!/usr/bin/python3
"""Defines a class called MagicClass."""
import math


class MagicClass:
    """Represenst a circle module."""

    def __init__(self, radius=0):
        """Initialize a MagicClass with radius 0.

        Arg:
            radius (float or int): Is the radius of the new MagicClass.
        """

        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """Returns the area of the _MagicClass."""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """Returns the circumference of the _MagicClass."""
        return 2 * math.pi * self._MagicClass__radius
