#!/usr/bin/python3
"""Deserializing objects to string using json"""


import json


def from_json_string(my_str):
    """function to deserialize an object using json
    Args:
        my_str (string): string to deserialize"""
    return json.loads(my_str)
