#!/usr/bin/python3
# 7-add_item.py
"""script that adds all arguments to a Python list"""
import sys

if __name__ == "__main__":
    load_from_json_file = \
            __import__('6-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    # Load existing items from file if it exist, if not create new
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    # Add command line arguments to the list
    items.extend(sys.argv[1:])

    # Save the updated list to the file
    save_to_json_file(items, "add_item.json")
