#!/usr/bin/python3
"""Reading a file"""


def read_file(filename=""):
    """Reading from a file and printing to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
