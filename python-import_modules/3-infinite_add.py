#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    total = 0
    for arg in argv[1:]:
        num = int(arg)
        total += num
    print(f"{total}")
