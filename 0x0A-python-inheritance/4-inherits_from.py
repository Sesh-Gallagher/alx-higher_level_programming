#!/usr/bin/python3
"""Module that represents a inherited class-checking function."""


def inherits_from(obj, a_class):
    """ Function that checks if an object is an
    inherited instance of a class"""

  if issubclass(type(obj), a_class) and type(obj) != a_class:
	return True	
  return False
