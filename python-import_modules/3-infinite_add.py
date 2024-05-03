#!/usr/bin/python3
from sys import argv
if __name__ =="__main__":
    num = len(argv)
    res = 0
    for i in range(1, num):
        res += int(argv[i])
print(res)
