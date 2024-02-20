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

    def to_json(self, attrs=None):
        """ obj to json """
        if attrs is None:
            return self.__dict__
        else:
            newdir = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dir[key] = value

            return new_dir
