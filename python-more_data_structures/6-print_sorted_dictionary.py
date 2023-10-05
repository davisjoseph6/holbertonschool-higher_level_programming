#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ordered_keys = sorted(a_dictionary)
    for key in ordered_keys:
        print(f'{key}: {a_dictionary[key]}')
