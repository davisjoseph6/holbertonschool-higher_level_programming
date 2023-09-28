#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if 97 <= ord(char) <= 122:
            u_char = chr(ord(char) - 32)
            result += u_char
        else:
            result += char
    print("{}".format(result))
