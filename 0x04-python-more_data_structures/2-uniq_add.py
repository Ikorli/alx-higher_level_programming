#!/usr/bin/python3
def uniq_add(my_list=[]):
    return sum([num for num in my_list if my_list.count(num) == 1])
