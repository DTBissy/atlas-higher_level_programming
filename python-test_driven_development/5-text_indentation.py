#!/usr/bin/python3
"""This this should test for max integers"""


def text_indentation(text):
    """ this returns a indented text after checking edge cases"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    new_line = True
    for char in text:
        if char != ' ' or new_line is False:
            print(char, end="")
            new_line = False
        elif char != ' ':
            new_line = False
        if char in ['.', '?', ':']:
            print()
            print()
            new_line = True
