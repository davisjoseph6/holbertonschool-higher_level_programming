#!/usr/bin/python3
def uppercase(str):
    result_str = ""
    for char in str:
        if 97 <= ord(char) <= 122:
            result_str += chr(ord(char) - 32)
        else:
            result_str += char
    print(result_str)
