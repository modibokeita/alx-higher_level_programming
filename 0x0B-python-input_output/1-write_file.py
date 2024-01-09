#!/usr/bin/python3

"""
define a function that
write a string
"""


def write_file(filename="", text=""):

    """
    writes a string to a text file (UTF8) and
    returns the number of characters written
    """

    with open(filename, mode="w", encoding="utf-8") as f:

        return f.write(text)
