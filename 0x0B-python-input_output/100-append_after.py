#!/usr/bin/python3
# 100-append_after.py
"""inserts line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file
    Args:
        filename (str): file to insert text
        search_string (str): specifc string
        new_string (str): string to insert
    """
    text = ""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            text = text + line
            if search_string in line:
                text += new_string
    with open(filename, mode="w", encoding="utf-8") as new:
        new.write(text)
