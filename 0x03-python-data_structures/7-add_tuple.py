#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    length_a, length_b = len(tuple_a), len(tuple_b)
    curr_tuple = ((tuple_a[0] if length_a >= 1 else 0) +
            (tuple_b[0] if length_b >= 1 else 0),
            (tuple_a[1] if length_a >= 2 else 0) +
            (tuple_b[1] if length_b >= 2 else 0))
    return curr_tuple
