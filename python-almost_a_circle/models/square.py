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
        return f"[Square] {self.id} {self.x}/{self.y}"