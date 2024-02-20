#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
module with class BaseGeometry

"""

class Square(Rectangle):
    """Square class that inherits from Rectangle that inherits BaseGeometry"""

    def __init__(self, size)
        '''Constructor.'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def ara (size):
        return size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
