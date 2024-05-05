#!/usr/bin/python3
def replace_in_list(my_idx, idx, element):
    if idx < len(my_idx) and idx >= 0:
        my_idx[idx] = element
        return (my_idx)