#!/usr/bin/python3
"""Defines a JSON-to-object function."""

import json


def from_json_string(my_str):
    """Return the an object (python Data Structure)
    represented by a JSON string.

    Args:
        my_str: JSON string to represent

    Returns: Object
    """
    return json.loads(my_str)
