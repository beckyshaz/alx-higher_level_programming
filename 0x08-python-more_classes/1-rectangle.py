#!/usr/bin/python3
"""Defining a class called
rectangle"""


class Rectangle:
    """
        Represents a rectangle
    """
    def __init__(self, width=0, height=0):
        """
            Initializing attributes of instances
            Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
            Defining a getter to retrive values of attributes
            and a setter to set it
        """
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
        """
            Defining a getter to retrive values of attributes
            and a setter to set it
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
