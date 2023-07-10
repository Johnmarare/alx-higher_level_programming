#!/usr/bin/python3
# 1-my_list.py
"""Class that shows inheritance"""


class MyList(list):
    """implement sorted printing for the builtin list class."""

    def print_sorted(self):
        """Print a list in sorted assending order"""
        print(sorted(self))
