#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lst_number = number % -10
elif number >= 0:
    lst_number = number % 10
if lst_number > 5:
    print(f"Last digit in {number} is {lst_number} and is greater than 5")
elif lst_number == 0:
    print(f"Last digit in {number} is {lst_number} and is 0")
else:
    print(f"Last digit in {number} is {lst_number} and is less than 6 and not 0")
