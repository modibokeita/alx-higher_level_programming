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
    with open(filename, encoding="utf-8") as f:

        for line in f:
            print(line, end="")
