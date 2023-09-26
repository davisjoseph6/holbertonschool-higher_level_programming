#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    last_dig = (-1) * number % 10
    last_dig = (-1) * last_dig
else:
    last_dig = number % 10

if last_dig == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
elif last_dig > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
else:
    print(f"Last digit of {number} is {last_dig} and is less than 6 and not 0")
