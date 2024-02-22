#!/usr/bin/python3
"""Module that defines a base class BaseGeometry."""


class BaseGeometry:
    """Represents base geometry class."""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the parameter as int."""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
