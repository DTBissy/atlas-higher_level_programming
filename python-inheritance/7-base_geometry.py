#!/usr/bin/python3
"""Emoty Class for geom"""


class BaseGeometry:
    """This will be my class methods and attributes"""
    def area(self):
        """The area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This will raise errors if not valid int"""
        self.name = name
        self.value = value
        if not isinstance(value, int):
            raise TypeError(f"{self.name} must be an integer")
        if value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")