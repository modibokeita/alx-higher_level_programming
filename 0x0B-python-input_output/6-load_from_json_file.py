#!/usr/bin/python3

"""
a function that creates
an Object from a “JSON file”
"""

import json


def load_from_json_file(filename):
    """
    that creates an Object
    from a “JSON file”
    """
    with open(filename, encoding="utf-8") as f:

        return json.load(f)
