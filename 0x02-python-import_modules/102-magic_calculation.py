#!/usr/bin/python3
def magic_calculation(a, b):
    if a < b:
        return a + b
    else:
        raise ValueError('a must be less than b')
