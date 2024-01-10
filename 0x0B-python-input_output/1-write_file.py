#!/usr/bin/python3
"""Defines a function that writes to file."""


def write_file(filename="", text=""):
    """function that can write a str to a UTF8 text file."""

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
