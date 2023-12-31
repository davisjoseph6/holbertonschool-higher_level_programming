#!/usr/bin/python3
"""Define a Square class that inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class, a subclass of Rectangle"""

    def __init__(self, size):
        """Initialize a Square with a given size."""
        self.integer_validator("size", size)
        super().__init__(size, size)  # Call the constructor of the parent

        def area(self):
            """Calculate the area of the sqaure."""
            return self.__width * self.__height

        def __str__(self):
            """Return a string representation of the Square."""
            return "[Square] {}/{}".format(self.__width, self.__height)
