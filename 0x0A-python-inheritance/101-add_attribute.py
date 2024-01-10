#!/usr/bin/python3
"""Defines a function that adds attributes."""


def add_attribute(obj, att, value):
    """Adds a new attribute to an object if possible.

    Args:
        object (any): object to add an attribute to.
        att (str): name of the attribute to add to object.
        value (any): The value of attribute.

    Raises:
        TypeError: If the attribute cannot be added.
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
