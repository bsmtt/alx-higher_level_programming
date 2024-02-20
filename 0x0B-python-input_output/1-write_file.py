#!/usr/bin/python3
"""
    Write File Module
"""


def write_file(filename="", text=""):
    """writes a string to a text file and return the number of lines"""

    with open(filename, 'w') as f:
        return f.write(text)
