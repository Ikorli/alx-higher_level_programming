#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    print(last_digit, end=" ")
    return last_digit

# Example usage
num = -98
result = print_last_digit(num)
print("is the expected output")
