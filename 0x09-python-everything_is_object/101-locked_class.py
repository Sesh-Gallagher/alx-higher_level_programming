#!/usr/bin/python3
""" Represents a lockedClass module """

class LockedClass:

    """ Prevents user from instantiating new LockedClass attr"""

    __slots__ = ["first_name"]
