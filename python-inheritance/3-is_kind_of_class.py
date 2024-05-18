#!/usr/bin/python3
"""This returns bool for if a object is inherited"""


def is_a_kind_of_class(obj, a_class):
    """THis will return my bool"""
    if type(obj) is a_class:
        return (type(obj) is a_class)
