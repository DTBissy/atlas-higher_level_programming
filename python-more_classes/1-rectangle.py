#!/usr/bin/python3
"""This is for rectangle """


class Rectangle:
    """ This is a rectangle class"""
    def __init__(self, width=0, height=0):
        """This method initializes its properties"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise TypeError("width must be >= 0")
        self.__widthwidth = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise TypeError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """this is my width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """This is my width setter"""
        if not isinstance(value, int):
            raise ValueError("width must be an integer")
        elif value < 0:
            raise ValueError("widht must be >= 0")

    @property
    def height(self):
        """this is my height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """This is my height setter"""
        if not isinstance(value, int):
            raise ValueError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
