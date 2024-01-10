#!/usr/bin/python3
"""module that represents a class-checking function."""


def is_same_class(obj, a_class):
    """Check if object is the exact instance of a given class"""

    if type(obj) == a_class:
        return True
    return False
