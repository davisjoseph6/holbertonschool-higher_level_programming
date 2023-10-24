#!/usr/bin/python3
""" Rectangle Module """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
