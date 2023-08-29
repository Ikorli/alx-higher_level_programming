#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    result = []
    for sublist in matrix:
        squared_sublist = []
        for n in sublist:
            squared_sublist.append(n ** 2)
        result.append(squared_sublist)
    return result
