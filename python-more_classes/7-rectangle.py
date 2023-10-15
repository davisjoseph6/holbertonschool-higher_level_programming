#!/usr/bin/python3
""" Real definition of a rectangle"""


class Rectangle:
    """ Rectangle that defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"
    
    def _init_(self, width=0, height=0):
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
        return (self._width * self._height)
    
    def perimeter(self):
        """that returns the rectangle perimeter"""
        if self._width == 0 or self._height == 0:
            return 0
        return ((self._width * 2) + (self._height * 2))
    
    def _str_(self):
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
    
    def _repr_(self):
        heightR = self.__height
        widthR = self.__width
        return ("Rectangle({}, {})".format(widthR, heightR))
    
    def _del_(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
