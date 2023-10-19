#!/usr/bin/python3
""" defines a class with public instance method area"""
class BaseGeometry:
    """ class named BaseGeometry with public instance method """
    def area(self):
        """ raise an exception is the class is empty """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ checks if the value is an integer """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
