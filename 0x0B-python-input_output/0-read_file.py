#!/usr/bin/python3
"""
    Read File Module
"""


def read_file(filename=""):
    """reads a text file and prints it"""

    with open(filename) as f:
        read_file = f.read()
        print(read_file, end="")
