#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0 or idx > 4:
        return None
    else:
        return my_list[idx]
