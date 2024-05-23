#!/usr/bin/python3
"""This is the rectangle that will inherit
from class Base"""
from models.base import *


class Rectangle(Base):
    """This is my Rectangle class and it inherits from my 'Base' class
    and i use super(id) to pull in the __init__ method of that class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

        super().__init__(id)

    @property
    def width(self):
        """This is my width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """THis is my width setter"""
        if not isinstance(value, int):
            raise TypeError("Must be an int")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """This is my height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """THis is my height setter"""
        if not isinstance(value, int):
            raise TypeError("Must be an int")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """This is my x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """THis is my x setter"""
        if not isinstance(value, int):
            raise TypeError("Must be an int")
        if value <= 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """This is my y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """THis is my y setter"""
        if not isinstance(value, int):
            raise TypeError("Must be an int")
        if value <= 0:
            raise ValueError("y must be >= 0")
        self.__y = value
