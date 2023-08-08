#!/usr/bin/python3
import random

number = random.randint(-10, 10)
message = "{:d} is negative".format(number) if number < 0 else \
          "{:d} is positive".format(number) if number > 0 else \
          "0 is zero"

print(message)
