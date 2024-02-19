#!/usr/bin/python3
"""
    My List Module
"""


class MyList(list):
    """ sort list """

    def print_sorted(self):
        print(sorted(list(self)))
