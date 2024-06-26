#!/usr/bin/python3
"""This is for rectangle """


class Rectangle:
    """ This is a rectangle class"""
    number_of_instances = 0
    print_symbol = "#"
    def __init__(self, width=0, height=0):
        """This method initializes its properties"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """this is my width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """This is my width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """this is my height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """This is my height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """This static method returns the biggest Rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 >= area_2:
            return rect_1
        if area_2 >= area_1:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(width=size, height=size)

    def area(self):
        """this returns a area"""
        return self.__width * self.__height

    def perimeter(self):
        """This returns the perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width)* 2

    def __str__(self):
        """This is the string for rectangle"""
        string = ""
        if self.width > 0 and self.height > 0:
            for row in range(self.height):
                for col in range(self.width):
                    string += '#'
                if row < self.height - 1:
                    string += '\n'
            return string
        else:
             return string

    def __repr__(self):
        """This method returns string of new object"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """This prints a custom message when deleting an instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
