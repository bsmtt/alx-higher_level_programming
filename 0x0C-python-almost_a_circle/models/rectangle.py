#!/usr/bin/python3
'''Module for Rectangle class.'''


from models.base import Base


class Rectangle(Base):
    ''' The Rectangle Class.'''
    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Constructor. '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def validate_int(self, name, val, equal=None):
        '''Method for validating the value.'''
        if type(val) != int:
            raise TypeError("{} must be an integer".format(name))
        if equal is not None and val < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif equal is None and val <= 0:
            raise ValueError("{} must be > 0".format(name))

    @property
    def width(self):
        '''Width of rectangle.'''
        return self.__width

    @width.setter
    def width(self, val):
        self.validate_int("width", val)
        self.__width = val

    @property
    def height(self):
        '''height of rectangle.'''
        return self.__height

    @height.setter
    def height(self, val):
        self.validate_int("height", val)
        self.__height = val

    @property
    def y(self):
        '''y of rectangle.'''
        return self.__y

    @y.setter
    def y(self, val):
        self.validate_int("y", val, True)
        self.__y = val

    @property
    def x(self):
        '''x of rectangle.'''
        return self.__x

    @x.setter
    def x(self, val):
        self.validate_int("x", val, True)
        self.__x = val

    def area(self):
        ''' area of this rectangle. '''
        return self.width * self.height
    
    def display(self): 
        r = '\n' * self.y
        r += (' ' * self.x + '#' * self.width + '\n') * self.height
        print(r, end='')

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        ''' assigns an argument to each attribute '''
        if id:
            self.id = id
        if width:
            self.width = width
        if height:
            self.height = height
        if x:
            self.x = x
        if y:
            self.y = y
    def update(self, *args, **kwargs):
        '''Updates instance attributes via no-keyword & keyword args.'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        '''Returns string info about this rectangle.'''
        return '[{}] ({}) {}/{} - {}/{}'.format(type(self).__name__, self.id, self.x, self.y, self.width, self.height)
