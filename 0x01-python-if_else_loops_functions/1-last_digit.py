#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
ldigit = abs(number) % 10

if ldigit > 5:
    comparison = "greater than 5"
elif ldigit == 0:
    comparison = "0"
else:
    comparison = "less than 6 and not 0"

print(f"Last digit of {number} is {ldigit} and is {comparison}")
