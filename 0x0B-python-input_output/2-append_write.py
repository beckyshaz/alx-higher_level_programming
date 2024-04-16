#!/usr/bin/python3
"""Appending to a file"""


def append_write(filename="", text=""):
    """Function that appends content to a file
    Args:
        filename (string): name of file to append to
        text (string): contents to append to a file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
