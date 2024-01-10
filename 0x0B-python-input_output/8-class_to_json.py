#!/usr/bin/python3
"""
Defines a Python class_to_json method."""


def class_to_json(obj):
    """Returns dictionary representation with simple data structure."""

    return obj.__dict__
