#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if char not in(96, 123):
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    else:
      print("{}".format(char), end="")