#!/usr/bin/python3
"""
    Define a class called lockedclass
"""


class LockedClass:
    """
        Defining a class that restricts the user from creating
        instances attribute
        apart from first_name
    """
    __slots__ = ['first_name']
