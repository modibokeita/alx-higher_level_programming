#!/usr/bin/python3

"""
A class try access
a property not define
"""


class BaseGeometry:

    """
    Try to access the property area
    but that property is not define
    """

    def area(self):
        raise Exception("area() is not implemented")
