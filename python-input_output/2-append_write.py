#!/usr/bin/python3
"""This will append to the end of a string"""


def append_write(filename="", text=""):
    """THis will append a string"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
