#!/usr/bin/python3
"""function that returns the dictionary description with
simple data structure for JSON serialization
of an object"""


import json


def class_to_json(obj):
    """serializing object called obj"""
    return json.dumps(obj)
