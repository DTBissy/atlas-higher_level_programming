#!/usr/bin/python3
"""THis is to return if a object is
exaclty the same as another"""


def is_same_class(obj, a_class):
    """THis returns true or false is a_clas is mathced"""
    if type(obj) == a_class:
        return True
    else:
        return False