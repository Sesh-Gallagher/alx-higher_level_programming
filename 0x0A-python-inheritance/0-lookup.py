#!/usr/bin/python3
"""Defines an object lookup up function."""


def lookup(obj):
    """Function that returns a list of an object's available attributes."""

    return (dir(obj))
