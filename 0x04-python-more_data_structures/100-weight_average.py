#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    total_weight = 0
    total_product = 0
    for weight, score in my_list:
        total_weight += weight
        total_product += weight * score
    if total_weight == 0:
        return 0
    return total_product / total_weight
