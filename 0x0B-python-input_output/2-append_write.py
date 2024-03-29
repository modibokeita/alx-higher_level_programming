#!/usr/bin/python3

"""define a function that
append text to a file
"""


def append_write(filename="", text=""):

    """
    appends a string at the end
    of a text file (UTF8)
    and returns the number of characters
    """
    with open(filename, mode="a", encoding="utf-8") as f:

        return f.write(text)
