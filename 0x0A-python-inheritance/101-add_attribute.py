#!/usr/bin/python3
# 101-add_attribute.py
"""adds a new atrribute if its possible"""


def add_attribute(obj, attribute, value):
    """Adds a new attribute to an object if possible"""
    if hasattr(obj, '__dict__') or hasattr(type(obj), '__slots__'):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
