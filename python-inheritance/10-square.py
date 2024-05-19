#!/usr/bin/python3
"""This is a square that inherits from a thing"""


Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):
    """This will be the square class"""

    def __init__(self, size):
        """This is for square methods and attributes
        And super overwrites the original classes __init__ method
        with our new one for
        the new class. But behaves the same"""
        self.integer_validator("size", size)
        super().__init__(size, size)

        self.__size = size

    def area(self):
        return self.__size**2
