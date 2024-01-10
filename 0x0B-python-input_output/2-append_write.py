#!/usr/bin/python3
"""Defines a appending to file  function."""


def append_write(filename="", text=""):
    """Appends a str to the end of a utf8 file

    Args:
        text (str): string to append file to
        filename (str): Name of the file to append to.
    Returns:
        The num of char to append."""

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
