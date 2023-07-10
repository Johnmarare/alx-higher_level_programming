#!/usr/bin/python3
# 4-inherits_from.py
"""Only subclass of"""


def inherits_from(obj, a_class):
    """Checks if object is an instance of a class
    that inherited deirectly or indirectly
    Args:
        obj (any): object to be checked
        a_class (type): class to check from
    Return:
        True if is instance
        else False.
        #return issubclass(type(obj), a_class)
    """
    if issubclass(type(obj), a_class):
        return True
    return False
