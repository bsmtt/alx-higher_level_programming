#!/usr/bin/python3
"""
    Append Module
"""


def append_write(filename="", text=""):
    """appends a string at the end of a file and return the number"""

    with open(filename, 'a') as f:
        return f.write(text)
