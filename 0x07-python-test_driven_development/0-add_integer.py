#!/usr/bin/python3

"""
add function adds two variables a and b
but the value of a and b must be intger or
float otherwise program will stop running
"""


def add_integer(a, b=98):

    """
    a and b must be integers or floats, otherwise raise
    a TypeError exception with the message a must be
    an integer or b must be an integer a and b must be
    first casted to integers if they are float
    Returns an integer: the addition of a and b
    """

    if type(a) not in [int, float]:
        """ checks if
        the value of a is int or float
        if not the print error message
        """

        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:

        """ checks if
        the value of b is int or float
        if not the print error message
        """
        raise TypeError("b must be an integer")

    """ return the result
    after checking everything in case there no TypeEerror
    otherwise raise type of error
    """

    return int(a) + int(b)
