#!/usr/bin/python3
"""Desirializing an object int a json file"""


import json


def load_from_json_file(filename):
    """function that desirializing an object into a json file"""
    with open(filename, "r") as f:
        j = json.load(f)
        return j
