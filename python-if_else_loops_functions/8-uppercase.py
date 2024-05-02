#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if char not in(65, 90):
            char = chr(ord(char) + 32)
        print("{}".format(char), end="")
    print("")