#!/usr/bin/python3
# 0-read_file.py
"""function that reads a text file"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdou"""
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
