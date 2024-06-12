#!/usr/bin/python3
"""Defining a class called square with property
getters and setters"""


class Square:
    """Initializing instances of the class square
    with private size and private position)"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) and value < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        return (self.__size * self.__size)

    def __str__(self):
        if self.__size == 0:
            return ""
        else:
            return ("#" * self.__size for i in range(self.__size))
        if self.__position[1] > 0:
            return " "
        else:
            return (" " * self.position[1] for i in range(self.__position[1]))

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
        if self.__position[1] > 0:
            print(" ")
        else:
            for i in range(self.__position[1]):
                print(" " * self.__position[1])
