#!/usr/bin/python3
def best_score(my_dictionary):
    if my_dictionary:
        return max(my_dictionary, key=my_dictionary.get)
    else:
        return None
