#!/usr/bin/python3

"""
A class that try access an undefine
property
"""


class BaseGeometry:

    """
    try to acces the area property
    which is not define that cases
    an error
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        """
        that validates value
        if value is not an integer: raise a TypeError exception
        with the message <name> must be an integer
        if value is less or equal to 0: raise a ValueError
        exception with the message <name> must be greater than 0
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
