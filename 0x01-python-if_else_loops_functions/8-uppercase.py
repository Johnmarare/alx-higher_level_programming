#!/usr/bin/python3


def islower(c):
    val = ord(c)
    return val >= 97 and val <= 122


def uppercase(str):
    for letter in str:
        print("{:c}".format(
            ord(letter) - 32 if islower(letter) else ord(letter)), end='')

    print()
