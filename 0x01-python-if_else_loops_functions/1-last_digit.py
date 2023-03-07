#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

if number < 0:
    rem = number % -10
else:
    rem = number % 10

if (number % 10 > 5):
    print(f"Last digit of {number:d} is {rem:d} and is greater than 5")
if (number % 10 == 0):
    print(f"Last digit of {number:d} is {rem:d} and is zero")
if (number % 10 < 6) and (number % 10 != 0):
    print(f"Last digit of {number:d} is {rem:d} and is less than 6 and not 0")
