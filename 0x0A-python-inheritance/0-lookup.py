#!/usr/bin/python3
"""An empty class that defines an object look-up function."""


def lookup(obj):
    """Function returns a list of an object's available attributes."""
    return (dir(obj))
