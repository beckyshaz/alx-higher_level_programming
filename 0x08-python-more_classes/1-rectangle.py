#!/usr/bin/python3
"""
    Defining a class called rectangle
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """
            Initializing attributes of instances
            Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
            Defining a getter to retrive values of attributes
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Defining a seeter to set or change values of attributes
            Args:
                value (int): Values of width and height
        """
        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        elif self.__width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
            Defining a getter to retrive values of attributes
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            Defining a seeter to set or change values of attributes
            Args:
                value (int): Values of width and height
        """
        if not isinstance(self.__height, int):
            raise TypeError("height must be an integer")
        elif self.__height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
