#!/usr/bin/python3
"""
This module represents a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
"""
class Rectangle:
    """
    This class represents a rectangle.
    """


    def __init__(self, width=0, height=0):
        """
        Initialize a rectangle with the given width and height
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Retrieve the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Seth the width of the rectangle with validation.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieve the height of the ractnagle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the width of the rectangle with validation.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


if __name__ == "__main__":
    my_rectangle = Rectangle(4, 2)
    print(my_rectangle.__dict__)

    my_rectangle.height = 10
    my_rectangle.width = 3
    print(my_rectangle.__dict__)
