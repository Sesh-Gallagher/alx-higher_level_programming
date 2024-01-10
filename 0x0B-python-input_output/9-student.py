#!/usr/bin/python3
"""Module for class Student."""


class Student:
    """Represent a class student that defines a student
    by attribute."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            age (int): age of student
            last_name (str): last name of student.
            first_name (str): first name of student.
        """

        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self):
        """Returns a dictionary representation of a Student."""

        return self.__dict__
