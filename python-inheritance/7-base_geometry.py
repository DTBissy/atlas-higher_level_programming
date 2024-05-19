#!/usr/bin/python3
"""Emoty Class for geom"""


class BaseGeometry:
    """This will be my class methods and attributes"""
    def area(self):
        """The area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This will raise errors if not valid int"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))