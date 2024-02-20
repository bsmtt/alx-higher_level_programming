#!/usr/bin/python3
"""Module for saving to json"""
import json
import os.path
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

my_list = []

if os.path.exists("add_item.json"):
    my_list = load_from_json_file("add_item.json")

for index in argv[1:]:
    my_list.append(index)

save_to_json_file(my_list, "add_item.json")
