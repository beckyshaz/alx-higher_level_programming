#!/usr/bin/python3
import json
"""serializing an object using json)"""


def to_json_string(my_obj):
    """ function that uses json to change any object into
    a string.
    Args:
        my_obj :object to change to string"""
    return json.dumps(my_obj)
