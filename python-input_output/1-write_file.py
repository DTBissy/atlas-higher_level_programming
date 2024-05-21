#!/usr/bin/python3
"""This will write to files"""


def write_file(filename="", text=""):
    """THis will write and return stuff in the file"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
