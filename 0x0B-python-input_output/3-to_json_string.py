#!/usr/bin/python3
"""Defines the string-to-JSON function."""

import json


def to_json_string(my_obj):
    """Returns the JSON representation of a string object.

    Args:
        my_obj: string to be represented

    Returns: JSON Representation."""
    return json.dumps(my_obj)
