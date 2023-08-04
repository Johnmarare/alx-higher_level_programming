#!/usr/bin/python3
"""Class Rectangle inheriting from Base"""

from models.base import Base


class Rectangle(Base):
    """
    A child class of class Base.
    Definition: This is a class defining a rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Args:
            width (int): the width of our rectangle
            height (int): the height of our rectangle
            x:
            y:
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)  # calls the superclass with init logic

        @property
        def width(self):
            """getter for the attribute"""
            return self.__width

        @width.setter
        def width(self, value):
            """setter of the attribute"""
            if not isinstance(int, value):
                raise TypeError("Width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            """getter of the height attribute"""
            return self.__height

        @height.setter
        def height(self, value):
            """setter for the height attribute"""
            if not isinstance(int, value):
                raise TypeError("Height must be an integer")
            if value <= 0:
                raise ValueError("Height must be > 0")
            self.__height = value

        @property
        def x(self):
            """getter of x attribute"""
            return self.__x

        @x.setter
        def x(self, value):
            """setter of the x attribute"""
            if not isinstance(int, value):
                raise TypeError("x must be an integer")
            if value <= 0:
                raise ValueError("x must be > 0")
            self.__x = value

        @property
        def y(self):
            """getter for the y attribute"""
            return self.__y

        @y.setter
        def y(self, value):
            """setter for the y attribute"""
            if not isinstance(int, value):
                raise TypeError("y must be an integer")
            if y <= 0:
                raise ValueError("y must be > 0")
            self.__y = value
