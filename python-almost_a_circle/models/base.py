#!/usr/bin/python3
"""This will be my base class for almost_a_circle"""


class Base:
    """This will be Base class ID keeper"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
