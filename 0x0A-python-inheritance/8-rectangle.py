#!/usr/bin/python3
# 8-rectangle.py
"""class Rectangle inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Childclass of BaseGeometry"""

    def __init__(self, width, height):
        """Initialization of rec"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
