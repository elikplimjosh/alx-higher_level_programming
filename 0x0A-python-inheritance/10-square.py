#!/usr/bin/python3
"""Module documentation."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class documentation."""

    def __init__(self, size):
        """Init documentation."""
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Method documentation."""
        return self.__size ** 2

