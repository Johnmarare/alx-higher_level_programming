#!/usr/bin/python3
# 0-lookup.py
"""Defines an object attribute lookup function"""


def lookup(obj):
    """Function that returns list of available atributes
    and methods of an object.
    we can make use of the built-in dir() function.
    Returns a list of all the valid attributes and methods of an object.
    """
    return (dir(obj))
