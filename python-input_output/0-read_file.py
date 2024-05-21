#!/usr/bin/python3
"""This is gonna read stuff"""


def read_file(filename=""):
    with open (filename) as f:
        for line in f:
            print(line, end="")