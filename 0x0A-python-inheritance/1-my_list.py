#!/usr/bin/python3
"""Refresents class MyList that inherits from list."""


class MyList(list):
    """class that inherits from  list class."""

    def print_sorted(self):
        """Print a list and MyList in sorted ascending order."""

        print(sorted(self))
