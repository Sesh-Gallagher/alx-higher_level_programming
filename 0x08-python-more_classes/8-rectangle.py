#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """An empty class represent a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):

        """Initializes the new Rectangle."""

        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):

        """Get width of rectangle."""
        return self.__width

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):

        """Get height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):

        """calculate the area of a rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):

        """calculate the perimeter of a rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):

        """calculates rectangle with the greater area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):

        """Represent the rectangle with the # character."""
        if self.__width == 0 or self.__height == 0:
            return ""

        ret = []
        for i in range(self.__height):
            [ret.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                ret.append("\n")
        return ("".join(ret))

    def __repr__(self):

        """string representation of the rectangle."""
        ret = "Rectangle(" + str(self.__width)
        ret += ", " + str(self.__height) + ")"
        return (ret)

    def __del__(self):

        """Print message for deletion of every rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
