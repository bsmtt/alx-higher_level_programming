#!/usr/bin/python3
""" Defines Square Class """


class Square:
    """Defines class Attributes
        Attributes:
            size: size of a square (1 side).
    """
    def __init__(self, size):
        """Creates new instances of square

            Args:
                size: length of side.
            Raises:
                TypeError: size integer.
                ValueError: size > 0.
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
