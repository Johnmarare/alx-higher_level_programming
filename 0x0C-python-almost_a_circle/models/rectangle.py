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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter of x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter of the x attribute"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for the y attribute"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle"""
        return (self.__height * self.__width)

    def display(self):
        """prints in stdout the Rectangle instance with charcter #"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """"custom string representation for Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
