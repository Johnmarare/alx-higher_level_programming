#!/usr/bin/python3
# 2-rectangle.py
"""Defines a rctangle class"""


class Rectangle:
    """Represents a rectangle and various methods."""

    def __init__(self, width=0, height=0):
        """Ïnitializes a rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets the width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height value"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of rectangle (L*W)"""

        return (self.__height * self.__width)

    def perimeter(self):
        """Returns perimeter of ractangle (2(L + w))"""
        if self.__width < 0 or self.__height < 0:
            return 0

        return (2 * (self.__height + self.__width))
