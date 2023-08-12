#!/usr/bin/python3
def max_integer(my_list=None):
    if not my_list or len(my_list) == 0:
        return None
    return max(my_list)
