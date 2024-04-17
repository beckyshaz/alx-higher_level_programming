#!/usr/bin/python3
"""function that returns the dictionary description with
simple data structure for JSON serialization
of an object"""


def class_to_json(obj):
    """serializing object called obj"""
    if isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}
    elif isinstance(obj, (list, tuple)):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, (str, int, bool)):
        return obj
    else:
        return str(obj)
