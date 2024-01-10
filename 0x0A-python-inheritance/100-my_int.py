#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Represents a new instance of class MyInt.

    Args:
        value(int): integer
    """

    def __eq__(self, value):
        """method to equal is override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """method to override != operator with == behavior."""
        return self.real == value
