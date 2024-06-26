#!/usr/bin/python3
"""Defining a rectangle
class"""


class Rectangle:
    """Defining a class called
    rectangle"""
    def __init__(self, width=0, height=0):
        """Initialising instance attributes
        Args:
            width (int):width of the rectangle
            height (int):height of the rectangle"""

        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        p = 2 * (self.width + self.height)
        if self.width == 0 or self.height == 0:
            p = 0
        return p
