#!/usr/bin/python3
"""Defining a class that raises exception"""


class BaseGeometry:
    """class has one method that it uses to raise
    exception"""
    def area(self):
        raise Exception("area() is not implemented")
