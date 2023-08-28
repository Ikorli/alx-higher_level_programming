#!/usr/bin/python3
list_division = __import__('4-list_division').list_division

def test_list_division(list1, list2):
    result = list_division(list1, list2, max(len(list1), len(list2)))
    print(result)

print("Test Case 1:")
my_list_1 = [10, 8, 4]
my_list_2 = [2, 4, 4]
test_list_division(my_list_1, my_list_2)
print("--")

print("Test Case 2:")
my_list_1 = [10, 8, 4, 4]
my_list_2 = [2, 0, "H", 2, 7]
test_list_division(my_list_1, my_list_2)
