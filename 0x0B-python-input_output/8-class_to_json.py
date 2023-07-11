#!/usr/bin/python3
# 8-class_to_json.py
"""dictionary description with simple data structure"""


def class_to_json(obj):
    """function that returns the dictionary description
    with simple data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    Args:
        obj (any): instance of a Class
    Return:
        Dictionary description
    """
    return (obj.__dict__)
