#!/usr/bin/python3
"""Defines a text read file function."""


def read_file(filename=""):
    """Function that reads and print the contents of a UTF8 text file."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
