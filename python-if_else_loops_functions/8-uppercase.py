#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if char not in(97, 123) and char not in(60, 95) :
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")