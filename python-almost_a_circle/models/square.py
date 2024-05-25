#!/usr/bin/python3
"""This is the rectangle that will inherit
from class Base"""
from models.base import *
from models.rectangle import *


class Square(Rectangle):
    """This my Square class which inherits from Rectangle and
    uses super to initialize the attritbutes from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return f"[Square] {self.id} {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """THis is my size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """THis is my width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """This will update arguments to the class"""
        args_len = len(args)
        if args_len >= 1:
            self.id = args[0]
        if args_len >= 2:
            self.size = args[1]
        if args_len >= 3:
            self.x = args[2]
        if args_len >= 4:
            self.y = args[3]

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """This method returns the dictionary representation of a Rectangle"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y,
        }