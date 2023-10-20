#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """Initialize a Square with a given size."""
        self.integer_validator("size", size)
        self.__width = size  # Set the width of the square
        self.__height = size  # Set the height of the square

    def area(self):
        """Calculate the area of the sqaure."""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the Square."""
        return "[Square] {}/{}".format(self.__width, self.__height)
