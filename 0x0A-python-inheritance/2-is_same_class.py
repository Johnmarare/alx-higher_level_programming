#!/usr/bin/python3
# 2-is_same_class.py
"""function that returns True if the
object is exactly an instance of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """True if is instance of class
    Args:
        obj (any): The object to check
        a_class (type): the class to match the type
    Returns:
        true if is instace of class
        else false.
    """
    if type(obj) == a_class:
        return True
    return False
