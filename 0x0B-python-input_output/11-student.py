#!/usr/bin/python3
"""Module for  a class Student."""


class Student:
    """ Represents class for  student JSONIFICATION."""

    def __init__(self, first_name, last_name, age):
        """Creates a new Student.

        Args:
            age (int): age of  student.
            first_name (str): first name of student.
            last_name (str): last name of student.
        """

        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of the Student."""

        if (type(attrs) is list and
                all(type(x) is str for x in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}

        return self.__dict__

    def reload_from_json(self, json):
        """Replace attributes of Student."""

        for k, j in json.items():
            setattr(self, k, j)
