#!/usr/bin/python3
# 5-save_to_json_file.py
"""Write an object to a text file using JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """ function that writes an Object(textfile)using a JSON representation
    Args:
        my_obj (any): object
        filename (str): file
    """
    with open(filename, mode="w", encoding="utf-8") as json_file:
        json.dump(my_obj, json_file)
