#!/usr/bin/python3
"""Defines a JSON file reading function."""

import json


def load_from_json_file(filename):
    """Loads a Python object from a JSON file.
    Args:
        filename: name of file to be loaded."""

    with open(filename, "r") as f:
        my_obj = json.load(f)
        return my_obj
