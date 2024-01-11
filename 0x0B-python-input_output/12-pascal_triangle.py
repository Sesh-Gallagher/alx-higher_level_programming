#!/usr/bin/python3
"""Module for  Pascal's Triangle function."""


def pascal_triangle(n):
    """Defines Pascal's Triangle of size i. """

    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        tri = triangle[-1]
        tmp = [1]
        for x in range(len(tri) - 1):
            tmp.append(tri[x] + tri[x + 1])
        tmp.append(1)
        triangle.append(tmp)

    return (triangle)
