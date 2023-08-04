#!/usr/bin/python3
"""Base of all other classes in the project"""


class Base:
    """Base of all classes in the project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Args:
            id (int): id attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
