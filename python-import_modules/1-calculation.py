#!/usr/bin/python3

from calculator_1 import add
if __name__ == "__main__":
    a = 1
    b = 2
    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))

from calculator_1 import sub
if __name__ == "__main__":
    a = 10
    b = 5
    result = sub(a, b)
    print("{} - {} = {}".format(a, b, result))

from calculator_1 import mul
if __name__ == "__main__":
    a = 10
    b = 5
    result = mul(a, b)
    print("{} * {} = {}".format(a, b, result))

from calculator_1 import div
if __name__ == "__main__":
    a = 10
    b = 5
    result = div(a, b)
    print("{} / {} = {}".format(a, b, result))
