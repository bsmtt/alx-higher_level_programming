#!/usr/bin/python3
'''Module for inherits_from.'''


def inherits_from(obj, a_class):
    '''subclass of a class.'''
    return isinstance(obj, a_class) and type(obj) != a_class
