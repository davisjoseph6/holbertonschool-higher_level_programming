#!/usr/bin/python3
"""Base module """

from models.base import Base


class Rectangle(Base):
    """ Rectangle class inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ Get the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width of the rectangle """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Get the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the height of the rectangle """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Get the x-coordinate of the rectangle's position """
        return self.__x

    @x.setter
    def x(self, value):
        """ Set the x-coordinate of the rectangle's position """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Get the y-coordinate of the rectangle's position """
        return self.__y

    @y.setter
    def y(self, value):
        """ Set the y-coordinate of the rectangle's position """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Calculate the area of the rectangle """
        return self.__height * self.__width

    def display(self):
        """ Display the rectangle using '#' characters """
        saima = "\n" * self.__y
        for aicha in range(self.__height):
            saima += " " * self.__x + "#" * self.__width + "\n"
        print(saima, end="")

    def __str__(self):
        """ String representation of the rectangle """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """ Update the attributes of the rectangle """
        if args:
            arg_names = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(arg_names):
                    setattr(self, arg_names[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
