#!/usr/bin/python3


def remove_char_at(str, n):
    """create a copy of string without charater pos n."""
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
