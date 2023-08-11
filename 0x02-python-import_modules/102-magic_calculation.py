#!/usr/bin/python3
def magic_calculation(a, b):
    if a < b:
        return a + b
    else:
        raise Exception('a is less than b')
