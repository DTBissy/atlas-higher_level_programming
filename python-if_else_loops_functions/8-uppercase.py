#!/usr/bin/python3
def uppercase(str):
    result = print("{}".format(char), end="")
    for char in str:
        if 97 <= ord(str) <= 122:
            result += chr(ord(char) - 32)
        else:
            result += char
    print(result)
