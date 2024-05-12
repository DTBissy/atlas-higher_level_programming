#!/usr/bin/python3
"""This a function that returns the sum of two integers
    """


def add_integer(a, b=98):
    """The sum of two integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be a integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return a + b
