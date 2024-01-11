#!/usr/bin/python3
"""Module for  a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """text to be inserted after each line containing a string."""

    text = ""

    with open(filename) as o:
        for line in o:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
