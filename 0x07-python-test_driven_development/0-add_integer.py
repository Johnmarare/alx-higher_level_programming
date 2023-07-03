#!/usr/bin/python3
# add_integer
"""Defines an addition function"""


def add_integer(a, b=98):
    """Function that adds two integers

        Args:
            a (int/float): first number
            b (int/float): second number. if no argument given b = 98.
        Raise:
            TypeError: a or b must be an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return (int(a + b))
