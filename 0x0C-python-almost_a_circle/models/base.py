#!/usr/bin/python3
"""creating a class called Base"""


class Base:
    """class base class with an init metod and private instance"""
    __nb_objects = 0
    def __init__(self, id=None):
        """Initializing the instance id of the class"""
        self.id = id
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
