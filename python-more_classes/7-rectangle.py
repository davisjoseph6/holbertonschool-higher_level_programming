#!/usr/bin/python3
"""
This module defines an rectangle class.
"""


class Rectangle:
    """
    Class attribute to keep track of the number of instances
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height) if self.width > 0 and self.height > 0 else 0

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        return str(self.print_symbol) * self.width + "\n" + \
                (str(self.print_symbol) * self.width + "\n") * (self.height -1) + \
                str(self.print_symbol) * self.width

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
