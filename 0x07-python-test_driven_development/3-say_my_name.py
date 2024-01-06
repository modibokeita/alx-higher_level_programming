#!/usr/bin/python3

"""
function say_my_name - is about
to print the first name and
last name
"""


def say_my_name(first_name, last_name=""):

    """checks if first name is string or
    not then if not it will raise error message
    first name must a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    """checks if last name is string or
    not then if not it will raise error message
    last name must a string
    """

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
