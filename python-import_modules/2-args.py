#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
  num = len(argv)

  if num < 2:
      print("0 arguments.")

  if num == 2:
      print("1 argument:")
      print("1: {}".format(argv[1]))
  else:
      print("{} arguments:".format(num - 1))
      for i in range(2, num):
          print("{}: {}".format(i, argv[i]))
