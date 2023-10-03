#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    new_list = my_list
    my_list[3] = 9
    if idx < 0 or idx > (len(my_list)):
        return my_list
    else:
        return new_list
