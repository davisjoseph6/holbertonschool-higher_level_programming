#!/usr/bin/python3
""" first class base """
class Base:
    """ base class """
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
class Rectangle(Base):
    """ child class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the Rectangle class.
        Args:
        width: Width of the rectangle.
        height: Height of the rectangle.
        x: X-coordinate of the rectangle's position (default is 0).
        y: Y-coordinate of the rectangle's position (default is 0).
        id:optional identifier.If not provided,a unique id will be assigned.
        constructor of the parent cls(Base)called using super().__init__(id).
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
