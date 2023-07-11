#!/usr/bin/python3
# 6-load_from_json_file.py
"""Create object from JSON file"""


import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”
    Args:
        filename (str): File
    Returns:
        The loaded object from JSON file.
    """
    with open(filename, mode="r+", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return (data)
