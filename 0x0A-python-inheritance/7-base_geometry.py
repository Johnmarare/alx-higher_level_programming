#!/usr/bin/python3
# 7-base_geometry.py
"""Class BaseGeo integer validator"""


class BaseGeometry:
    """Integer validator"""

    def __init__(self):
        """Initializes class"""
        pass

    def area(self):
        """area function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer validator function"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
