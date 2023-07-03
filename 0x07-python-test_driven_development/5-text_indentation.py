#!/usr/bin/python3
# 5-text_indentation.py
"""Defines a text indentation function"""


def text_indentation(text):
    """print text with two new lines after these punc marks '.', '?' and ':'.

    Args:
        text (string): The text to be printed.
    Raises:
        TypeError: if text is not string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    new_string = ""
    punctuation_marks = (".", "?", ":")

    for char in text:
        new_string += char
        if char in punctuation_marks:
            new_string += "\n\n"

    lines = new_string.split("\n")
    formated_text = "\n".join(line.strip() for line in lines)

    print(formated_text)
