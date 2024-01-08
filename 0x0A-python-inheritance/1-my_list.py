#!/usr/bin/python3

"""class MyList that inherits from list"""


class MyList(list):
    """A class that inherites list class"""

    def print_sorted(self):

        """ prints sorted list"""

        print(sorted(self))
