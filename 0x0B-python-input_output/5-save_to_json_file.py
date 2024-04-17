#!/usr/bin/python3
""" writes an Object to a text file, using
a JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """Function that saves objects to a file using
    JSON representation.
    Args:
        my_obj: object of any data type hierachy that
                is to be saved
        filename: file to save the dat"""
    with open(filename, "w") as f:
        return json.dump(x, f)
