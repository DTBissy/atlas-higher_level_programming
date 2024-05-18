#!/usr/bin/python3
"""This returns bool if its a subclass"""


def inherits_from(obj, a_class):
    """THis checks if item is a subclass"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
