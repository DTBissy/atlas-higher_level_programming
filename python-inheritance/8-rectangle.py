#!/usr/bin/python3
"""Im gonna do it. IM GONNA IMPORT"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This is a rectangle thats inherting
    BaseGeometrys class attributes"""

    def __init__(self, width, height):
        """Woooww Didint know about this"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
