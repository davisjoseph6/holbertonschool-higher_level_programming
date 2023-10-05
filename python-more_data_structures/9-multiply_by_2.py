#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dicti = a_dictionary.copy()
    for key, value in new_dicti.items():
        new_dicti[key] = value * 2
    return new_dicti
