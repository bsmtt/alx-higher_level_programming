#!/usr/bin/python3
'''Module for Square class.'''
from models.rectangle import Rectangle

class Square(Rectangle):
    ''' The Square Class.'''
    def __init__(self, size, x=0, y=0, id=None):
        ''' Constructor. '''
        super().__init__(size, size, x, y, id)

    def validate_int(self, name, val, equal=None):
        '''Method for validating the value.'''
        if type(val) != int:
            raise TypeError("{} must be an integer".format(name))
        if equal is not None and val < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif equal is None and val <= 0:
            raise ValueError("{} must be > 0".format(name))

    @property
    def size(self):
        '''size of Square.'''
        return self.width

    @size.setter
    def size(self, val):
        '''Set size of this square.'''
        self.validate_int("width", val)
        self.width = val
        self.height = val

    def __update(self, id=None, size=None, x=None, y=None):
        '''Internal method that updates  attributes '''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Updates attributes.'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def __str__(self):
        '''Returns string info about this square.'''
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

