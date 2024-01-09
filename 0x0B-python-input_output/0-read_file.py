#!/usr/bin/pyton3

"""
function that reads a text file
(UTF8) and prints it to stdout
"""


def read_file(filename=""):

    """
    read a file and print the content
    of that file in output
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        """
        loop over the the file and print
        the each line in the file
        """
        print(f.read(), end="")
