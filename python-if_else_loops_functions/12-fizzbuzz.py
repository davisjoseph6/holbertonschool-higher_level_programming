#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            print(f"FizzBuzz".format(n), end=" ")
        elif n % 3 == 0:
            print(f"Fizz".format(n), end=" ")
        elif n % 5 == 0:
            print(f"Buzz".format(n), end=" ")
        else:
            print("{:d}".format(n), end=" ")
