#!/usr/bin/python3
"""This function prints a square wuth #"""


def print_square(size):
    """This checks before it returns a square"""
    if not(isinstance(size,(int, float))):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for _ in range(size):
        print("#" * size)
