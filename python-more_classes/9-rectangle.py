#!/usr/bin/python3
""" Real definition of a rectangle"""


class Rectangle:
    """ Rectangle that defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """  that returns the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """that returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """that returns the rectangle with #"""
        heightR = self.__height
        widthR = self.__width
        s = ""
        if heightR == 0 or widthR == 0:
            return s
        else:
            for h in range(heightR):
                for w in range(widthR):
                    s += str(self.print_symbol)
                if h != heightR - 1:
                    s += "\n"
            return s

    def __repr__(self):
        heightR = self.__height
        widthR = self.__width
        return ("Rectangle({}, {})".format(widthR, heightR))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
