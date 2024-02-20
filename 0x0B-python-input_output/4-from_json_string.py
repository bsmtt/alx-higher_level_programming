#!/usr/bin/python3
"""
    Fro JSON Module
"""

import json


def from_json_string(my_str):
    """returns the Object represented by an JSON"""
    return json.loads(my_str)
