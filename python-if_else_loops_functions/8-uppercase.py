#!/usr/bin/python3
def uppercase(str):
    for char in str:
        print("{}".format(chr(ord(char) - 32) if 96 <= ord(
        char) <= 123 else char), end-"")
        print()