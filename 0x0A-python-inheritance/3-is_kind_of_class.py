#!/usr/bin/python3
"""Module that represents a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Checks if the object is an instance or
    if inherited instance of a class. """

    if isinstance(obj, a_class):
        return True
    return False
