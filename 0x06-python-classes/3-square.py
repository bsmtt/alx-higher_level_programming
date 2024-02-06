#!/usr/bin/python3
""" Defines Square Class """


class Square:
    """
        Defines class Attributes
    """
    def __init__(self, size):
        """
            Creates new instances of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
            Calculates the area of square.

            Returns: the current square area.
        """
        return self.__size ** 2
