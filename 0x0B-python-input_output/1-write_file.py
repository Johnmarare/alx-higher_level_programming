#!/usr/bin/python3
# 1-write_file.py
"""write to a file"""


def write_file(filename="", text=""):
    """function that writes a string to a text file
    Args:
        filename (str): The file
        text (str): text to be written
    Returns:
        Number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)

        num_chars = len(text)
        return (num_chars)
