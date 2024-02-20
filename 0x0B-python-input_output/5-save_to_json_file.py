#!/usr/bin/python3
"""
    Save To File Module
"""


import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file """

    with open(filename, 'w') as f:
        return f.write(json.dumps(my_obj))
