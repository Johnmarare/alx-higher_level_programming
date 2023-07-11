#!/usr/bin/python3
# 3-to_json_string.py
""""JSON representation of an oblect(string)"""


import json


def to_json_string(my_obj):
    """function that returns the JSON representation of an object (string)
    Args:
        my_obj (str): object
    Return:
        JSON representation
    """
    return (json.dumps(my_obj))
