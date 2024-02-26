#!/usr/bin/python3
'''Module for Base unit tests.'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    '''Tests the Base class.'''

    def test_A_nb_objects_private(self):
        '''Tests if nb_objects is private class attribute.'''
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_B_nb_objects_initialized(self):
        '''Tests if nb_objects initializes to zero.'''
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_create_object(self):
        '''Tests Base() instantiation.'''
        base = Base()
        self.assertEqual(str(type(base)), "<class 'models.base.Base'>")
        self.assertEqual(base.__dict__, {"id": 1})
        self.assertEqual(base.id, 1)

    def test_create_two_objects_ids(self):
        '''Tests consecutive ids.'''
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_nb_attr_equal_id(self):
        '''Tests sync between class and instance id.'''
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_G_custom_id_int(self):
        '''Tests custom int id.'''
        b = Base(98)
        self.assertEqual(b.id, 98)