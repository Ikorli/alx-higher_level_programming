#!/usr/bin/python3
list_division = __import__('4-list_division').list_division

def test_list_division(my_l_1, my_l_2):
    max_length = max(len(my_l_1), len(my_l_2))
    result = list_division(my_l_1, my_l_2, max_length)
    return result

# Test case 1
my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = test_list_division(my_l_1, my_l_2)
print(result)

print("--")

# Test case 2
my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = test_list_division(my_l_1, my_l_2)
print(result)
