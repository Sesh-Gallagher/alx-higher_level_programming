#!/usr/bin/python3
"""Defines a function for the addition of integers."""


def add_integer(a, b=98):
    """Returns the integer addition of a and b.

    args:

    int a: first number
    int b: second number

    Returns:
        The sum of two given integers

    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: If either of a or b are not  non-integer and non-float.
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return (int(a) + int(b))
