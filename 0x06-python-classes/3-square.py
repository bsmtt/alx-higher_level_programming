#!/usr/bin/python3
"""Class Square"""


class Square:
    """
    defines properties of square.

    Attributes:
        size: len of a square.
    """
    def __init__(self, size=0):
        """Creates new instances of square.

        Args:
            size: len of the square .
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area of square.

        Returns: the current square area.
        """
        return self.__size ** 2
