#!/usr/bin/python3
"""Writing string to a textfile"""


def write_file(filename="", text=""):
    """function that writes string to a textfile
    args:
        filename (string): name of file
        text (string): contents to be written to a file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
