#!/usr/bin/python3
"""a class BaseGeometry (based on 5-base_geometry.py)."""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an exception with a message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
