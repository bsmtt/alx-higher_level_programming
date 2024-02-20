#!/usr/bin/python3
"""
    Student Module
"""


class Student:
    """Student attributes"""

    def __init__(self, first_name, last_name, age):
        """method for initialized all atributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ obj to json """
        return self.__dict__
