#!/usr/bin/python3
"""Module of class MyInt that inherits from int."""


class MyInt(int):
    """Represents a new instance of class MyInt."""

    def __eq__(self, value):
        """function to equal is override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Function to override != operator with == behavior."""

        return self.real == value
