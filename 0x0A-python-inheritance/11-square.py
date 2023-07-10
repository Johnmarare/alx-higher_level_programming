#!/usr/bin/python3
# 11-square.py
"""class square inheriting from rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square is a ractangle subclass"""

    def __init__(self, size):
        """Initialization"""
        self.integer_validator("size", size)

        self.__size = size
        super().__init__(size, size)

    def area(self):
        """calculates area of square"""
        return (self.__size * self.__size)

    def __str__(self):
        """square description"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
