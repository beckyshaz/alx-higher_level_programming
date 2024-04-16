#!/usr/bin/python3
"""serializing an object using json)"""


import json


def to_json_string(my_obj):
    """ function that uses json to change any object into
    a string.
    Args:
        my_obj :object to change to string"""
    return json.dumps(my_obj)
