#!/usr/bin/python3
def best_score(my_dictionary):
    return max(my_dictionary, key=lambda key: my_dictionary[key], default=None)

