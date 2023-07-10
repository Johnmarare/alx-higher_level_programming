#!/usr/bin/python3
# 101-add_attribute.py
"""adds a new atrribute if its possible"""


def add_attribute(obj, attribute, value):
    """Adds a new attribute to an object if possible"""
    if not hasattr(obj, '__dict__') or hasattr(type(obj), '__slots__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
