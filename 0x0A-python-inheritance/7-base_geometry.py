#!/usr/bin/python3
# 7-base_geometry.py
"""Class BaseGeo integer validator"""


class BaseGeometry:
    """Integer validator"""

    def area(self):
        """area function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer validator function"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
