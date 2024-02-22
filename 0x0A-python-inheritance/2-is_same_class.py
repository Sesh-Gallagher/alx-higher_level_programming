#!/usr/bin/python3
"""Defines an module that represents a class-checking function."""


def is_same_class(obj, a_class):
    """Returns true if object is the exact instance of a specified class"""
    if type(obj) == a_class:
        return True
    return False
