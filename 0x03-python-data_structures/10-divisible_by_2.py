#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list or len(my_list) < 1:
        return None
    return [i % 2 == 0 for i in my_list]
