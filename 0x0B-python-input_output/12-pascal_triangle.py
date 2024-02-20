#!/usr/bin/python3
"""
    pascal module
"""


def pascal_triangle(n):
    """ pascal triangle"""
    my_list = []
    if n <= 0:
        return my_list
    for i in range(n):
        num = 11**i
        li = [int(n) for n in str(num)]
        my_list.append(li)
    return my_list
