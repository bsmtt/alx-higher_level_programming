#!/usr/bin/python3
"""class Square"""


class Square:
    """
    defines properties of square.

    Attributes:
        size: size of a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Creates new instances .

        Args:
            __size (int): size of the square.
            __position (tuple): position.
        """
        self.size = size
        self.position = position

    def area(self):
        """Calculates the area of square.

        Returns: the current square area.
        """
        return self.__size ** 2

    @property
    def size(self):
        """size of a square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter for size.

        Args:
            value (int): len of a square.

        Raises:
            TypeError:  must be an integer.
            ValueError: must be >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Returns the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ setter for position.

        Args:
            value (tuple): position of the square.

        Raises:
            TypeError: position must be a tuple of 2 positive integers
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints the square with the character #
        """

        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ",  end="")
                print("#" * (self.__size))
