#!/usr/bin/python3
# 4-from_json_string.py
"""function that returns an object (python D/S)represented by a JSON string"""


import json


def from_json_string(my_str):
    """Converts a JSON string to a python string
    Args:
        my_str (str): JSON string
    Return:
        object represented i python data structure
    """
    return (json.loads(my_str))
