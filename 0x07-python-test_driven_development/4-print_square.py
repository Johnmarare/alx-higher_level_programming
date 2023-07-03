#!/usr/bin/python3
# 4-print_square.py
"""Defines a square-printing function."""


def print_square(size):
    """Print a square with the # character

    Args:
        size (int): The Length of square
    Raises:
        TypeError: If size is not of type int
        ValueError: if size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print("")
