#!/usr/bin/python3
# 10-square.py
"""Class square inheriting from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square inheriting from rectangle"""

    def __init__(self, size):
        """Initialization of the square"""
        self.integer_validator('size', size)

        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Implementation of area method"""
        return (self.__size * self.__size)
