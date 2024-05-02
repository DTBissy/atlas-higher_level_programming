#!/usr/bin/python3
def uppercase(str):
    result = ''
    for char in str:
        if 'a' <= ord(chr) <= 'z':
            result = "{:c}".format(ord(char) - 32)
        else:
            result += char
    print(result)
