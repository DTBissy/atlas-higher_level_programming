#!/usr/bin/python3
"""My class"""


class Square:
    """Square"""
    def __init__(self, size=0, position=(0, 0)):
        """My private size"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """My size getter """
        return self.__size

    @property
    def position(self):
        """My property getter"""
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value)!= 2 or not all(isinstance(i, int)
        and i > 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")
            return
        for i in range(0, self.__position[1]):
            print()
        for _ in range(0, self.__size):
            print(' ' * self.__position[0], end='')
            print('#' * self.__size)
