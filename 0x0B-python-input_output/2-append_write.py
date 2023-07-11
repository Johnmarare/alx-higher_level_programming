#!/usr/bin/python3
# 2-append_write.py
"""Append to a file"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file
    Args:
        filename (str): file
        text (str): file contents
    Returns:
        Number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        f.write(text)

        num_chars = len(text)
        return (num_chars)
