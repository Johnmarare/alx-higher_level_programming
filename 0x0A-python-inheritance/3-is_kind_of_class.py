#!/usr/bin/python3
# 3-is_kind_of_class.py
"""Saame class or inherit from"""


def is_kind_of_class(obj, a_class):
    """Object is an instance of
    Args:
        obj (any): object to check
        a_class (type): class / subclass to check
    Return:
        True if is instance of
        else False
    """
    if isinstance(obj, a_class):
        return True
    return False
