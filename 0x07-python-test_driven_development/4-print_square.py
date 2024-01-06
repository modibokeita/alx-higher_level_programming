#!/usr/bin/python3

"""
function print_square - prints
whatever size pass into it
with the character #
"""


def print_square(size):

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for _ in range(size):
        print("#" * size)
