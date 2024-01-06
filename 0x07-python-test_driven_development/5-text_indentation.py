#!/usr/bin/python3

"""
def text_indentation checks
for some specific characters
and prints 2 new lines after
those characters which are
['.', '?', ':']
"""


def text_indentation(text):

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    current_line = ""

    for char in text:

        current_line += char

        if char in ['.', '?', ':']:
            print(current_line.strip())
            print("")
            current_line = ""
    if current_line:
        print(current_line.strip())
