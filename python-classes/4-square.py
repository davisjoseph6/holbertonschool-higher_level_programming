#!/usr/bin/python3

class Square:
    """
    This class represents a square with a given size.
    """

    def __init__(self, size=0):
        """
        Initializes a Square object with a specified size.

        :param size: The size of the square (default is 0).
        :type size: int
        """
        self.__size = size

    @property
    def size(self):
        """
        Get the size of the square.

        :return: The size of the square.
        :rtype: int
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        :param value: The new size to set.
        :type value: int
        :raises TypeError: If the value is not an integer.
        :raises ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        :return: The area of the square.
        :rtype: int
        """
        return self.__size ** 2

