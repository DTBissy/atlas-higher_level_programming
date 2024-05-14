#!/usr/bin/python3
"""This this should test for max integers"""


def text_indentation(text):
    if not(isinstance(text, str)):
        raise TypeError("text must be a string")
    new_line = True
    for char in text:
        if char == ' ' and new_line:
            continue
        elif char in ['.', '?', ':']:
            print()
            print()
            new_line = True
        else:
            print(char, end="")
            new_line = False
